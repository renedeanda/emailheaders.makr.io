
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
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
            {children}
          </HeaderProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
