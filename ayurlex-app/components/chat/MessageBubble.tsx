import React from 'react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Copy, ThumbsUp, ThumbsDown, RotateCcw, Volume2 } from 'lucide-react';
import { clsx } from 'clsx';
import { motion } from 'framer-motion';
import { ChatMessage, Source } from '../../lib/api/chat';
import { SourceCard } from '../shared/SourceCard';

interface MessageBubbleProps {
  message: ChatMessage;
  onSourceClick: (source: Source) => void;
  onRegenerate?: () => void;
}

export const MessageBubble: React.FC<MessageBubbleProps> = ({ message, onSourceClick, onRegenerate }) => {
  const isUser = message.role === 'user';

  const copyToClipboard = () => {
    navigator.clipboard.writeText(message.content);
  };

  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={clsx(
        "flex w-full py-6 px-4 md:px-0",
        isUser ? "bg-botanical-900/50" : ""
      )}
    >
      <div className="max-w-4xl mx-auto w-full flex gap-4 md:gap-6">
        <div className="shrink-0 flex flex-col items-center">
          <div className={clsx(
            "w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm",
            isUser ? "bg-botanical-300 text-botanical-900" : "bg-botanical-400 text-botanical-50"
          )}>
            {isUser ? 'U' : 'A'}
          </div>
        </div>

        <div className="flex-1 min-w-0 flex flex-col gap-4">
          <div className="prose prose-invert prose-botanical max-w-none text-botanical-50 prose-p:leading-relaxed prose-pre:bg-botanical-800 prose-pre:border prose-pre:border-botanical-600 prose-a:text-botanical-300 hover:prose-a:text-botanical-400">
            <ReactMarkdown 
              remarkPlugins={[remarkGfm]}
              components={{
                code({node, inline, className, children, ...props}: any) {
                  const match = /language-(\w+)/.exec(className || '')
                  return !inline && match ? (
                    <div className="rounded-md overflow-hidden bg-botanical-900 my-4 border border-botanical-600">
                      <div className="flex items-center justify-between px-4 py-2 bg-botanical-800 border-b border-botanical-600 text-xs font-mono text-botanical-200">
                        {match[1]}
                      </div>
                      <pre className="p-4 overflow-x-auto text-sm">
                        <code className={className} {...props}>
                          {children}
                        </code>
                      </pre>
                    </div>
                  ) : (
                    <code className="bg-botanical-800 px-1.5 py-0.5 rounded text-sm text-botanical-200 font-mono" {...props}>
                      {children}
                    </code>
                  )
                },
                table({children}) {
                  return (
                    <div className="overflow-x-auto my-6 border border-botanical-600 rounded-lg">
                      <table className="w-full text-sm text-left">{children}</table>
                    </div>
                  )
                },
                th({children}) {
                  return <th className="bg-botanical-800 px-4 py-3 font-semibold border-b border-botanical-600">{children}</th>
                },
                td({children}) {
                  return <td className="px-4 py-3 border-b border-botanical-700">{children}</td>
                }
              }}
            >
              {message.content}
            </ReactMarkdown>
          </div>

          {!isUser && message.sources && message.sources.length > 0 && (
            <div className="mt-2">
              <h4 className="text-xs font-semibold text-botanical-200 uppercase tracking-wider mb-2">Sources</h4>
              <div className="flex flex-wrap gap-2">
                {message.sources.map(source => (
                  <SourceCard key={source.id} source={source} onClick={onSourceClick} />
                ))}
              </div>
            </div>
          )}

          {!isUser && (
            <div className="flex items-center gap-2 mt-2">
              <button 
                onClick={copyToClipboard}
                className="p-1.5 text-botanical-200 hover:text-botanical-50 hover:bg-botanical-700 rounded transition-colors" 
                title="Copy response"
              >
                <Copy size={16} />
              </button>
              <button 
                className="p-1.5 text-botanical-200 hover:text-botanical-50 hover:bg-botanical-700 rounded transition-colors"
                title="Read aloud"
              >
                <Volume2 size={16} />
              </button>
              {onRegenerate && (
                <button 
                  onClick={onRegenerate}
                  className="p-1.5 text-botanical-200 hover:text-botanical-50 hover:bg-botanical-700 rounded transition-colors"
                  title="Regenerate"
                >
                  <RotateCcw size={16} />
                </button>
              )}
              <div className="w-px h-4 bg-botanical-600 mx-1" />
              <button className="p-1.5 text-botanical-200 hover:text-green-500 hover:bg-botanical-700 rounded transition-colors">
                <ThumbsUp size={16} />
              </button>
              <button className="p-1.5 text-botanical-200 hover:text-red-500 hover:bg-botanical-700 rounded transition-colors">
                <ThumbsDown size={16} />
              </button>
            </div>
          )}
        </div>
      </div>
    </motion.div>
  );
};
