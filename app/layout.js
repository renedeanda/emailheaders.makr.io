import { Inter } from 'next/font/google'
import { ThemeProvider } from '../context/ThemeContext'
import { HeaderProvider } from '../context/HeaderContext'
import { Analytics } from '@vercel/analytics/react'
import Script from 'next/script'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata = {
  title: 'Free Email Header Analyzer - Parse & Verify Email Headers Instantly',
  description: 'Analyze email headers for security issues, trace email paths, and verify SPF/DKIM records. Free professional tool for email forensics and troubleshooting.',
  keywords: 'email header analyzer, email parser, email security, SPF DKIM checker, email forensics, email troubleshooting',
  openGraph: {
    title: 'Free Email Header Analyzer - Parse & Verify Email Headers',
    description: 'Analyze email headers for security issues, trace email paths, and verify SPF/DKIM records. Free professional email forensics tool.',
    type: 'website',
    url: 'https://emailheaders.makr.io',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Free Email Header Analyzer - Parse & Verify Email Headers',
    description: 'Analyze email headers for security issues, trace email paths, and verify SPF/DKIM records. Free professional email forensics tool.',
  },
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.svg" type="image/svg+xml" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              "@context": "https://schema.org",
              "@type": "WebApplication",
              name: "Email Header Analyzer",
              description: "Free email header analysis tool for parsing email headers, verifying SPF/DKIM records, and email security forensics",
              url: "https://emailheaders.makr.io",
              applicationCategory: "SecurityApplication",
              offers: {
                "@type": "Offer",
                price: "0",
                priceCurrency: "USD"
              },
              provider: {
                "@type": "Organization",
                name: "MAKR.io",
                url: "https://makr.io"
              },
              featureList: [
                "Email header parsing",
                "SPF record verification",
                "DKIM record checking",
                "Email path tracing",
                "Security analysis",
                "Free to use"
              ]
            })
          }}
        />
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