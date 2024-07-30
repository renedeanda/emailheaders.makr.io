
import { jsPDF } from 'jspdf'
import 'jspdf-autotable'

export async function generatePDF(parsedHeaders) {
  const doc = new jsPDF()

  doc.setFontSize(20)
  doc.text('Email Header Analysis Report', 14, 22)

  doc.setFontSize(12)
  doc.text(`Generated on: ${new Date().toLocaleString()}`, 14, 32)

  Object.entries(parsedHeaders).forEach(([key, value], index) => {
    doc.setFontSize(14)
    doc.text(`${key}:`, 14, 50 + (index * 30))
    
    doc.setFontSize(12)
    doc.text(JSON.stringify(value, null, 2), 14, 56 + (index * 30))
  })

  doc.save('email-header-analysis.pdf')
}
