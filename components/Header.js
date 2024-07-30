
'use client'

import DarkModeToggle from './DarkModeToggle'
import Link from 'next/link'

export default function Header() {
  return (
    <header className="bg-white dark:bg-gray-800 shadow-md">
      <nav className="container mx-auto px-6 py-3">
        <div className="flex justify-between items-center">
          <Link href="/" className="text-2xl font-bold text-primary-600 dark:text-primary-400">
            EmailHeaderX
          </Link>
          <DarkModeToggle />
        </div>
      </nav>
    </header>
  )
}
