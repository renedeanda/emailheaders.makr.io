
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
