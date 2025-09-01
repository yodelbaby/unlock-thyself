
import React, { useState, useRef, useEffect } from 'react';
import Button from './Button';
import Card from './Card';
import RorschachImage from './RorschachImage';
import { UserResponse } from '../types';

interface TestScreenProps {
  imageIndex: number;
  totalImages: number;
  rorschachKey: number;
  onNext: (response: UserResponse) => void;
  onPrevious: () => void;
  initialResponse?: UserResponse;
}

const placeholders = [
  "e.g. A solitary figure contemplating a vast, empty landscape...",
  "e.g. Two mirrored beasts locked in an eternal struggle...",
  "e.g. The cross-section of a strange, alien fruit...",
  "e.g. A ceremonial mask from a long-forgotten culture...",
  "e.g. An abstract representation of cosmic expansion...",
];

const TestScreen: React.FC<TestScreenProps> = ({ imageIndex, totalImages, rorschachKey, onNext, onPrevious, initialResponse }) => {
  const [response, setResponse] = useState(initialResponse?.text || '');
  const svgRef = useRef<SVGSVGElement>(null);

  useEffect(() => {
    setResponse(initialResponse?.text || '');
  }, [initialResponse, imageIndex]);

  const handleSubmit = () => {
    if (!response.trim()) {
      return;
    }

    let imageDataUrl: string;
    if (initialResponse?.image) {
      imageDataUrl = initialResponse.image;
    } else if (svgRef.current) {
      const svgElement = svgRef.current;
      const serializer = new XMLSerializer();
      const svgString = serializer.serializeToString(svgElement);
      imageDataUrl = `data:image/svg+xml;base64,${btoa(svgString)}`;
    } else {
      console.error("Could not get image data.");
      return;
    }
    onNext({ text: response, image: imageDataUrl });
  };

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault(); // Prevent adding a new line
      if (response.trim()) {
        handleSubmit();
      }
    }
  };

  return (
    <Card className="animate-fade-in">
      <h2 className="text-2xl font-bold text-center text-white mb-2">
        Inkblot {imageIndex + 1} of {totalImages}
      </h2>
      <p className="text-center text-white mb-6">What do you see in the image below?</p>
      
      <div className="bg-black p-4 rounded-lg mb-6 border-4 border-gray-700 shadow-inner">
         {initialResponse?.image ? (
            <img src={initialResponse.image} alt={`Inkblot ${imageIndex + 1}`} className="w-full h-auto bg-white" />
         ) : (
            <RorschachImage ref={svgRef} key={rorschachKey} width={500} height={350} />
         )}
      </div>

      <textarea
        value={response}
        onChange={(e) => setResponse(e.target.value)}
        onKeyDown={handleKeyDown}
        placeholder={placeholders[imageIndex % placeholders.length]}
        className="w-full h-32 p-3 bg-gray-950 border border-gray-600 rounded-lg text-gray-200 focus:ring-2 focus:ring-gray-500 focus:outline-none transition-colors duration-200"
      />
      <div className="mt-6 flex justify-between items-center">
        <div>
          {imageIndex > 0 && (
            <Button onClick={onPrevious} className="bg-transparent text-white border border-white hover:bg-white hover:text-black">
              Previous
            </Button>
          )}
        </div>
        <Button onClick={handleSubmit} disabled={!response.trim()}>
          Next
        </Button>
      </div>
    </Card>
  );
};

export default TestScreen;