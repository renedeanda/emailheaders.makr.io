
'use client'
import { useState, useEffect } from 'react'
import { motion } from 'framer-motion'
import { getSavedAnalyses } from '../utils/localStorage'
import { useModal } from './ModalProvider'

export default function SavedAnalyses() {
  const [savedAnalyses, setSavedAnalyses] = useState([])
  const { openModal } = useModal()

  useEffect(() => {
    setSavedAnalyses(getSavedAnalyses())
  }, [])

  const handleViewAnalysis = (analysis) => {
    openModal(
      <div>
        <h2 className="text-xl font-bold mb-4">Analysis Details</h2>
        <pre className="whitespace-pre-wrap overflow-x-auto">
          {JSON.stringify(analysis.headers, null, 2)}
        </pre>
      </div>
    )
  }

  return (
    <motion.div
      className="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6 mt-8"
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
                onClick={() => handleViewAnalysis(analysis)}
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
