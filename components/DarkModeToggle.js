
'use client'
import { useTheme } from '../context/ThemeContext'

export default function DarkModeToggle() {
  const { theme, toggleTheme } = useTheme()

  return (
    <div className="flex items-center">
      <span className="mr-2 text-sm text-gray-600 dark:text-gray-300">
        {theme === 'dark' ? 'Dark' : 'Light'}
      </span>
      <div
        className="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in"
      >
        <input
          type="checkbox"
          name="toggle"
          id="toggle"
          checked={theme === 'dark'}
          onChange={toggleTheme}
          className="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer"
        />
        <label
          htmlFor="toggle"
          className="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer"
        ></label>
      </div>
    </div>
  )
}
