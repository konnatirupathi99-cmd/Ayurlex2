"use client";
import React, { useState } from 'react';
import Sidebar from '@/components/Sidebar';
import ChatWindow from '@/components/ChatWindow';
import Topbar from '@/components/Topbar';

export default function Home() {
  const [researchMode, setResearchMode] = useState(false);
  const [language, setLanguage] = useState("English");
  
  return (
    <main className="flex w-full h-full">
      <Sidebar />
      <div className="flex flex-col flex-grow relative bg-[var(--color-ayur-800)] border-l border-[var(--color-ayur-700)]">
        <Topbar 
          researchMode={researchMode} 
          setResearchMode={setResearchMode} 
          language={language}
          setLanguage={setLanguage}
        />
        <ChatWindow 
          researchMode={researchMode}
          language={language}
        />
      </div>
    </main>
  );
}
