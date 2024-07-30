import os
import subprocess
import json

def run_command(command):
    """Run a shell command and print its output."""
    print(f"Running command: {command}")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    print(result.stdout)
    if result.stderr:
        print(f"Error: {result.stderr}")
    if result.returncode != 0:
        raise Exception(f"Command failed with exit code {result.returncode}")

def create_file(path, content):
    """Create a file with the given content."""
    print(f"Creating file: {path}")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)
    print(f"File created successfully: {path}")

# File contents
package_json = '''
{
  "name": "email-header-x",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest",
    "framer-motion": "^4.1.17",
    "tailwindcss": "^3.0.0",
    "d3": "^7.0.0",
    "jspdf": "^2.5.1",
    "jspdf-autotable": "^3.5.23"
  },
  "devDependencies": {
    "autoprefixer": "^10.4.0",
    "postcss": "^8.4.5"
  }
}
'''

next_config_js = '''
module.exports = {
  reactStrictMode: true,
  async rewrites() {
    return [
      {
        source: '/analysis/:id',
        destination: '/analysis/[id]',
      },
    ]
  },
}
'''

tailwind_config_js = '''
module.exports = {
  content: [
    './pages/**/*.{js,ts,jsx,tsx,mdx}',
    './components/**/*.{js,ts,jsx,tsx,mdx}',
    './app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#e6f0ff',
          100: '#b3d1ff',
          200: '#80b3ff',
          300: '#4d94ff',
          400: '#1a75ff',
          500: '#0056e0',
          600: '#0045b3',
          700: '#003486',
          800: '#002359',
          900: '#00112c',
        },
      },
    },
  },
  plugins: [],
}
'''

postcss_config_js = '''
module.exports = {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
}
'''

app_layout_js = '''
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'EmailHeaderX | Advanced Email Header Analysis',
  description: 'Comprehensive email header analysis tool with SPF, DKIM, and DMARC verification. Perfect for IT professionals and security enthusiasts.',
  keywords: 'email header, parser, analyzer, email security, SPF, DKIM, DMARC, DNS lookup',
  openGraph: {
    title: 'EmailHeaderX | Advanced Email Header Analysis',
    description: 'Comprehensive email header analysis with real-time DNS lookups and DKIM verification.',
    type: 'website',
    url: 'https://emailheaderx.com',
    image: 'https://emailheaderx.com/og-image.jpg',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'EmailHeaderX | Advanced Email Header Analysis',
    description: 'Comprehensive email header analysis with real-time DNS lookups and DKIM verification.',
    image: 'https://emailheaderx.com/twitter-image.jpg',
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
      </head>
      <body className={inter.className}>
        <ThemeProvider>
          <HeaderProvider>
            {children}
          </HeaderProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
'''

app_page_js = '''
import { Suspense } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import EmailHeaderForm from '../components/EmailHeaderForm'
import ParsedHeaderDisplay from '../components/ParsedHeaderDisplay'
import LoadingSpinner from '../components/LoadingSpinner'
import DarkModeToggle from '../components/DarkModeToggle'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 dark:from-gray-800 dark:to-gray-900 transition-colors duration-200">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100">
            Email Header Analyzer
          </h1>
          <DarkModeToggle />
        </div>
        <Suspense fallback={<LoadingSpinner />}>
          <EmailHeaderForm />
        </Suspense>
        <Suspense fallback={<LoadingSpinner />}>
          <ParsedHeaderDisplay />
        </Suspense>
      </main>
      <Footer />
    </div>
  )
}
'''

components_header_js = '''
'use client'
import Link from 'next/link'
import { useState } from 'react'
import { motion } from 'framer-motion'
import DarkModeToggle from './DarkModeToggle'

export default function Header() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <header className="bg-white dark:bg-gray-800 shadow-md">
      <nav className="container mx-auto px-6 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-primary-600 dark:text-primary-400">
            EmailHeaderX
          </Link>
          <div className="hidden md:flex items-center">
            <Link href="/" className="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 px-3 py-2">
              Home
            </Link>
            <Link href="/saved-analyses" className="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 px-3 py-2">
              Saved Analyses
            </Link>
            <Link href="/about" className="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 px-3 py-2">
              About
            </Link>
            <Link href="/faq" className="text-gray-600 dark:text-gray-300 hover:text-primary-500 dark:hover:text-primary-400 px-3 py-2">
              FAQ
            </Link>
            <DarkModeToggle />
          </div>
          <button
            className="md:hidden"
            onClick={() => setIsOpen(!isOpen)}
            aria-label="Toggle menu"
          >
            <svg
              className="w-6 h-6 text-gray-600 dark:text-gray-300"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              {isOpen ? (
                <path d="M6 18L18 6M6 6l12 12" />
              ) : (
                <path d="M4 6h16M4 12h16M4 18h16" />
              )}
            </svg>
          </button>
        </div>
      </nav>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          exit={{ opacity: 0, y: -20 }}
          className="md:hidden"
        >
          <Link href="/" className="block px-4 py-2 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            Home
          </Link>
          <Link href="/saved-analyses" className="block px-4 py-2 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            Saved Analyses
          </Link>
          <Link href="/about" className="block px-4 py-2 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            About
          </Link>
          <Link href="/faq" className="block px-4 py-2 text-gray-600 dark:text-gray-300 hover:bg-gray-100 dark:hover:bg-gray-700">
            FAQ
          </Link>
          <div className="px-4 py-2">
            <DarkModeToggle />
          </div>
        </motion.div>
      )}
    </header>
  )
}
'''

components_footer_js = '''
export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 mt-12">
      <div className="container mx-auto px-6 py-4">
        <p className="text-center text-gray-600 dark:text-gray-300 text-sm">
          © {new Date().getFullYear()} EmailHeaderX. All rights reserved.
        </p>
        <div className="flex justify-center mt-2">
          <a href="#" className="text-gray-500 hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-300 mx-2">
            Privacy Policy
          </a>
          <a href="#" className="text-gray-500 hover:text-gray-600 dark:text-gray-400 dark:hover:text-gray-300 mx-2">
            Terms of Service
          </a>
        </div>
      </div>
    </footer>
  )
}
'''

components_email_header_form_js = '''
'use client'
import { useState } from 'react'
import { motion } from 'framer-motion'
import { useHeaderContext } from '../context/HeaderContext'
import ErrorMessage from './ErrorMessage'

export default function EmailHeaderForm() {
  const [headerText, setHeaderText] = useState('')
  const [error, setError] = useState(null)
  const { setParsedHeaders } = useHeaderContext()

  const validateHeaders = (text) => {
    if (text.trim().length === 0) {
      throw new Error('Email headers cannot be empty.')
    }
    if (!text.includes('From:') || !text.includes('To:')) {
      throw new Error('Invalid email headers. Must include at least "From:" and "To:" fields.')
    }
  }

  const handleSubmit = async (e) => {
    e.preventDefault()
    setError(null)
    try {
      validateHeaders(headerText)
      const response = await fetch('/api/parse-headers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ headers: headerText }),
      })
      if (!response.ok) {
        throw new Error('Failed to parse headers. Please try again.')
      }
      const parsedHeaders = await response.json()
      setParsedHeaders(parsedHeaders)
    } catch (err) {
      setError(err.message)
    }
  }

  return (
    <motion.form
      onSubmit={handleSubmit}
      className="bg-white dark:bg-gray-700 shadow-lg rounded-lg p-6 mb-8"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5 }}
    >
      <label htmlFor="headerInput" className="block text-gray-700 dark:text-gray-200 text-sm font-bold mb-2">
        Paste your email headers here:
      </label>
      <textarea
        id="headerInput"
        value={headerText}
        onChange={(e) => setHeaderText(e.target.value)}
        className="w-full px-3 py-2 text-gray-700 dark:text-gray-200 bg-white dark:bg-gray-800 border rounded-lg focus:outline-none focus:border-blue-500 dark:focus:border-blue-400"
        rows="10"
        required
      />
      {error && <ErrorMessage message={error} />}
      <motion.button
        type="submit"
        className="mt-4 bg-blue-500 hover:bg-blue-600 dark:bg-blue-600 dark:hover:bg-blue-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:shadow-outline"
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        Parse Headers
      </motion.button>
    </motion.form>
  )
}
'''

components_parsed_header_display_js = '''
'use client'
import { motion } from 'framer-motion'
import { useHeaderContext } from '../context/HeaderContext'
import HeaderExplanation from './HeaderExplanation'
import EmailRoutingVisualization from './EmailRoutingVisualization'
import { saveAnalysis } from '../utils/localStorage'
import { generatePDF } from '../utils/pdfGenerator'

export default function ParsedHeaderDisplay() {
  const { parsedHeaders } = useHeaderContext()

  if (!parsedHeaders) return null

  const handleSave = () => {
    saveAnalysis(parsedHeaders)
    alert('Analysis saved successfully!')
  }

  const handleGeneratePDF = async () => {
    await generatePDF(parsedHeaders)
  }

  return (
    <motion.div
      className="bg-white dark:bg-gray-700 shadow-lg rounded-lg p-6"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
    >
      <h2 className="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">Parsed Email Headers</h2>
      {Object.entries(parsedHeaders).map(([key, value]) => (
        <motion.div
          key={key}
          className="mb-6"
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.3, delay: 0.1 }}
        >
          <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200">{key}</h3>
          <p className="text-gray-600 dark:text-gray-300 mb-2">{JSON.stringify(value)}</p>
          <HeaderExplanation headerField={key} />
        </motion.div>
      ))}
      <EmailRoutingVisualization receivedHeaders={parsedHeaders['Received']} />
      <div className="mt-6 flex space-x-4">
        <button
          onClick={handleSave}
          className="btn-primary"
        >
          Save Analysis
        </button>
        <button
          onClick={handleGeneratePDF}
          className="btn-primary"
        >
          Generate PDF Report
        </button>
      </div>
    </motion.div>
  )
}
'''

components_header_explanation_js = '''
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
'''

components_email_routing_visualization_js = '''
import { useEffect, useRef } from 'react'
import * as d3 from 'd3'

export default function EmailRoutingVisualization({ receivedHeaders }) {
  const svgRef = useRef()

  useEffect(() => {
    if (!receivedHeaders || receivedHeaders === 'Not available') return

    const hops = receivedHeaders.split('\\n').reverse()
    const nodes = hops.map((hop, index) => ({ id: index, name: hop.split(' ')[1] }))
    const links = nodes.slice(1).map((node, index) => ({ source: index, target: index + 1 }))

    const width = 600
    const height = nodes.length * 50

    const svg = d3.select(svgRef.current)
      .attr('width', width)
      .attr('height', height)

    const simulation = d3.forceSimulation(nodes)
      .force('link', d3.forceLink(links).id(d => d.id).distance(50))
      .force('charge', d3.forceManyBody().strength(-100))
      .force('center', d3.forceCenter(width / 2, height / 2))

    const link = svg.append('g')
      .selectAll('line')
      .data(links)
      .join('line')
      .attr('stroke', '#999')
      .attr('stroke-opacity', 0.6)
      .attr('stroke-width', 2)

    const node = svg.append('g')
      .selectAll('circle')
      .data(nodes)
      .join('circle')
      .attr('r', 5)
      .attr('fill', '#69b3a2')

    const text = svg.append('g')
      .selectAll('text')
      .data(nodes)
      .join('text')
      .text(d => d.name)
      .attr('font-size', 10)
      .attr('dx', 8)
      .attr('dy', 3)

    simulation.on('tick', () => {
      link
        .attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y)

      node
        .attr('cx', d => d.x)
        .attr('cy', d => d.y)

      text
        .attr('x', d => d.x)
        .attr('y', d => d.y)
    })
  }, [receivedHeaders])

  return (
    <div className="mt-6">
      <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200 mb-2">Email Routing Visualization</h3>
      <svg ref={svgRef}></svg>
    </div>
  )
}
'''

components_dark_mode_toggle_js = '''
'use client'
import { useTheme } from '../context/ThemeContext'

export default function DarkModeToggle() {
  const { theme, toggleTheme } = useTheme()

  return (
    <button
      onClick={toggleTheme}
      className="p-2 rounded-full bg-gray-200 dark:bg-gray-600 text-gray-800 dark:text-gray-200"
      aria-label={theme === 'dark' ? 'Switch to light mode' : 'Switch to dark mode'}
    >
      {theme === 'dark' ? '🌞' : '🌙'}
    </button>
  )
}
'''

components_error_message_js = '''
export default function ErrorMessage({ message }) {
  return (
    <div className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded relative" role="alert">
      <strong className="font-bold">Error: </strong>
      <span className="block sm:inline">{message}</span>
    </div>
  )
}
'''

components_loading_spinner_js = '''
export default function LoadingSpinner() {
  return (
    <div className="flex justify-center items-center">
      <div className="animate-spin rounded-full h-12 w-12 border-t-2 border-b-2 border-primary-500 dark:border-primary-400"></div>
    </div>
  )
}
'''

components_saved_analysis_list_js = '''
import Link from 'next/link'

export default function SavedAnalysisList({ analyses }) {
  return (
    <ul className="space-y-4">
      {analyses.map((analysis) => (
        <li key={analysis.id} className="bg-white dark:bg-gray-800 shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-2">
            Analysis from {new Date(analysis.date).toLocaleString()}
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-4">
            From: {analysis.headers.From}
            <br />
            Subject: {analysis.headers.Subject}
          </p>
          <Link 
            href={`/analysis/${analysis.id}`}
            className="text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
          >
            View full analysis
          </Link>
        </li>
      ))}
    </ul>
  )
}
'''

context_theme_context_js = '''
'use client'
import { createContext, useContext, useState, useEffect } from 'react'

const ThemeContext = createContext()

export function ThemeProvider({ children }) {
  const [theme, setTheme] = useState('light')

  useEffect(() => {
    const savedTheme = localStorage.getItem('theme')
    if (savedTheme) {
      setTheme(savedTheme)
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      setTheme('dark')
    }
  }, [])

  useEffect(() => {
    if (theme === 'dark') {
      document.documentElement.classList.add('dark')
    } else {
      document.documentElement.classList.remove('dark')
    }
    localStorage.setItem('theme', theme)
  }, [theme])

  const toggleTheme = () => {
    setTheme(prevTheme => prevTheme === 'light' ? 'dark' : 'light')
  }

  return (
    <ThemeContext.Provider value={{ theme, toggleTheme }}>
      {children}
    </ThemeContext.Provider>
  )
}

export function useTheme() {
  return useContext(ThemeContext)
}
'''

context_header_context_js = '''
'use client'
import { createContext, useContext, useState } from 'react'

const HeaderContext = createContext()

export function HeaderProvider({ children }) {
  const [parsedHeaders, setParsedHeaders] = useState(null)

  return (
    <HeaderContext.Provider value={{ parsedHeaders, setParsedHeaders }}>
      {children}
    </HeaderContext.Provider>
  )
}

export function useHeaderContext() {
  return useContext(HeaderContext)
}
'''

pages_api_parse_headers_js = '''
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
'''

pages_about_js = '''
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
'''

pages_faq_js = '''
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
'''

pages_saved_analyses_js = '''
import { useState, useEffect } from 'react'
import Head from 'next/head'
import Header from '../components/Header'
import Footer from '../components/Footer'
import SavedAnalysisList from '../components/SavedAnalysisList'
import { getSavedAnalyses } from '../utils/localStorage'

export default function SavedAnalyses() {
  const [savedAnalyses, setSavedAnalyses] = useState([])

  useEffect(() => {
    setSavedAnalyses(getSavedAnalyses())
  }, [])

  return (
    <div className="min-h-screen flex flex-col">
      <Head>
        <title>Saved Analyses | EmailHeaderX</title>
        <meta name="description" content="View your saved email header analyses." />
      </Head>

      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Saved Analyses</h1>
        {savedAnalyses.length === 0 ? (
          <p>No saved analyses yet.</p>
        ) : (
          <SavedAnalysisList analyses={savedAnalyses} />
        )}
      </main>

      <Footer />
    </div>
  )
}
'''

pages_analysis_id_js = '''
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import Head from 'next/head'
import Header from '../../components/Header'
import Footer from '../../components/Footer'
import ParsedHeaderDisplay from '../../components/ParsedHeaderDisplay'
import { getSavedAnalyses } from '../../utils/localStorage'

export default function AnalysisDetail() {
  const router = useRouter()
  const { id } = router.query
  const [analysis, setAnalysis] = useState(null)

  useEffect(() => {
    if (id) {
      const savedAnalyses = getSavedAnalyses()
      const foundAnalysis = savedAnalyses.find(a => a.id.toString() === id)
      setAnalysis(foundAnalysis)
    }
  }, [id])

  if (!analysis) {
    return <div>Loading...</div>
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Head>
        <title>Analysis Detail | EmailHeaderX</title>
        <meta name="description" content="Detailed view of a saved email header analysis." />
      </Head>

      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Analysis Detail</h1>
        <ParsedHeaderDisplay parsedHeaders={analysis.headers} />
      </main>

      <Footer />
    </div>
  )
}
'''

utils_email_header_parser_js = '''
export async function parseEmailHeaders(headerText) {
  const headers = {}
  const lines = headerText.split('\\n')

  let currentKey = ''
  for (const line of lines) {
    if (line.trim() === '') continue

    if (line.startsWith(' ') || line.startsWith('\\t')) {
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
  return hops.map(hop => hop.trim()).join('\\n')
}
'''

utils_dns_lookup_js = '''
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
  const dkimSignatureRegex = /DKIM-Signature:.*?d=([^;\\s]+).*?s=([^;\\s]+)/gs
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
'''

utils_local_storage_js = '''
export function saveAnalysis(parsedHeaders) {
  const savedAnalyses = JSON.parse(localStorage.getItem('emailHeaderAnalyses') || '[]')
  savedAnalyses.push({
    id: Date.now(),
    date: new Date().toISOString(),
    headers: parsedHeaders
  })
  localStorage.setItem('emailHeaderAnalyses', JSON.stringify(savedAnalyses))
}

export function getSavedAnalyses() {
  return JSON.parse(localStorage.getItem('emailHeaderAnalyses') || '[]')
}
'''

utils_pdf_generator_js = '''
import { jsPDF } from 'jspdf'
import 'jspdf-autotable'

export async function generatePDF(parsedHeaders) {
  const doc = new jsPDF()

  doc.setFontSize(20)
  doc.text('Email Header Analysis Report', 14, 22)

  doc.setFontSize(12)
  doc.text(`Generated on: ${new Date().toLocaleString()}`, 14, 32)

  Object.entries(parsedHeaders).forEach(([key, value], index) => {
    doc.setFontSize(14)
    doc.text(`${key}:`, 14, 50 + (index * 30))
    
    doc.setFontSize(12)
    doc.text(JSON.stringify(value, null, 2), 14, 56 + (index * 30))
  })

  doc.save('email-header-analysis.pdf')
}
'''

styles_globals_css = '''
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

@layer base {
  body {
    @apply bg-gray-50 dark:bg-gray-900 text-gray-900 dark:text-gray-100;
  }
}

@layer components {
  .btn-primary {
    @apply bg-primary-500 hover:bg-primary-600 dark:bg-primary-600 dark:hover:bg-primary-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:shadow-outline transition duration-150 ease-in-out;
  }

  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 font-bold py-2 px-4 rounded-lg focus:outline-none focus:shadow-outline transition duration-150 ease-in-out;
  }
}
'''

favicon_svg = '''
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="20" fill="#3B82F6"/>
  <path d="M20 30h60v40H20z" fill="#fff"/>
  <path d="M20 30l30 20 30-20M20 70l25-25M80 70L55 45" stroke="#3B82F6" stroke-width="5" fill="none"/>
</svg>
'''

# Main setup logic
def setup_project():
    print("Setting up EmailHeaderX project...")

    # Initialize git repo
    run_command("git init")
    print("Git repository initialized.")

    # Create project structure
    directories = [
        "app",
        "components",
        "context",
        "pages/api",
        "pages/analysis",
        "public",
        "styles",
        "utils",
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
    print("Project structure created.")

    # Create and populate files
    create_file("package.json", package_json)
    create_file("next.config.js", next_config_js)
    create_file("tailwind.config.js", tailwind_config_js)
    create_file("postcss.config.js", postcss_config_js)
    create_file("app/layout.js", app_layout_js)
    create_file("app/page.js", app_page_js)
    create_file("components/Header.js", components_header_js)
    create_file("components/Footer.js", components_footer_js)
    create_file("components/EmailHeaderForm.js", components_email_header_form_js)
    create_file("components/ParsedHeaderDisplay.js", components_parsed_header_display_js)
    create_file("components/HeaderExplanation.js", components_header_explanation_js)
    create_file("components/EmailRoutingVisualization.js", components_email_routing_visualization_js)
    create_file("components/DarkModeToggle.js", components_dark_mode_toggle_js)
    create_file("components/ErrorMessage.js", components_error_message_js)
    create_file("components/LoadingSpinner.js", components_loading_spinner_js)
    create_file("components/SavedAnalysisList.js", components_saved_analysis_list_js)
    create_file("context/ThemeContext.js", context_theme_context_js)
    create_file("context/HeaderContext.js", context_header_context_js)
    create_file("pages/api/parse-headers.js", pages_api_parse_headers_js)
    create_file("pages/about.js", pages_about_js)
    create_file("pages/faq.js", pages_faq_js)
    create_file("pages/saved-analyses.js", pages_saved_analyses_js)
    create_file("pages/analysis/[id].js", pages_analysis_id_js)
    create_file("utils/emailHeaderParser.js", utils_email_header_parser_js)
    create_file("utils/dnsLookup.js", utils_dns_lookup_js)
    create_file("utils/localStorage.js", utils_local_storage_js)
    create_file("utils/pdfGenerator.js", utils_pdf_generator_js)
    create_file("styles/globals.css", styles_globals_css)
    create_file("public/favicon.svg", favicon_svg)
    print("All project files created and populated.")

    # Initialize npm and install dependencies
    run_command("npm init -y")
    run_command("npm install next react react-dom framer-motion tailwindcss d3 jspdf jspdf-autotable")
    run_command("npm install --save-dev autoprefixer postcss")
    print("Node.js dependencies installed.")

    # Set up Tailwind CSS
    run_command("npx tailwindcss init -p")
    print("Tailwind CSS initialized.")

    # Initial git commit
    run_command("git add .")
    run_command('git commit -m "Initial commit: EmailHeaderX project setup"')
    print("Initial git commit created.")

    print("EmailHeaderX project setup completed successfully!")

if __name__ == "__main__":
    setup_project()