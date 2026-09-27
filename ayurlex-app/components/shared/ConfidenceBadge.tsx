import React from 'react';
import { ShieldCheck, AlertTriangle } from 'lucide-react';
import { clsx } from 'clsx';

interface ConfidenceBadgeProps {
  score: number;
}

export const ConfidenceBadge: React.FC<ConfidenceBadgeProps> = ({ score }) => {
  const percentage = Math.round(score * 100);
  const isHigh = score >= 0.8;
  const isMedium = score >= 0.5 && score < 0.8;
  
  return (
    <div className={clsx(
      "flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border",
      isHigh ? "bg-green-500/10 text-green-400 border-green-500/20" : 
      isMedium ? "bg-amber-500/10 text-amber-400 border-amber-500/20" : 
      "bg-red-500/10 text-red-400 border-red-500/20"
    )}>
      {isHigh ? <ShieldCheck size={14} /> : <AlertTriangle size={14} />}
      {percentage}% Confidence
    </div>
  );
};
