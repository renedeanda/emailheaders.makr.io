
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
