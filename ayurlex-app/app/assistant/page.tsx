"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  Leaf, 
  Send, 
  Globe, 
  CheckCircle2, 
  BookOpen, 
  ShieldAlert, 
  Scale, 
  ExternalLink,
  AlertTriangle,
  Info,
  Beaker
} from "lucide-react";
import styles from "./assistant.module.css";

export default function AskAyurlexAssistant() {
  const [inputText, setInputText] = useState("");

  const handleKeyDown = (e: React.KeyboardEvent<HTMLTextAreaElement>) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      // Handle send
    }
  };

  return (
    <div className={styles.assistantContainer}>
      {/* Main Conversation Workspace */}
      <div className={styles.mainWorkspace}>
        {/* Assistant Header */}
        <header className={styles.header}>
          <div className={styles.headerInfo}>
            <h1 className={styles.headerTitle}>Ask better questions. Build wiser innovations.</h1>
            <p className={styles.headerSubtitle}>
              AYURLEX supports Ayurveda research, formulation analysis, traditional knowledge tracing, 
              evidence verification, intellectual property, and jurisdictional pathways.
            </p>
          </div>
          <div className={styles.statusBadge}>
            <div className={styles.statusIndicator}></div>
            Citation layer online
          </div>
        </header>

        {/* Chat Toolbar */}
        <div className={styles.chatToolbar}>
          <div className={styles.toolbarLeft}>
            <div className={styles.toolbarItem}>
              <Leaf size={14} className="text-botanical-600" />
              <strong>AYURLEX Assistant</strong>
            </div>
            <div className={styles.toolbarItem}>
              <Globe size={14} />
              <select className={styles.contextValueSelect} style={{ background: 'transparent', border: 'none', padding: 0 }}>
                <option>English</option>
                <option>Hindi</option>
                <option>Sanskrit</option>
                <option>Marathi</option>
                <option>Tamil</option>
                <option>Telugu</option>
                <option>Kannada</option>
                <option>Malayalam</option>
                <option>Bengali</option>
                <option>Gujarati</option>
                <option>Punjabi</option>
                <option>Odia</option>
                <option>Urdu</option>
                <option>Nepali</option>
                <option>Sinhala</option>
                <option>French</option>
              </select>
            </div>
            <div className={styles.toolbarItem}>
              <ShieldAlert size={14} />
              <span>Evidence-grounded · Ayurveda only</span>
            </div>
          </div>
          <div className={styles.toolbarItem}>
            <CheckCircle2 size={14} className="text-botanical-600" />
            Live citation indicator
          </div>
        </div>

        {/* Conversation Area */}
        <div className={styles.conversationArea}>
          
          {/* User Message */}
          <div className={`${styles.message} ${styles.messageUser}`}>
            <div className={`${styles.avatar} ${styles.avatarUser}`}>
              <User size={18} />
            </div>
            <div className={styles.messageContent}>
              Can you help me diagnose my chronic joint pain using Ashwagandha?
            </div>
          </div>

          {/* Assistant Guardrail Message */}
          <div className={styles.message}>
            <div className={`${styles.avatar} ${styles.avatarAssistant}`}>
              <Leaf size={18} />
            </div>
            <div className={`${styles.messageContent} ${styles.messageGuardrail}`}>
              <AlertTriangle className={styles.guardrailIcon} size={18} />
              I’m designed only for Ayurveda-related questions. I can help connect this topic to an Ayurvedic formulation, traditional knowledge, evidence, innovation, intellectual property, or a market pathway.
              <br/><br/>
              <em>AYURLEX does not provide medical diagnosis or emergency medical advice. Please consult a qualified practitioner for clinical guidance.</em>
            </div>
          </div>

          {/* User Message 2 */}
          <div className={`${styles.message} ${styles.messageUser}`}>
            <div className={`${styles.avatar} ${styles.avatarUser}`}>
              <User size={18} />
            </div>
            <div className={styles.messageContent}>
              How can I differentiate a turmeric innovation without overclaiming in the EU market?
            </div>
          </div>

          {/* Assistant Response Message */}
          <div className={styles.message}>
            <div className={`${styles.avatar} ${styles.avatarAssistant}`}>
              <Leaf size={18} />
            </div>
            <div className={styles.messageContent}>
              <p>Differentiating a Turmeric (<em>Curcuma longa</em>) formulation in the EU market requires a careful balance between leveraging traditional knowledge and adhering to EFSA (European Food Safety Authority) health claim regulations.</p>
              <br/>
              <p><strong>1. Traditional Knowledge (TK) Positioning</strong><br/>
              In the EU, Traditional Herbal Registration (THR) allows for specific claims based on long-standing use (minimum 30 years, including 15 years within the EU). Classical texts like the <em>Suśruta Saṁhitā</em> document its use as a <em>viṣaghna</em> (anti-toxic) and <em>kusthaghna</em> (skin-alleviating) agent [1].</p>
              <br/>
              <p><strong>2. Evidence-Backed Botanical Synergies</strong><br/>
              To differentiate without unauthorized claims, focus on bioavailability enhancements (e.g., Piperine/Black Pepper) supported by modern pharmacokinetic studies [2]. You can claim "contains Turmeric, traditionally used..." rather than making direct disease-treatment claims which are strictly prohibited for food supplements.</p>
              
              <div className={styles.messageMetadata}>
                <span className="flex items-center gap-1"><BookOpen size={12}/> Guidance Lens: Regulatory Pathway</span>
                <span className="flex items-center gap-1"><Globe size={12}/> Jurisdiction: European Union (EFSA)</span>
                <span className="flex items-center gap-1"><Info size={12}/> Language: English</span>
              </div>
            </div>
          </div>

        </div>

        {/* Composer Area */}
        <div className={styles.composerContainer}>
          <div className={styles.suggestions}>
            <button className={styles.suggestionChip}>
              "How can I differentiate a turmeric innovation without overclaiming?"
            </button>
            <button className={styles.suggestionChip}>
              "Map an Ayurvedic formulation for India and the EU."
            </button>
            <button className={styles.suggestionChip}>
              "What should I document before working with community knowledge?"
            </button>
          </div>

          <div className={styles.composerInputWrapper}>
            <div className={styles.scopeLabel}>
              <Leaf size={12} /> Ayurveda-only scope
            </div>
            <textarea 
              className={styles.composerInput}
              placeholder="Ask about an ingredient, formulation, traditional knowledge or innovation pathway..."
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={2}
            />
            <div className={styles.composerActions}>
              <button className={styles.sendButton}>
                <Send size={16} />
              </button>
              <span className={styles.composerHint}>Shift + Enter for new line</span>
            </div>
          </div>
        </div>
      </div>

      {/* Context and Evidence Sidebar */}
      <div className={styles.sidebar}>
        
        {/* Context Lens */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <Scale size={16} /> Context Lens
          </div>
          <div className={styles.contextList}>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>Primary Jurisdiction</span>
              <select className={styles.contextValueSelect}>
                <option>European Union (EFSA)</option>
                <option>India (Ayush)</option>
                <option>US (FDA / DSHEA)</option>
                <option>UK (MHRA)</option>
              </select>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>Pathway Readiness</span>
              <span className={styles.contextValue}>
                <span className={styles.statusIndicator} style={{backgroundColor: 'var(--color-amber)'}}></span> Moderate (65/100)
              </span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>Category Reminder</span>
              <span className={styles.contextValue}>Food Supplement / Botanicals</span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>Claim Sensitivity</span>
              <span className={styles.contextValue} style={{color: 'var(--color-terracotta)'}}>High (Restricted)</span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>Evidence Expected</span>
              <span className={styles.contextValue}>History of Safe Use, Pharmacokinetics</span>
            </div>
          </div>
        </div>

        {/* Answer Quality Panel */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <CheckCircle2 size={16} /> Answer Quality
          </div>
          <div className={styles.qualityPanel}>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>Source Coverage</span>
              <span className={styles.contextValue}>Comprehensive</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>Classical References</span>
              <span className={styles.contextValue}>Verified (Suśruta)</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>Journal Index</span>
              <span className={styles.contextValue}>Europe PMC Synced</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>Open Questions</span>
              <span className={styles.contextValue}>Pending formulation details</span>
            </div>
          </div>
        </div>

        {/* Live Citation Panel */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <BookOpen size={16} /> Live Citations
          </div>
          
          <div className={styles.citationCard}>
            <div className={styles.citationHeader}>
              <span className={`${styles.citationType} ${styles.citationTypeClassical}`}>Classical Text</span>
              <CheckCircle2 size={14} className={styles.verifiedBadge} />
            </div>
            <div className={styles.citationTitle}>Suśruta Saṁhitā, Sūtrasthāna</div>
            <div className={styles.citationMeta}>Author: Suśruta | Chapter 38 (Dravyasaṅgrahaṇīya)</div>
            <div className={styles.citationExcerpt}>
              "Haridrā (Turmeric) is indicated in the Haridrādi Gaṇa for alleviating skin conditions (Kuṣṭha) and acting as an anti-toxic (Viṣaghna)."
            </div>
            <Link href="#" className={styles.citationLink}>
              <ExternalLink size={12} /> View original Sanskrit & Translation
            </Link>
          </div>

          <div className={styles.citationCard}>
            <div className={styles.citationHeader}>
              <span className={styles.citationType}>Journal</span>
              <CheckCircle2 size={14} className={styles.verifiedBadge} />
            </div>
            <div className={styles.citationTitle}>Bioavailability of Curcumin: Problems and Promises</div>
            <div className={styles.citationMeta}>Anand P, et al. | Year: 2007 | Source: Europe PMC</div>
            <div className={styles.citationExcerpt}>
              "Piperine enhances the serum concentration, extent of absorption and bioavailability of curcumin in both rats and humans with no adverse effects."
            </div>
            <Link href="#" className={styles.citationLink}>
              <ExternalLink size={12} /> Verify Source details via Europe PMC
            </Link>
          </div>

          <div style={{fontSize: '0.625rem', color: 'var(--color-text-light)', marginTop: '0.5rem', fontStyle: 'italic'}}>
            Note: Always verify chapter, translation, edition, and current publication details before including in formal submissions.
          </div>
        </div>

        {/* Responsible Use Note */}
        <div className={styles.sidebarSection} style={{borderBottom: 'none'}}>
          <div className={styles.responsibleUse}>
            <Info className="flex-shrink-0" size={16} style={{color: 'var(--color-botanical-green)'}} />
            <div>
              AYURLEX structures research and maps evidence, but does not replace certified practitioners, regulators, scientific reviewers, or qualified legal counsel.
            </div>
          </div>
        </div>

      </div>
    </div>
  );
}

function User({ size }: { size: number }) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
      <path d="M19 21v-2a4 4 0 0 0-4-4H9a4 4 0 0 0-4 4v2" />
      <circle cx="12" cy="7" r="4" />
    </svg>
  );
}
