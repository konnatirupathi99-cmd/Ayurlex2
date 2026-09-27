import React from 'react';
import { Paperclip } from 'lucide-react';

interface FileUploaderProps {
  onFileSelect: (file: File) => void;
}

export const FileUploader: React.FC<FileUploaderProps> = ({ onFileSelect }) => {
  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    if (e.target.files && e.target.files[0]) {
      onFileSelect(e.target.files[0]);
    }
  };

  return (
    <div className="relative">
      <input
        type="file"
        id="file-upload"
        className="hidden"
        onChange={handleFileChange}
        accept=".pdf,.doc,.docx,.txt"
      />
      <label
        htmlFor="file-upload"
        className="flex items-center justify-center w-10 h-10 rounded-full text-botanical-100 hover:text-botanical-50 hover:bg-botanical-700 transition-colors cursor-pointer"
        title="Upload Document"
      >
        <Paperclip size={20} />
      </label>
    </div>
  );
};
