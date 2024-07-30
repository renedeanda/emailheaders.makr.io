
export function saveAnalysis(parsedHeaders) {
  const savedAnalyses = JSON.parse(localStorage.getItem('emailHeaderAnalyses') || '[]')
  savedAnalyses.push({
    id: Date.now(),
    date: new Date().toISOString(),
    headers: parsedHeaders
  })
  localStorage.setItem('emailHeaderAnalyses', JSON.stringify(savedAnalyses))
}

export function getSavedAnalyses() {
  return JSON.parse(localStorage.getItem('emailHeaderAnalyses') || '[]')
}
