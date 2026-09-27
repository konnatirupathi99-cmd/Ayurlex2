import React from 'react';
import { ChatInterface } from '@/components/chat/ChatInterface';

export default function ChatPage() {
  return (
    <div className="h-full">
      <div className="mb-4">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white">AYURLEX Assistant</h1>
        <p className="text-gray-500 dark:text-gray-400">Interact with the AI using text, voice, or file uploads.</p>
      </div>
      
      <ChatInterface />
    </div>
  );
}
