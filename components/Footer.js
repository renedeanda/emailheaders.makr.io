
export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 mt-12">
      <div className="container mx-auto px-6 py-4">
        <p className="text-center text-gray-600 dark:text-gray-300 text-sm">
          © {new Date().getFullYear()} EmailHeaderX. All rights reserved.
        </p>
      </div>
    </footer>
  )
}
