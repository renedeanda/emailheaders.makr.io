import os

def update_file(file_path, new_content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(new_content)
    print(f"Updated {file_path}")

dns_lookup_content = '''
import dns from 'dns';
import { promisify } from 'util';

const resolveTxt = promisify(dns.resolveTxt);

export async function lookupSPF(fromDomain) {
  try {
    const domain = fromDomain.split('@')[1];
    if (!domain) {
      throw new Error('Invalid email format');
    }
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
        explanation: `No SPF record found for the domain ${domain}.`
      };
    }
  } catch (error) {
    console.error('SPF lookup error:', error);
    if (error.code === 'ENOTFOUND') {
      return {
        status: 'error',
        explanation: `Domain not found: ${fromDomain.split('@')[1]}. Please check if the domain is correct.`
      };
    } else if (error.code === 'ECONNREFUSED') {
      return {
        status: 'error',
        explanation: 'Connection to DNS server was refused. There might be network issues.'
      };
    } else {
      return {
        status: 'error',
        explanation: `SPF lookup failed: ${error.message}. There might be an issue with the DNS server or the domain configuration.`
      };
    }
  }
}

function interpretSPF(mechanisms) {
  let explanation = 'This SPF record:';
  mechanisms.forEach(mech => {
    if (mech.startsWith('include:')) {
      explanation += `\\n- Includes the SPF record of ${mech.split(':')[1]}`;
    } else if (mech.startsWith('a')) {
      explanation += `\\n- Allows the domain's A record`;
    } else if (mech.startsWith('mx')) {
      explanation += `\\n- Allows the domain's MX records`;
    } else if (mech.startsWith('ip4:') || mech.startsWith('ip6:')) {
      explanation += `\\n- Allows the IP address ${mech.split(':')[1]}`;
    } else if (mech === '-all') {
      explanation += `\\n- Fails any other servers not listed (strict)`;
    } else if (mech === '~all') {
      explanation += `\\n- Softly fails any other servers not listed (lenient)`;
    }
  });
  return explanation;
}

export async function verifyDKIM(headerText) {
  const dkimResults = [];
  const dkimSignatureRegex = /DKIM-Signature:.*?d=([^;\\s]+).*?s=([^;\\s]+)/gs;
  let match;

  while ((match = dkimSignatureRegex.exec(headerText)) !== null) {
    const [, domain, selector] = match;
    try {
      const dkimRecord = await resolveTxt(`${selector}._domainkey.${domain}`);
      dkimResults.push({
        selector,
        domain,
        result: dkimRecord ? 'pass' : 'fail',
      });
    } catch (error) {
      console.error('DKIM lookup error:', error);
      dkimResults.push({
        selector,
        domain,
        result: 'lookup failed',
      });
    }
  }

  return dkimResults.length > 0 ? dkimResults : [{ selector: 'N/A', domain: 'N/A', result: 'No DKIM signature found' }];
}
'''

saved_analyses_content = '''
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
'''

update_file('utils/dnsLookup.js', dns_lookup_content)
update_file('components/SavedAnalyses.js', saved_analyses_content)

# Update ParsedHeaderDisplay.js to handle the improved SPF lookup results
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
      className="bg-white dark:bg-gray-800 shadow-lg rounded-lg p-6"
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

print("Files have been updated successfully.")
print("Please review the changes and test your application.")
              