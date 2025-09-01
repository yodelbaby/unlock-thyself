import React, { useState } from 'react';
import { jsPDF } from 'jspdf';
import Button from './Button';
import Card from './Card';
import { Diagnosis, UserResponse } from '../types';

interface ResultScreenProps {
  diagnosis: Diagnosis | null;
  error: string;
  onRestart: () => void;
  responses: UserResponse[];
}

/**
 * Converts an SVG data URL to a PNG data URL.
 * @param svgDataUrl The `data:image/svg+xml;base64,...` string.
 * @returns A promise that resolves with a PNG data URL.
 */
const svgToPng = (svgDataUrl: string): Promise<string> => {
  return new Promise((resolve, reject) => {
    const img = new Image();

    img.onload = () => {
      const canvas = document.createElement('canvas');
      // Render at a higher resolution for better PDF quality
      const scale = 2;
      canvas.width = img.width * scale;
      canvas.height = img.height * scale;
      const ctx = canvas.getContext('2d');

      if (!ctx) {
        return reject(new Error('Could not get canvas context'));
      }
      
      // Draw the SVG image onto the canvas
      ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
      const pngDataUrl = canvas.toDataURL('image/png');
      resolve(pngDataUrl);
    };

    img.onerror = (err) => {
      reject(new Error(`Failed to load SVG image for conversion: ${err}`));
    };

    img.src = svgDataUrl;
  });
};

const ResultScreen: React.FC<ResultScreenProps> = ({ diagnosis, error, onRestart, responses }) => {
  const [isDownloading, setIsDownloading] = useState(false);

  const handleDownloadPdf = async () => {
    if (!diagnosis || isDownloading) return;

    setIsDownloading(true);
    try {
      const doc = new jsPDF();
      const pageHeight = doc.internal.pageSize.height;
      const pageWidth = doc.internal.pageSize.width;
      const margin = 20;
      let currentY = margin;

      // --- Header ---
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(22);
      doc.text('Psychoanalytical Profile', 105, currentY, { align: 'center' });
      currentY += 20;

      // --- Diagnosis Section ---
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(16);
      const diagnosisTitle = `Diagnosis: ${diagnosis.name}`;
      const titleLines = doc.splitTextToSize(diagnosisTitle, pageWidth - margin * 2);
      const titleDimensions = doc.getTextDimensions(titleLines);
      doc.text(titleLines, margin, currentY);
      currentY += titleDimensions.h + 3; // Precise height + padding

      doc.setFont('helvetica', 'normal');
      doc.setFontSize(12);
      const diagnosisTextLines = doc.splitTextToSize(diagnosis.text, pageWidth - margin * 2);
      const diagnosisTextDimensions = doc.getTextDimensions(diagnosisTextLines);
      doc.text(diagnosisTextLines, margin, currentY);
      currentY += diagnosisTextDimensions.h + 15; // Precise height + padding

      // --- Responses Section ---
      doc.setFont('helvetica', 'bold');
      doc.setFontSize(16);
      doc.text('Patient Interpretations', margin, currentY);
      currentY += 10;

      // Loop through each response to create the two-column layout
      for (const [index, response] of responses.entries()) {
        const pngDataUrl = await svgToPng(response.image);
        
        // --- Define column dimensions and positions ---
        const leftColX = margin;
        const imageWidth = 80;
        const imageHeight = 60;
        
        const rightColX = leftColX + imageWidth + 10;
        const rightColWidth = pageWidth - rightColX - margin;
        
        // --- Calculate precise block heights for page break logic ---
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(12);
        const imageTitleDimensions = doc.getTextDimensions(`Image ${index + 1}`);

        doc.setFont('helvetica', 'normal');
        const responseLines = doc.splitTextToSize(response.text, rightColWidth);
        const responseTextDimensions = doc.getTextDimensions(responseLines);
        
        const imageSectionHeight = imageHeight + imageTitleDimensions.h; // image + title height
        const blockHeight = Math.max(responseTextDimensions.h, imageSectionHeight) + 15; // +15 for padding below

        // Check for page break BEFORE drawing the block
        if (currentY + blockHeight > pageHeight - margin) {
          doc.addPage();
          currentY = margin;
          // Add section header again on new page
          doc.setFont('helvetica', 'bold');
          doc.setFontSize(16);
          doc.text('Patient Interpretations (continued)', margin, currentY);
          currentY += 10;
        }

        // --- Draw Left Column (Title + Image) ---
        doc.setFont('helvetica', 'bold');
        doc.setFontSize(12);
        doc.text(`Image ${index + 1}`, leftColX, currentY);
        const imageYStart = currentY + imageTitleDimensions.h;
        doc.addImage(pngDataUrl, 'PNG', leftColX, imageYStart, imageWidth, imageHeight);

        // --- Calculate vertical alignment for the text ---
        const imageCenterY = imageYStart + (imageHeight / 2);
        let textStartY = imageCenterY - (responseTextDimensions.h / 2);
        textStartY = Math.max(currentY, textStartY); // Prevent text from drawing above the title

        // --- Draw Right Column (Response Text) ---
        doc.setFont('helvetica', 'normal');
        doc.setFontSize(12);
        doc.text(responseLines, rightColX, textStartY);

        // --- Update Y position for the next block ---
        currentY += blockHeight;
      }

      doc.save('psychoanalytical_profile.pdf');
    } catch (err) {
      console.error("Failed to generate PDF:", err);
      // You could add a user-facing error message here
    } finally {
      setIsDownloading(false);
    }
  };

  return (
    <Card className="animate-fade-in">
      <h2 className="text-3xl font-extrabold text-center text-white mb-6">
        Your Diagnosis
      </h2>
      {error ? (
        <div className="text-center text-gray-200 bg-gray-800 p-4 rounded-lg">
          <p className="font-bold">An Error Occurred</p>
          <p>{error}</p>
        </div>
      ) : diagnosis ? (
        <div className="text-gray-300">
            <h3 className="text-lg font-bold text-gray-400 mb-2">
                Diagnosis: <span className="text-gray-200 font-semibold">{diagnosis.name}</span>
            </h3>
            <p className="text-xl whitespace-pre-wrap">{diagnosis.text}</p>
        </div>
      ) : null}
      <div className="mt-8 flex justify-center items-center gap-4">
        <Button 
          onClick={handleDownloadPdf} 
          disabled={!diagnosis || isDownloading} 
          className="bg-transparent text-white border border-white hover:bg-white hover:text-black"
        >
          {isDownloading ? 'Generating...' : 'Download PDF'}
        </Button>
        
      </div>
    </Card>
  );
};

export default ResultScreen;