"use client";

import React from "react";
import Link from "next/link";
import { 
  Leaf, 
  Search, 
  Globe, 
  Bell, 
  User, 
  Download,
  CheckCircle2,
  TrendingUp,
  TrendingDown,
  ArrowRight,
  BookOpen,
  Scale,
  ShieldCheck,
  AlertTriangle,
  Beaker,
  FileText
} from "lucide-react";
import styles from "./page.module.css";

export default function OverviewDashboard() {
  return (
    <div className={styles.dashboard}>
      {/* Navigation */}
      <nav className={styles.nav}>
        <Link href="/" className={styles.logo}>
          <Leaf size={24} />
          AYURLEX
        </Link>
        <div className={styles.navActions}>
          <button className={styles.navButton}>
            <Globe size={18} />
            <span>EN</span>
          </button>
          <button className={styles.navButton}>
            <Search size={18} />
            <span>Search (⌘K)</span>
          </button>
          <button className={styles.navButton}>
            <Bell size={18} />
          </button>
          <button className={styles.navButton}>
            <User size={18} />
          </button>
          <button className={styles.exportButton}>
            <Download size={16} /> Export
          </button>
        </div>
      </nav>

      {/* Hero Section */}
      <section className={styles.hero}>
        <div className={styles.heroPattern}></div>
        <div className={styles.heroContent}>
          <div className={styles.heroEditorial}>Make the next wise move.</div>
          <h1 className={styles.heroTitle}>Ayurveda Innovation Intelligence</h1>
          <p className={styles.heroDescription}>
            Transform Ayurvedic knowledge into responsible and differentiated innovations. AYURLEX provides an evidence-aware workspace tailored for researchers, founders, and practitioners.
          </p>
          
          <div className={styles.badges}>
            <div className={styles.badge}><CheckCircle2 size={16} /> Ayurveda-only answers</div>
            <div className={styles.badge}><Globe size={16} /> 16 language lenses</div>
            <div className={styles.badge}><Scale size={16} /> Jurisdiction pathways</div>
            <div className={styles.badge}><BookOpen size={16} /> Live citation layer</div>
          </div>
        </div>
      </section>

      {/* Command Bar */}
      <div className={styles.commandBar}>
        <Search className={styles.commandIcon} size={20} />
        <input 
          type="text" 
          className={styles.commandInput} 
          placeholder="Ask about an ingredient, formulation, traditional knowledge or innovation pathway..." 
        />
        <button className={styles.scopeBadge}>
          <Leaf size={14} /> Ayurveda-only scope
        </button>
      </div>

      <main className={styles.mainContent}>
        {/* Workspace Signal */}
        <section className={styles.workspaceSignal}>
          <div className={styles.signalScore}>
            <div className={styles.scoreValue}>84</div>
            <div className={styles.scoreLabel}>Readiness Score</div>
          </div>
          <div className={styles.signalContent}>
            <div className={styles.signalHeader}>
              <TrendingUp size={16} /> Innovation Signal
            </div>
            <div className={styles.signalInsight}>
              Your <strong>Turmeric</strong> innovation has a strong India fit. The open question is EU claim substantiation.
            </div>
            <button className={styles.signalAction}>
              Compare Jurisdictions
            </button>
          </div>
        </section>

        {/* Workspace Metrics */}
        <h2 className={styles.sectionTitle}>Workspace Intelligence</h2>
        <div className={`${styles.grid} ${styles.metricsGrid}`}>
          <div className={styles.metricCard}>
            <div className={styles.metricHeader}>
              <span>Grounded Answers</span>
              <BookOpen size={16} />
            </div>
            <div className={styles.metricValue}>1,248</div>
            <div className={styles.metricTrend}>
              <TrendingUp size={14} /> +12% this week
            </div>
            <div style={{fontSize: '0.75rem', color: 'var(--color-text-light)', marginTop: '0.5rem'}}>Evidence-backed references cited.</div>
          </div>
          <div className={styles.metricCard}>
            <div className={styles.metricHeader}>
              <span>Jurisdiction Lenses</span>
              <Globe size={16} />
            </div>
            <div className={styles.metricValue}>4</div>
            <div className={styles.metricTrend} style={{color: 'var(--color-botanical-green)'}}>
              Active monitoring
            </div>
            <div style={{fontSize: '0.75rem', color: 'var(--color-text-light)', marginTop: '0.5rem'}}>IN, EU, US, UK pathways active.</div>
          </div>
          <div className={styles.metricCard}>
            <div className={styles.metricHeader}>
              <span>Open Evidence Gaps</span>
              <AlertTriangle size={16} />
            </div>
            <div className={styles.metricValue}>3</div>
            <div className={styles.metricTrend} style={{color: 'var(--color-terracotta)'}}>
              <TrendingDown size={14} /> Requires attention
            </div>
            <div style={{fontSize: '0.75rem', color: 'var(--color-text-light)', marginTop: '0.5rem'}}>Clinical substantiation pending.</div>
          </div>
          <div className={styles.metricCard}>
            <div className={styles.metricHeader}>
              <span>Innovation Briefs</span>
              <FileText size={16} />
            </div>
            <div className={styles.metricValue}>12</div>
            <div className={styles.metricTrend}>
              <TrendingUp size={14} /> +2 recent briefs
            </div>
            <div style={{fontSize: '0.75rem', color: 'var(--color-text-light)', marginTop: '0.5rem'}}>Generated innovation reports.</div>
          </div>
        </div>

        {/* Innovation Workbench */}
        <h2 className={styles.sectionTitle}>Innovation Workbench</h2>
        <div className={`${styles.grid} ${styles.workbenchGrid}`}>
          <div className={styles.moduleCard}>
            <div className={styles.moduleHeader}>
              <div className={styles.moduleIcon}><Beaker size={24} /></div>
              <span className={styles.moduleCategory}>Analysis</span>
            </div>
            <h3 className={styles.moduleTitle}>Formulation Intelligence</h3>
            <p className={styles.moduleDescription}>
              Deconstruct complex Ayurvedic formulations, map ingredient synergies, and validate against classical references.
            </p>
            <div className={styles.moduleFooter}><ArrowRight size={20} /></div>
          </div>

          <div className={styles.moduleCard}>
            <div className={styles.moduleHeader}>
              <div className={styles.moduleIcon}><BookOpen size={24} /></div>
              <span className={styles.moduleCategory}>Knowledge</span>
            </div>
            <h3 className={styles.moduleTitle}>Traditional Knowledge</h3>
            <p className={styles.moduleDescription}>
              Trace origins across classical texts, explore TKDL alignments, and understand historical usage contexts.
            </p>
            <div className={styles.moduleFooter}><ArrowRight size={20} /></div>
          </div>

          <div className={styles.moduleCard}>
            <div className={styles.moduleHeader}>
              <div className={styles.moduleIcon}><Scale size={24} /></div>
              <span className={styles.moduleCategory}>Regulatory</span>
            </div>
            <h3 className={styles.moduleTitle}>Regulatory Pathways</h3>
            <p className={styles.moduleDescription}>
              Navigate global compliance, compare jurisdiction requirements, and assess claim viability across markets.
            </p>
            <div className={styles.moduleFooter}><ArrowRight size={20} /></div>
          </div>

          <div className={styles.moduleCard}>
            <div className={styles.moduleHeader}>
              <div className={styles.moduleIcon}><ShieldCheck size={24} /></div>
              <span className={styles.moduleCategory}>Protection</span>
            </div>
            <h3 className={styles.moduleTitle}>IP & Prior Art</h3>
            <p className={styles.moduleDescription}>
              Analyze patent landscapes, uncover prior art boundaries, and identify white-space for true innovation.
            </p>
            <div className={styles.moduleFooter}><ArrowRight size={20} /></div>
          </div>
        </div>

        {/* Recent Briefs */}
        <h2 className={styles.sectionTitle}>Recent Briefs</h2>
        <div className={styles.recentBriefs}>
          <ul className={styles.briefList}>
            <li className={styles.briefItem}>
              <div className={styles.briefInfo}>
                <span className={styles.briefTitle}>Ashwagandha Cognitive Formulation Review</span>
                <div className={styles.briefMeta}>
                  <span>Ingredient: Ashwagandha</span>
                  <span>Market: US / EU</span>
                  <span>Today, 10:42 AM</span>
                </div>
              </div>
              <div className={styles.briefScore}>
                <CheckCircle2 size={14} /> High Grounding (94%)
              </div>
            </li>
            <li className={styles.briefItem}>
              <div className={styles.briefInfo}>
                <span className={styles.briefTitle}>Triphala Delivery Mechanism Patents</span>
                <div className={styles.briefMeta}>
                  <span>Ingredient: Triphala</span>
                  <span>Market: India</span>
                  <span>Yesterday, 02:15 PM</span>
                </div>
              </div>
              <div className={styles.briefScore}>
                <CheckCircle2 size={14} /> Moderate Grounding (81%)
              </div>
            </li>
          </ul>
        </div>

        {/* Responsible Use Panel */}
        <div className={styles.responsibleUse}>
          <AlertTriangle className={styles.warningIcon} size={20} />
          <div>
            <strong>Responsible Innovation Companion</strong><br/>
            AYURLEX is designed as a research and innovation intelligence tool. It does not provide medical diagnosis, emergency advice, unsupported clinical claims, or definitive legal and regulatory conclusions. Always consult certified practitioners, qualified legal counsel, and appropriate regulatory bodies for definitive guidance. AYURLEX distinctly separates classical Ayurvedic references from modern scientific evidence and regulatory interpretations.
          </div>
        </div>

      </main>
    </div>
  );
}
