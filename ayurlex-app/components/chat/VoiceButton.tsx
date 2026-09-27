import React, { useState } from 'react';
import { Mic, MicOff } from 'lucide-react';
import { clsx } from 'clsx';

export const VoiceButton: React.FC = () => {
  const [isRecording, setIsRecording] = useState(false);

  return (
    <button
      onClick={() => setIsRecording(!isRecording)}
      className={clsx(
        "flex items-center justify-center w-10 h-10 rounded-full transition-colors",
        isRecording 
          ? "bg-red-500/20 text-red-500 hover:bg-red-500/30" 
          : "text-botanical-100 hover:text-botanical-50 hover:bg-botanical-700"
      )}
      title={isRecording ? "Stop Recording" : "Voice Input"}
    >
      {isRecording ? <MicOff size={20} className="animate-pulse" /> : <Mic size={20} />}
    </button>
  );
};
