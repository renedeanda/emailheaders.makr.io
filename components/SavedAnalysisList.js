
import Link from 'next/link'

export default function SavedAnalysisList({ analyses }) {
  return (
    <ul className="space-y-4">
      {analyses.map((analysis) => (
        <li key={analysis.id} className="bg-white dark:bg-gray-800 shadow-md rounded-lg p-6">
          <h2 className="text-xl font-semibold mb-2">
            Analysis from {new Date(analysis.date).toLocaleString()}
          </h2>
          <p className="text-gray-600 dark:text-gray-300 mb-4">
            From: {analysis.headers.From}
            <br />
            Subject: {analysis.headers.Subject}
          </p>
          <Link 
            href={`/analysis/${analysis.id}`}
            className="text-primary-500 hover:text-primary-600 dark:text-primary-400 dark:hover:text-primary-500"
          >
            View full analysis
          </Link>
        </li>
      ))}
    </ul>
  )
}
