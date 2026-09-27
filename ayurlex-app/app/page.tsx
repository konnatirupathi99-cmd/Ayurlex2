"use client";

import React, { useState } from 'react';
import { Sidebar } from '../components/ui/Sidebar';
import { Topbar } from '../components/ui/Topbar';
import { ChatWindow } from '../components/chat/ChatWindow';
import { ReportPanel } from '../components/shared/ReportPanel';
import { SettingsPanel } from '../components/shared/SettingsPanel';
import { CitationDrawer } from '../components/shared/CitationDrawer';
import { Source } from '../lib/api/chat';

export default function App() {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [activeTab, setActiveTab] = useState('chat');
  const [selectedSource, setSelectedSource] = useState<Source | null>(null);

  const renderContent = () => {
    switch (activeTab) {
      case 'chat':
        return <ChatWindow onSourceClick={setSelectedSource} />;
      case 'analyses':
        return <ReportPanel />;
      case 'settings':
        return <SettingsPanel />;
      default:
        return (
          <div className="flex-1 flex items-center justify-center bg-botanical-900 text-botanical-200">
            <p>This section is under construction.</p>
          </div>
        );
    }
  };

  return (
    <div className="flex h-screen bg-botanical-900 overflow-hidden font-sans">
      <Sidebar 
        isOpen={sidebarOpen} 
        setIsOpen={setSidebarOpen} 
        activeTab={activeTab} 
        setActiveTab={setActiveTab} 
      />
      
      <div className="flex-1 flex flex-col min-w-0">
        <Topbar 
          onMenuClick={() => setSidebarOpen(true)} 
          modelStatus="ready"
        />
        
        <main className="flex-1 relative overflow-hidden flex flex-col">
          {renderContent()}
        </main>
      </div>

      <CitationDrawer 
        source={selectedSource} 
        isOpen={!!selectedSource} 
        onClose={() => setSelectedSource(null)} 
      />
    </div>
  );
}
