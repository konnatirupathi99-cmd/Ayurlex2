"use client";

import React, { createContext, useContext, useState, useEffect } from 'react';
import englishDict from '../locales/en/ui.json';

type LanguageCode = 'en' | 'hi' | 'sa' | 'mr' | 'ta' | 'te' | 'kn' | 'ml' | 'bn' | 'gu' | 'pa' | 'or' | 'ur' | 'ne' | 'si' | 'fr';

interface LanguageContextType {
  language: LanguageCode;
  setLanguage: (lang: LanguageCode) => void;
  languageName: string;
  t: (key: string) => string;
}

const LanguageContext = createContext<LanguageContextType | undefined>(undefined);

export const LANGUAGE_NAMES: Record<LanguageCode, string> = {
  'en': 'English',
  'hi': 'हिन्दी',
  'sa': 'संस्कृतम्',
  'mr': 'मराठी',
  'ta': 'தமிழ்',
  'te': 'తెలుగు',
  'kn': 'ಕನ್ನಡ',
  'ml': 'മലയാളം',
  'bn': 'বাংলা',
  'gu': 'ગુજરાતી',
  'pa': 'ਪੰਜਾਬੀ',
  'or': 'ଓଡ଼ିଆ',
  'ur': 'اردو',
  'ne': 'नेपाली',
  'si': 'සිංහල',
  'fr': 'Français'
};

export function LanguageProvider({ children }: { children: React.ReactNode }) {
  const [language, setLanguageState] = useState<LanguageCode>('en');
  const [dict, setDict] = useState<Record<string, any>>(englishDict);

  // Hydrate from localStorage if available
  useEffect(() => {
    const saved = localStorage.getItem('ayurlex_language') as LanguageCode;
    if (saved && Object.keys(LANGUAGE_NAMES).includes(saved)) {
      setLanguageState(saved);
    }
  }, []);

  useEffect(() => {
    if (language === 'en') {
      setDict(englishDict);
      return;
    }
    
    // Dynamically load the language resource
    import(`../locales/${language}/ui.json`)
      .then((module) => {
        setDict(module.default || module);
      })
      .catch((err) => {
        console.error(`Failed to load language resources for ${language}`, err);
        setDict(englishDict); // fallback
      });
  }, [language]);

  const setLanguage = (lang: LanguageCode) => {
    setLanguageState(lang);
    localStorage.setItem('ayurlex_language', lang);
  };

  const t = (key: string): string => {
    const keys = key.split('.');
    let value: any = dict;
    
    for (const k of keys) {
      if (value === undefined) break;
      value = value[k];
    }
    
    if (typeof value !== 'string') {
      value = englishDict;
      for (const k of keys) {
        if (value === undefined) break;
        value = value[k];
      }
    }
    
    return typeof value === 'string' ? value : key;
  };

  return (
    <LanguageContext.Provider value={{ language, setLanguage, languageName: LANGUAGE_NAMES[language], t }}>
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
