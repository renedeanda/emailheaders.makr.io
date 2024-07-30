
import Head from 'next/head'
import Header from '../components/Header'
import Footer from '../components/Footer'

export default function About() {
  return (
    <div className="min-h-screen flex flex-col">
      <Head>
        <title>About EmailHeaderX | Advanced Email Header Analysis</title>
        <meta name="description" content="Learn about EmailHeaderX, the comprehensive email header analysis tool for IT professionals and security enthusiasts." />
      </Head>

      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-4">About EmailHeaderX</h1>
        <p className="mb-4">
          EmailHeaderX is a powerful tool designed to help IT professionals, security enthusiasts, and curious users analyze and understand email headers. Our advanced parsing engine provides detailed insights into email routing, authentication, and security measures.
        </p>
        <p className="mb-4">
          With real-time DNS lookups for SPF records and DKIM verification, EmailHeaderX goes beyond simple header parsing to provide a comprehensive view of an email's journey and authenticity.
        </p>
        <h2 className="text-2xl font-bold mt-8 mb-4">Key Features</h2>
        <ul className="list-disc list-inside mb-4">
          <li>Detailed parsing of email headers</li>
          <li>Real-time SPF record lookup</li>
          <li>DKIM signature verification</li>
          <li>User-friendly interface with dark mode support</li>
          <li>Mobile-responsive design</li>
        </ul>
        <p>
          Whether you're investigating potential phishing attempts, troubleshooting email delivery issues, or simply curious about the behind-the-scenes of email communication, EmailHeaderX provides the insights you need.
        </p>
      </main>

      <Footer />
    </div>
  )
}
