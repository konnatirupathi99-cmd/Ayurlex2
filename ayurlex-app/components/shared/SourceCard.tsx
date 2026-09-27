import React from 'react';
import { FileText, ExternalLink, ShieldCheck } from 'lucide-react';
import { Source } from '../../lib/api/chat';

interface SourceCardProps {
  source: Source;
  onClick: (source: Source) => void;
}

export const SourceCard: React.FC<SourceCardProps> = ({ source, onClick }) => {
  return (
    <div 
      onClick={() => onClick(source)}
      className="flex flex-col gap-2 p-3 bg-botanical-800 border border-botanical-600 rounded-lg hover:border-botanical-400 cursor-pointer transition-all hover:bg-botanical-700/50 card-surface"
    >
      <div className="flex items-start justify-between gap-2">
        <div className="flex items-center gap-2 text-botanical-50 font-medium text-sm">
          <FileText size={14} className="text-botanical-400" />
          <span className="line-clamp-1">{source.title}</span>
        </div>
        <ExternalLink size={14} className="text-botanical-200 shrink-0" />
      </div>
      
      {source.snippet && (
        <p className="text-xs text-botanical-100 line-clamp-2">
          "{source.snippet}"
        </p>
      )}
      
      {source.confidenceScore && (
        <div className="flex items-center gap-1.5 mt-1">
          <ShieldCheck size={12} className={source.confidenceScore > 0.9 ? "text-green-500" : "text-amber-500"} />
          <span className="text-[10px] font-medium text-botanical-200">
            {Math.round(source.confidenceScore * 100)}% Match
          </span>
        </div>
      )}
    </div>
  );
};
