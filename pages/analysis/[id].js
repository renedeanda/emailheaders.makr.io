
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import Head from 'next/head'
import Header from '../../components/Header'
import Footer from '../../components/Footer'
import ParsedHeaderDisplay from '../../components/ParsedHeaderDisplay'
import { getSavedAnalyses } from '../../utils/localStorage'

export default function AnalysisDetail() {
  const router = useRouter()
  const { id } = router.query
  const [analysis, setAnalysis] = useState(null)

  useEffect(() => {
    if (id) {
      const savedAnalyses = getSavedAnalyses()
      const foundAnalysis = savedAnalyses.find(a => a.id.toString() === id)
      setAnalysis(foundAnalysis)
    }
  }, [id])

  if (!analysis) {
    return <div>Loading...</div>
  }

  return (
    <div className="min-h-screen flex flex-col">
      <Head>
        <title>Analysis Detail | EmailHeaderX</title>
        <meta name="description" content="Detailed view of a saved email header analysis." />
      </Head>

      <Header />

      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-8">Analysis Detail</h1>
        <ParsedHeaderDisplay parsedHeaders={analysis.headers} />
      </main>

      <Footer />
    </div>
  )
}
