"use client";

import React, { useState, useEffect } from 'react';
import { 
  Activity, 
  Database, 
  Cpu, 
  AlertTriangle, 
  Clock, 
  Users,
  Search,
  CheckCircle2,
  XCircle
} from 'lucide-react';

export default function MonitoringDashboard() {
  const [activeTab, setActiveTab] = useState<'application' | 'ai' | 'rag' | 'database'>('application');

  // Mock real-time metrics
  const metrics = {
    application: {
      uptime: "99.98%",
      apiErrors24h: 12,
      avgLatency: "145ms",
      requestsPerMin: 450,
    },
    ai: {
      modelCalls24h: 12450,
      tokenUsage: "4.2M",
      generationLatency: "2.1s",
      failedRequests: 3
    },
    rag: {
      retrievalCount: 8900,
      emptyRetrievals: 45,
      retrievalLatency: "320ms",
      citationFailures: 2
    },
    database: {
      activeConnections: 42,
      queriesPerSec: 156,
      storageUsed: "45.2 GB",
      connectionFailures: 0
    }
  };

  const logs = [
    { time: "10:24:01", module: "AI", status: "success", msg: "Generation completed", latency: "2104ms" },
    { time: "10:23:55", module: "RAG", status: "success", msg: "Hybrid search executed", latency: "312ms" },
    { time: "10:23:40", module: "Database", status: "error", msg: "Connection pool timeout", latency: "5000ms" },
    { time: "10:23:12", module: "Application", status: "success", msg: "POST /chat/stream", latency: "145ms" },
    { time: "10:22:05", module: "RAG", status: "warning", msg: "Empty retrieval for query", latency: "120ms" }
  ];

  return (
    <div className="p-6 max-w-7xl mx-auto space-y-6">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold text-gray-900 dark:text-white flex items-center gap-2">
          <Activity className="text-blue-500" />
          AYURLEX Telemetry & Observability
        </h1>
        <div className="flex items-center gap-2 text-sm text-green-600 bg-green-50 dark:bg-green-900/30 px-3 py-1 rounded-full border border-green-200 dark:border-green-800">
          <span className="w-2 h-2 rounded-full bg-green-500 animate-pulse"></span>
          System Operational
        </div>
      </div>

      {/* Tabs */}
      <div className="flex space-x-2 border-b border-gray-200 dark:border-gray-700 pb-2">
        {['application', 'ai', 'rag', 'database'].map((tab) => (
          <button
            key={tab}
            onClick={() => setActiveTab(tab as any)}
            className={`px-4 py-2 capitalize font-medium rounded-t-lg transition-colors ${
              activeTab === tab 
                ? 'bg-blue-50 text-blue-700 border-b-2 border-blue-600 dark:bg-blue-900/20 dark:text-blue-400'
                : 'text-gray-500 hover:text-gray-700 hover:bg-gray-50 dark:text-gray-400 dark:hover:bg-gray-800'
            }`}
          >
            {tab}
          </button>
        ))}
      </div>

      {/* Metric Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {Object.entries(metrics[activeTab]).map(([key, value]) => (
          <div key={key} className="bg-white dark:bg-gray-800 p-4 rounded-xl border border-gray-200 dark:border-gray-700 shadow-sm">
            <h3 className="text-sm font-medium text-gray-500 dark:text-gray-400 capitalize flex justify-between">
              {key.replace(/([A-Z])/g, ' $1').trim()}
              {key.toLowerCase().includes('fail') || key.toLowerCase().includes('error') ? (
                <AlertTriangle className="w-4 h-4 text-amber-500" />
              ) : (
                <CheckCircle2 className="w-4 h-4 text-green-500" />
              )}
            </h3>
            <p className="text-2xl font-bold text-gray-900 dark:text-white mt-2">{value}</p>
          </div>
        ))}
      </div>

      {/* Live Log Stream */}
      <div className="mt-8 bg-gray-900 rounded-xl overflow-hidden border border-gray-700 shadow-lg">
        <div className="bg-gray-800 px-4 py-3 border-b border-gray-700 flex justify-between items-center">
          <h2 className="text-sm font-semibold text-gray-200 flex items-center gap-2">
            <Clock className="w-4 h-4" />
            Live Structured Logs
          </h2>
          <div className="text-xs text-gray-400">Filtering sensitive data automatically</div>
        </div>
        <div className="p-4 font-mono text-sm overflow-x-auto space-y-2 max-h-96 overflow-y-auto">
          {logs.map((log, i) => (
            <div key={i} className="flex gap-4 items-start border-b border-gray-800 pb-2">
              <span className="text-gray-500 w-20 shrink-0">{log.time}</span>
              <span className={`px-2 py-0.5 rounded text-xs shrink-0 ${
                log.status === 'success' ? 'bg-green-900/50 text-green-400' :
                log.status === 'error' ? 'bg-red-900/50 text-red-400' :
                'bg-amber-900/50 text-amber-400'
              }`}>
                {log.status.toUpperCase()}
              </span>
              <span className="text-blue-400 w-24 shrink-0">[{log.module}]</span>
              <span className="text-gray-300 flex-1">{log.msg}</span>
              <span className="text-gray-500 shrink-0">{log.latency}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
