import os

def update_file(file_path, new_content):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w') as file:
        file.write(new_content)
    print(f"Updated {file_path}")

# Update app/page.js
app_page_content = '''
import { Suspense } from 'react'
import Header from '../components/Header'
import Footer from '../components/Footer'
import EmailHeaderForm from '../components/EmailHeaderForm'
import ParsedHeaderDisplay from '../components/ParsedHeaderDisplay'
import SavedAnalyses from '../components/SavedAnalyses'
import LoadingSpinner from '../components/LoadingSpinner'
import PromotionBanner from '../components/PromotionBanner'

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-green-50 dark:from-gray-800 dark:to-gray-900 transition-colors duration-200">
      <Header />
      <PromotionBanner />
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold text-gray-800 dark:text-gray-100 mb-8">
          EmailHeaderX: Advanced Email Header Analysis
        </h1>
        
        <div className="bg-white dark:bg-gray-700 shadow-lg rounded-lg p-6 mb-8">
          <h2 className="text-2xl font-bold mb-4 text-gray-800 dark:text-gray-100">ABOUT EMAIL HEADERS</h2>
          <p className="text-gray-600 dark:text-gray-300">
            EmailHeaderX is a powerful tool that makes email headers human-readable by parsing them according to RFC 822. 
            Email headers are present on every email you receive via the Internet and provide 
            valuable diagnostic information such as routing paths, spam filter results, and authentication details. 
            By understanding email headers, you can:
          </p>
          <ul className="list-disc list-inside mt-2 text-gray-600 dark:text-gray-300">
            <li>Trace the journey of an email from sender to recipient</li>
            <li>Verify the authenticity of emails and detect potential phishing attempts</li>
            <li>Troubleshoot email delivery issues and delays</li>
            <li>Gain insights into email security measures like SPF, DKIM, and DMARC</li>
          </ul>
        </div>

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
'''
update_file('app/page.js', app_page_content)

# Update components/Footer.js
footer_content = '''
export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 mt-12">
      <div className="container mx-auto px-6 py-4">
        <div className="text-center text-gray-500 text-sm py-4">
          &copy; {new Date().getFullYear()} Crafted with 🧡 + 🤖 by the <a href="https://rede.io/?utm_source=emailheaderx" className="text-amber-500 hover:underline">Rede team</a>.
        </div>
      </div>
    </footer>
  )
}
'''
update_file('components/Footer.js', footer_content)

# Create components/PromotionBanner.js
promotion_banner_content = '''
export default function PromotionBanner() {
  return (
    <div className="bg-primary-500 text-white py-2 text-center">
      <a href="https://rede.io/?utm_source=emailheaderx" className="font-bold hover:underline">
        Check out 📚 Rede.io for your daily tech newsletter!
      </a>
    </div>
  )
}
'''
update_file('components/PromotionBanner.js', promotion_banner_content)

print("All files have been updated successfully.")
print("Please review the changes and test your application.")

