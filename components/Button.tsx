import React from 'react';

interface ButtonProps {
  onClick: () => void;
  disabled?: boolean;
  children: React.ReactNode;
  className?: string;
}

const Button: React.FC<ButtonProps> = ({ onClick, disabled = false, children, className = '' }) => {
  return (
    <button
      onClick={onClick}
      disabled={disabled}
      className={`
        px-6 py-3 bg-white text-black font-bold rounded-lg shadow-md
        hover:bg-gray-200 focus:outline-none focus:ring-2 focus:ring-white focus:ring-opacity-75
        disabled:bg-gray-800 disabled:text-gray-400 disabled:cursor-not-allowed
        transition-all duration-200 ease-in-out transform hover:scale-105
        ${className}
      `}
    >
      {children}
    </button>
  );
};

export default Button;