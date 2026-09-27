"use client";

import React from "react";
import Link from "next/link";
import { 
  Plus, 
  Database, 
  History, 
  FileText, 
  Search, 
  CheckCircle2, 
  Activity,
  AlertCircle
} from "lucide-react";

export default function WorkspaceDashboard() {
  return (
    <div className="space-y-8 pb-8">
      {/* Welcome Section */}
      <section className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 bg-white p-6 sm:p-8 rounded-2xl border border-stone-200 shadow-sm">
        <div>
          <h1 className="text-3xl font-bold text-stone-900 tracking-tight">Welcome to AYURLEX</h1>
          <p className="text-stone-500 mt-2 text-lg">Your intelligence workspace for Ayurvedic innovation.</p>
        </div>
        <Link href="/analysis/new" className="inline-flex items-center justify-center rounded-lg bg-botanical-700 hover:bg-botanical-800 text-white font-medium px-6 py-3 transition-colors shadow-sm whitespace-nowrap">
          <Plus className="w-5 h-5 mr-2" />
          New Analysis
        </Link>
      </section>

      {/* Intelligence Summary */}
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        <SummaryCard title="Total Analyses" value="12" icon={<Activity className="w-5 h-5 text-blue-500" />} />
        <SummaryCard title="Knowledge Documents" value="3,482" icon={<Database className="w-5 h-5 text-botanical-500" />} />
        <SummaryCard title="Evidence Retrieved" value="156" icon={<FileText className="w-5 h-5 text-amber-500" />} />
        <SummaryCard title="Active Analysis" value="1" icon={<Search className="w-5 h-5 text-purple-500" />} />
      </section>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2 space-y-8">
          {/* Quick Actions */}
          <section>
            <h2 className="text-lg font-bold text-stone-900 mb-4">Quick Actions</h2>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <QuickActionCard 
                href="/analysis/new"
                title="New Analysis"
                description="Start analysing an Ayurvedic innovation."
                icon={<Plus className="w-6 h-6 text-botanical-600" />}
              />
              <QuickActionCard 
                href="/knowledge"
                title="Knowledge Base"
                description="Explore and manage reference documents."
                icon={<Database className="w-6 h-6 text-blue-600" />}
              />
              <QuickActionCard 
                href="/history"
                title="Analysis History"
                description="Review previous intelligence reports."
                icon={<History className="w-6 h-6 text-amber-600" />}
              />
            </div>
          </section>

          {/* Recent Analyses */}
          <section>
            <div className="flex items-center justify-between mb-4">
              <h2 className="text-lg font-bold text-stone-900">Recent Analyses</h2>
              <Link href="/history" className="text-sm font-medium text-botanical-600 hover:text-botanical-800">
                View All
              </Link>
            </div>
            <div className="bg-white border border-stone-200 rounded-xl shadow-sm overflow-hidden">
              <div className="overflow-x-auto">
                <table className="w-full text-sm text-left">
                  <thead className="bg-stone-50 border-b border-stone-200 text-stone-600">
                    <tr>
                      <th className="px-6 py-4 font-semibold">Innovation</th>
                      <th className="px-6 py-4 font-semibold">Jurisdiction</th>
                      <th className="px-6 py-4 font-semibold">Status</th>
                      <th className="px-6 py-4 font-semibold">Date</th>
                      <th className="px-6 py-4 font-semibold text-right">Confidence</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-stone-100">
                    <AnalysisRow id="1" name="Ashwagandha Ext. Matrix" jurisdiction="International" status="Completed" date="Oct 12, 2024" confidence="82%" />
                    <AnalysisRow id="2" name="Triphala Digestive Blend" jurisdiction="India" status="Needs Review" date="Oct 10, 2024" confidence="64%" />
                    <AnalysisRow id="3" name="Brahmi Focus Supplement" jurisdiction="Auto" status="Processing" date="Oct 14, 2024" confidence="--" />
                  </tbody>
                </table>
              </div>
            </div>
          </section>
        </div>

        {/* Sidebar Widgets */}
        <div className="space-y-8">
          {/* System Status */}
          <section className="bg-white p-6 rounded-xl border border-stone-200 shadow-sm">
            <h2 className="text-base font-bold text-stone-900 mb-4">System Status</h2>
            <div className="space-y-4">
              <StatusItem label="AI Intelligence Engine" status="operational" />
              <StatusItem label="Knowledge Retrieval" status="operational" />
              <StatusItem label="Evidence System" status="operational" />
              <StatusItem label="Backend Connection" status="warning" />
            </div>
          </section>

          {/* Mini Help/Tip */}
          <section className="bg-botanical-50 p-6 rounded-xl border border-botanical-100 text-botanical-900">
            <h3 className="font-bold mb-2 flex items-center gap-2">
              <AlertCircle className="w-5 h-5" />
              Research Tip
            </h3>
            <p className="text-sm text-botanical-800 leading-relaxed">
              When entering ingredients, use specific botanical names or standard Ayurvedic terminology for the most accurate evidence retrieval and intelligence mapping.
            </p>
          </section>
        </div>
      </div>
    </div>
  );
}

function SummaryCard({ title, value, icon }: { title: string, value: string, icon: React.ReactNode }) {
  return (
    <div className="bg-white p-5 rounded-xl border border-stone-200 shadow-sm flex items-start gap-4">
      <div className="p-3 bg-stone-50 rounded-lg border border-stone-100">
        {icon}
      </div>
      <div>
        <p className="text-sm font-medium text-stone-500 mb-1">{title}</p>
        <p className="text-2xl font-bold text-stone-900">{value}</p>
      </div>
    </div>
  );
}

function QuickActionCard({ href, title, description, icon }: { href: string, title: string, description: string, icon: React.ReactNode }) {
  return (
    <Link href={href} className="group block p-5 bg-white rounded-xl border border-stone-200 hover:border-botanical-300 hover:shadow-md transition-all text-left">
      <div className="w-10 h-10 rounded-lg bg-botanical-50 flex items-center justify-center mb-4 group-hover:bg-botanical-100 transition-colors">
        {icon}
      </div>
      <h3 className="font-semibold text-stone-900 mb-1">{title}</h3>
      <p className="text-xs text-stone-500 line-clamp-2">{description}</p>
    </Link>
  );
}

function AnalysisRow({ id, name, jurisdiction, status, date, confidence }: { id: string, name: string, jurisdiction: string, status: string, date: string, confidence: string }) {
  const getStatusStyle = (s: string) => {
    if (s === 'Completed') return 'bg-green-100 text-green-800 border-green-200';
    if (s === 'Needs Review') return 'bg-amber-100 text-amber-800 border-amber-200';
    return 'bg-blue-100 text-blue-800 border-blue-200';
  };

  return (
    <tr className="hover:bg-stone-50 group cursor-pointer" onClick={() => window.location.href = `/analysis/${id}`}>
      <td className="px-6 py-4 font-medium text-stone-900">{name}</td>
      <td className="px-6 py-4 text-stone-500">{jurisdiction}</td>
      <td className="px-6 py-4">
        <span className={`px-2.5 py-1 text-xs font-semibold rounded-full border ${getStatusStyle(status)}`}>
          {status}
        </span>
      </td>
      <td className="px-6 py-4 text-stone-500">{date}</td>
      <td className="px-6 py-4 text-right font-medium text-stone-900">{confidence}</td>
    </tr>
  );
}

function StatusItem({ label, status }: { label: string, status: 'operational' | 'warning' | 'error' }) {
  const getStatusIcon = () => {
    if (status === 'operational') return <CheckCircle2 className="w-4 h-4 text-botanical-500" />;
    if (status === 'warning') return <AlertCircle className="w-4 h-4 text-amber-500" />;
    return <AlertCircle className="w-4 h-4 text-red-500" />;
  };

  return (
    <div className="flex items-center justify-between text-sm">
      <span className="text-stone-600">{label}</span>
      <div className="flex items-center gap-2">
        <span className="text-stone-900 font-medium capitalize hidden sm:inline-block">{status}</span>
        {getStatusIcon()}
      </div>
    </div>
  );
}
