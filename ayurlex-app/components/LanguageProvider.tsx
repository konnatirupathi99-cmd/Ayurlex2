"use client";

import React, { createContext, useContext, useState, useEffect } from 'react';

type LanguageCode = 'en' | 'hi' | 'te';

interface LanguageContextType {
  language: LanguageCode;
  setLanguage: (lang: LanguageCode) => void;
  languageName: string;
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

const LANGUAGE_NAMES: Record<LanguageCode, string> = {
  'en': 'English',
  'hi': 'हिन्दी',
  'te': 'తెలుగు'
};

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguageState] = useState<LanguageCode>('en');

  // Hydrate from localStorage if available
  useEffect(() => {
    const saved = localStorage.getItem('ayurlex_language') as LanguageCode;
    if (saved && ['en', 'hi', 'te'].includes(saved)) {
      setLanguageState(saved);
    }
  }, []);

  const setLanguage = (lang: LanguageCode) => {
    setLanguageState(lang);
    localStorage.setItem('ayurlex_language', lang);
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, languageName: LANGUAGE_NAMES[language] }}>
      {children}
    </LanguageContext.Provider>
  );
}

export function useLanguage() {
  const context = useContext(LanguageContext);
  if (context === undefined) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
}
