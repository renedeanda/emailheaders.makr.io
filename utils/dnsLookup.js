
import dns from 'dns';
import { promisify } from 'util';

const resolveTxt = promisify(dns.resolveTxt);

export async function lookupSPF(fromDomain) {
  try {
    const domain = fromDomain.split('@')[1];
    if (!domain) {
      throw new Error('Invalid email format');
    }
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
        explanation: `No SPF record found for the domain ${domain}.`
      };
    }
  } catch (error) {
    console.error('SPF lookup error:', error);
    if (error.code === 'ENOTFOUND') {
      return {
        status: 'error',
        explanation: `Domain not found: ${fromDomain.split('@')[1]}. Please check if the domain is correct.`
      };
    } else if (error.code === 'ECONNREFUSED') {
      return {
        status: 'error',
        explanation: 'Connection to DNS server was refused. There might be network issues.'
      };
    } else {
      return {
        status: 'error',
        explanation: `SPF lookup failed: ${error.message}. There might be an issue with the DNS server or the domain configuration.`
      };
    }
  }
}

function interpretSPF(mechanisms) {
  let explanation = 'This SPF record:';
  mechanisms.forEach(mech => {
    if (mech.startsWith('include:')) {
      explanation += `\n- Includes the SPF record of ${mech.split(':')[1]}`;
    } else if (mech.startsWith('a')) {
      explanation += `\n- Allows the domain's A record`;
    } else if (mech.startsWith('mx')) {
      explanation += `\n- Allows the domain's MX records`;
    } else if (mech.startsWith('ip4:') || mech.startsWith('ip6:')) {
      explanation += `\n- Allows the IP address ${mech.split(':')[1]}`;
    } else if (mech === '-all') {
      explanation += `\n- Fails any other servers not listed (strict)`;
    } else if (mech === '~all') {
      explanation += `\n- Softly fails any other servers not listed (lenient)`;
    }
  });
  return explanation;
}

export async function verifyDKIM(headerText) {
  const dkimResults = [];
  const dkimSignatureRegex = /DKIM-Signature:.*?d=([^;\s]+).*?s=([^;\s]+)/gs;
  let match;

  while ((match = dkimSignatureRegex.exec(headerText)) !== null) {
    const [, domain, selector] = match;
    try {
      const dkimRecord = await resolveTxt(`${selector}._domainkey.${domain}`);
      dkimResults.push({
        selector,
        domain,
        result: dkimRecord ? 'pass' : 'fail',
      });
    } catch (error) {
      console.error('DKIM lookup error:', error);
      dkimResults.push({
        selector,
        domain,
        result: 'lookup failed',
      });
    }
  }

  return dkimResults.length > 0 ? dkimResults : [{ selector: 'N/A', domain: 'N/A', result: 'No DKIM signature found' }];
}
