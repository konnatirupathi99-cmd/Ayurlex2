"use client";

import React, { useState } from "react";
import { 
  Search, 
  Filter,
  ExternalLink,
  BookOpen,
  FileText,
  Scale,
  ChevronRight,
  X
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";

type EvidenceCategory = 'Traditional Knowledge' | 'Clinical Study' | 'Patent' | 'Regulatory Guideline';

interface EvidenceSource {
  id: string;
  title: string;
  category: EvidenceCategory;
  language: string;
  excerpt: string;
  relevance: 'High' | 'Medium' | 'Low';
  date: string;
  fullText: string;
}

const mockEvidence: EvidenceSource[] = [
  {
    id: "TKDL-2023-A45",
    title: "Ayurvedic Pharmacopoeia of India (API) Vol. 1",
    category: "Traditional Knowledge",
    language: "Sanskrit/English",
    excerpt: "Withania somnifera (Ashwagandha) root powder is indicated for cognitive enhancement (Medhya) in adult populations...",
    relevance: "High",
    date: "2010-01-01",
    fullText: "Detailed monographs on the preparation, chemical constituents, and therapeutic uses of Ashwagandha as per traditional texts and modern standardization techniques. The document specifies that the root powder..."
  },
  {
    id: "PAT-US-1029483",
    title: "Method of extracting withanolides from Withania species",
    category: "Patent",
    language: "English",
    excerpt: "A method for obtaining high-yield withanolide extracts using supercritical fluid extraction...",
    relevance: "Medium",
    date: "2019-05-14",
    fullText: "The present invention relates to an improved method for extracting active withanolides from the roots and leaves of Withania somnifera..."
  },
  {
    id: "CLIN-2022-892",
    title: "Efficacy of Turmeric and Ashwagandha in Joint Health",
    category: "Clinical Study",
    language: "English",
    excerpt: "A double-blind, randomized, placebo-controlled study demonstrating significant improvements in joint mobility...",
    relevance: "High",
    date: "2022-11-20",
    fullText: "Patients administered a combination of 500mg Turmeric extract and 250mg Ashwagandha extract showed a 40% improvement in WOMAC scores..."
  },
  {
    id: "REG-AYUSH-2021",
    title: "Ministry of Ayush - Guidelines for Export of Polyherbal Formulations",
    category: "Regulatory Guideline",
    language: "English/Hindi",
    excerpt: "Standardization protocols and heavy metal limits for polyherbal formulations intended for European and US markets...",
    relevance: "High",
    date: "2021-08-05",
    fullText: "All polyherbal formulations must comply with the permissible limits for Lead, Arsenic, Mercury, and Cadmium as outlined in Annexure II..."
  }
];

export default function EvidenceExplorer() {
  const [searchQuery, setSearchQuery] = useState("");
  const [selectedSource, setSelectedSource] = useState<EvidenceSource | null>(null);

  const getCategoryIcon = (category: EvidenceCategory) => {
    switch (category) {
      case 'Traditional Knowledge': return <BookOpen className="w-4 h-4 text-amber-600" />;
      case 'Clinical Study': return <FileText className="w-4 h-4 text-blue-600" />;
      case 'Patent': return <Scale className="w-4 h-4 text-purple-600" />;
      case 'Regulatory Guideline': return <Scale className="w-4 h-4 text-emerald-600" />;
    }
  };

  const getRelevanceColor = (relevance: string) => {
    switch (relevance) {
      case 'High': return 'bg-emerald-100 text-emerald-800 border-emerald-200';
      case 'Medium': return 'bg-amber-100 text-amber-800 border-amber-200';
      case 'Low': return 'bg-stone-100 text-stone-800 border-stone-200';
      default: return 'bg-stone-100 text-stone-800 border-stone-200';
    }
  };

  return (
    <div className="flex h-full max-h-screen overflow-hidden">
      {/* Main Content */}
      <div className={`flex-1 flex flex-col h-full overflow-hidden transition-all duration-300 ${selectedSource ? 'pr-[400px] xl:pr-[500px]' : ''}`}>
        <div className="p-6 h-full flex flex-col space-y-6 overflow-y-auto">
          {/* Header */}
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div>
              <h1 className="text-2xl font-bold text-stone-900 tracking-tight">Evidence Explorer</h1>
              <p className="text-stone-500 mt-1">Browse, search, and verify all source documents.</p>
            </div>
          </div>

          {/* Filters and Search */}
          <div className="bg-white rounded-xl shadow-sm border border-stone-200 p-4 flex flex-col md:flex-row gap-4 shrink-0">
            <div className="relative flex-1">
              <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-400 w-5 h-5" />
              <input 
                type="text" 
                placeholder="Search by Title, ID, or content..." 
                className="w-full pl-10 pr-4 py-2 rounded-lg border border-stone-200 focus:outline-none focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-all bg-stone-50"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
              />
            </div>
            <div className="flex flex-wrap gap-3">
              <button className="inline-flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 bg-white hover:bg-stone-50 transition-colors">
                <Filter className="w-4 h-4 text-stone-500" />
                Category
              </button>
              <button className="inline-flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 bg-white hover:bg-stone-50 transition-colors">
                Relevance
              </button>
            </div>
          </div>

          {/* Evidence Grid */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-4 pb-6">
            {mockEvidence.map((source, idx) => (
              <motion.div 
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: idx * 0.05 }}
                key={source.id}
                onClick={() => setSelectedSource(source)}
                className={`bg-white rounded-xl p-5 border cursor-pointer hover:shadow-md transition-all ${selectedSource?.id === source.id ? 'border-botanical-500 ring-1 ring-botanical-500/20' : 'border-stone-200'}`}
              >
                <div className="flex items-start justify-between gap-4 mb-3">
                  <div className="flex items-center gap-2">
                    <span className="p-1.5 rounded-lg bg-stone-50 border border-stone-100">
                      {getCategoryIcon(source.category)}
                    </span>
                    <span className="text-xs font-medium text-stone-500 uppercase tracking-wider">{source.category}</span>
                  </div>
                  <span className={`text-xs px-2 py-1 rounded-md border font-medium ${getRelevanceColor(source.relevance)}`}>
                    {source.relevance} Relevance
                  </span>
                </div>
                
                <h3 className="text-base font-semibold text-stone-900 mb-2 leading-tight">
                  {source.title}
                </h3>
                
                <p className="text-sm text-stone-600 line-clamp-2 mb-4">
                  {source.excerpt}
                </p>
                
                <div className="flex items-center justify-between mt-auto pt-4 border-t border-stone-100">
                  <div className="flex items-center gap-3">
                    <span className="text-xs font-mono text-stone-400 bg-stone-50 px-2 py-1 rounded">{source.id}</span>
                    <span className="text-xs text-stone-400">{source.language}</span>
                  </div>
                  <button className="text-sm font-medium text-botanical-600 hover:text-botanical-700 inline-flex items-center gap-1">
                    View Source
                    <ChevronRight className="w-4 h-4" />
                  </button>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </div>

      {/* Side Drawer */}
      <AnimatePresence>
        {selectedSource && (
          <motion.div 
            initial={{ x: '100%', opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            exit={{ x: '100%', opacity: 0 }}
            transition={{ type: 'spring', damping: 25, stiffness: 200 }}
            className="fixed inset-y-0 right-0 w-[400px] xl:w-[500px] bg-white border-l border-stone-200 shadow-2xl z-40 flex flex-col"
          >
            <div className="flex items-center justify-between p-4 sm:p-6 border-b border-stone-200 bg-stone-50/50">
              <h2 className="text-lg font-semibold text-stone-900">Source Details</h2>
              <button 
                onClick={() => setSelectedSource(null)}
                className="p-2 text-stone-400 hover:text-stone-600 hover:bg-stone-100 rounded-full transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="flex-1 overflow-y-auto p-4 sm:p-6 space-y-6">
              <div>
                <div className="flex items-center gap-2 mb-3">
                  <span className="p-1.5 rounded-lg bg-stone-50 border border-stone-100">
                    {getCategoryIcon(selectedSource.category)}
                  </span>
                  <span className="text-sm font-medium text-stone-500 uppercase tracking-wider">{selectedSource.category}</span>
                </div>
                <h3 className="text-xl font-bold text-stone-900 leading-tight mb-2">
                  {selectedSource.title}
                </h3>
                <div className="flex flex-wrap items-center gap-2 text-sm text-stone-500 font-mono">
                  <span className="bg-stone-100 px-2 py-1 rounded">{selectedSource.id}</span>
                  <span>•</span>
                  <span>{selectedSource.date}</span>
                </div>
              </div>

              <div className="space-y-4">
                <div className="bg-stone-50 rounded-xl p-4 border border-stone-100">
                  <h4 className="text-xs font-semibold text-stone-900 uppercase tracking-wider mb-2">Relevance</h4>
                  <div className="flex items-center gap-2">
                    <span className={`text-sm px-2.5 py-1 rounded-md border font-medium ${getRelevanceColor(selectedSource.relevance)}`}>
                      {selectedSource.relevance}
                    </span>
                    <span className="text-sm text-stone-600">to current analysis context</span>
                  </div>
                </div>

                <div className="bg-stone-50 rounded-xl p-4 border border-stone-100">
                  <h4 className="text-xs font-semibold text-stone-900 uppercase tracking-wider mb-2">Language</h4>
                  <p className="text-sm text-stone-700">{selectedSource.language}</p>
                </div>
              </div>

              <div>
                <h4 className="text-sm font-semibold text-stone-900 mb-3 border-b border-stone-200 pb-2">Relevant Excerpt</h4>
                <div className="bg-amber-50/50 border-l-4 border-amber-400 p-4 rounded-r-lg text-sm text-stone-800 italic leading-relaxed">
                  "{selectedSource.excerpt}"
                </div>
              </div>

              <div>
                <h4 className="text-sm font-semibold text-stone-900 mb-3 border-b border-stone-200 pb-2">Full Context</h4>
                <div className="text-sm text-stone-700 leading-relaxed space-y-3">
                  <p>{selectedSource.fullText}</p>
                </div>
              </div>
            </div>

            <div className="p-4 sm:p-6 border-t border-stone-200 bg-stone-50/50 flex gap-3">
              <button className="flex-1 px-4 py-2 bg-botanical-600 text-white rounded-lg font-medium shadow-sm hover:bg-botanical-700 transition-colors flex items-center justify-center gap-2">
                <ExternalLink className="w-4 h-4" />
                View Original Document
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}
