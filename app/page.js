
import { Suspense } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import EmailHeaderForm from '../components/EmailHeaderForm'
import ParsedHeaderDisplay from '../components/ParsedHeaderDisplay'
import LoadingSpinner from '../components/LoadingSpinner'
import DarkModeToggle from '../components/DarkModeToggle'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 dark:from-gray-800 dark:to-gray-900 transition-colors duration-200">
      <Header />
      <main className="container mx-auto px-4 py-8">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100">
            Email Header Analyzer
          </h1>
          <DarkModeToggle />
        </div>
        <Suspense fallback={<LoadingSpinner />}>
          <EmailHeaderForm />
        </Suspense>
        <Suspense fallback={<LoadingSpinner />}>
          <ParsedHeaderDisplay />
        </Suspense>
      </main>
      <Footer />
    </div>
  )
}
