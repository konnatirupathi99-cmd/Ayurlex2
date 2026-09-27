import React from 'react';
import { X, ExternalLink, ShieldCheck } from 'lucide-react';
import { Source } from '../../lib/api/chat';

interface CitationDrawerProps {
  source: Source | null;
  isOpen: boolean;
  onClose: () => void;
}

export const CitationDrawer: React.FC<CitationDrawerProps> = ({ source, isOpen, onClose }) => {
  if (!source) return null;

  return (
    <>
      {isOpen && (
        <div 
          className="fixed inset-0 bg-black/50 z-40 md:hidden"
          onClick={onClose}
        />
      )}
      <div 
        className={`fixed inset-y-0 right-0 z-50 w-full md:w-96 bg-botanical-800 border-l border-botanical-600 transform transition-transform duration-300 ease-in-out flex flex-col ${
          isOpen ? "translate-x-0" : "translate-x-full"
        }`}
      >
        <div className="p-4 border-b border-botanical-600 flex items-center justify-between">
          <h3 className="font-semibold text-botanical-50">Citation Details</h3>
          <button 
            onClick={onClose}
            className="p-1.5 text-botanical-200 hover:text-botanical-50 rounded-lg hover:bg-botanical-700 transition-colors"
          >
            <X size={20} />
          </button>
        </div>
        
        <div className="flex-1 overflow-y-auto p-4 flex flex-col gap-6">
          <div>
            <h4 className="text-xl font-medium text-botanical-50 mb-2">{source.title}</h4>
            <div className="flex items-center gap-2 mb-4">
              <span className="px-2 py-1 bg-botanical-700 text-botanical-100 rounded text-xs font-medium uppercase tracking-wider">
                Document
              </span>
              {source.confidenceScore && (
                <div className="flex items-center gap-1.5 px-2 py-1 bg-botanical-700/50 rounded text-xs font-medium">
                  <ShieldCheck size={14} className={source.confidenceScore > 0.9 ? "text-green-500" : "text-amber-500"} />
                  <span className="text-botanical-200">
                    {Math.round(source.confidenceScore * 100)}% Match
                  </span>
                </div>
              )}
            </div>
            
            <div className="bg-botanical-900 border border-botanical-600 rounded-lg p-4">
              <h5 className="text-xs font-semibold text-botanical-200 uppercase tracking-wider mb-2">Relevant Excerpt</h5>
              <p className="text-sm text-botanical-50 leading-relaxed">
                "{source.snippet || 'No excerpt available.'}"
              </p>
            </div>
          </div>
          
          <div className="mt-auto">
            <button className="w-full flex items-center justify-center gap-2 py-2.5 bg-botanical-400 hover:bg-botanical-300 text-botanical-50 rounded-lg font-medium transition-colors">
              <ExternalLink size={16} />
              View Full Source
            </button>
          </div>
        </div>
      </div>
    </>
  );
};
