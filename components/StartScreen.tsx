import React from 'react';
import Button from './Button';
import Card from './Card';

interface StartScreenProps {
  onStart: () => void;
}

const StartScreen: React.FC<StartScreenProps> = ({ onStart }) => {
  return (
    <Card className="text-center animate-fade-in">
      <h1 className="text-4xl sm:text-5xl font-extrabold text-white mb-4">
        Unlock Thyself
      </h1>
      <p className="text-gray-300 mb-8 text-lg">
        Learn about your inner self through a short inkblot analysis.
      </p>
      <Button onClick={onStart}>
        Begin Analysis
      </Button>
    </Card>
  );
};

export default StartScreen;