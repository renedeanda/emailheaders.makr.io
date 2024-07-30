
import Head from 'next/head'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function FAQ() {
  const faqs = [
    {
      question: "What are email headers?",
      answer: "Email headers are lines of metadata at the beginning of an email message that contain information about the sender, recipient, routing, and various authentication mechanisms used in email delivery."
    },
    {
      question: "Why should I analyze email headers?",
      answer: "Analyzing email headers can help you verify the authenticity of an email, troubleshoot delivery issues, track the email's journey, and identify potential security threats like phishing or spoofing attempts."
    },
    {
      question: "What is SPF?",
      answer: "SPF (Sender Policy Framework) is an email authentication method designed to detect forging sender addresses during the delivery of the email. It allows domain owners to specify which mail servers are authorized to send email on behalf of their domain."
    },
    {
      question: "What is DKIM?",
      answer: "DKIM (DomainKeys Identified Mail) is an email authentication technique that allows the receiver to check that an email was indeed sent and authorized by the owner of that domain. This is done by giving the email a digital signature."
    },
    {
      question: "How does EmailHeaderX verify DKIM signatures?",
      answer: "EmailHeaderX extracts DKIM signatures from the email headers, then performs DNS lookups to retrieve the public keys associated with the signatures. It then verifies these signatures against the email content to ensure the email hasn't been tampered with during transit."
    }
  ]

  return (
    <div className="min-h-screen flex flex-col">
      <Head>
        <title>FAQ | EmailHeaderX - Advanced Email Header Analysis</title>
        <meta name="description" content="Frequently asked questions about email headers, SPF, DKIM, and how EmailHeaderX analyzes them." />
      </Head>

      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Frequently Asked Questions</h1>
        <div className="space-y-6">
          {faqs.map((faq, index) => (
            <div key={index} className="bg-white dark:bg-gray-800 shadow-md rounded-lg p-6">
              <h2 className="text-xl font-semibold mb-2">{faq.question}</h2>
              <p className="text-gray-600 dark:text-gray-300">{faq.answer}</p>
            </div>
          ))}
        </div>
      </main>

      <Footer />
    </div>
  )
}
