
import React from 'react';

interface CardProps {
  children: React.ReactNode;
  className?: string;
}

const Card: React.FC<CardProps> = ({ children, className = '' }) => {
  return (
    <div
      className={`
        bg-black border border-gray-700 rounded-xl shadow-lg 
        p-6 sm:p-8 transition-all duration-300
        ${className}
      `}
    >
      {children}
    </div>
  );
};

export default Card;