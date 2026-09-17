"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  Search, 
  Filter,
  Calendar,
  ChevronDown,
  ArrowRight,
  CheckCircle2,
  AlertTriangle,
  Clock,
  MoreVertical
} from "lucide-react";
import { motion } from "framer-motion";

type AnalysisStatus = 'completed' | 'processing' | 'failed';

interface AnalysisRecord {
  id: string;
  name: string;
  date: string;
  status: AnalysisStatus;
  confidence: number;
  jurisdiction: string;
  language: string;
}

const mockHistory: AnalysisRecord[] = [
  {
    id: "ANL-2024-089",
    name: "Ashwagandha Cognitive Support Blend",
    date: "2024-10-15",
    status: "completed",
    confidence: 94,
    jurisdiction: "International",
    language: "English"
  },
  {
    id: "ANL-2024-088",
    name: "Turmeric Joint Relief Formula V2",
    date: "2024-10-14",
    status: "completed",
    confidence: 88,
    jurisdiction: "India",
    language: "English"
  },
  {
    id: "ANL-2024-087",
    name: "Tulsi Respiratory Extract",
    date: "2024-10-12",
    status: "processing",
    confidence: 0,
    jurisdiction: "Auto",
    language: "Hindi"
  },
  {
    id: "ANL-2024-086",
    name: "Brahmi Focus Complex",
    date: "2024-10-10",
    status: "failed",
    confidence: 0,
    jurisdiction: "India",
    language: "Telugu"
  },
  {
    id: "ANL-2024-085",
    name: "Triphala Digestive Aid",
    date: "2024-10-05",
    status: "completed",
    confidence: 97,
    jurisdiction: "International",
    language: "English"
  }
];

export default function AnalysisHistory() {
  const [searchQuery, setSearchQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("All");

  const getStatusIcon = (status: AnalysisStatus) => {
    switch (status) {
      case 'completed': return <CheckCircle2 className="w-4 h-4 text-emerald-600" />;
      case 'processing': return <Clock className="w-4 h-4 text-amber-600" />;
      case 'failed': return <AlertTriangle className="w-4 h-4 text-red-600" />;
    }
  };

  const getStatusBadge = (status: AnalysisStatus) => {
    switch (status) {
      case 'completed': 
        return <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-emerald-50 text-emerald-700 border border-emerald-200">{getStatusIcon(status)} Completed</span>;
      case 'processing': 
        return <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-amber-50 text-amber-700 border border-amber-200">{getStatusIcon(status)} Processing</span>;
      case 'failed': 
        return <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium bg-red-50 text-red-700 border border-red-200">{getStatusIcon(status)} Failed</span>;
    }
  };

  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-bold text-stone-900 tracking-tight">Analysis History</h1>
          <p className="text-stone-500 mt-1">Review past intelligence reports and formulations.</p>
        </div>
        <Link 
          href="/analysis/new" 
          className="inline-flex items-center justify-center px-4 py-2 bg-botanical-600 text-white rounded-lg font-medium shadow-sm shadow-botanical-600/20 hover:bg-botanical-700 transition-colors"
        >
          New Analysis
        </Link>
      </div>

      {/* Filters and Search */}
      <div className="bg-white rounded-xl shadow-sm border border-stone-200 p-4 flex flex-col md:flex-row gap-4">
        <div className="relative flex-1">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 text-stone-400 w-5 h-5" />
          <input 
            type="text" 
            placeholder="Search by innovation name or ID..." 
            className="w-full pl-10 pr-4 py-2 rounded-lg border border-stone-200 focus:outline-none focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-all bg-stone-50"
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
          />
        </div>
        <div className="flex flex-wrap gap-3">
          <button className="inline-flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 bg-white hover:bg-stone-50 transition-colors">
            <Filter className="w-4 h-4 text-stone-500" />
            Jurisdiction
            <ChevronDown className="w-4 h-4 text-stone-400" />
          </button>
          <button className="inline-flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 bg-white hover:bg-stone-50 transition-colors">
            Language
            <ChevronDown className="w-4 h-4 text-stone-400" />
          </button>
          <button className="inline-flex items-center gap-2 px-4 py-2 border border-stone-200 rounded-lg text-sm font-medium text-stone-700 bg-white hover:bg-stone-50 transition-colors">
            <Calendar className="w-4 h-4 text-stone-500" />
            Date Range
          </button>
        </div>
      </div>

      {/* Results Table */}
      <div className="bg-white rounded-xl shadow-sm border border-stone-200 overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-sm text-left">
            <thead className="text-xs text-stone-500 uppercase bg-stone-50/50 border-b border-stone-200">
              <tr>
                <th scope="col" className="px-6 py-4 font-medium">Innovation</th>
                <th scope="col" className="px-6 py-4 font-medium">Date</th>
                <th scope="col" className="px-6 py-4 font-medium">Jurisdiction / Lang</th>
                <th scope="col" className="px-6 py-4 font-medium">Status</th>
                <th scope="col" className="px-6 py-4 font-medium">Confidence</th>
                <th scope="col" className="px-6 py-4 text-right font-medium">Actions</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-stone-200">
              {mockHistory.map((record, idx) => (
                <motion.tr 
                  initial={{ opacity: 0, y: 10 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ delay: idx * 0.05 }}
                  key={record.id} 
                  className="hover:bg-stone-50/50 transition-colors group"
                >
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="font-medium text-stone-900">{record.name}</div>
                    <div className="text-stone-500 text-xs mt-0.5">{record.id}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-stone-600">
                    {record.date}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    <div className="text-stone-700">{record.jurisdiction}</div>
                    <div className="text-stone-500 text-xs mt-0.5">{record.language}</div>
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    {getStatusBadge(record.status)}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap">
                    {record.status === 'completed' ? (
                      <div className="flex items-center gap-2">
                        <div className="w-full bg-stone-200 rounded-full h-1.5 max-w-[60px]">
                          <div 
                            className="bg-botanical-600 h-1.5 rounded-full" 
                            style={{ width: `${record.confidence}%` }}
                          ></div>
                        </div>
                        <span className="text-xs font-medium text-stone-700">{record.confidence}%</span>
                      </div>
                    ) : (
                      <span className="text-stone-400 text-xs">-</span>
                    )}
                  </td>
                  <td className="px-6 py-4 whitespace-nowrap text-right">
                    <div className="flex items-center justify-end gap-2 opacity-0 group-hover:opacity-100 transition-opacity">
                      {record.status === 'completed' && (
                        <Link 
                          href={`/analysis/${record.id}`}
                          className="inline-flex items-center gap-1.5 px-3 py-1.5 text-sm font-medium text-botanical-700 bg-botanical-50 rounded-lg hover:bg-botanical-100 transition-colors"
                        >
                          Open Report
                          <ArrowRight className="w-3.5 h-3.5" />
                        </Link>
                      )}
                      <button className="p-1.5 text-stone-400 hover:text-stone-600 hover:bg-stone-100 rounded-lg transition-colors">
                        <MoreVertical className="w-5 h-5" />
                      </button>
                    </div>
                  </td>
                </motion.tr>
              ))}
            </tbody>
          </table>
        </div>
        
        {/* Pagination (Mock) */}
        <div className="px-6 py-4 border-t border-stone-200 flex items-center justify-between bg-stone-50/30">
          <span className="text-sm text-stone-500">Showing <span className="font-medium text-stone-900">1</span> to <span className="font-medium text-stone-900">5</span> of <span className="font-medium text-stone-900">24</span> results</span>
          <div className="flex gap-2">
            <button className="px-3 py-1 border border-stone-200 rounded-lg text-sm text-stone-400 bg-stone-100 cursor-not-allowed">Previous</button>
            <button className="px-3 py-1 border border-stone-200 rounded-lg text-sm text-stone-700 bg-white hover:bg-stone-50 transition-colors">Next</button>
          </div>
        </div>
      </div>
    </div>
  );
}
