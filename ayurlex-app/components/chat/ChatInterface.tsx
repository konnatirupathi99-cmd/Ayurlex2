"use client";

import React, { useState, useRef, useEffect } from 'react';
import { Send, Mic, Paperclip, AlertTriangle, CheckCircle, ShieldAlert } from 'lucide-react';
import { CitationCard } from '@/components/ui/CitationCard';

interface Message {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  status?: string;
  metadata?: {
    confidence?: string;
    limitations?: string[];
    sources?: string[];
    citations?: any[];
  };
  isStreaming?: boolean;
}

export const ChatInterface = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isProcessing, setIsProcessing] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isProcessing) return;

    const userMsg: Message = { id: Date.now().toString(), role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsProcessing(true);

    const assistantMsgId = (Date.now() + 1).toString();
    setMessages(prev => [...prev, { 
      id: assistantMsgId, 
      role: 'assistant', 
      content: '', 
      status: 'Connecting...',
      isStreaming: true 
    }]);

    try {
      // Consume SSE Stream from Backend
      const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api'}/chat/stream`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: userMsg.content, session_id: "demo-session" })
      });

      if (!response.body) throw new Error("No response body");
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      
      let fullContent = "";
      let finalMetadata = {};

      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        
        const chunk = decoder.decode(value);
        const lines = chunk.split('\n');
        
        for (const line of lines) {
          if (line.startsWith('data: ')) {
            try {
              const payload = JSON.parse(line.slice(6));
              
              if (payload.event === 'status') {
                setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, status: payload.data } : m));
              } else if (payload.event === 'token') {
                fullContent += payload.data;
                setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, content: fullContent } : m));
              } else if (payload.event === 'metadata') {
                finalMetadata = payload.data;
                setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, metadata: finalMetadata } : m));
              } else if (payload.event === 'error') {
                fullContent += `\n\nERROR: ${payload.data}`;
                setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, content: fullContent } : m));
              }
            } catch (e) {
              console.error("Parse error on chunk", line);
            }
          }
        }
      }

      // Mark streaming complete
      setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, isStreaming: false, status: undefined } : m));

    } catch (error) {
      console.error(error);
      setMessages(prev => prev.map(m => m.id === assistantMsgId ? { ...m, content: "Network error occurred.", isStreaming: false, status: undefined } : m));
    } finally {
      setIsProcessing(false);
    }
  };

  return (
    <div className="flex flex-col h-[calc(100vh-120px)] bg-gray-50 dark:bg-gray-900 rounded-xl border border-gray-200 dark:border-gray-800 shadow-sm overflow-hidden relative">
      {/* Chat Area */}
      <div className="flex-1 overflow-y-auto p-4 md:p-6 space-y-6">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center px-4">
            <div className="w-16 h-16 bg-blue-100 dark:bg-blue-900/30 rounded-full flex items-center justify-center mb-4">
              <ShieldAlert className="w-8 h-8 text-blue-600 dark:text-blue-400" />
            </div>
            <h2 className="text-2xl font-bold text-gray-800 dark:text-gray-100 mb-2">AYURLEX Intelligence Assistant</h2>
            <p className="text-gray-500 dark:text-gray-400 max-w-lg">
              Ask about Ayurvedic formulation IP, regulatory compliance, ABS, or traditional knowledge. 
              All answers are strictly sourced from authoritative evidence.
            </p>
          </div>
        ) : (
          messages.map((msg) => (
            <div key={msg.id} className={`flex ${msg.role === 'user' ? 'justify-end' : 'justify-start'}`}>
              <div className={`max-w-[85%] rounded-2xl p-5 ${
                msg.role === 'user' 
                  ? 'bg-blue-600 text-white shadow-md' 
                  : 'bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 shadow-sm text-gray-800 dark:text-gray-200'
              }`}>
                {/* Assistant Processing Status */}
                {msg.role === 'assistant' && msg.status && (
                  <div className="flex items-center gap-2 text-sm text-blue-500 font-medium mb-3 pb-2 border-b border-gray-100 dark:border-gray-700">
                    <div className="w-4 h-4 rounded-full border-2 border-blue-500 border-t-transparent animate-spin"></div>
                    {msg.status}
                  </div>
                )}

                {/* Content */}
                <div className="prose dark:prose-invert max-w-none text-sm md:text-base whitespace-pre-wrap">
                  {msg.content}
                </div>

                {/* Assistant Metadata (Citations, Confidence) */}
                {msg.role === 'assistant' && !msg.isStreaming && msg.metadata && (
                  <div className="mt-6 pt-4 border-t border-gray-200 dark:border-gray-700">
                    <div className="flex items-center gap-4 mb-4">
                      {msg.metadata.confidence === 'Rejected' ? (
                         <span className="flex items-center gap-1 text-xs font-bold bg-red-100 text-red-700 px-2 py-1 rounded">
                           <AlertTriangle className="w-3 h-3" /> REJECTED
                         </span>
                      ) : (
                         <span className="flex items-center gap-1 text-xs font-bold bg-green-100 text-green-700 px-2 py-1 rounded">
                           <CheckCircle className="w-3 h-3" /> SOURCE VERIFIED
                         </span>
                      )}
                    </div>
                    
                    {msg.metadata.limitations && msg.metadata.limitations.length > 0 && (
                      <div className="mb-4 p-3 bg-amber-50 dark:bg-amber-900/20 border border-amber-200 dark:border-amber-800 rounded">
                        <h4 className="text-xs font-bold text-amber-800 dark:text-amber-500 mb-1 flex items-center gap-1">
                          <AlertTriangle className="w-3 h-3" /> LIMITATIONS IDENTIFIED
                        </h4>
                        <ul className="list-disc list-inside text-xs text-amber-700 dark:text-amber-400">
                          {msg.metadata.limitations.map((l, idx) => <li key={idx}>{l}</li>)}
                        </ul>
                      </div>
                    )}

                    {/* Citations (Rendered if available) */}
                    {msg.metadata.citations && msg.metadata.citations.length > 0 && (
                      <div className="space-y-3 mt-4">
                        <h4 className="text-xs font-bold text-gray-500 uppercase">Authoritative Evidence</h4>
                        {msg.metadata.citations.map((cit, idx) => (
                           <CitationCard 
                             key={idx}
                             citationId={cit.citation_id}
                             documentTitle={cit.document_title}
                             authority={cit.authority}
                             source={cit.source}
                             jurisdiction={cit.jurisdiction}
                             publicationDate={cit.publication_date}
                             pageOrSection={cit.page_or_section}
                             relevantExcerpt={cit.relevant_excerpt}
                             relevanceScore={cit.relevance_score}
                           />
                        ))}
                      </div>
                    )}
                  </div>
                )}
              </div>
            </div>
          ))
        )}
        <div ref={messagesEndRef} />
      </div>

      {/* Input Area */}
      <div className="p-4 bg-white dark:bg-gray-800 border-t border-gray-200 dark:border-gray-700">
        <form onSubmit={handleSubmit} className="relative flex items-center">
          <button type="button" className="absolute left-3 text-gray-400 hover:text-gray-600 dark:hover:text-gray-200">
            <Paperclip className="w-5 h-5" />
          </button>
          <input 
            type="text" 
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={isProcessing}
            placeholder="Ask AYURLEX (e.g. Can I patent a formulation of Giloy and Brahmi in the US?)"
            className="w-full pl-12 pr-24 py-4 rounded-xl border border-gray-300 dark:border-gray-600 bg-gray-50 dark:bg-gray-900 focus:outline-none focus:ring-2 focus:ring-blue-500 text-gray-900 dark:text-gray-100"
          />
          <div className="absolute right-2 flex items-center space-x-2">
            <button type="button" className="p-2 text-gray-400 hover:text-blue-500">
              <Mic className="w-5 h-5" />
            </button>
            <button 
              type="submit" 
              disabled={isProcessing || !input.trim()}
              className="p-2 bg-blue-600 hover:bg-blue-700 disabled:opacity-50 text-white rounded-lg transition-colors"
            >
              <Send className="w-5 h-5" />
            </button>
          </div>
        </form>
        <p className="text-center text-xs text-gray-400 mt-2">
          AYURLEX AI provides legal and regulatory intelligence. Verify critical compliance with local authorities.
        </p>
      </div>
    </div>
  );
};
