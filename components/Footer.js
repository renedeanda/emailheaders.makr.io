
export default function Footer() {
  return (
    <footer className="bg-gray-100 dark:bg-gray-800 mt-12">
      <div className="container mx-auto px-6 py-4">
        <div className="text-center text-gray-500 text-sm py-4">
          &copy; {new Date().getFullYear()} Crafted with 🧡 + 🤖 by the <a href="https://rede.io/?utm_source=emailheaders" className="text-amber-500 hover:underline">Rede team</a>.
        </div>
      </div>
    </footer>
  )
}
