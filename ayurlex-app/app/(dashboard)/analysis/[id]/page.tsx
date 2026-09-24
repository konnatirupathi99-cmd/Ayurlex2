"use client";

import React, { useState, useEffect } from "react";
import { 
  Download, 
  Share2, 
  Plus, 
  ShieldCheck, 
  AlertTriangle, 
  CheckCircle2, 
  Info,
  ChevronRight,
  ChevronDown,
  ExternalLink,
  X,
  FileText,
  Copy,
  Languages
} from "lucide-react";
import { motion, AnimatePresence } from "framer-motion";
import { useLanguage } from "@/components/LanguageProvider";

function TerminologyCard({ input, normalized, scientific }: { input: string, normalized: string, scientific: string }) {
  const [expanded, setExpanded] = useState(false);
  return (
    <div className="border border-stone-200 rounded-lg overflow-hidden bg-white">
      <button 
        onClick={() => setExpanded(!expanded)} 
        className="w-full px-4 py-3 flex items-center justify-between bg-stone-50 hover:bg-stone-100 transition-colors"
      >
        <div className="flex items-center gap-3">
          <Languages className="w-4 h-4 text-botanical-600" />
          <span className="font-medium text-stone-900">{input}</span>
        </div>
        {expanded ? <ChevronDown className="w-4 h-4 text-stone-400" /> : <ChevronRight className="w-4 h-4 text-stone-400" />}
      </button>
      <AnimatePresence>
        {expanded && (
          <motion.div 
            initial={{ height: 0 }} 
            animate={{ height: "auto" }} 
            exit={{ height: 0 }} 
            className="overflow-hidden"
          >
            <div className="p-4 bg-white border-t border-stone-100 space-y-2 text-sm">
              <div className="grid grid-cols-3 gap-2">
                <span className="text-stone-500 font-medium">User Input</span>
                <span className="col-span-2 text-stone-900">{input}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-stone-500 font-medium">Normalized Term</span>
                <span className="col-span-2 text-botanical-700 font-medium">{normalized}</span>
              </div>
              <div className="grid grid-cols-3 gap-2">
                <span className="text-stone-500 font-medium">Scientific Name</span>
                <span className="col-span-2 text-stone-700 italic">{scientific}</span>
              </div>
            </div>
          </motion.div>
        )}
      </AnimatePresence>
    </div>
  );
}

type Tab = 'Overview' | 'Classical Ayurvedic Rationale' | 'Contemporary Scientific Evidence' | 'Product or Process Novelty' | 'Jurisdictional Interpretation';

export default function IntelligenceReport({ params }: { params: { id: string } }) {
  const [activeTab, setActiveTab] = useState<Tab>('Overview');
  const [evidenceDrawerOpen, setEvidenceDrawerOpen] = useState(false);
  const [selectedEvidence, setSelectedEvidence] = useState<any>(null);
  
  const { languageName } = useLanguage();
  const [reportLang, setReportLang] = useState(languageName);

  useEffect(() => {
    const mockLang = sessionStorage.getItem('ayurlex_mock_report_lang');
    if (mockLang) {
      setReportLang(mockLang);
    } else {
      setReportLang(languageName);
    }
  }, [languageName]);

  const tabs: Tab[] = [
    'Overview', 
    'Classical Ayurvedic Rationale', 
    'Contemporary Scientific Evidence', 
    'Product or Process Novelty', 
    'Jurisdictional Interpretation'
  ];

  const openEvidence = (evidence: any) => {
    setSelectedEvidence(evidence);
    setEvidenceDrawerOpen(true);
  };

  return (
    <div className="space-y-6 pb-12 relative">
      {/* Report Header */}
      <div className="flex flex-col md:flex-row md:items-start justify-between gap-4 bg-white p-6 rounded-2xl border border-stone-200 shadow-sm">
        <div>
          <h1 className="text-sm font-bold tracking-wider text-botanical-700 uppercase mb-2">AYURLEX Intelligence Report</h1>
          <h2 className="text-2xl font-bold text-stone-900 mb-2">Ashwagandha & Turmeric Immunity Blend</h2>
          <div className="flex flex-wrap items-center gap-x-4 gap-y-2 text-sm text-stone-500">
            <span>ID: {params.id}</span>
            <span>•</span>
            <span>Jurisdiction: International</span>
            <span>•</span>
            <span>Language: {reportLang}</span>
            <span>•</span>
            <span>Date: Oct 14, 2024</span>
          </div>
        </div>
        <div className="flex flex-wrap items-center gap-3">
          <button className="inline-flex items-center justify-center rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-800 font-medium px-4 py-2 transition-colors text-sm">
            <Download className="w-4 h-4 mr-2" /> Export
          </button>
          <button className="inline-flex items-center justify-center rounded-lg bg-stone-100 hover:bg-stone-200 text-stone-800 font-medium px-4 py-2 transition-colors text-sm">
            <Share2 className="w-4 h-4 mr-2" /> Share
          </button>
          <button className="inline-flex items-center justify-center rounded-lg bg-botanical-700 hover:bg-botanical-800 text-white font-medium px-4 py-2 transition-colors text-sm shadow-sm">
            <Plus className="w-4 h-4 mr-2" /> New Analysis
          </button>
        </div>
      </div>

      {/* Summary Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <div className="bg-white p-5 rounded-xl border border-stone-200 shadow-sm border-t-4 border-t-blue-500">
          <p className="text-sm font-medium text-stone-500 mb-1">Formulation Context</p>
          <p className="text-lg font-bold text-stone-900">Potentially Novel</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-stone-200 shadow-sm border-t-4 border-t-amber-500">
          <p className="text-sm font-medium text-stone-500 mb-1">IP Context</p>
          <p className="text-lg font-bold text-stone-900">Further Review Recommended</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-stone-200 shadow-sm border-t-4 border-t-botanical-500">
          <p className="text-sm font-medium text-stone-500 mb-1">Evidence Confidence</p>
          <p className="text-lg font-bold text-stone-900">78%</p>
        </div>
        <div className="bg-white p-5 rounded-xl border border-stone-200 shadow-sm border-t-4 border-t-red-500">
          <p className="text-sm font-medium text-stone-500 mb-1">Review Priority</p>
          <p className="text-lg font-bold text-stone-900">Moderate</p>
        </div>
      </div>

      {/* Tabs Navigation */}
      <div className="border-b border-stone-200 overflow-x-auto no-scrollbar">
        <nav className="flex space-x-8 min-w-max px-2">
          {tabs.map(tab => (
            <button
              key={tab}
              onClick={() => setActiveTab(tab)}
              className={`
                whitespace-nowrap py-4 px-1 border-b-2 font-medium text-sm transition-colors
                ${activeTab === tab 
                  ? 'border-botanical-600 text-botanical-700' 
                  : 'border-transparent text-stone-500 hover:text-stone-700 hover:border-stone-300'}
              `}
            >
              {tab}
            </button>
          ))}
        </nav>
      </div>

      {/* Tab Content Area */}
      <div className="bg-white rounded-2xl border border-stone-200 shadow-sm min-h-[500px]">
        {activeTab === 'Overview' && (
          <div className="p-6 sm:p-8 space-y-8 animate-in fade-in duration-500">
            <div>
              <h3 className="text-lg font-bold text-stone-900 mb-4">Executive Summary</h3>
              <p className="text-stone-600 leading-relaxed">
                The analysed formulation combines Ashwagandha (Withania somnifera) and Turmeric (Curcuma longa). 
                AI intelligence indicates that while individual ingredients have extensive traditional knowledge references 
                for immunity and wellness, the specific combination and extraction matrix described may present novel 
                characteristics. Further review of prior-art is recommended to ensure IP viability.
              </p>
            </div>

            <div className="space-y-4">
              <h3 className="text-lg font-bold text-stone-900">Normalized Terminology</h3>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <TerminologyCard input="అశ్వగంధ" normalized="Ashwagandha" scientific="Withania somnifera" />
                <TerminologyCard input="పసుపు" normalized="Turmeric" scientific="Curcuma longa" />
              </div>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div className="space-y-4">
                <h3 className="text-lg font-bold text-stone-900">Key Intelligence Signals</h3>
                <div className="space-y-3">
                  <div className="flex items-start gap-3 p-4 rounded-lg bg-blue-50 border border-blue-100">
                    <Info className="w-5 h-5 text-blue-600 shrink-0 mt-0.5" />
                    <div>
                      <p className="text-sm font-semibold text-blue-900">12 Evidence Sources Retrieved</p>
                      <p className="text-xs text-blue-800 mt-1">Cross-referenced across IP and classical texts.</p>
                    </div>
                  </div>
                  <div className="flex items-start gap-3 p-4 rounded-lg bg-amber-50 border border-amber-100">
                    <AlertTriangle className="w-5 h-5 text-amber-600 shrink-0 mt-0.5" />
                    <div>
                      <p className="text-sm font-semibold text-amber-900">Further Review Recommended</p>
                      <p className="text-xs text-amber-800 mt-1">Potential overlap with 2 existing international patents.</p>
                    </div>
                  </div>
                </div>
              </div>

              <div>
                <h3 className="text-lg font-bold text-stone-900 mb-4">Analysis Confidence</h3>
                <div className="bg-stone-50 p-6 rounded-xl border border-stone-200">
                  <div className="flex justify-between items-end mb-2">
                    <span className="text-3xl font-black text-botanical-700 tracking-tighter">78%</span>
                    <span className="text-sm font-medium text-stone-500 mb-1">High Confidence</span>
                  </div>
                  <div className="w-full bg-stone-200 rounded-full h-3 mb-4 overflow-hidden">
                    <div className="bg-botanical-600 h-3 rounded-full" style={{ width: '78%' }}></div>
                  </div>
                  <p className="text-xs text-stone-500 leading-relaxed italic">
                    Confidence reflects the available evidence and analysis consistency. It does not represent legal certainty.
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'Classical Ayurvedic Rationale' && (
          <div className="p-6 sm:p-8 animate-in fade-in duration-500">
            <h3 className="text-lg font-bold text-stone-900 mb-6">Classical Ayurvedic Rationale</h3>
            <div className="space-y-4">
              <div className="border border-stone-200 rounded-xl p-5 hover:border-botanical-300 transition-colors bg-white">
                <div className="flex justify-between items-start mb-2">
                  <div className="flex items-center gap-2">
                    <span className="bg-stone-100 text-stone-600 text-xs font-bold px-2 py-1 rounded">TK-1</span>
                    <h4 className="font-bold text-stone-900">Charaka Samhita Reference</h4>
                  </div>
                  <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-botanical-100 text-botanical-800">High Relevance</span>
                </div>
                <p className="text-sm font-medium text-stone-700 mb-2">Traditional Knowledge Context:</p>
                <blockquote className="border-l-2 border-stone-300 pl-4 py-1 text-sm text-stone-600 italic mb-4 bg-stone-50 rounded-r-lg">
                  "Use of Haridra (Turmeric) for balancing doshas and promoting general immunity is well documented..."
                </blockquote>
                <div className="flex gap-4">
                  <button onClick={() => openEvidence({ id: 'TK-1', title: 'Charaka Samhita Sutrasthana', type: 'Classical Text', relevance: 'High' })} className="text-sm font-medium text-botanical-600 flex items-center hover:text-botanical-800 bg-botanical-50 px-3 py-1.5 rounded-lg w-max">
                    <FileText className="w-4 h-4 mr-2" /> View Source
                  </button>
                  <span className="text-sm text-stone-500 flex items-center"><Info className="w-4 h-4 mr-1"/> Botanical: <i>Curcuma longa</i></span>
                </div>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'Contemporary Scientific Evidence' && (
          <div className="p-6 sm:p-8 animate-in fade-in duration-500">
            <h3 className="text-lg font-bold text-stone-900 mb-6">Contemporary Scientific Evidence</h3>
            <div className="space-y-4">
              <div className="border border-stone-200 rounded-xl p-5 hover:border-botanical-300 transition-colors bg-white">
                <div className="flex justify-between items-start mb-2">
                  <div className="flex items-center gap-2">
                    <span className="bg-stone-100 text-stone-600 text-xs font-bold px-2 py-1 rounded">SCI-1</span>
                    <h4 className="font-bold text-stone-900">Clinical Efficacy of Ashwagandha</h4>
                  </div>
                  <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-blue-100 text-blue-800">Strong Evidence</span>
                </div>
                <p className="text-sm text-stone-700 mb-4">
                  Recent double-blind placebo-controlled studies have corroborated the adaptogenic properties of <i className="text-stone-900">Withania somnifera</i> root extract.
                </p>
                <div className="bg-amber-50 border border-amber-200 rounded p-3 mb-4 flex gap-2">
                   <AlertTriangle className="w-4 h-4 text-amber-600 shrink-0" />
                   <p className="text-xs text-amber-900">Evidence Gap: Long-term synergistic effects of combining with Curcumin remain under-studied in modern clinical contexts.</p>
                </div>
                <button onClick={() => openEvidence({ id: 'SCI-1', title: 'Journal of Ethnopharmacology', type: 'Scientific Journal', relevance: 'High' })} className="text-sm font-medium text-botanical-600 flex items-center hover:text-botanical-800 bg-botanical-50 px-3 py-1.5 rounded-lg w-max">
                  <FileText className="w-4 h-4 mr-2" /> View Journal Abstract
                </button>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'Product or Process Novelty' && (
          <div className="p-6 sm:p-8 space-y-8 animate-in fade-in duration-500">
            <h3 className="text-lg font-bold text-stone-900 mb-4">Product or Process Novelty (IP)</h3>
            
            <div className="space-y-4">
              <div className="border border-stone-200 rounded-xl p-5 bg-white">
                <div className="flex justify-between items-start mb-2">
                  <h4 className="font-bold text-stone-900">Patent Context</h4>
                  <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-amber-100 text-amber-800">Review Advised</span>
                </div>
                <p className="text-sm text-stone-600 mb-4">Found 2 internationally filed patents detailing similar extraction methods for <i>Withania somnifera</i>.</p>
                <button onClick={() => openEvidence({ id: 'P-102', title: 'Extraction of Withanolides', type: 'Patent', relevance: 'High' })} className="text-sm font-medium text-botanical-600 flex items-center hover:text-botanical-800">
                  <ExternalLink className="w-4 h-4 mr-1" /> View Related Evidence
                </button>
              </div>

              <div className="border border-stone-200 rounded-xl p-5 bg-white">
                <div className="flex justify-between items-start mb-2">
                  <h4 className="font-bold text-stone-900">Prior-Art Considerations</h4>
                  <span className="px-2.5 py-1 text-xs font-semibold rounded-full bg-stone-100 text-stone-800">Standard</span>
                </div>
                <p className="text-sm text-stone-600 mb-4">Extensive prior art exists for the individual use of the listed botanicals, reducing likelihood of novelty for mere admixture.</p>
              </div>
            </div>
          </div>
        )}

        {activeTab === 'Jurisdictional Interpretation' && (
          <div className="p-6 sm:p-8 animate-in fade-in duration-500">
             <h3 className="text-lg font-bold text-stone-900 mb-6">Jurisdictional Interpretation</h3>
            <div className="bg-blue-50 border border-blue-200 rounded-xl p-5 mb-8">
              <div className="flex gap-3">
                <Info className="w-6 h-6 text-blue-600 shrink-0" />
                <div>
                  <h4 className="font-bold text-blue-900 mb-1">Regulatory Context</h4>
                  <p className="text-sm text-blue-800 leading-relaxed mb-3">
                    This system provides intelligence signals regarding Access and Benefit Sharing (ABS) and product classification based on the biological resources identified. <strong>It does not provide a final legal determination.</strong>
                  </p>
                </div>
              </div>
            </div>

            <div className="space-y-6">
              <div className="flex items-start gap-4 bg-white p-5 rounded-xl border border-stone-200">
                <div className="w-10 h-10 rounded-full bg-amber-100 flex items-center justify-center shrink-0">
                  <AlertTriangle className="w-5 h-5 text-amber-600" />
                </div>
                <div>
                  <h4 className="font-bold text-stone-900">ABS Applicability (India)</h4>
                  <p className="text-sm text-stone-600 mt-1">
                    The use of biological resources from India for commercial utilization may require prior intimation/approval under the Biological Diversity Act, 2002.
                  </p>
                </div>
              </div>
              <div className="flex items-start gap-4 bg-white p-5 rounded-xl border border-stone-200">
                <div className="w-10 h-10 rounded-full bg-botanical-100 flex items-center justify-center shrink-0">
                  <CheckCircle2 className="w-5 h-5 text-botanical-600" />
                </div>
                <div>
                  <h4 className="font-bold text-stone-900">Classification Pathway</h4>
                  <p className="text-sm text-stone-600 mt-1">
                    Potential classification under "Ayurvedic Proprietary Medicine" if manufactured in India under Section 3(a) of Drugs and Cosmetics Act, 1940.
                  </p>
                </div>
              </div>
            </div>
          </div>
        )}

      </div>

      {/* Evidence Drawer Overlay */}
      {evidenceDrawerOpen && (
        <div className="fixed inset-0 bg-stone-900/40 z-50 flex justify-end animate-in fade-in duration-300">
          <div className="bg-white w-full max-w-md h-full shadow-2xl flex flex-col animate-in slide-in-from-right duration-300">
            <div className="flex items-center justify-between p-6 border-b border-stone-200">
              <div>
                <span className="text-xs font-bold text-botanical-600 bg-botanical-50 px-2 py-1 rounded uppercase tracking-wider">{selectedEvidence?.type || 'Source'}</span>
                <h3 className="text-lg font-bold text-stone-900 mt-2">{selectedEvidence?.title || 'Evidence Detail'}</h3>
              </div>
              <button onClick={() => setEvidenceDrawerOpen(false)} className="p-2 hover:bg-stone-100 rounded-full transition-colors text-stone-500">
                <X className="w-5 h-5" />
              </button>
            </div>
            
            <div className="flex-1 overflow-y-auto p-6 space-y-6">
              <div>
                <h4 className="text-xs font-bold text-stone-500 uppercase tracking-wider mb-2">Metadata</h4>
                <div className="bg-stone-50 rounded-lg p-4 text-sm space-y-2 border border-stone-200">
                  <div className="flex justify-between"><span className="text-stone-500">Source ID</span><span className="font-medium">{selectedEvidence?.id}</span></div>
                  <div className="flex justify-between"><span className="text-stone-500">Language</span><span className="font-medium">Sanskrit / English</span></div>
                  <div className="flex justify-between"><span className="text-stone-500">Relevance</span><span className="font-medium text-red-600">{selectedEvidence?.relevance}</span></div>
                </div>
              </div>

              <div>
                <h4 className="text-xs font-bold text-stone-500 uppercase tracking-wider mb-2">Relevant Excerpt</h4>
                <div className="bg-botanical-50 border border-botanical-200 rounded-lg p-5 text-sm text-stone-800 leading-relaxed relative group">
                  <button className="absolute top-2 right-2 p-1.5 bg-white rounded shadow-sm opacity-0 group-hover:opacity-100 transition-opacity text-stone-500 hover:text-stone-900">
                    <Copy className="w-4 h-4" />
                  </button>
                  "...this combination has been documented to support systemic wellness and dosha balance when prepared as a decoction..."
                </div>
              </div>
            </div>

            <div className="p-6 border-t border-stone-200 bg-stone-50">
              <button className="w-full py-2.5 bg-white border border-stone-300 rounded-lg text-sm font-medium text-stone-700 hover:bg-stone-100 transition-colors flex items-center justify-center gap-2 shadow-sm">
                <Copy className="w-4 h-4" /> Copy Citation
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
