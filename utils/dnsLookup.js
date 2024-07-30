
import dns from 'dns';
import { promisify } from 'util';

const resolveTxt = promisify(dns.resolveTxt);

export async function lookupSPF(fromDomain) {
  try {
    const domain = fromDomain.split('@')[1];
    const records = await resolveTxt(domain);
    const spfRecord = records.find(record => record[0].startsWith('v=spf1'));
    
    if (spfRecord) {
      const spfParts = spfRecord[0].split(' ');
      const mechanisms = spfParts.slice(1).filter(part => !part.startsWith('v=spf1'));
      
      return {
        status: 'found',
        record: spfRecord[0],
        mechanisms: mechanisms,
        explanation: interpretSPF(mechanisms)
      };
    } else {
      return {
        status: 'not_found',
        explanation: 'No SPF record found for this domain.'
      };
    }
  } catch (error) {
    console.error('SPF lookup error:', error);
    return {
      status: 'error',
      explanation: 'SPF lookup failed. There might be an issue with the DNS server or the domain might not exist.'
    };
  }
}

function interpretSPF(mechanisms) {
  let explanation = 'This SPF record:';
  mechanisms.forEach(mech => {
    if (mech.startsWith('include:')) {
      explanation += `
- Includes the SPF record of ${mech.split(':')[1]}`;
    } else if (mech.startsWith('a')) {
      explanation += '
- Allows the domain's A record';
    } else if (mech.startsWith('mx')) {
      explanation += '
- Allows the domain's MX records';
    } else if (mech.startsWith('ip4:') || mech.startsWith('ip6:')) {
      explanation += `
- Allows the IP address ${mech.split(':')[1]}`;
    } else if (mech === '-all') {
      explanation += '
- Fails any other servers not listed (strict)';
    } else if (mech === '~all') {
      explanation += '
- Softly fails any other servers not listed (lenient)';
    }
  });
  return explanation;
}

// Existing verifyDKIM function here
