
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import { ModalProvider } from '../components/ModalProvider'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'EmailHeaderX | Advanced Email Header Analysis',
  description: 'Comprehensive email header analysis tool with SPF and DKIM verification. Perfect for IT professionals and security enthusiasts.',
  keywords: 'email header, parser, analyzer, email security, SPF, DKIM, DMARC, DNS lookup',
  openGraph: {
    title: 'EmailHeaderX | Advanced Email Header Analysis',
    description: 'Comprehensive email header analysis with real-time DNS lookups and DKIM verification.',
    type: 'website',
    url: 'https://emailheaders.makr.io',
    image: 'https://emailheaders.makr.io/og-image.jpg',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'EmailHeaderX | Advanced Email Header Analysis',
    description: 'Comprehensive email header analysis with real-time DNS lookups and DKIM verification.',
    image: 'https://emailheaders.makr.io/twitter-image.jpg',
  },
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
      </head>
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
