
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
