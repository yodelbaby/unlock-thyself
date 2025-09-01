
import React, { useState } from 'react';
import { AppState, Diagnosis, UserResponse } from './types';
import { getGoofyDiagnosis } from './services/geminiService';
import { TOTAL_IMAGES } from './constants';
import StartScreen from './components/StartScreen';
import TestScreen from './components/TestScreen';
import LoadingScreen from './components/LoadingScreen';
import ResultScreen from './components/ResultScreen';

const App: React.FC = () => {
  const [appState, setAppState] = useState<AppState>(AppState.START);
  const [responses, setResponses] = useState<UserResponse[]>([]);
  const [diagnosis, setDiagnosis] = useState<Diagnosis | null>(null);
  const [error, setError] = useState<string>('');
  const [currentImageIndex, setCurrentImageIndex] = useState<number>(0);
  
  // Use a key to force re-mounting of RorschachImage component
  const [rorschachKey, setRorschachKey] = useState<number>(Date.now());

  const handleStart = () => {
    setAppState(AppState.TEST);
    setCurrentImageIndex(0);
    setResponses([]);
    setDiagnosis(null);
    setError('');
    setRorschachKey(Date.now());
  };

  const handleNextResponse = async (response: UserResponse) => {
    const newResponses = [...responses];
    newResponses[currentImageIndex] = response; // Add or update the response
    setResponses(newResponses);

    if (currentImageIndex < TOTAL_IMAGES - 1) {
      setCurrentImageIndex(prev => prev + 1);
      // Only generate a new image if we are moving to a slide that hasn't been visited yet
      if (currentImageIndex + 1 >= newResponses.length) {
        setRorschachKey(Date.now());
      }
    } else {
      setAppState(AppState.DIAGNOSING);
      try {
        const result = await getGoofyDiagnosis(newResponses.map(r => r.text));
        setDiagnosis(result);
        setAppState(AppState.RESULT);
      } catch (err) {
        console.error(err);
        setError('Failed to get a diagnosis. The cosmos is not aligned. Please try again.');
        setAppState(AppState.RESULT);
      }
    }
  };

  const handlePrevious = () => {
    if (currentImageIndex > 0) {
      setCurrentImageIndex(prev => prev - 1);
    }
  };

  const renderContent = () => {
    switch (appState) {
      case AppState.START:
        return <StartScreen onStart={handleStart} />;
      case AppState.TEST:
        return (
          <TestScreen
            imageIndex={currentImageIndex}
            totalImages={TOTAL_IMAGES}
            rorschachKey={rorschachKey}
            onNext={handleNextResponse}
            onPrevious={handlePrevious}
            initialResponse={responses[currentImageIndex]}
          />
        );
      case AppState.DIAGNOSING:
        return <LoadingScreen />;
      case AppState.RESULT:
        return <ResultScreen diagnosis={diagnosis} error={error} onRestart={handleStart} responses={responses} />;
      default:
        return <StartScreen onStart={handleStart} />;
    }
  };

  return (
    <div className="min-h-screen bg-white text-black flex flex-col items-center justify-center p-4 font-sans">
      <div className="w-full max-w-2xl mx-auto">
        {renderContent()}
      </div>
    </div>
  );
};

export default App;