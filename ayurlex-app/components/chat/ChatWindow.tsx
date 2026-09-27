import React, { useState, useRef, useEffect } from 'react';
import { Send, StopCircle } from 'lucide-react';
import { ChatMessage, Source, sendMessage } from '../../lib/api/chat';
import { MessageBubble } from './MessageBubble';
import { LoadingState } from './LoadingState';
import { FileUploader } from './FileUploader';
import { VoiceButton } from './VoiceButton';

interface ChatWindowProps {
  onSourceClick: (source: Source) => void;
}

export const ChatWindow: React.FC<ChatWindowProps> = ({ onSourceClick }) => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim() || isLoading) return;

    const userMessage: ChatMessage = {
      id: Date.now().toString(),
      role: 'user',
      content: input,
      timestamp: new Date().toISOString()
    };

    setMessages(prev => [...prev, userMessage]);
    setInput('');
    setIsLoading(true);

    try {
      const tempId = (Date.now() + 1).toString();
      setMessages(prev => [...prev, {
        id: tempId,
        role: 'assistant',
        content: '',
        timestamp: new Date().toISOString()
      }]);

      const finalMessage = await sendMessage(
        userMessage.content,
        messages,
        (chunk) => {
          setMessages(prev => prev.map(msg => 
            msg.id === tempId ? { ...msg, content: chunk } : msg
          ));
        }
      );
      
      setMessages(prev => prev.map(msg => 
        msg.id === tempId ? finalMessage : msg
      ));
    } catch (error) {
      console.error('Failed to send message:', error);
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col h-full bg-botanical-900 overflow-hidden relative">
      <div className="flex-1 overflow-y-auto pb-32">
        {messages.length === 0 ? (
          <div className="h-full flex flex-col items-center justify-center text-center px-4">
            <div className="w-16 h-16 rounded-2xl bg-botanical-800 border border-botanical-600 flex items-center justify-center mb-6">
              <span className="text-3xl font-bold text-botanical-400">A</span>
            </div>
            <h2 className="text-2xl font-semibold text-botanical-50 mb-2">How can I assist you today?</h2>
            <p className="text-botanical-200 max-w-md">
              Ask about Ayurvedic formulations, IP regulations, or upload a document for analysis.
            </p>
          </div>
        ) : (
          <div className="flex flex-col">
            {messages.map(msg => (
              <MessageBubble 
                key={msg.id} 
                message={msg} 
                onSourceClick={onSourceClick}
                onRegenerate={msg.role === 'assistant' ? () => {} : undefined}
              />
            ))}
            {isLoading && messages[messages.length - 1]?.content === '' && <LoadingState />}
            <div ref={messagesEndRef} />
          </div>
        )}
      </div>

      <div className="absolute bottom-0 left-0 right-0 bg-gradient-to-t from-botanical-900 via-botanical-900 to-transparent pt-10 pb-6 px-4 md:px-8">
        <div className="max-w-4xl mx-auto">
          <form 
            onSubmit={handleSubmit}
            className="relative flex items-end bg-botanical-800 border border-botanical-600 rounded-2xl p-2 shadow-lg focus-within:border-botanical-400 focus-within:ring-1 focus-within:ring-botanical-400 transition-all"
          >
            <div className="flex items-center self-center px-1">
              <FileUploader onFileSelect={(file) => console.log('File selected:', file)} />
            </div>
            
            <textarea
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Message AYURLEX..."
              className="flex-1 max-h-32 min-h-[44px] bg-transparent border-none resize-none px-3 py-3 text-botanical-50 placeholder-botanical-200 focus:outline-none focus:ring-0"
              rows={1}
              onKeyDown={(e) => {
                if (e.key === 'Enter' && !e.shiftKey) {
                  e.preventDefault();
                  handleSubmit(e);
                }
              }}
            />

            <div className="flex items-center gap-1 self-center pr-1">
              <VoiceButton />
              {isLoading ? (
                <button 
                  type="button"
                  className="flex items-center justify-center w-10 h-10 rounded-full bg-botanical-600 text-botanical-50 hover:bg-botanical-500 transition-colors"
                >
                  <StopCircle size={20} />
                </button>
              ) : (
                <button 
                  type="submit"
                  disabled={!input.trim()}
                  className="flex items-center justify-center w-10 h-10 rounded-full bg-botanical-400 text-botanical-50 hover:bg-botanical-300 disabled:opacity-50 disabled:hover:bg-botanical-400 transition-colors"
                >
                  <Send size={18} className="ml-1" />
                </button>
              )}
            </div>
          </form>
          <div className="text-center mt-2">
            <span className="text-xs text-botanical-200">
              AYURLEX can make mistakes. Verify important information.
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};
