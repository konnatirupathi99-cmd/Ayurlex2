import React from 'react';
import { AnalysisCard } from './AnalysisCard';

export const ReportPanel: React.FC = () => {
  const analyses = [
    {
      id: '1',
      title: 'Ashwagandha Extract Formulation',
      summary: 'Analysis of novel extraction method vs traditional methods. Patentability assessment looks promising.',
      confidence: 0.88,
      date: '2 hours ago'
    },
    {
      id: '2',
      title: 'Triphala Quality Standards',
      summary: 'Regulatory compliance check for EU export. Minor adjustments needed in heavy metal testing documentation.',
      confidence: 0.95,
      date: 'Yesterday'
    }
  ];

  return (
    <div className="flex-1 overflow-y-auto p-6 bg-botanical-900">
      <div className="max-w-4xl mx-auto">
        <h2 className="text-2xl font-semibold text-botanical-50 mb-6">Recent Analyses</h2>
        <div className="grid gap-4 md:grid-cols-2">
          {analyses.map(analysis => (
            <AnalysisCard 
              key={analysis.id}
              title={analysis.title}
              summary={analysis.summary}
              confidence={analysis.confidence}
              date={analysis.date}
            />
          ))}
        </div>
      </div>
    </div>
  );
};
