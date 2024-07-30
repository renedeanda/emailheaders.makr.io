
import { jsPDF } from 'jspdf'
import 'jspdf-autotable'

export async function generatePDF(parsedHeaders) {
  const doc = new jsPDF()

  // Set colors
  const primaryColor = '#0056e0'
  const secondaryColor = '#4d94ff'

  // Title
  doc.setFontSize(24)
  doc.setTextColor(primaryColor)
  doc.text('Email Header Analysis Report', 14, 22)

  // Date
  doc.setFontSize(12)
  doc.setTextColor(secondaryColor)
  doc.text(`Generated on: ${new Date().toLocaleString()}`, 14, 32)

  // Headers
  let yPos = 50
  Object.entries(parsedHeaders).forEach(([key, value]) => {
    doc.setFontSize(14)
    doc.setTextColor(primaryColor)
    doc.text(`${key}:`, 14, yPos)
    yPos += 6

    doc.setFontSize(10)
    doc.setTextColor('#000000')

    if (key === 'DKIM' && Array.isArray(value)) {
      value.forEach((dkimResult, index) => {
        Object.entries(dkimResult).forEach(([dkimKey, dkimValue]) => {
          const text = `${dkimKey}: ${dkimValue}`
          const textLines = doc.splitTextToSize(text, 180)
          doc.text(textLines, 14, yPos)
          yPos += textLines.length * 5
        })
        if (index < value.length - 1) {
          yPos += 5 // Add space between DKIM entries
        }
      })
    } else {
      const text = typeof value === 'object' ? JSON.stringify(value, null, 2) : value.toString()
      const textLines = doc.splitTextToSize(text, 180)
      doc.text(textLines, 14, yPos)
      yPos += textLines.length * 5
    }

    yPos += 10 // Add space between header entries
    
    // Add a new page if we're near the bottom
    if (yPos > 280) {
      doc.addPage()
      yPos = 20
    }
  })

  doc.save('email-header-analysis.pdf')
}
