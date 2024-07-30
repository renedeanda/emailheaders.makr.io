
export async function parseEmailHeaders(headerText) {
  const headers = {}
  const lines = headerText.split('\n')

  let currentKey = ''
  for (const line of lines) {
    if (line.trim() === '') continue

    if (line.startsWith(' ') || line.startsWith('\t')) {
      // Continuation of previous header
      headers[currentKey] += ' ' + line.trim()
    } else {
      const [key, ...valueParts] = line.split(':')
      currentKey = key.trim()
      headers[currentKey] = valueParts.join(':').trim()
    }
  }

  // Extract and format key information
  const formattedHeaders = {
    'From': headers['From'] || 'Not available',
    'To': headers['To'] || 'Not available',
    'Subject': headers['Subject'] || 'Not available',
    'Date': headers['Date'] || 'Not available',
    'Message-ID': headers['Message-ID'] || 'Not available',
    'Received': extractReceivedChain(headers['Received']),
    'Authentication-Results': headers['Authentication-Results'] || 'Not available',
  }

  return formattedHeaders
}

function extractReceivedChain(receivedHeader) {
  if (!receivedHeader) return 'Not available'
  // Split the Received header into individual hops
  const hops = receivedHeader.split('; ')
  return hops.map(hop => hop.trim()).join('\n')
}
