"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  BookOpen,
  Search,
  Plus,
  ShieldCheck,
  Globe,
  FileText,
  ExternalLink,
  AlertTriangle,
  Library,
  BookMarked,
  Microscope,
  Scale,
  MessageCircle,
  Database,
  CheckCircle2,
  Bookmark,
  Leaf
} from "lucide-react";
import styles from "./library.module.css";

export default function KnowledgeLibrary() {
  const [activeLayer, setActiveLayer] = useState("classical");

  return (
    <div className={styles.libraryContainer}>
      {/* Library Header */}
      <header className={styles.header}>
        <div className={styles.headerPattern}></div>
        <div className={styles.headerContent}>
          <div className={styles.headerInfo}>
            <h1 className={styles.headerTitle}>Keep the evidence close to the decision.</h1>
            <p className={styles.headerSubtitle}>
              Your source-aware research archive. Reports, source trails, terminology decisions, and working notes remain visible and traceable.
            </p>
          </div>
          <Link href="/guide" className={styles.primaryAction} style={{textDecoration: 'none', color: 'inherit'}}>
            <Plus size={18} /> New research brief
          </Link>
        </div>
      </header>

      {/* Global Search and Filters */}
      <div className={styles.searchBar}>
        <div className={styles.searchInputWrapper}>
          <Search className={styles.searchIcon} size={20} />
          <input 
            type="text" 
            className={styles.searchInput} 
            placeholder="Search classical texts, journals, materia medica, and reports..." 
          />
          <div className={styles.searchFilters}>
            <button className={styles.filterBadge}>Classical</button>
            <button className={styles.filterBadge}>Journal</button>
            <button className={styles.filterBadge}>Materia Medica</button>
            <button className={styles.filterBadge}>Regulatory</button>
            <button className={styles.filterBadge}>IP</button>
          </div>
        </div>
      </div>

      {/* Source-Aware Banner */}
      <div className={styles.sourceAwareBanner}>
        <div className={styles.bannerContent}>
          <div className={styles.bannerText}>
            <strong>Traceable Evidence Trail</strong><br />
            Every innovation brief you create here leaves a traceable trail back to the primary source material, ensuring verifiable claims.
          </div>
          <div className={styles.bannerMetrics}>
            <div className={styles.bannerMetric}>
              <div className={styles.bannerMetricValue}>42,000+</div>
              <div className={styles.bannerMetricLabel}>Indexed Sources</div>
            </div>
            <div className={styles.bannerMetric}>
              <div className={styles.bannerMetricValue}><Database size={16} /> Active</div>
              <div className={styles.bannerMetricLabel}>Europe PMC Sync</div>
            </div>
            <div className={styles.bannerMetric}>
              <div className={styles.bannerMetricValue}><Globe size={16} /> 16</div>
              <div className={styles.bannerMetricLabel}>Supported Languages</div>
            </div>
          </div>
        </div>
      </div>

      <main className={styles.mainContent}>
        {/* Sidebar: Knowledge Layers */}
        <aside className={styles.sidebar}>
          <div className={styles.layerNav}>
            <div className={styles.layerTitle}>Knowledge Layers</div>
            
            <div 
              className={`${styles.layerItem} ${activeLayer === 'classical' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('classical')}
            >
              <span className="flex items-center gap-2"><BookMarked size={16} /> Classical Sources</span>
              <span className={styles.layerCount}>3</span>
            </div>
            
            <div 
              className={`${styles.layerItem} ${activeLayer === 'journal' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('journal')}
            >
              <span className="flex items-center gap-2"><Microscope size={16} /> Journal Index</span>
              <span className={styles.layerCount}>Live</span>
            </div>

            <div 
              className={`${styles.layerItem} ${activeLayer === 'materia' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('materia')}
            >
              <span className="flex items-center gap-2"><Leaf size={16} /> Materia Medica</span>
            </div>

            <div 
              className={`${styles.layerItem} ${activeLayer === 'terminology' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('terminology')}
            >
              <span className="flex items-center gap-2"><MessageCircle size={16} /> Terminology Map</span>
            </div>

            <div 
              className={`${styles.layerItem} ${activeLayer === 'market' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('market')}
            >
              <span className="flex items-center gap-2"><Scale size={16} /> Market Context</span>
            </div>

            <div 
              className={`${styles.layerItem} ${activeLayer === 'reports' ? styles.layerItemActive : ''}`}
              onClick={() => setActiveLayer('reports')}
            >
              <span className="flex items-center gap-2"><FileText size={16} /> Innovation Reports</span>
              <span className={styles.layerCount}>12</span>
            </div>
          </div>

          <div className={styles.disclaimerBox} style={{marginTop: 'auto'}}>
            <AlertTriangle className={styles.disclaimerIcon} size={18} />
            <div>
              <strong>Responsible Source Note</strong><br />
              Indexed sources provided here act as evidence leads. They must be reviewed in full context before use in clinical, commercial, regulatory, or product decisions.
            </div>
          </div>
        </aside>

        {/* Dynamic Content Area based on Active Layer */}
        <div className={styles.contentArea}>
          
          {activeLayer === 'classical' && (
            <>
              <div className={styles.sectionHeader}>
                <h2 className={styles.sectionTitle}><BookMarked size={20} /> Classical Source Library</h2>
              </div>
              <p style={{color: 'var(--color-text-light)', fontSize: '0.875rem', marginBottom: '1rem'}}>
                Ensure that chapter, edition, Sanskrit passage, and translations are thoroughly verified against authoritative physical texts or verified portals.
              </p>
              
              <div className={styles.grid2Col}>
                
                {/* Caraka Samhita */}
                <div className={styles.sourceCard}>
                  <div className={styles.sourceHeader}>
                    <span className={`${styles.sourceType} ${styles.typeClassical}`}>Classical Text</span>
                    <button style={{background: 'none', border: 'none', color: 'var(--color-sage)', cursor: 'pointer'}}>
                      <Bookmark size={18} />
                    </button>
                  </div>
                  <h3 className={styles.sourceTitle}>Caraka Saṁhitā</h3>
                  <div className={styles.sourceMeta}>
                    <span>Sūtrasthāna, Vimānasthāna, Śārīrasthāna, Indriyasthāna, Cikitsāsthāna, Kalpasthāna, Siddhisthāna</span>
                  </div>
                  <div className={styles.sourceExcerpt}>
                    The foundational text of Ayurveda emphasizing internal medicine (Kāyacikitsā), rationale of treatments, and philosophical foundations.
                  </div>
                  <div className={styles.sourceActions}>
                    <div className={styles.verificationBadge}>
                      <CheckCircle2 size={12} /> Multiple editions indexed
                    </div>
                    <Link href="#" className={styles.sourceLink}>
                      Authoritative Portal <ExternalLink size={14} />
                    </Link>
                  </div>
                </div>

                {/* Susruta Samhita */}
                <div className={styles.sourceCard}>
                  <div className={styles.sourceHeader}>
                    <span className={`${styles.sourceType} ${styles.typeClassical}`}>Classical Text</span>
                    <button style={{background: 'none', border: 'none', color: 'var(--color-sage)', cursor: 'pointer'}}>
                      <Bookmark size={18} />
                    </button>
                  </div>
                  <h3 className={styles.sourceTitle}>Suśruta Saṁhitā</h3>
                  <div className={styles.sourceMeta}>
                    <span>Sūtrasthāna, Nidānasthāna, Śārīrasthāna, Cikitsāsthāna, Kalpasthāna, Uttaratantra</span>
                  </div>
                  <div className={styles.sourceExcerpt}>
                    The foundational text emphasizing surgery (Śalya Tantra), detailed anatomical descriptions, and the classification of medicinal herbs.
                  </div>
                  <div className={styles.sourceActions}>
                    <div className={styles.verificationBadge}>
                      <CheckCircle2 size={12} /> Standard editions indexed
                    </div>
                    <Link href="#" className={styles.sourceLink}>
                      Authoritative Portal <ExternalLink size={14} />
                    </Link>
                  </div>
                </div>

                {/* Astanga Hridaya */}
                <div className={styles.sourceCard}>
                  <div className={styles.sourceHeader}>
                    <span className={`${styles.sourceType} ${styles.typeClassical}`}>Classical Text</span>
                    <button style={{background: 'none', border: 'none', color: 'var(--color-sage)', cursor: 'pointer'}}>
                      <Bookmark size={18} />
                    </button>
                  </div>
                  <h3 className={styles.sourceTitle}>Aṣṭāṅga Hṛdaya</h3>
                  <div className={styles.sourceMeta}>
                    <span>Author: Vāgbhaṭa</span>
                  </div>
                  <div className={styles.sourceExcerpt}>
                    A poetic synthesis of both Caraka and Suśruta Saṁhitā, providing a highly organized and accessible summary of the eight branches of Ayurveda.
                  </div>
                  <div className={styles.sourceActions}>
                    <div className={styles.verificationBadge}>
                      <CheckCircle2 size={12} /> Fully indexed
                    </div>
                    <Link href="#" className={styles.sourceLink}>
                      Authoritative Portal <ExternalLink size={14} />
                    </Link>
                  </div>
                </div>

              </div>
            </>
          )}

          {activeLayer === 'journal' && (
            <>
              <div className={styles.sectionHeader}>
                <h2 className={styles.sectionTitle}><Microscope size={20} /> Contemporary Journal Index</h2>
              </div>
              
              {/* Complex filter bar for Journals */}
              <div style={{display: 'flex', gap: '0.75rem', flexWrap: 'wrap', marginBottom: '2rem'}}>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Ingredient</option></select>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Condition / Area</option></select>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Formulation</option></select>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Evidence Type</option><option>RCT</option><option>In-vitro</option></select>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Publication Year</option></select>
                <select className={styles.filterBadge} style={{outline: 'none'}}><option>Author</option></select>
              </div>

              <div className={styles.grid2Col}>
                <div className={styles.sourceCard}>
                  <div className={styles.sourceHeader}>
                    <span className={`${styles.sourceType} ${styles.typeJournal}`}>Journal Article</span>
                    <button style={{background: 'none', border: 'none', color: 'var(--color-sage)', cursor: 'pointer'}}>
                      <Bookmark size={18} />
                    </button>
                  </div>
                  <h3 className={styles.sourceTitle}>Bioavailability of Curcumin: Problems and Promises</h3>
                  <div className={styles.sourceMeta}>
                    <span>Anand P, Kunnumakkara AB, Newman RA, Aggarwal BB</span>
                    <span>Mol Pharm. 2007 Nov-Dec;4(6):807-18. | DOI: 10.1021/mp700113r</span>
                  </div>
                  <div className={styles.sourceExcerpt}>
                    "Curcumin has been shown to exhibit antioxidant, anti-inflammatory, antiviral, antibacterial, antifungal, and anticancer activities... Piperine enhances the serum concentration, extent of absorption and bioavailability of curcumin in both rats and humans."
                  </div>
                  <div className={styles.sourceActions}>
                    <div className={styles.verificationBadge}>
                      <ShieldCheck size={12} /> Europe PMC Verified
                    </div>
                    <Link href="#" className={styles.sourceLink}>
                      Europe PMC Record <ExternalLink size={14} />
                    </Link>
                  </div>
                </div>
              </div>
            </>
          )}

          {activeLayer === 'reports' && (
            <>
              <div className={styles.sectionHeader}>
                <h2 className={styles.sectionTitle}><FileText size={20} /> Innovation Report Library</h2>
              </div>
              
              <div style={{display: 'flex', flexDirection: 'column'}}>
                
                <div className={styles.reportCard}>
                  <div className={styles.reportInfo}>
                    <div className={styles.reportTitle}>Ashwagandha Cognitive Formulation Review</div>
                    <div className={styles.reportMeta}>
                      <span className={styles.reportMetaTag}>Ashwagandha</span>
                      <span className={styles.reportMetaTag}>US / EU</span>
                      <span>Completed</span>
                      <span>Oct 12, 2026</span>
                    </div>
                  </div>
                  <div style={{display: 'flex', gap: '1.5rem', alignItems: 'center'}}>
                    <div className={styles.reportScore}>
                      <CheckCircle2 size={16} /> 94% Grounding
                    </div>
                    <Link href="/workspace" className={styles.primaryAction} style={{padding: '0.5rem 1rem', fontSize: '0.875rem', textDecoration: 'none', color: 'inherit'}}>
                      Open Report
                    </Link>
                  </div>
                </div>

                <div className={styles.reportCard}>
                  <div className={styles.reportInfo}>
                    <div className={styles.reportTitle}>Triphala Delivery Mechanism Patents</div>
                    <div className={styles.reportMeta}>
                      <span className={styles.reportMetaTag}>Triphala</span>
                      <span className={styles.reportMetaTag}>India</span>
                      <span>Active Review</span>
                      <span>Oct 10, 2026</span>
                    </div>
                  </div>
                  <div style={{display: 'flex', gap: '1.5rem', alignItems: 'center'}}>
                    <div className={styles.reportScore} style={{color: 'var(--color-indigo)'}}>
                      <CheckCircle2 size={16} /> 81% Grounding
                    </div>
                    <Link href="/workspace" className={styles.primaryAction} style={{padding: '0.5rem 1rem', fontSize: '0.875rem', textDecoration: 'none', color: 'inherit'}}>
                      Open Report
                    </Link>
                  </div>
                </div>

              </div>
            </>
          )}
          
          {/* Fallback for other layers */}
          {['materia', 'terminology', 'market'].includes(activeLayer) && (
            <div style={{
              textAlign: 'center', 
              padding: '4rem', 
              backgroundColor: 'white', 
              border: '1px dashed var(--color-border)', 
              borderRadius: '1rem',
              color: 'var(--color-text-light)'
            }}>
              <Library size={48} style={{margin: '0 auto 1rem', color: 'var(--color-sage)'}} />
              <h3 style={{fontSize: '1.25rem', color: 'var(--color-text)', marginBottom: '0.5rem'}}>Select a source to begin mapping</h3>
              <p>The {activeLayer} layer connects directly to verified databases.</p>
            </div>
          )}

        </div>
      </main>
    </div>
  );
}
