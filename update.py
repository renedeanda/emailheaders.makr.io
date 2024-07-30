import os

def update_file(file_path, new_content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(new_content)
    print(f"Updated {file_path}")

# Update Modal.js
modal_content = '''
import { useEffect } from 'react';
import { createPortal } from 'react-dom';
import { motion, AnimatePresence } from 'framer-motion';

export default function Modal({ isOpen, onClose, children }) {
  useEffect(() => {
    const handleEscape = (event) => {
      if (event.key === 'Escape') {
        onClose();
      }
    };

    if (isOpen) {
      document.addEventListener('keydown', handleEscape);
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleEscape);
      document.body.style.overflow = '';
    };
  }, [isOpen, onClose]);

  return createPortal(
    <AnimatePresence>
      {isOpen && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          exit={{ opacity: 0 }}
          onClick={onClose}
          className="fixed inset-0 bg-black bg-opacity-50 z-50 flex justify-center items-center"
        >
          <motion.div
            initial={{ y: -50, opacity: 0 }}
            animate={{ y: 0, opacity: 1 }}
            exit={{ y: -50, opacity: 0 }}
            onClick={(e) => e.stopPropagation()}
            className="bg-white dark:bg-gray-800 rounded-lg p-6 max-w-lg w-full mx-4"
          >
            {children}
          </motion.div>
        </motion.div>
      )}
    </AnimatePresence>,
    document.body
  );
}
'''
update_file('components/Modal.js', modal_content)

# Create ModalProvider.js
modal_provider_content = '''
import React, { createContext, useContext, useState } from 'react';
import Modal from './Modal';

const ModalContext = createContext();

export function ModalProvider({ children }) {
  const [modalContent, setModalContent] = useState(null);

  const openModal = (content) => setModalContent(content);
  const closeModal = () => setModalContent(null);

  return (
    <ModalContext.Provider value={{ openModal, closeModal }}>
      {children}
      <Modal isOpen={!!modalContent} onClose={closeModal}>
        {modalContent}
      </Modal>
    </ModalContext.Provider>
  );
}

export const useModal = () => useContext(ModalContext);
'''
update_file('components/ModalProvider.js', modal_provider_content)

# Update SavedAnalyses.js
saved_analyses_content = '''
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
'''
update_file('components/SavedAnalyses.js', saved_analyses_content)

# Update app/layout.js
app_layout_content = '''
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import { ModalProvider } from '../components/ModalProvider'
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
            <ModalProvider>
              {children}
            </ModalProvider>
          </HeaderProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
'''
update_file('app/layout.js', app_layout_content)

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

print("All files have been updated successfully.")
print("Please review the changes and test your application.")

