"use client";

import React, { useState } from "react";
import { 
  UploadCloud, 
  Search, 
  Filter, 
  FileText, 
  MoreVertical, 
  Trash2, 
  Eye,
  CheckCircle2,
  RefreshCw,
  AlertCircle
} from "lucide-react";

export default function KnowledgeBase() {
  const [isDragging, setIsDragging] = useState(false);

  return (
    <div className="space-y-8 pb-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-bold text-stone-900">Knowledge Base</h1>
        <p className="text-stone-500 mt-1">Manage the reference documents used for AYURLEX evidence retrieval.</p>
      </div>

      {/* Upload Area */}
      <div 
        className={`border-2 border-dashed rounded-2xl p-12 text-center transition-colors ${isDragging ? 'border-botanical-500 bg-botanical-50' : 'border-stone-300 bg-white hover:border-botanical-400 hover:bg-stone-50'}`}
        onDragOver={(e) => { e.preventDefault(); setIsDragging(true); }}
        onDragLeave={() => setIsDragging(false)}
        onDrop={(e) => { e.preventDefault(); setIsDragging(false); }}
      >
        <div className="w-16 h-16 bg-botanical-100 rounded-full flex items-center justify-center mx-auto mb-4">
          <UploadCloud className="w-8 h-8 text-botanical-600" />
        </div>
        <h2 className="text-xl font-bold text-stone-900 mb-2">Upload Reference Documents</h2>
        <p className="text-sm text-stone-500 mb-6">Drag and drop files here, or click to browse. Supported formats: PDF, TXT.</p>
        <button className="px-6 py-2.5 bg-white border border-stone-300 rounded-lg text-sm font-medium text-stone-700 hover:bg-stone-50 transition-colors shadow-sm">
          Browse Files
        </button>
      </div>

      {/* Document Library */}
      <div className="bg-white border border-stone-200 rounded-xl shadow-sm overflow-hidden">
        {/* Toolbar */}
        <div className="p-4 border-b border-stone-200 flex flex-col sm:flex-row justify-between gap-4">
          <div className="relative w-full sm:w-96">
            <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-400" />
            <input 
              type="text" 
              placeholder="Search knowledge base..." 
              className="w-full pl-9 pr-4 py-2 bg-stone-50 border border-stone-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500"
            />
          </div>
          <button className="flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 hover:bg-stone-50 transition-colors">
            <Filter className="w-4 h-4" /> Filters
          </button>
        </div>

        {/* Table */}
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left whitespace-nowrap">
            <thead className="bg-stone-50 border-b border-stone-200 text-stone-600">
              <tr>
                <th className="px-6 py-4 font-semibold">Document Name</th>
                <th className="px-6 py-4 font-semibold">Category</th>
                <th className="px-6 py-4 font-semibold">Language</th>
                <th className="px-6 py-4 font-semibold">Upload Date</th>
                <th className="px-6 py-4 font-semibold">Status</th>
                <th className="px-6 py-4 font-semibold text-right">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-stone-100">
              <DocumentRow 
                name="Charaka Samhita - Sutrasthana.pdf" 
                category="Classical Text" 
                language="Sanskrit/English" 
                date="Oct 12, 2024" 
                status="Indexed" 
              />
              <DocumentRow 
                name="Patent_US10293847_Withania.pdf" 
                category="Patent" 
                language="English" 
                date="Oct 14, 2024" 
                status="Processing" 
              />
              <DocumentRow 
                name="Regulatory_Guidelines_AYUSH_2023.txt" 
                category="Regulatory Guideline" 
                language="English" 
                date="Sep 28, 2024" 
                status="Indexed" 
              />
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}

function DocumentRow({ name, category, language, date, status }: { name: string, category: string, language: string, date: string, status: string }) {
  
  const getStatusDisplay = () => {
    if (status === 'Indexed') {
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold rounded-full bg-green-100 text-green-800 border border-green-200">
          <CheckCircle2 className="w-3.5 h-3.5" /> Indexed
        </span>
      );
    }
    if (status === 'Processing') {
      return (
        <span className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold rounded-full bg-blue-100 text-blue-800 border border-blue-200">
          <RefreshCw className="w-3.5 h-3.5 animate-spin" /> Processing
        </span>
      );
    }
    return (
      <span className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-semibold rounded-full bg-red-100 text-red-800 border border-red-200">
        <AlertCircle className="w-3.5 h-3.5" /> Failed
      </span>
    );
  };

  return (
    <tr className="hover:bg-stone-50 transition-colors group">
      <td className="px-6 py-4">
        <div className="flex items-center gap-3">
          <div className="p-2 bg-stone-100 rounded text-stone-500">
            <FileText className="w-4 h-4" />
          </div>
          <span className="font-medium text-stone-900 max-w-[200px] sm:max-w-xs truncate">{name}</span>
        </div>
      </td>
      <td className="px-6 py-4 text-stone-500">{category}</td>
      <td className="px-6 py-4 text-stone-500">{language}</td>
      <td className="px-6 py-4 text-stone-500">{date}</td>
      <td className="px-6 py-4">
        {getStatusDisplay()}
      </td>
      <td className="px-6 py-4 text-right">
        <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
          <button className="p-1.5 text-stone-400 hover:text-stone-900 rounded hover:bg-stone-200 transition-colors" title="View">
            <Eye className="w-4 h-4" />
          </button>
          <button className="p-1.5 text-stone-400 hover:text-red-600 rounded hover:bg-red-50 transition-colors" title="Delete">
            <Trash2 className="w-4 h-4" />
          </button>
        </div>
      </td>
    </tr>
  );
}
