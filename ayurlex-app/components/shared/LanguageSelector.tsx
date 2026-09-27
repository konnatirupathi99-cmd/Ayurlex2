import React, { useState } from 'react';
import { Globe, ChevronDown } from 'lucide-react';

export const LanguageSelector: React.FC = () => {
  const [isOpen, setIsOpen] = useState(false);
  const [language, setLanguage] = useState('English');
  const languages = ['English', 'हिंदी', 'संस्कृत', 'தமிழ்'];

  return (
    <div className="relative">
      <button 
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-3 py-1.5 rounded-md text-sm font-medium text-botanical-100 hover:text-botanical-50 hover:bg-botanical-800 transition-colors"
      >
        <Globe size={16} />
        <span className="hidden sm:inline">{language}</span>
        <ChevronDown size={14} className={`transition-transform ${isOpen ? 'rotate-180' : ''}`} />
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-32 bg-botanical-800 border border-botanical-600 rounded-lg shadow-lg overflow-hidden z-50 language-menu">
          {languages.map(lang => (
            <button
              key={lang}
              onClick={() => {
                setLanguage(lang);
                setIsOpen(false);
              }}
              className="w-full text-left px-4 py-2 text-sm text-botanical-100 hover:bg-botanical-700 hover:text-botanical-50 transition-colors"
            >
              {lang}
            </button>
          ))}
        </div>
      )}
    </div>
  );
};
