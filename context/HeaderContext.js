
'use client'
import { createContext, useContext, useState } from 'react'

const HeaderContext = createContext()

export function HeaderProvider({ children }) {
  const [parsedHeaders, setParsedHeaders] = useState(null)

  return (
    <HeaderContext.Provider value={{ parsedHeaders, setParsedHeaders }}>
      {children}
    </HeaderContext.Provider>
  )
}

export function useHeaderContext() {
  return useContext(HeaderContext)
}
