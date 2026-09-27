import React, { useState } from 'react';

export interface CitationProps {
  citationId: string;
  documentTitle: string;
  authority: string;
  source: string;
  jurisdiction: string;
  publicationDate: string;
  pageOrSection: string;
  relevantExcerpt: string;
  referenceUrl?: string;
  relevanceScore: number;
}

export const CitationCard: React.FC<CitationProps> = ({
  citationId,
  documentTitle,
  authority,
  source,
  jurisdiction,
  publicationDate,
  pageOrSection,
  relevantExcerpt,
  referenceUrl,
  relevanceScore
}) => {
  const [activeTab, setActiveTab] = useState<'evidence' | 'context' | null>(null);

  return (
    <div className="bg-white dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-4 mb-4 shadow-sm hover:shadow-md transition-shadow">
      <div className="flex justify-between items-start mb-2">
        <div>
          <span className="text-xs font-bold bg-blue-100 text-blue-800 px-2 py-1 rounded mr-2">
            [{citationId}]
          </span>
          <h4 className="inline text-md font-semibold text-gray-900 dark:text-gray-100">
            {documentTitle}
          </h4>
        </div>
        <div className="text-right">
          <span className="text-xs font-medium text-gray-500 bg-gray-100 dark:bg-gray-700 px-2 py-1 rounded">
            Match: {(relevanceScore * 100).toFixed(0)}%
          </span>
        </div>
      </div>

      <div className="grid grid-cols-2 gap-2 text-sm text-gray-600 dark:text-gray-400 mb-4">
        <div><strong className="text-gray-700 dark:text-gray-300">Authority:</strong> {authority}</div>
        <div><strong className="text-gray-700 dark:text-gray-300">Jurisdiction:</strong> {jurisdiction}</div>
        <div><strong className="text-gray-700 dark:text-gray-300">Date:</strong> {publicationDate}</div>
        <div><strong className="text-gray-700 dark:text-gray-300">Location:</strong> {pageOrSection}</div>
      </div>

      <div className="flex space-x-2 text-sm">
        <button 
          onClick={() => setActiveTab(activeTab === 'evidence' ? null : 'evidence')}
          className="px-3 py-1.5 bg-gray-50 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 rounded border border-gray-200 dark:border-gray-600 transition-colors"
        >
          View Evidence
        </button>
        <button 
          onClick={() => setActiveTab(activeTab === 'context' ? null : 'context')}
          className="px-3 py-1.5 bg-gray-50 hover:bg-gray-100 dark:bg-gray-700 dark:hover:bg-gray-600 text-gray-700 dark:text-gray-200 rounded border border-gray-200 dark:border-gray-600 transition-colors"
        >
          View Context
        </button>
        {referenceUrl && (
          <a 
            href={referenceUrl} 
            target="_blank" 
            rel="noopener noreferrer"
            className="px-3 py-1.5 bg-blue-50 hover:bg-blue-100 text-blue-700 dark:bg-blue-900/30 dark:text-blue-400 dark:hover:bg-blue-900/50 rounded border border-blue-200 dark:border-blue-800 transition-colors"
          >
            View Source Document
          </a>
        )}
      </div>

      {activeTab === 'evidence' && (
        <div className="mt-4 p-3 bg-yellow-50 dark:bg-yellow-900/20 border-l-4 border-yellow-400 rounded">
          <h5 className="text-xs font-bold text-yellow-800 dark:text-yellow-500 mb-1">EXACT EXCERPT</h5>
          <p className="text-sm text-gray-800 dark:text-gray-200 italic">
            "{relevantExcerpt}"
          </p>
        </div>
      )}

      {activeTab === 'context' && (
        <div className="mt-4 p-3 bg-gray-50 dark:bg-gray-900/50 rounded border border-gray-100 dark:border-gray-700">
          <h5 className="text-xs font-bold text-gray-600 dark:text-gray-400 mb-1">BROADER CONTEXT</h5>
          <p className="text-sm text-gray-600 dark:text-gray-400">
            This excerpt was found in {source}, published by {authority}. It pertains to the jurisdiction of {jurisdiction}. 
            The semantic relevance engine determined a {(relevanceScore * 100).toFixed(1)}% match for your query.
          </p>
        </div>
      )}
    </div>
  );
};
