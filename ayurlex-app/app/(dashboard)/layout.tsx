"use client";

import React, { useState } from "react";
import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  Leaf, 
  LayoutDashboard, 
  PlusCircle, 
  Database, 
  History, 
  Settings, 
  HelpCircle,
  Menu,
  X,
  Search,
  Bell,
  Globe,
  User
} from "lucide-react";

import { useLanguage } from "@/components/LanguageProvider";

function LanguageSelector() {
  const { language, setLanguage } = useLanguage();
  return (
    <select 
      value={language} 
      onChange={(e) => setLanguage(e.target.value as 'en'|'hi'|'te')}
      className="appearance-none bg-transparent font-medium uppercase outline-none cursor-pointer"
    >
      <option value="en">EN</option>
      <option value="hi">HI</option>
      <option value="te">TE</option>
    </select>
  );
}

export default function DashboardLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const pathname = usePathname();

  const getPageTitle = () => {
    if (pathname === '/workspace') return 'Overview';
    if (pathname?.includes('/analysis/new')) return 'New Analysis';
    if (pathname?.includes('/analysis')) return 'Intelligence Report';
    if (pathname?.includes('/evidence')) return 'Evidence Explorer';
    if (pathname?.includes('/knowledge')) return 'Knowledge Base';
    if (pathname?.includes('/history')) return 'Analysis History';
    if (pathname?.includes('/settings')) return 'Settings';
    return 'Dashboard';
  };

  return (
    <div className="min-h-screen bg-background flex">
      {/* Mobile Sidebar Overlay */}
      {sidebarOpen && (
        <div 
          className="fixed inset-0 bg-stone-900/50 z-40 md:hidden" 
          onClick={() => setSidebarOpen(false)}
        />
      )}

      {/* Sidebar Navigation */}
      <aside className={`
        fixed inset-y-0 left-0 z-50 w-64 bg-white border-r border-stone-200 transform transition-transform duration-200 ease-in-out flex flex-col
        ${sidebarOpen ? 'translate-x-0' : '-translate-x-full'} 
        md:relative md:translate-x-0
      `}>
        <div className="h-16 flex items-center justify-between px-6 border-b border-stone-200">
          <Link href="/workspace" className="text-xl font-bold tracking-tighter text-botanical-900 flex items-center gap-2">
            <Leaf className="h-5 w-5 text-botanical-600" />
            AYURLEX
          </Link>
          <button className="md:hidden text-stone-500" onClick={() => setSidebarOpen(false)}>
            <X className="w-5 h-5" />
          </button>
        </div>

        <nav className="flex-1 overflow-y-auto py-4 px-3 space-y-1">
          <NavItem href="/workspace" icon={<LayoutDashboard />} label="Overview" active={pathname === '/workspace'} />
          <NavItem href="/analysis/new" icon={<PlusCircle />} label="New Analysis" active={pathname?.includes('/analysis/new')} />
          <NavItem href="/evidence" icon={<Search />} label="Evidence Explorer" active={pathname?.includes('/evidence')} />
          <NavItem href="/knowledge" icon={<Database />} label="Knowledge Base" active={pathname?.includes('/knowledge')} />
          <NavItem href="/history" icon={<History />} label="Analysis History" active={pathname?.includes('/history')} />
          <NavItem href="/settings" icon={<Settings />} label="Settings" active={pathname?.includes('/settings')} />
        </nav>

        <div className="p-4 border-t border-stone-200 space-y-1">
          <NavItem href="/help" icon={<HelpCircle />} label="Help & Support" active={false} />
          <div className="flex items-center gap-3 px-3 py-3 mt-2 rounded-lg hover:bg-stone-50 cursor-pointer">
             <div className="w-8 h-8 rounded-full bg-botanical-100 flex items-center justify-center text-botanical-800">
                <User className="w-4 h-4" />
             </div>
             <div className="flex-1 overflow-hidden">
                <p className="text-sm font-medium text-stone-900 truncate">Dr. Researcher</p>
                <p className="text-xs text-stone-500 truncate">Pro Account</p>
             </div>
          </div>
        </div>
      </aside>

      {/* Main Content Area */}
      <div className="flex-1 flex flex-col min-w-0 h-screen overflow-hidden">
        {/* Top Bar */}
        <header className="h-16 bg-white border-b border-stone-200 flex items-center justify-between px-4 sm:px-6 z-10 shrink-0">
          <div className="flex items-center gap-4">
            <button 
              className="md:hidden text-stone-600 hover:text-stone-900"
              onClick={() => setSidebarOpen(true)}
            >
              <Menu className="w-6 h-6" />
            </button>
            <h1 className="text-lg font-semibold text-stone-900 hidden sm:block">
              {getPageTitle()}
            </h1>
          </div>

          <div className="flex items-center gap-4">
            {/* Search */}
            <div className="hidden lg:flex relative">
              <Search className="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-stone-400" />
              <input 
                type="text" 
                placeholder="Search analysis..." 
                className="pl-9 pr-4 py-2 border border-stone-200 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 bg-stone-50 w-64"
              />
            </div>

            <div className="flex items-center gap-2 text-stone-600 border-l border-stone-200 pl-4">
              <button className="p-2 hover:bg-stone-100 rounded-full transition-colors relative">
                <Bell className="w-5 h-5" />
                <span className="absolute top-1.5 right-1.5 w-2 h-2 bg-red-500 rounded-full"></span>
              </button>
              
              <div className="relative group cursor-pointer">
                <button className="p-2 hover:bg-stone-100 rounded-full transition-colors flex items-center gap-1">
                  <Globe className="w-5 h-5" />
                  <span className="text-xs font-medium uppercase hidden sm:block">
                    <LanguageSelector />
                  </span>
                </button>
              </div>
            </div>
          </div>
        </header>

        {/* Scrollable Main Content */}
        <main className="flex-1 overflow-y-auto bg-stone-50/50 p-4 sm:p-6 lg:p-8">
          <div className="max-w-7xl mx-auto w-full">
            {children}
          </div>
        </main>
      </div>
    </div>
  );
}

function NavItem({ href, icon, label, active }: { href: string, icon: React.ReactNode, label: string, active: boolean }) {
  return (
    <Link 
      href={href} 
      className={`
        flex items-center gap-3 px-3 py-2.5 rounded-lg text-sm font-medium transition-colors
        ${active 
          ? 'bg-botanical-50 text-botanical-800' 
          : 'text-stone-600 hover:bg-stone-100 hover:text-stone-900'}
      `}
    >
      <span className={active ? "text-botanical-600" : "text-stone-400"}>
        {React.cloneElement(icon as React.ReactElement<any>, { className: "w-5 h-5" })}
      </span>
      {label}
    </Link>
  );
}
