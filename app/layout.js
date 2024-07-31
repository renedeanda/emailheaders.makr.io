
import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import { Analytics } from '@vercel/analytics/react';
import Script from 'next/script';
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
        <Script
          strategy="afterInteractive"
          src={`https://www.googletagmanager.com/gtag/js?id=${process.env.NEXT_PUBLIC_GA_ID}`}
        />
        <Script id="google-analytics" strategy="afterInteractive">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', '${process.env.NEXT_PUBLIC_GA_ID}');
          `}
        </Script>
      </head>
      <body className={inter.className}>
        <ThemeProvider>
          <HeaderProvider>
              {children}
              <Analytics />
          </HeaderProvider>
        </ThemeProvider>
      </body>
    </html>
  )
}
