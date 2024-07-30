
export default function HeaderExplanation({ headerField }) {
  const explanations = {
    'From': 'The "From" header indicates the sender of the email. It typically includes the sender\'s name and email address.',
    'To': 'The "To" header specifies the primary recipient(s) of the email.',
    'Subject': 'The "Subject" header contains a brief summary or title of the email\'s content.',
    'Date': 'The "Date" header shows when the email was sent, typically in a standardized format.',
    'Message-ID': 'The "Message-ID" is a unique identifier for the email, often used for threading and deduplication.',
    'Received': 'The "Received" headers trace the path of the email from sender to recipient, with each server adding its own header.',
    'SPF': 'Sender Policy Framework (SPF) is an email authentication method to detect forging sender addresses during email delivery.',
    'DKIM': 'DomainKeys Identified Mail (DKIM) provides a way to validate that an email was sent and authorized by the owner of that domain.',
    'DMARC': 'Domain-based Message Authentication, Reporting, and Conformance (DMARC) is an email authentication protocol that builds on SPF and DKIM.',
  }

  return (
    <div className="mt-2 p-3 bg-gray-100 dark:bg-gray-600 rounded-md">
      <p className="text-sm text-gray-700 dark:text-gray-300">{explanations[headerField] || 'No explanation available for this field.'}</p>
    </div>
  )
}
