import React from 'react';
import { Leaf, MessageSquare, Database, FileText, Settings, ShieldAlert, History } from 'lucide-react';

export default function Sidebar() {
  return (
    <aside className="w-64 bg-[var(--color-ayur-900)] flex flex-col h-full py-4 border-r border-[var(--color-ayur-700)]">
      <div className="flex items-center gap-2 px-6 mb-8 text-[var(--color-ayur-200)]">
        <Leaf size={28} />
        <h1 className="text-2xl font-semibold tracking-wide text-white">AYURLEX</h1>
      </div>
      
      <nav className="flex-1 px-4 space-y-2">
        <SidebarItem icon={<MessageSquare size={20} />} label="New Research" active />
        <SidebarItem icon={<History size={20} />} label="Recent Chats" />
        <SidebarItem icon={<Database size={20} />} label="Knowledge Base" />
        <SidebarItem icon={<FileText size={20} />} label="Upload Documents" />
        <SidebarItem icon={<ShieldAlert size={20} />} label="IP Intelligence" />
      </nav>
      
      <div className="px-4 mt-auto">
        <SidebarItem icon={<Settings size={20} />} label="Settings" />
      </div>
    </aside>
  );
}

function SidebarItem({ icon, label, active = false }: { icon: React.ReactNode, label: string, active?: boolean }) {
  return (
    <button className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg transition-colors text-left ${active ? 'bg-[var(--color-ayur-600)] text-white' : 'text-[var(--color-ayur-100)] hover:bg-[var(--color-ayur-700)] hover:text-white'}`}>
      {icon}
      <span className="font-medium text-sm">{label}</span>
    </button>
  );
}
