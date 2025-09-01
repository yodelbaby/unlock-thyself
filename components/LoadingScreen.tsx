
import React from 'react';
import Card from './Card';

const LoadingScreen: React.FC = () => {
  const seriousMessages = [
    "Calibrating psychometric apparatus...",
    "Cross-referencing subconscious archetypes...",
    "Synthesizing projective data...",
    "Engaging heuristic analysis protocols...",
    "Mapping cognitive dissonances...",
    "Initializing psycho-cartography...",
  ];

  const [message, setMessage] = React.useState(seriousMessages[0]);

  React.useEffect(() => {
    const intervalId = setInterval(() => {
      setMessage(seriousMessages[Math.floor(Math.random() * seriousMessages.length)]);
    }, 2000);
    return () => clearInterval(intervalId);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  return (
    <Card className="text-center animate-fade-in">
      <div className="flex justify-center items-center mb-6">
        <svg className="animate-spin h-10 w-10 text-gray-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4"></circle>
          <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
        </svg>
      </div>
      <h2 className="text-2xl font-bold text-gray-200 mb-4">Diagnosing...</h2>
      <p className="text-gray-400 transition-opacity duration-500">{message}</p>
    </Card>
  );
};

export default LoadingScreen;