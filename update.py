import os

def update_file(file_path, new_content):
    if os.path.exists(file_path):
        with open(file_path, 'w') as file:
            file.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"File not found: {file_path}")

# Update app/page.js
app_page_content = '''
import { Suspense } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import EmailHeaderForm from '../components/EmailHeaderForm'
import ParsedHeaderDisplay from '../components/ParsedHeaderDisplay'
import SavedAnalyses from '../components/SavedAnalyses'
import LoadingSpinner from '../components/LoadingSpinner'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 dark:from-gray-800 dark:to-gray-900 transition-colors duration-200">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100 mb-8">
          Email Header Analyzer
        </h1>
        <Suspense fallback={<LoadingSpinner />}>
          <EmailHeaderForm />
        </Suspense>
        <Suspense fallback={<LoadingSpinner />}>
          <ParsedHeaderDisplay />
        </Suspense>
        <Suspense fallback={<LoadingSpinner />}>
          <SavedAnalyses />
        </Suspense>
      </main>
      <Footer />
    </div>
  )
}
'''
update_file('app/page.js', app_page_content)

# Update components/Header.js
header_content = '''
'use client'
import Link from 'next/link'
import DarkModeToggle from './DarkModeToggle'

export default function Header() {
  return (
    <header className="bg-white dark:bg-gray-800 shadow-md">
      <nav className="container mx-auto px-6 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-primary-600 dark:text-primary-400">
            EmailHeaderX
          </Link>
          <DarkModeToggle />
        </div>
      </nav>
    </header>
  )
}
'''
update_file('components/Header.js', header_content)

# Update components/DarkModeToggle.js
dark_mode_toggle_content = '''
'use client'
import { useTheme } from '../context/ThemeContext'

export default function DarkModeToggle() {
  const { theme, toggleTheme } = useTheme()

  return (
    <div className="flex items-center">
      <span className="mr-2 text-sm text-gray-600 dark:text-gray-300">
        {theme === 'dark' ? 'Dark' : 'Light'}
      </span>
      <div
        className="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in"
      >
        <input
          type="checkbox"
          name="toggle"
          id="toggle"
          checked={theme === 'dark'}
          onChange={toggleTheme}
          className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer"
        />
        <label
          htmlFor="toggle"
          className="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"
        ></label>
      </div>
    </div>
  )
}
'''
update_file('components/DarkModeToggle.js', dark_mode_toggle_content)

# Update styles/globals.css
globals_css_content = '''
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
    @apply bg-primary-500 hover:bg-primary-600 dark:bg-primary-600 dark:hover:bg-primary-700 text-white font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-opacity-50 transition duration-150 ease-in-out;
  }

  .btn-secondary {
    @apply bg-gray-200 hover:bg-gray-300 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-800 dark:text-gray-200 font-bold py-2 px-4 rounded-lg focus:outline-none focus:ring-2 focus:ring-gray-400 focus:ring-opacity-50 transition duration-150 ease-in-out;
  }

  .toggle-checkbox:checked {
    @apply right-0 border-primary-500;
  }
  .toggle-checkbox:checked + .toggle-label {
    @apply bg-primary-500;
  }
}
'''
update_file('app/globals.css', globals_css_content)

# Update utils/dnsLookup.js
dns_lookup_content = '''
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
      explanation += `\n- Includes the SPF record of ${mech.split(':')[1]}`;
    } else if (mech.startsWith('a')) {
      explanation += '\n- Allows the domain\'s A record';
    } else if (mech.startsWith('mx')) {
      explanation += '\n- Allows the domain\'s MX records';
    } else if (mech.startsWith('ip4:') || mech.startsWith('ip6:')) {
      explanation += `\n- Allows the IP address ${mech.split(':')[1]}`;
    } else if (mech === '-all') {
      explanation += '\n- Fails any other servers not listed (strict)';
    } else if (mech === '~all') {
      explanation += '\n- Softly fails any other servers not listed (lenient)';
    }
  });
  return explanation;
}

// Existing verifyDKIM function here
'''
update_file('utils/dnsLookup.js', dns_lookup_content)

# Update components/ParsedHeaderDisplay.js
parsed_header_display_content = '''
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

  const renderHeaderValue = (key, value) => {
    if (key === 'SPF') {
      return (
        <div className="bg-gray-100 dark:bg-gray-700 p-4 rounded-md">
          <p className="font-semibold">{value.status === 'found' ? 'SPF Record Found' : 'SPF Record Not Found'}</p>
          {value.status === 'found' && (
            <>
              <p className="mt-2"><span className="font-semibold">Record:</span> {value.record}</p>
              <p className="mt-2"><span className="font-semibold">Mechanisms:</span></p>
              <ul className="list-disc list-inside ml-4">
                {value.mechanisms.map((mech, index) => (
                  <li key={index}>{mech}</li>
                ))}
              </ul>
            </>
          )}
          <p className="mt-2"><span className="font-semibold">Explanation:</span> {value.explanation}</p>
        </div>
      )
    } else if (key === 'DKIM' && Array.isArray(value)) {
      return (
        <div>
          {value.map((dkimResult, index) => (
            <div key={index} className="bg-gray-100 dark:bg-gray-700 p-4 rounded-md mb-2">
              <p><span className="font-semibold">Selector:</span> {dkimResult.selector}</p>
              <p><span className="font-semibold">Domain:</span> {dkimResult.domain}</p>
              <p><span className="font-semibold">Result:</span> 
                <span className={dkimResult.result === 'pass' ? 'text-green-600 dark:text-green-400' : 'text-red-600 dark:text-red-400'}>
                  {dkimResult.result}
                </span>
              </p>
            </div>
          ))}
        </div>
      )
    } else {
      return <p className="break-words">{JSON.stringify(value, null, 2)}</p>
    }
  }

  return (
    <motion.div
      className="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6 mb-8"
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
          {renderHeaderValue(key, value)}
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
update_file('components/ParsedHeaderDisplay.js', parsed_header_display_content)

# Create components/SavedAnalyses.js
saved_analyses_content = '''
'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { getSavedAnalyses } from '../utils/localStorage'

export default function SavedAnalyses() {
  const [savedAnalyses, setSavedAnalyses] = useState([])

  useEffect(() => {
    setSavedAnalyses(getSavedAnalyses())
  }, [])

  return (
    <motion.div
      className="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6"
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay: 0.2 }}
    >
      <h2 className="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">Saved Analyses</h2>
      {savedAnalyses.length === 0 ? (
        <p className="text-gray-600 dark:text-gray-300">No saved analyses yet.</p>
      ) : (
        <ul className="space-y-4">
          {savedAnalyses.map((analysis) => (
            <li key={analysis.id} className="bg-gray-100 dark:bg-gray-700 p-4 rounded-md">
              <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200">
                Analysis from {new Date(analysis.date).toLocaleString()}
              </h3>
              <p className="text-gray-600 dark:text-gray-300 mt-2">
                From: {analysis.headers.From}
                <br />
                Subject: {analysis.headers.Subject}
              </p>
              <button
                onClick={() => {/* Implement view full analysis functionality */}}
                className="mt-2 text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
              >
                View full analysis
              </button>
            </li>
          ))}
        </ul>
      )}
    </motion.div>
  )
}
'''
update_file('components/SavedAnalyses.js', saved_analyses_content)

# Remove unused files
files_to_remove = [
    'pages/about.js',
    'pages/faq.js',
    'pages/saved-analyses.js',
    'pages/analysis/[id].js',
]

for file_path in files_to_remove:
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Removed {file_path}")
    else:
        print(f"File not found: {file_path}")

# Update tailwind.config.js to ensure dark mode is working correctly
tailwind_config_content = '''
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
update_file('tailwind.config.js', tailwind_config_content)

# Update context/ThemeContext.js to ensure it's working with the new toggle
theme_context_content = '''
'use client'
import React, { createContext, useContext, useState, useEffect } from 'react'

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
  const context = useContext(ThemeContext)
  if (context === undefined) {
    throw new Error('useTheme must be used within a ThemeProvider')
  }
  return context
}
'''
update_file('context/ThemeContext.js', theme_context_content)

# Update app/layout.js to ensure ThemeProvider is properly set up
app_layout_content = '''
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'EmailHeaderX | Advanced Email Header Analysis',
  description: 'Comprehensive email header analysis tool with SPF, DKIM, and DMARC verification.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
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
update_file('app/layout.js', app_layout_content)

# Update components/Footer.js to remove unnecessary links
footer_content = '''
export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 mt-12">
      <div className="container mx-auto px-6 py-4">
        <p className="text-center text-gray-600 dark:text-gray-300 text-sm">
          © {new Date().getFullYear()} EmailHeaderX. All rights reserved.
        </p>
      </div>
    </footer>
  )
}
'''
update_file('components/Footer.js', footer_content)

print("All updates completed successfully!")

# Additional cleanup
print("\nPerforming additional cleanup...")

# Remove any remaining references to removed pages in other files
files_to_check = [
    'app/page.js',
    'components/Header.js',
    'components/Footer.js',
]

for file_path in files_to_check:
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        
        # Remove import statements and links to removed pages
        content = content.replace("import Link from 'next/link'", "")
        content = content.replace('<Link href="/about"', '<!-- <Link href="/about"')
        content = content.replace('<Link href="/faq"', '<!-- <Link href="/faq"')
        content = content.replace('<Link href="/saved-analyses"', '<!-- <Link href="/saved-analyses"')
        content = content.replace('</Link>', '</Link> -->')
        
        with open(file_path, 'w') as file:
            file.write(content)
        
        print(f"Cleaned up references in {file_path}")
    else:
        print(f"File not found: {file_path}")

print("\nScript execution completed. Please review the changes and test your application.")