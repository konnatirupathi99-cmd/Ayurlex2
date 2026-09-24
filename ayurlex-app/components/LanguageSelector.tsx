"use client";

import React, { useState, useRef, useEffect } from "react";
import { Globe, Check, Search, ChevronDown } from "lucide-react";
import { useLanguage, LANGUAGE_NAMES } from "./LanguageProvider";

export function LanguageSelector() {
  const { language, setLanguage } = useLanguage();
  const [isOpen, setIsOpen] = useState(false);
  const [searchQuery, setSearchQuery] = useState("");
  const dropdownRef = useRef<HTMLDivElement>(null);

  // Close dropdown on click outside
  useEffect(() => {
    function handleClickOutside(event: MouseEvent) {
      if (dropdownRef.current && !dropdownRef.current.contains(event.target as Node)) {
        setIsOpen(false);
      }
    }
    document.addEventListener("mousedown", handleClickOutside);
    return () => document.removeEventListener("mousedown", handleClickOutside);
  }, []);

  const filteredLanguages = Object.entries(LANGUAGE_NAMES).filter(([_, name]) =>
    name.toLowerCase().includes(searchQuery.toLowerCase())
  );

  return (
    <div className="relative" ref={dropdownRef}>
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-3 py-2 rounded-lg hover:bg-stone-100 transition-colors text-stone-700"
        aria-label="Select Language"
      >
        <Globe className="w-5 h-5 text-botanical-600" />
        <span className="hidden sm:inline-flex font-medium text-sm gap-1 items-center">
          {LANGUAGE_NAMES[language]}
          <ChevronDown className="w-4 h-4 text-stone-400" />
        </span>
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-64 bg-white rounded-xl shadow-lg border border-stone-200 z-50 overflow-hidden flex flex-col max-h-[70vh]">
          <div className="p-3 border-b border-stone-100 bg-stone-50">
            <h3 className="text-xs font-semibold text-stone-500 uppercase tracking-wider mb-2 flex items-center gap-1.5">
              <Globe className="w-3.5 h-3.5" />
              Select Language
            </h3>
            <div className="relative">
              <Search className="absolute left-2.5 top-1/2 -translate-y-1/2 w-4 h-4 text-stone-400" />
              <input
                type="text"
                placeholder="Search languages..."
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                className="w-full pl-8 pr-3 py-1.5 bg-white border border-stone-200 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500"
              />
            </div>
          </div>

          <div className="overflow-y-auto flex-1 p-1">
            {filteredLanguages.length > 0 ? (
              filteredLanguages.map(([code, name]) => (
                <button
                  key={code}
                  onClick={() => {
                    setLanguage(code as any);
                    setIsOpen(false);
                    setSearchQuery("");
                  }}
                  className={`w-full flex items-center justify-between px-3 py-2.5 rounded-md text-sm transition-colors ${
                    language === code
                      ? "bg-botanical-50 text-botanical-800 font-medium"
                      : "text-stone-700 hover:bg-stone-50 hover:text-stone-900"
                  }`}
                >
                  <span className="text-left">{name}</span>
                  {language === code && <Check className="w-4 h-4 text-botanical-600" />}
                </button>
              ))
            ) : (
              <div className="px-3 py-4 text-center text-sm text-stone-500">
                No languages found
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
