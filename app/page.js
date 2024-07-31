
import { Suspense } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import EmailHeaderForm from '../components/EmailHeaderForm'
import ParsedHeaderDisplay from '../components/ParsedHeaderDisplay'
import LoadingSpinner from '../components/LoadingSpinner'
import PromotionBanner from '../components/PromotionBanner'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 dark:from-gray-800 dark:to-gray-900 transition-colors duration-200">
      <Header />
      <PromotionBanner />
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100 mb-8">
          Email Header Analyzer
        </h1>

        <Suspense fallback={<LoadingSpinner />}>
          <EmailHeaderForm />
        </Suspense>
        <div className="bg-white dark:bg-gray-700 shadow-lg rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">ABOUT EMAIL HEADERS</h2>
          <p className="text-gray-600 dark:text-gray-300">
            This tool makes email headers human-readable by parsing them according to RFC 822.
            Email headers are present on every email you receive via the Internet and provide
            valuable diagnostic information such as routing paths, spam filter results, and authentication details.
            By understanding email headers, you can:
          </p>
          <ul className="list-disc list-inside mt-2 text-gray-600 dark:text-gray-300">
            <li>Trace the journey of an email from sender to recipient</li>
            <li>Verify the authenticity of emails and detect potential phishing attempts</li>
            <li>Troubleshoot email delivery issues and delays</li>
            <li>Gain insights into email security measures like SPF, DKIM, and DMARC</li>
          </ul>
        </div>
        <Suspense fallback={<LoadingSpinner />}>
          <ParsedHeaderDisplay />
        </Suspense>
      </main>
      <Footer />
    </div>
  )
}
