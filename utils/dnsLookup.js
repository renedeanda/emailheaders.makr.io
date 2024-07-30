
import dns from 'dns'
import { promisify } from 'util'

const resolveTxt = promisify(dns.resolveTxt)

export async function lookupSPF(fromDomain) {
  try {
    const domain = fromDomain.split('@')[1]
    const records = await resolveTxt(domain)
    const spfRecord = records.find(record => record[0].startsWith('v=spf1'))
    return spfRecord ? spfRecord[0] : 'No SPF record found'
  } catch (error) {
    console.error('SPF lookup error:', error)
    return 'SPF lookup failed'
  }
}

export async function verifyDKIM(headerText) {
  const dkimResults = []
  const dkimSignatureRegex = /DKIM-Signature:.*?d=([^;\s]+).*?s=([^;\s]+)/gs
  let match

  while ((match = dkimSignatureRegex.exec(headerText)) !== null) {
    const [, domain, selector] = match
    try {
      const dkimRecord = await resolveTxt(`${selector}._domainkey.${domain}`)
      dkimResults.push({
        selector,
        domain,
        result: dkimRecord ? 'pass' : 'fail',
      })
    } catch (error) {
      console.error('DKIM lookup error:', error)
      dkimResults.push({
        selector,
        domain,
        result: 'lookup failed',
      })
    }
  }

  return dkimResults.length > 0 ? dkimResults : [{ selector: 'N/A', domain: 'N/A', result: 'No DKIM signature found' }]
}
