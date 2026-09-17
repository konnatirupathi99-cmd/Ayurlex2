"use client";

import React from "react";
import Link from "next/link";
import { 
  ArrowRight, 
  Search, 
  ShieldCheck, 
  BookOpen, 
  Leaf, 
  Scale, 
  FileText 
} from "lucide-react";
import { motion } from "framer-motion";

export default function LandingPage() {
  return (
    <div className="min-h-screen bg-background">
      {/* Navigation Bar */}
      <nav className="fixed top-0 w-full z-50 bg-background/80 backdrop-blur-md border-b border-stone-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex justify-between items-center h-16">
            {/* Logo */}
            <div className="flex-shrink-0 flex items-center">
              <Link href="/" className="text-2xl font-bold tracking-tighter text-botanical-900 flex items-center gap-2">
                <Leaf className="h-6 w-6 text-botanical-600" />
                AYURLEX
              </Link>
            </div>
            
            {/* Center Navigation */}
            <div className="hidden md:flex space-x-8">
              <Link href="#platform" className="text-sm font-medium text-stone-600 hover:text-botanical-700 transition-colors">
                Platform
              </Link>
              <Link href="#how-it-works" className="text-sm font-medium text-stone-600 hover:text-botanical-700 transition-colors">
                How It Works
              </Link>
              <Link href="#knowledge" className="text-sm font-medium text-stone-600 hover:text-botanical-700 transition-colors">
                Knowledge Intelligence
              </Link>
            </div>

            {/* Right Side Actions */}
            <div className="flex items-center space-x-4">
              <Link href="/login" className="text-sm font-medium text-stone-600 hover:text-botanical-700 transition-colors">
                Sign In
              </Link>
              <Link href="/workspace" className="inline-flex items-center justify-center rounded-md text-sm font-medium transition-colors bg-botanical-900 text-white hover:bg-botanical-800 h-9 px-4 py-2 shadow-sm">
                Start Analysis
              </Link>
            </div>
          </div>
        </div>
      </nav>

      <main className="pt-24 pb-16">
        {/* Hero Section */}
        <section className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-20 pb-24 text-center">
          <motion.div 
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.6 }}
            className="max-w-3xl mx-auto"
          >
            <h1 className="text-5xl md:text-6xl font-extrabold tracking-tight text-stone-900 mb-6 leading-tight">
              AI Intelligence for <br />
              <span className="text-botanical-700">Ayurvedic Innovation</span>
            </h1>
            <p className="text-lg md:text-xl text-stone-600 mb-10 leading-relaxed text-balance">
              Analyse Ayurvedic innovations with structured AI intelligence, evidence-aware research, and clear insights across intellectual property, traditional knowledge, regulatory, and research contexts.
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Link href="/analysis/new" className="inline-flex items-center justify-center rounded-lg text-base font-medium transition-colors bg-botanical-700 text-white hover:bg-botanical-800 h-12 px-8 shadow-md hover:shadow-lg">
                Start New Analysis
                <ArrowRight className="ml-2 h-5 w-5" />
              </Link>
              <Link href="#platform" className="inline-flex items-center justify-center rounded-lg text-base font-medium transition-colors border border-stone-200 bg-white text-stone-900 hover:bg-stone-50 h-12 px-8 shadow-sm">
                Explore Platform
              </Link>
            </div>
          </motion.div>

          {/* Abstract Hero Visual */}
          <motion.div 
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.4, duration: 0.8 }}
            className="mt-20 mx-auto max-w-4xl relative"
          >
            <div className="aspect-[2/1] rounded-2xl border border-stone-200 bg-gradient-to-b from-white to-stone-50 shadow-xl overflow-hidden flex flex-col items-center justify-center p-8 relative">
               <div className="absolute inset-0 bg-[linear-gradient(to_right,#80808012_1px,transparent_1px),linear-gradient(to_bottom,#80808012_1px,transparent_1px)] bg-[size:24px_24px]"></div>
               <div className="z-10 flex flex-col items-center gap-6">
                  <div className="bg-white px-6 py-3 rounded-full border border-botanical-200 shadow-sm text-sm font-medium text-stone-800 flex items-center gap-2">
                    <Leaf className="w-4 h-4 text-botanical-500" /> AYURVEDIC INNOVATION
                  </div>
                  <div className="h-8 w-px bg-botanical-300"></div>
                  <div className="bg-botanical-50 px-8 py-4 rounded-xl border border-botanical-200 shadow-sm text-botanical-900 font-semibold flex items-center gap-2">
                     AI INTELLIGENCE
                  </div>
                  <div className="h-8 w-px bg-botanical-300"></div>
                  <div className="bg-white px-6 py-3 rounded-full border border-stone-200 shadow-sm text-sm font-medium text-stone-800 flex items-center gap-2">
                    <BookOpen className="w-4 h-4 text-stone-500" /> KNOWLEDGE & EVIDENCE
                  </div>
                  <div className="h-8 w-px bg-botanical-300"></div>
                  <div className="bg-white px-6 py-3 rounded-lg border border-botanical-200 shadow-md text-sm font-bold text-botanical-800 flex items-center gap-2">
                    <FileText className="w-4 h-4" /> STRUCTURED INSIGHTS
                  </div>
               </div>
            </div>
          </motion.div>
        </section>

        {/* Core Platform Features */}
        <section id="platform" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 bg-white rounded-3xl border border-stone-100 shadow-sm">
          <div className="text-center mb-16">
            <h2 className="text-3xl font-bold text-stone-900 mb-4">Core Platform Features</h2>
            <p className="text-stone-600 max-w-2xl mx-auto">Comprehensive intelligence modules designed specifically for Ayurvedic research and innovation.</p>
          </div>
          
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <FeatureCard 
              icon={<Search className="h-6 w-6 text-botanical-600" />}
              title="Formulation Intelligence"
              description="Understand formulation and innovation context with AI-driven breakdown of botanical ingredients."
            />
            <FeatureCard 
              icon={<ShieldCheck className="h-6 w-6 text-botanical-600" />}
              title="IP Intelligence"
              description="Explore intellectual property and innovation considerations, identifying potential prior-art."
            />
            <FeatureCard 
              icon={<BookOpen className="h-6 w-6 text-botanical-600" />}
              title="Traditional Knowledge"
              description="Identify potentially relevant classical knowledge references from established texts."
            />
            <FeatureCard 
              icon={<Leaf className="h-6 w-6 text-botanical-600" />}
              title="ABS Context"
              description="Highlight areas where further biological-resource review may be relevant under biodiversity frameworks."
            />
            <FeatureCard 
              icon={<Scale className="h-6 w-6 text-botanical-600" />}
              title="Regulatory Intelligence"
              description="Explore possible product and regulatory context across different jurisdictions."
            />
            <FeatureCard 
              icon={<FileText className="h-6 w-6 text-botanical-600" />}
              title="Evidence-Based Analysis"
              description="Connect insights directly to retrieved sources and evidence, avoiding hallucinated claims."
            />
          </div>
        </section>

        {/* How AYURLEX Works */}
        <section id="how-it-works" className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-24 text-center">
          <h2 className="text-3xl font-bold text-stone-900 mb-16">How AYURLEX Works</h2>
          <div className="flex flex-col md:flex-row justify-center items-center md:items-start gap-4 md:gap-8 max-w-5xl mx-auto">
             <WorkflowStep number="1" title="Describe Innovation" delay={0} />
             <WorkflowArrow />
             <WorkflowStep number="2" title="AI Understands Context" delay={0.1} />
             <WorkflowArrow />
             <WorkflowStep number="3" title="Knowledge Retrieval" delay={0.2} />
             <WorkflowArrow />
             <WorkflowStep number="4" title="Intelligence Analysis" delay={0.3} />
             <WorkflowArrow />
             <WorkflowStep number="5" title="Evidence Review" delay={0.4} />
             <WorkflowArrow />
             <WorkflowStep number="6" title="Structured Report" delay={0.5} isLast />
          </div>
        </section>

        {/* Final CTA */}
        <section className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-20 text-center bg-botanical-900 rounded-3xl shadow-xl text-white relative overflow-hidden">
          <div className="absolute inset-0 opacity-10 bg-[radial-gradient(circle_at_center,_var(--tw-gradient-stops))] from-white via-transparent to-transparent"></div>
          <div className="relative z-10">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Ready to Analyse Your Innovation?</h2>
            <p className="text-botanical-100 text-lg mb-10 max-w-2xl mx-auto">
              Join professionals using AYURLEX to navigate the intersection of traditional Ayurveda and modern regulatory intelligence.
            </p>
            <Link href="/workspace" className="inline-flex items-center justify-center rounded-lg text-lg font-medium transition-colors bg-white text-botanical-900 hover:bg-stone-100 h-14 px-10 shadow-lg">
              Start with AYURLEX
              <ArrowRight className="ml-2 h-5 w-5" />
            </Link>
          </div>
        </section>
      </main>
    </div>
  );
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode, title: string, description: string }) {
  return (
    <div className="group p-8 rounded-2xl bg-stone-50 border border-stone-200 hover:border-botanical-300 hover:shadow-md transition-all duration-300 text-left">
      <div className="w-12 h-12 rounded-xl bg-white border border-stone-200 flex items-center justify-center mb-6 group-hover:bg-botanical-50 group-hover:border-botanical-200 transition-colors">
        {icon}
      </div>
      <h3 className="text-xl font-bold text-stone-900 mb-3">{title}</h3>
      <p className="text-stone-600 leading-relaxed">{description}</p>
    </div>
  );
}

function WorkflowStep({ number, title, delay, isLast = false }: { number: string, title: string, delay: number, isLast?: boolean }) {
  return (
    <motion.div 
      initial={{ opacity: 0, y: 10 }}
      whileInView={{ opacity: 1, y: 0 }}
      viewport={{ once: true }}
      transition={{ delay, duration: 0.5 }}
      className="flex flex-col items-center flex-1"
    >
      <div className={`w-12 h-12 rounded-full flex items-center justify-center font-bold text-lg mb-4 shadow-sm z-10 relative
        ${isLast ? 'bg-botanical-600 text-white border-none' : 'bg-white border border-stone-200 text-botanical-700'}`}>
        {number}
      </div>
      <p className="text-sm font-medium text-stone-800 w-24 leading-tight">{title}</p>
    </motion.div>
  );
}

function WorkflowArrow() {
  return (
    <div className="hidden md:flex items-center pt-6 text-stone-300 flex-1">
      <div className="h-px bg-stone-300 w-full"></div>
      <ArrowRight className="w-4 h-4 -ml-1" />
    </div>
  );
}
