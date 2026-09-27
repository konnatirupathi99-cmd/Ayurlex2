import React from 'react';
import { BarChart2, ChevronRight } from 'lucide-react';
import { ConfidenceBadge } from './ConfidenceBadge';

interface AnalysisCardProps {
  title: string;
  summary: string;
  confidence: number;
  date: string;
}

export const AnalysisCard: React.FC<AnalysisCardProps> = ({ title, summary, confidence, date }) => {
  return (
    <div className="bg-botanical-800 border border-botanical-600 rounded-xl p-5 hover:border-botanical-400 transition-all cursor-pointer group">
      <div className="flex items-start justify-between mb-3">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-lg bg-botanical-900 flex items-center justify-center text-botanical-300 group-hover:text-botanical-400 transition-colors">
            <BarChart2 size={20} />
          </div>
          <div>
            <h3 className="font-medium text-botanical-50">{title}</h3>
            <p className="text-xs text-botanical-200">{date}</p>
          </div>
        </div>
        <ConfidenceBadge score={confidence} />
      </div>
      <p className="text-sm text-botanical-100 line-clamp-2 mb-4">
        {summary}
      </p>
      <div className="flex items-center text-sm font-medium text-botanical-300 group-hover:text-botanical-400 transition-colors">
        View full analysis <ChevronRight size={16} className="ml-1" />
      </div>
    </div>
  );
};
