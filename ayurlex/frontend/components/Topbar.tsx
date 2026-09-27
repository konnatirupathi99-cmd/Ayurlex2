import React from 'react';
import { Beaker, Globe } from 'lucide-react';

export default function Topbar({ 
  researchMode, 
  setResearchMode,
  language,
  setLanguage
}: { 
  researchMode: boolean, 
  setResearchMode: (val: boolean) => void,
  language: string,
  setLanguage: (val: string) => void
}) {
  return (
    <header className="h-16 flex items-center justify-between px-6 border-b border-[var(--color-ayur-700)] bg-[var(--color-ayur-800)]/80 backdrop-blur">
      <div className="flex items-center gap-4">
        <h2 className="text-lg font-medium text-white tracking-wide">Research Chat</h2>
      </div>
      
      <div className="flex items-center gap-4">
        <div className="flex items-center gap-2 px-3 py-1.5 bg-[var(--color-ayur-700)] rounded-md border border-[var(--color-ayur-600)]">
          <Globe size={16} className="text-[var(--color-ayur-200)]" />
          <select 
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="bg-transparent text-sm text-[var(--color-ayur-25)] outline-none border-none cursor-pointer"
          >
            <option value="English">English</option>
            <option value="Hindi">Hindi</option>
            <option value="Telugu">Telugu</option>
            <option value="Auto">Auto Detect</option>
          </select>
        </div>
        
        <button 
          onClick={() => setResearchMode(!researchMode)}
          className={`flex items-center gap-2 px-4 py-1.5 rounded-md text-sm font-medium transition-colors border ${
            researchMode 
            ? 'bg-[var(--color-ayur-400)] text-white border-[var(--color-ayur-300)]' 
            : 'bg-[var(--color-ayur-700)] text-[var(--color-ayur-100)] border-[var(--color-ayur-600)] hover:bg-[var(--color-ayur-600)]'
          }`}
        >
          <Beaker size={16} />
          Research Mode
        </button>
      </div>
    </header>
  );
}
