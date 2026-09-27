import React from 'react';
import { Settings, Sliders, Bell, Shield, Database } from 'lucide-react';

export const SettingsPanel: React.FC = () => {
  return (
    <div className="flex-1 overflow-y-auto p-6 bg-botanical-900">
      <div className="max-w-3xl mx-auto">
        <div className="flex items-center gap-3 mb-8">
          <div className="w-10 h-10 rounded-lg bg-botanical-800 flex items-center justify-center text-botanical-300">
            <Settings size={24} />
          </div>
          <h2 className="text-2xl font-semibold text-botanical-50">Settings</h2>
        </div>

        <div className="space-y-6">
          <section className="bg-botanical-800 border border-botanical-600 rounded-xl overflow-hidden">
            <div className="p-4 border-b border-botanical-600 bg-botanical-800/50 flex items-center gap-2">
              <Sliders size={18} className="text-botanical-200" />
              <h3 className="font-medium text-botanical-50">Model Preferences</h3>
            </div>
            <div className="p-4 space-y-4">
              <div>
                <label className="block text-sm font-medium text-botanical-100 mb-1">Response Style</label>
                <select className="w-full bg-botanical-900 border border-botanical-600 rounded-lg px-3 py-2 text-botanical-50 focus:outline-none focus:border-botanical-400">
                  <option>Balanced (Default)</option>
                  <option>Academic & Traditional</option>
                  <option>Regulatory & Legal</option>
                  <option>Concise</option>
                </select>
              </div>
              <div className="flex items-center justify-between">
                <div>
                  <h4 className="text-sm font-medium text-botanical-50">Provide Citations</h4>
                  <p className="text-xs text-botanical-200 mt-0.5">Always include source references for claims.</p>
                </div>
                <label className="relative inline-flex items-center cursor-pointer">
                  <input type="checkbox" className="sr-only peer" defaultChecked />
                  <div className="w-11 h-6 bg-botanical-600 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-botanical-400"></div>
                </label>
              </div>
            </div>
          </section>

          <section className="bg-botanical-800 border border-botanical-600 rounded-xl overflow-hidden">
            <div className="p-4 border-b border-botanical-600 bg-botanical-800/50 flex items-center gap-2">
              <Database size={18} className="text-botanical-200" />
              <h3 className="font-medium text-botanical-50">Knowledge Base</h3>
            </div>
            <div className="p-4">
              <div className="space-y-3">
                {['Classical Texts (Samhitas)', 'AYUSH Guidelines', 'Patent Databases', 'Modern Research Papers'].map(db => (
                  <label key={db} className="flex items-center gap-3">
                    <input type="checkbox" defaultChecked className="w-4 h-4 rounded border-botanical-600 bg-botanical-900 text-botanical-400 focus:ring-botanical-400 focus:ring-offset-botanical-800" />
                    <span className="text-sm text-botanical-100">{db}</span>
                  </label>
                ))}
              </div>
            </div>
          </section>
        </div>
      </div>
    </div>
  );
};
