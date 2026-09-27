import React, { useState, useRef, useEffect } from 'react';
import { Send, FileText, CheckCircle2, Loader2, Sparkles, ShieldCheck, Leaf } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';

type Message = {
  id: string;
  role: 'user' | 'assistant';
  content: string;
  isStreaming?: boolean;
  researchSteps?: ResearchStep[];
  confidence?: string;
};

type ResearchStep = {
  id: string;
  label: string;
  status: 'pending' | 'loading' | 'complete';
};

export default function ChatWindow({ 
  researchMode,
  language
}: { 
  researchMode: boolean,
  language: string
}) {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  const handleSend = async () => {
    if (!input.trim() || isLoading) return;

    const userMsg: Message = { id: Date.now().toString(), role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    // Mock research steps for Research Mode
    const mockSteps: ResearchStep[] = [
      { id: '1', label: 'QUERY RECEIVED', status: 'complete' },
      { id: '2', label: 'LANGUAGE DETECTED', status: 'pending' },
      { id: '3', label: 'TERMINOLOGY IDENTIFIED', status: 'pending' },
      { id: '4', label: 'JURISDICTION IDENTIFIED', status: 'pending' },
      { id: '5', label: 'KNOWLEDGE SEARCH', status: 'pending' },
      { id: '6', label: 'EVIDENCE REVIEW', status: 'pending' },
      { id: '7', label: 'AI SYNTHESIS', status: 'pending' },
    ];

    const astMsgId = (Date.now() + 1).toString();
    
    if (researchMode) {
      setMessages(prev => [...prev, { id: astMsgId, role: 'assistant', content: '', isStreaming: true, researchSteps: [...mockSteps] }]);
      
      // Simulate steps
      for (let i = 1; i < mockSteps.length; i++) {
        await new Promise(r => setTimeout(r, 600));
        setMessages(prev => prev.map(m => {
          if (m.id === astMsgId && m.researchSteps) {
            const newSteps = [...m.researchSteps];
            newSteps[i].status = 'complete';
            if (i + 1 < newSteps.length) newSteps[i+1].status = 'loading';
            return { ...m, researchSteps: newSteps };
          }
          return m;
        }));
      }
    } else {
      setMessages(prev => [...prev, { id: astMsgId, role: 'assistant', content: 'Analyzing...', isStreaming: true }]);
    }

    try {
      const res = await fetch('http://localhost:8000/api/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ 
          message: userMsg.content,
          conversation_id: 'default',
          language,
          jurisdiction: 'auto',
          research_mode: researchMode
        })
      });
      
      const data = await res.json();
      
      setMessages(prev => prev.map(m => {
        if (m.id === astMsgId) {
          return {
            ...m,
            content: data.answer,
            isStreaming: false,
            confidence: data.confidence,
            researchSteps: m.researchSteps?.map(s => ({ ...s, status: 'complete' }))
          };
        }
        return m;
      }));

    } catch (error) {
      setMessages(prev => prev.map(m => m.id === astMsgId ? { ...m, content: "Error connecting to backend.", isStreaming: false } : m));
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="flex flex-col flex-1 overflow-hidden relative">
      <div className="flex-1 overflow-y-auto p-6 space-y-6">
        {messages.length === 0 ? (
          <div className="flex flex-col items-center justify-center h-full text-[var(--color-ayur-100)] opacity-60">
            <Sparkles size={48} className="mb-4 text-[var(--color-ayur-400)]" />
            <h2 className="text-xl font-medium mb-2">Evidence-Grounded Intelligence</h2>
            <p className="text-sm text-center max-w-md">
              Ask about Ayurvedic formulations, Intellectual Property considerations, prior art, or regulatory context.
            </p>
          </div>
        ) : (
          messages.map(msg => (
            <MessageBubble key={msg.id} message={msg} researchMode={researchMode} />
          ))
        )}
        <div ref={bottomRef} />
      </div>

      <div className="p-4 bg-[var(--color-ayur-900)] border-t border-[var(--color-ayur-700)]">
        <div className="max-w-4xl mx-auto relative">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                handleSend();
              }
            }}
            placeholder="Ask AYURLEX about formulations, patents, or regulatory intel..."
            className="w-full bg-[var(--color-ayur-800)] text-white border border-[var(--color-ayur-600)] rounded-xl px-4 py-3 pr-12 focus:outline-none focus:border-[var(--color-ayur-400)] resize-none h-[56px] transition-colors overflow-hidden"
            rows={1}
          />
          <button 
            onClick={handleSend}
            disabled={!input.trim() || isLoading}
            className="absolute right-2 top-2 p-2 bg-[var(--color-ayur-400)] hover:bg-[var(--color-ayur-300)] disabled:opacity-50 disabled:hover:bg-[var(--color-ayur-400)] text-white rounded-lg transition-colors"
          >
            <Send size={18} />
          </button>
        </div>
        <div className="text-center mt-2 text-xs text-[var(--color-ayur-100)]">
          AYURLEX provides AI-assisted research. Always verify regulatory & IP conclusions with official authorities.
        </div>
      </div>
    </div>
  );
}

function MessageBubble({ message, researchMode }: { message: Message, researchMode: boolean }) {
  const isUser = message.role === 'user';
  
  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex ${isUser ? 'justify-end' : 'justify-start'} w-full max-w-4xl mx-auto`}
    >
      <div className={`flex gap-4 max-w-[85%] ${isUser ? 'flex-row-reverse' : 'flex-row'}`}>
        
        <div className={`w-8 h-8 rounded-full flex items-center justify-center shrink-0 ${isUser ? 'bg-[var(--color-ayur-500)] text-white' : 'bg-[var(--color-ayur-400)] text-white'}`}>
          {isUser ? 'U' : <Leaf size={16} />}
        </div>
        
        <div className="flex flex-col gap-2 min-w-0">
          {!isUser && message.researchSteps && researchMode && (
            <div className="bg-[var(--color-ayur-900)] border border-[var(--color-ayur-700)] rounded-lg p-3 text-xs font-mono space-y-2 mb-2 w-72">
              {message.researchSteps.map(step => (
                <div key={step.id} className="flex items-center gap-2">
                  {step.status === 'complete' && <CheckCircle2 size={14} className="text-[var(--color-ayur-200)]" />}
                  {step.status === 'loading' && <Loader2 size={14} className="animate-spin text-[var(--color-ayur-100)]" />}
                  {step.status === 'pending' && <div className="w-3.5 h-3.5 rounded-full border border-[var(--color-ayur-600)]" />}
                  <span className={step.status === 'complete' ? 'text-[var(--color-ayur-200)]' : 'text-[var(--color-ayur-100)]'}>
                    {step.label}
                  </span>
                </div>
              ))}
            </div>
          )}

          {message.content && (
            <div className={`px-5 py-3.5 rounded-2xl ${
              isUser 
                ? 'bg-[var(--color-ayur-600)] text-[var(--color-ayur-25)] rounded-tr-sm' 
                : 'bg-[var(--color-ayur-900)] border border-[var(--color-ayur-700)] text-[var(--color-ayur-25)] rounded-tl-sm'
            }`}>
              <div className="whitespace-pre-wrap leading-relaxed text-sm">
                {message.content}
              </div>
            </div>
          )}

          {!isUser && message.confidence && (
            <div className="flex items-center gap-2 mt-1">
              <span className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-[10px] font-medium tracking-wide border ${
                message.confidence === 'SUPPORTED BY EVIDENCE' 
                  ? 'bg-[#1C302C] text-[#84A899] border-[#356659]' 
                  : message.confidence === 'INSUFFICIENT EVIDENCE'
                  ? 'bg-amber-950/30 text-amber-500 border-amber-900/50'
                  : 'bg-[var(--color-ayur-700)] text-[var(--color-ayur-100)] border-[var(--color-ayur-600)]'
              }`}>
                <ShieldCheck size={12} />
                {message.confidence}
              </span>
            </div>
          )}
        </div>
      </div>
    </motion.div>
  );
}
