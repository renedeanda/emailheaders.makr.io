
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
