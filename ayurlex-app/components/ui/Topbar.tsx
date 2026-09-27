import React from 'react';
import { Menu, Search } from 'lucide-react';
import { LanguageSelector } from '../shared/LanguageSelector';

interface TopbarProps {
  onMenuClick: () => void;
  modelStatus: 'ready' | 'processing' | 'error';
}

export const Topbar: React.FC<TopbarProps> = ({ onMenuClick, modelStatus }) => {
  return (
    <header className="h-16 flex items-center justify-between px-4 bg-botanical-900 border-b border-botanical-600 sticky top-0 z-30">
      <div className="flex items-center gap-4">
        <button 
          onClick={onMenuClick}
          className="md:hidden text-botanical-100 hover:text-botanical-50 transition-colors p-1"
        >
          <Menu size={24} />
        </button>
        <div className="flex items-center gap-2">
          <span className="text-sm font-medium text-botanical-100 hidden sm:inline-block">Model Status:</span>
          <div className="flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-botanical-800 border border-botanical-700">
            <div className={`w-2 h-2 rounded-full ${
              modelStatus === 'ready' ? 'bg-green-500' : 
              modelStatus === 'processing' ? 'bg-amber-500 animate-pulse' : 'bg-red-500'
            }`} />
            <span className="text-xs font-medium text-botanical-50 capitalize">{modelStatus}</span>
          </div>
        </div>
      </div>

      <div className="flex items-center gap-4">
        <div className="relative hidden md:block group">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-botanical-200 group-focus-within:text-botanical-400 transition-colors" size={16} />
          <input 
            type="text" 
            placeholder="Search knowledge base..." 
            className="w-64 bg-botanical-800 border border-botanical-600 rounded-full pl-9 pr-4 py-1.5 text-sm text-botanical-50 placeholder-botanical-200 focus:outline-none focus:border-botanical-400 focus:ring-1 focus:ring-botanical-400 transition-all"
          />
        </div>
        <LanguageSelector />
      </div>
    </header>
  );
};
