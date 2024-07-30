
import { parseEmailHeaders } from '../../utils/emailHeaderParser'
import { verifyDKIM, lookupSPF } from '../../utils/dnsLookup'

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const { headers } = req.body
    const parsedHeaders = await parseEmailHeaders(headers)

    // Perform DNS lookups and DKIM verification
    const spfResult = await lookupSPF(parsedHeaders['From'])
    const dkimResults = await verifyDKIM(headers)

    // Update parsed headers with DNS lookup results
    parsedHeaders['SPF'] = spfResult
    parsedHeaders['DKIM'] = dkimResults

    res.status(200).json(parsedHeaders)
  } catch (error) {
    res.status(500).json({ error: 'Failed to parse headers: ' + error.message })
  }
}
