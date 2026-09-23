"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  Printer, 
  Save, 
  ArrowLeft,
  ArrowRight,
  CheckCircle2, 
  Circle,
  FileText,
  MessageCircle,
  ShieldAlert,
  Target,
  Users,
  Lightbulb,
  Map
} from "lucide-react";
import styles from "./guide.module.css";

const PHASES = [
  { id: 1, title: "Frame the Ayurvedic opportunity" },
  { id: 2, title: "Ground the knowledge" },
  { id: 3, title: "Shape the innovation" },
  { id: 4, title: "Compare jurisdictions" },
  { id: 5, title: "Validate responsibly" },
  { id: 6, title: "Build the impact case" }
];

export default function InnovationGuide() {
  const [currentPhase, setCurrentPhase] = useState(1);
  const [completedOutputs, setCompletedOutputs] = useState<Record<string, boolean>>({
    'problem-statement': true,
  });

  const toggleOutput = (id: string) => {
    setCompletedOutputs(prev => ({
      ...prev,
      [id]: !prev[id]
    }));
  };

  return (
    <div className={styles.guideContainer}>
      {/* Guide Introduction Header */}
      <header className={styles.header}>
        <div className={styles.headerPattern}></div>
        <div className={styles.headerContent}>
          <div className={styles.headerEmphasis}>Innovation Guide Playbook</div>
          <h1 className={styles.headerTitle}>From Ayurvedic insight to responsible impact.</h1>
          <p className={styles.headerDescription}>
            Ayurveda innovation spans formulations, products, services, digital tools, evidence systems, knowledge interfaces, and sustainable models. This guide provides a structured framework focusing on provenance, evidence limits, context, safety, and impact.
          </p>
        </div>
        <div className={styles.headerActions}>
          <button className={styles.actionButton}>
            <Save size={18} /> Save Report
          </button>
          <button className={styles.actionButton}>
            <Printer size={18} /> Print Export
          </button>
        </div>
      </header>

      <div className={styles.layout}>
        {/* Step Navigation Sidebar */}
        <aside className={styles.sidebar}>
          <div>
            <div className={styles.navLabel}>Innovation Route</div>
            <div className={styles.stepList}>
              {PHASES.map((phase) => {
                const isActive = phase.id === currentPhase;
                const isCompleted = phase.id < currentPhase;
                
                return (
                  <div 
                    key={phase.id} 
                    className={`${styles.stepItem} ${isActive ? styles.stepItemActive : ''} ${isCompleted ? styles.stepItemCompleted : ''}`}
                    onClick={() => setCurrentPhase(phase.id)}
                  >
                    <div className={styles.stepIndicator}>
                      {isCompleted ? <CheckCircle2 size={16} /> : phase.id}
                    </div>
                    <div className={styles.stepContent}>
                      <div className={styles.stepTitle}>{phase.title}</div>
                      {isActive && <div className={styles.stepStatus}>In Progress</div>}
                      {isCompleted && <div className={styles.stepStatus}>Completed</div>}
                    </div>
                  </div>
                );
              })}
            </div>
          </div>

          {/* Ethical Guardrails Panel */}
          <div className={styles.guardrailPanel}>
            <ShieldAlert className={styles.guardrailIcon} size={20} />
            <div>
              <strong>Ethical Guardrails</strong><br />
              This guide explicitly distinguishes between classical references, modern scientific evidence, innovation novelty, and regulatory interpretation.
            </div>
          </div>
        </aside>

        {/* Main Content Area */}
        <main className={styles.mainContent}>
          {currentPhase === 1 && (
            <>
              <div className={styles.phaseHeader}>
                <div className={styles.phaseTag}>Phase 1</div>
                <h2 className={styles.phaseTitle}>Frame the Ayurvedic opportunity</h2>
                <div className={styles.phaseTasks}>
                  <div className={styles.taskCard}>
                    <Target className={styles.taskIcon} size={18} />
                    <span className={styles.taskText}>Define the unmet need</span>
                  </div>
                  <div className={styles.taskCard}>
                    <Users className={styles.taskIcon} size={18} />
                    <span className={styles.taskText}>Identify intended user</span>
                  </div>
                  <div className={styles.taskCard}>
                    <Lightbulb className={styles.taskIcon} size={18} />
                    <span className={styles.taskText}>Explain Ayurvedic rationale</span>
                  </div>
                  <div className={styles.taskCard}>
                    <Map className={styles.taskIcon} size={18} />
                    <span className={styles.taskText}>Define innovation boundary</span>
                  </div>
                </div>
              </div>

              <div className={styles.phaseBody}>
                
                {/* Working Outputs */}
                <div>
                  <h3 className={styles.sectionHeading}>
                    <FileText size={20} /> Working Outputs
                  </h3>
                  <div className={styles.outputsGrid}>
                    <div 
                      className={styles.outputCard} 
                      onClick={() => toggleOutput('problem-statement')}
                      style={completedOutputs['problem-statement'] ? { borderColor: 'var(--color-botanical-green)', backgroundColor: 'white' } : {}}
                    >
                      <div className={styles.outputHeader}>
                        <div className={styles.outputTitle}>
                          {completedOutputs['problem-statement'] ? <CheckCircle2 size={18} className="text-botanical-600" /> : <Circle size={18} className="text-stone-400" />}
                          Problem Statement
                        </div>
                        <div className={styles.outputStatus}>
                          {completedOutputs['problem-statement'] ? 'Saved' : 'Draft'}
                        </div>
                      </div>
                      <div style={{fontSize: '0.875rem', color: 'var(--color-text-light)'}}>
                        Define the core challenge this innovation addresses.
                      </div>
                      <div className={styles.outputAction}>Edit Document</div>
                    </div>

                    <div 
                      className={styles.outputCard}
                      onClick={() => toggleOutput('use-context')}
                      style={completedOutputs['use-context'] ? { borderColor: 'var(--color-botanical-green)', backgroundColor: 'white' } : {}}
                    >
                      <div className={styles.outputHeader}>
                        <div className={styles.outputTitle}>
                          {completedOutputs['use-context'] ? <CheckCircle2 size={18} className="text-botanical-600" /> : <Circle size={18} className="text-stone-400" />}
                          Use-Context Note
                        </div>
                        <div className={styles.outputStatus}>
                          {completedOutputs['use-context'] ? 'Saved' : 'Pending'}
                        </div>
                      </div>
                      <div style={{fontSize: '0.875rem', color: 'var(--color-text-light)'}}>
                        Detail how and where the user will interact with this.
                      </div>
                      <div className={styles.outputAction}>Start Draft</div>
                    </div>

                    <div 
                      className={styles.outputCard}
                      onClick={() => toggleOutput('success-metric')}
                      style={completedOutputs['success-metric'] ? { borderColor: 'var(--color-botanical-green)', backgroundColor: 'white' } : {}}
                    >
                      <div className={styles.outputHeader}>
                        <div className={styles.outputTitle}>
                          {completedOutputs['success-metric'] ? <CheckCircle2 size={18} className="text-botanical-600" /> : <Circle size={18} className="text-stone-400" />}
                          Success Metric
                        </div>
                        <div className={styles.outputStatus}>
                          {completedOutputs['success-metric'] ? 'Saved' : 'Pending'}
                        </div>
                      </div>
                      <div style={{fontSize: '0.875rem', color: 'var(--color-text-light)'}}>
                        Define measurable outcomes for clinical or market success.
                      </div>
                      <div className={styles.outputAction}>Start Draft</div>
                    </div>
                  </div>
                </div>

                {/* Ask AYURLEX Prompt */}
                <div className={styles.askPromptBox}>
                  <div className={styles.askIcon}>
                    <MessageCircle size={20} />
                  </div>
                  <div className={styles.askContent}>
                    <div className={styles.askLabel}>Ask AYURLEX</div>
                    <div className={styles.askText}>"What evidence would change our decision at this phase?"</div>
                    <button className={styles.askButton}>Ask Assistant</button>
                  </div>
                </div>

              </div>
            </>
          )}

          {/* Render placeholders for other phases if needed */}
          {currentPhase !== 1 && (
            <div className={styles.phaseHeader} style={{ height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', backgroundColor: 'white', color: 'var(--color-text-light)' }}>
              <h2 className={styles.phaseTitle} style={{ color: 'var(--color-sage)' }}>{PHASES.find(p => p.id === currentPhase)?.title}</h2>
              <p>Phase content is currently being loaded...</p>
            </div>
          )}

          {/* Phase Controls */}
          <div className={styles.phaseControls}>
            <button 
              className={styles.controlButton} 
              disabled={currentPhase === 1}
              onClick={() => setCurrentPhase(Math.max(1, currentPhase - 1))}
              style={{ opacity: currentPhase === 1 ? 0.5 : 1 }}
            >
              <ArrowLeft size={18} /> Previous Phase
            </button>
            <button 
              className={`${styles.controlButton} ${styles.controlButtonPrimary}`}
              onClick={() => setCurrentPhase(Math.min(6, currentPhase + 1))}
            >
              {currentPhase === 6 ? 'Complete Guide' : 'Next Phase'} <ArrowRight size={18} />
            </button>
          </div>
        </main>
      </div>
    </div>
  );
}
