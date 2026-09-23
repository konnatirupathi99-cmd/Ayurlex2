"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  FolderKanban, 
  MessageSquare, 
  FileBarChart, 
  Plus, 
  Lock, 
  Globe, 
  Clock, 
  Leaf, 
  Scale, 
  ArrowRight,
  Filter,
  Search,
  ExternalLink
} from "lucide-react";
import styles from "./workspace.module.css";

// Mock Data
const MOCK_PROJECTS = [
  {
    id: 1,
    name: "Ashwagandha Cognitive Formulation",
    focus: "Formulation Analysis",
    jurisdiction: "United States (DSHEA)",
    status: "Active",
    lastUpdated: "2 hours ago",
    linkedChats: 2,
    linkedReports: 1
  },
  {
    id: 2,
    name: "Triphala Delivery Mechanism",
    focus: "IP & Prior Art",
    jurisdiction: "India (AYUSH)",
    status: "Completed",
    lastUpdated: "3 days ago",
    linkedChats: 1,
    linkedReports: 2
  },
  {
    id: 3,
    name: "European Turmeric Supplement",
    focus: "Regulatory Pathway",
    jurisdiction: "European Union",
    status: "Paused",
    lastUpdated: "1 week ago",
    linkedChats: 4,
    linkedReports: 0
  }
];

const MOCK_CHATS = [
  {
    id: 101,
    title: "EFSA claims for Ashwagandha root extract",
    language: "English",
    lastUpdated: "Today, 10:42 AM",
    projectId: 1
  },
  {
    id: 102,
    title: "Triphala references in Suśruta Saṁhitā",
    language: "Sanskrit",
    lastUpdated: "Yesterday, 2:15 PM",
    projectId: 2
  }
];

const MOCK_REPORTS = [
  {
    id: 201,
    title: "Jurisdiction Matrix: US vs EU for Botanicals",
    type: "Jurisdiction Comparison",
    created: "Oct 12, 2026",
    projectId: 1
  }
];

export default function MyWorkspace() {
  // Toggle this to see authenticated vs unauthenticated states
  const [isAuthenticated, setIsAuthenticated] = useState(false);
  
  // State for toggling empty states for demonstration
  const [showEmptyStates, setShowEmptyStates] = useState(false);

  return (
    <div className={styles.workspaceContainer}>
      
      {/* Workspace Header */}
      <header className={styles.header}>
        <div className={styles.headerPattern}></div>
        <div className={styles.headerContent}>
          <div className={styles.headerInfo}>
            <h1 className={styles.headerTitle}>Keep the work that should compound.</h1>
            <p className={styles.headerSubtitle}>
              Save innovation projects, return to chat history and keep generated reports in one secure Ayurveda research workspace.
            </p>
          </div>
          <button className={styles.newProjectButton}>
            <Plus size={18} /> New project
          </button>
        </div>
      </header>

      {/* Preview Mode Banner */}
      {!isAuthenticated && (
        <div className={styles.previewBanner}>
          <div className={styles.previewBannerInfo}>
            <div className={styles.previewBannerTitle}>
              <Lock size={18} /> Preview mode is active
            </div>
            <div className={styles.previewBannerText}>
              You are viewing sample workspace content. Signing in enables private saving and connects your projects across sessions. Note: We never display another user's records.
            </div>
          </div>
          <button className={styles.signInButton} onClick={() => setIsAuthenticated(true)}>
            Sign in to save
          </button>
        </div>
      )}

      <main className={styles.mainContent}>
        
        {/* Workspace Metrics */}
        <div className={styles.metricsGrid}>
          <div className={styles.metricCard}>
            <div className={styles.metricIcon}>
              <FolderKanban size={24} />
            </div>
            <div>
              <div className={styles.metricValue}>{showEmptyStates ? 0 : MOCK_PROJECTS.length}</div>
              <div className={styles.metricLabel}>Saved Projects</div>
            </div>
          </div>
          <div className={styles.metricCard}>
            <div className={styles.metricIcon}>
              <MessageSquare size={24} />
            </div>
            <div>
              <div className={styles.metricValue}>{showEmptyStates ? 0 : MOCK_CHATS.length}</div>
              <div className={styles.metricLabel}>Chat Sessions</div>
            </div>
          </div>
          <div className={styles.metricCard}>
            <div className={styles.metricIcon}>
              <FileBarChart size={24} />
            </div>
            <div>
              <div className={styles.metricValue}>{showEmptyStates ? 0 : MOCK_REPORTS.length}</div>
              <div className={styles.metricLabel}>Generated Reports</div>
            </div>
          </div>
        </div>

        {/* Innovation Projects Panel */}
        <section>
          <div className={styles.sectionHeader}>
            <h2 className={styles.sectionTitle}>
              <FolderKanban size={20} /> Innovation Projects
            </h2>
            <div className={styles.filters}>
              <select className={styles.filterSelect}>
                <option>All Statuses</option>
                <option>Active</option>
                <option>Paused</option>
                <option>Completed</option>
              </select>
              <select className={styles.filterSelect}>
                <option>All Jurisdictions</option>
                <option>India</option>
                <option>United States</option>
                <option>European Union</option>
              </select>
            </div>
          </div>
          
          {showEmptyStates ? (
            <div className={styles.emptyState}>
              <div className={styles.emptyIcon}><FolderKanban size={32} /></div>
              <div className={styles.emptyTitle}>No projects yet</div>
              <div className={styles.emptyDesc}>Group your research, chat sessions, and reports by creating your first Ayurveda innovation project.</div>
              <button className={styles.newProjectButton}><Plus size={16} /> Create Project</button>
            </div>
          ) : (
            <div className={styles.cardsGrid}>
              {MOCK_PROJECTS.map(project => (
                <div key={project.id} className={styles.projectCard}>
                  <div className={styles.projectHeader}>
                    <div className={styles.projectName}>{project.name}</div>
                    <div className={`${styles.projectStatus} ${
                      project.status === 'Active' ? styles.statusActive : 
                      project.status === 'Completed' ? styles.statusCompleted : styles.statusPaused
                    }`}>
                      {project.status}
                    </div>
                  </div>
                  <div className={styles.projectDetails}>
                    <div className={styles.projectDetail}>
                      <Leaf size={14} className="text-stone-400" /> Focus: {project.focus}
                    </div>
                    <div className={styles.projectDetail}>
                      <Scale size={14} className="text-stone-400" /> Jurisdiction: {project.jurisdiction}
                    </div>
                    <div className={styles.projectDetail}>
                      <Clock size={14} className="text-stone-400" /> Updated: {project.lastUpdated}
                    </div>
                  </div>
                  <div className={styles.projectFooter}>
                    <div className={styles.projectLinks}>
                      <Link href="#" className={styles.projectLink}>
                        <MessageSquare size={12} /> {project.linkedChats} Chats
                      </Link>
                      <Link href="#" className={styles.projectLink}>
                        <FileBarChart size={12} /> {project.linkedReports} Reports
                      </Link>
                    </div>
                    <Link href="#" className={styles.projectLink}>Open <ArrowRight size={14} /></Link>
                  </div>
                </div>
              ))}
            </div>
          )}
        </section>

        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(400px, 1fr))', gap: '3rem' }}>
          
          {/* Chat History Panel */}
          <section>
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>
                <MessageSquare size={20} /> Chat History
              </h2>
              <div className={styles.filters}>
                <div className={styles.filterSelect} style={{display: 'flex', alignItems: 'center', gap: '0.25rem'}}>
                  <Search size={14}/> Search
                </div>
              </div>
            </div>
            
            {showEmptyStates ? (
              <div className={styles.emptyState} style={{padding: '3rem 1.5rem'}}>
                <div className={styles.emptyIcon} style={{width: '3rem', height: '3rem'}}><MessageSquare size={24} /></div>
                <div className={styles.emptyTitle}>No saved chats</div>
                <div className={styles.emptyDesc}>Start exploring traditional knowledge or regulatory pathways.</div>
                <Link href="/assistant" className={styles.signInButton} style={{textDecoration: 'none'}}>Ask AYURLEX</Link>
              </div>
            ) : (
              <div style={{display: 'flex', flexDirection: 'column', gap: '1rem'}}>
                {MOCK_CHATS.map(chat => (
                  <div key={chat.id} className={styles.itemCard}>
                    <div className={styles.itemInfo}>
                      <div className={styles.itemTitle}>
                        <MessageSquare size={16} className="text-sage-500" /> {chat.title}
                      </div>
                      <div className={styles.itemMeta}>
                        <span className={styles.itemMetaTag}>
                          <Globe size={12} className="inline mr-1" /> {chat.language}
                        </span>
                        <span>{chat.lastUpdated}</span>
                      </div>
                    </div>
                    <Link href="/assistant" className={styles.itemAction}>
                      Resume <ArrowRight size={16} />
                    </Link>
                  </div>
                ))}
              </div>
            )}
          </section>

          {/* Generated Reports Panel */}
          <section>
            <div className={styles.sectionHeader}>
              <h2 className={styles.sectionTitle}>
                <FileBarChart size={20} /> Generated Reports
              </h2>
            </div>

            {showEmptyStates ? (
              <div className={styles.emptyState} style={{padding: '3rem 1.5rem'}}>
                <div className={styles.emptyIcon} style={{width: '3rem', height: '3rem'}}><FileBarChart size={24} /></div>
                <div className={styles.emptyTitle}>No reports generated</div>
                <div className={styles.emptyDesc}>Complete a jurisdiction matrix or innovation brief to save reports here.</div>
              </div>
            ) : (
              <div style={{display: 'flex', flexDirection: 'column', gap: '1rem'}}>
                {MOCK_REPORTS.map(report => (
                  <div key={report.id} className={styles.itemCard}>
                    <div className={styles.itemInfo}>
                      <div className={styles.itemTitle}>
                        <FileBarChart size={16} className="text-terracotta-500" /> {report.title}
                      </div>
                      <div className={styles.itemMeta}>
                        <span className={styles.itemMetaTag}>{report.type}</span>
                        <span>{report.created}</span>
                      </div>
                    </div>
                    <div style={{display: 'flex', gap: '0.75rem'}}>
                      <Link href="#" className={styles.itemAction}>
                        <ExternalLink size={16} /> Open
                      </Link>
                      <Link href="#" className={styles.itemAction}>
                        <Download size={16} /> Export
                      </Link>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </section>

        </div>
        
        {/* Helper to toggle states for testing/demo */}
        <div style={{marginTop: '2rem', display: 'flex', justifyContent: 'center', gap: '1rem'}}>
           <button onClick={() => setShowEmptyStates(!showEmptyStates)} className={styles.signInButton}>
             Toggle Empty States (Demo)
           </button>
           <button onClick={() => setIsAuthenticated(!isAuthenticated)} className={styles.signInButton}>
             Toggle Authenticated Mode (Demo)
           </button>
        </div>

      </main>
    </div>
  );
}
