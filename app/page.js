
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
