
'use client'
import { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { getSavedAnalyses } from '../utils/localStorage'

export default function SavedAnalyses() {
  const [savedAnalyses, setSavedAnalyses] = useState([])
  const [selectedAnalysis, setSelectedAnalysis] = useState(null)

  useEffect(() => {
    setSavedAnalyses(getSavedAnalyses())
  }, [])

  const openModal = (analysis) => {
    setSelectedAnalysis(analysis)
  }

  const closeModal = () => {
    setSelectedAnalysis(null)
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
                onClick={() => openModal(analysis)}
                className="mt-2 text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
              >
                View full analysis
              </button>
            </li>
          ))}
        </ul>
      )}

      <AnimatePresence>
        {selectedAnalysis && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4"
            onClick={closeModal}
          >
            <motion.div
              initial={{ y: -50, opacity: 0 }}
              animate={{ y: 0, opacity: 1 }}
              exit={{ y: 50, opacity: 0 }}
              className="bg-white dark:bg-gray-800 p-6 rounded-lg max-w-2xl w-full max-h-[90vh] overflow-y-auto"
              onClick={(e) => e.stopPropagation()}
            >
              <h2 className="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">
                Full Analysis
              </h2>
              {Object.entries(selectedAnalysis.headers).map(([key, value]) => (
                <div key={key} className="mb-4">
                  <h3 className="text-lg font-semibold text-gray-700 dark:text-gray-200">{key}</h3>
                  <p className="text-gray-600 dark:text-gray-300 whitespace-pre-wrap">{JSON.stringify(value, null, 2)}</p>
                </div>
              ))}
              <button
                onClick={closeModal}
                className="mt-4 bg-primary-500 hover:bg-primary-600 text-white font-bold py-2 px-4 rounded"
              >
                Close
              </button>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </motion.div>
  )
}
