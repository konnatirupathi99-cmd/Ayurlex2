import React from 'react';
import { MessageSquarePlus, MessageSquare, BookOpen, BarChart2, Settings, History, Menu } from 'lucide-react';
import { clsx } from 'clsx';
import { twMerge } from 'tailwind-merge';

interface SidebarProps {
  isOpen: boolean;
  setIsOpen: (isOpen: boolean) => void;
  activeTab: string;
  setActiveTab: (tab: string) => void;
}

export const Sidebar: React.FC<SidebarProps> = ({ isOpen, setIsOpen, activeTab, setActiveTab }) => {
  const tabs = [
    { id: 'chat', label: 'New Chat', icon: MessageSquarePlus },
    { id: 'history', label: 'History', icon: History },
    { id: 'knowledge', label: 'Knowledge Base', icon: BookOpen },
    { id: 'analyses', label: 'Analyses', icon: BarChart2 },
  ];

  return (
    <>
      {/* Mobile overlay */}
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/50 z-40 md:hidden"
          onClick={() => setIsOpen(false)}
        />
      )}
      
      <div 
        className={twMerge(
          "fixed inset-y-0 left-0 z-50 w-64 bg-botanical-800 border-r border-botanical-600 transform transition-transform duration-300 ease-in-out md:relative md:translate-x-0 flex flex-col",
          isOpen ? "translate-x-0" : "-translate-x-full"
        )}
      >
        <div className="p-4 flex items-center justify-between">
          <div className="flex items-center gap-2">
            <div className="w-8 h-8 rounded bg-botanical-400 flex items-center justify-center">
              <span className="text-botanical-50 font-bold">A</span>
            </div>
            <h1 className="text-xl font-semibold text-botanical-50">AYURLEX</h1>
          </div>
          <button 
            className="md:hidden text-botanical-100 hover:text-botanical-50 transition-colors"
            onClick={() => setIsOpen(false)}
          >
            <Menu size={24} />
          </button>
        </div>

        <nav className="flex-1 px-3 py-4 space-y-1">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={clsx(
                "w-full flex items-center gap-3 px-3 py-2 rounded-lg transition-all duration-200 text-sm font-medium",
                activeTab === tab.id 
                  ? "bg-botanical-500 text-botanical-50 border border-botanical-600" 
                  : "text-botanical-100 hover:bg-botanical-700 hover:text-botanical-50"
              )}
            >
              <tab.icon size={18} />
              {tab.label}
            </button>
          ))}
        </nav>

        <div className="p-4 border-t border-botanical-600">
          <button
            onClick={() => setActiveTab('settings')}
            className={clsx(
              "w-full flex items-center gap-3 px-3 py-2 rounded-lg transition-all duration-200 text-sm font-medium",
              activeTab === 'settings'
                ? "bg-botanical-500 text-botanical-50 border border-botanical-600" 
                : "text-botanical-100 hover:bg-botanical-700 hover:text-botanical-50"
            )}
          >
            <Settings size={18} />
            Settings
          </button>
        </div>
      </div>
    </>
  );
};
