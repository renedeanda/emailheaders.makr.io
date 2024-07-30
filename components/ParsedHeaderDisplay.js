
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
