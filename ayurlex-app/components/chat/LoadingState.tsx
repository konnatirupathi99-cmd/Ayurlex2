import React from 'react';
import { Activity } from 'lucide-react';

export const LoadingState: React.FC = () => {
  return (
    <div className="flex w-full py-6 px-4 md:px-0">
      <div className="max-w-4xl mx-auto w-full flex gap-4 md:gap-6">
        <div className="shrink-0 flex flex-col items-center">
          <div className="w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm bg-botanical-400 text-botanical-50 spin">
            <Activity size={16} />
          </div>
        </div>
        <div className="flex-1 flex items-center">
          <div className="flex gap-1.5 items-center h-8">
            <div className="w-2 h-2 rounded-full bg-botanical-400 animate-bounce" style={{ animationDelay: '0ms' }} />
            <div className="w-2 h-2 rounded-full bg-botanical-300 animate-bounce" style={{ animationDelay: '150ms' }} />
            <div className="w-2 h-2 rounded-full bg-botanical-200 animate-bounce" style={{ animationDelay: '300ms' }} />
          </div>
        </div>
      </div>
    </div>
  );
};
