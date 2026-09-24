"use client";

import React, { useState } from "react";
import Link from "next/link";
import { 
  AlertTriangle, 
  Download, 
  FileText, 
  MessageCircle, 
  Save, 
  Globe,
  MapPin,
  Scale
} from "lucide-react";
import styles from "./jurisdictions.module.css";

export default function JurisdictionsIntelligence() {
  const [selectedMarket, setSelectedMarket] = useState("India");

  const handleExportCSV = () => {
    const csvContent = "data:text/csv;charset=utf-8," 
      + "Decision Lens,India,European Union,United States,Australia\n"
      + "Category first question,Is it a classical formulation or a new proprietary medicine?,Is the botanical a novel food or approved for supplements?,Is the ingredient an NDI or does it have a history of safe use?,Is the ingredient pre-cleared for use in listed medicines?\n"
      + "Claim sensitivity,High for proprietary; specific rules for classical.,Extremely High; EFSA botanical claims on hold.,Moderate; strictly structure/function only.,High; requires sponsor evidence dossier.\n"
      + "Evidence emphasis,Textual references from authoritative books.,Safety history & pharmacokinetic data.,Safety & historical use.,TGA approved evidence requirements.\n"
      + "Early action,Verify formulation against Schedule I books.,Check Novel Food status.,Review FDA warning letters for similar ingredients.,Search TGA ingredient database.";
    
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", "ayurlex-jurisdiction-matrix.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  const handleExportPDF = () => {
    window.print();
  };

  const handleSaveToWorkspace = () => {
    // Mock save logic, triggering unauthenticated state for demo
    alert("Please sign in to save this jurisdiction comparison report to your workspace.");
  };

  return (
    <div className={styles.jurisdictionsContainer}>
      {/* Page Header */}
      <header className={styles.header}>
        <div className={styles.headerPattern}></div>
        <div className={styles.headerContent}>
          <div className={styles.headerInfo}>
            <h1 className={styles.headerTitle}>Compare the route before you scale.</h1>
            <p className={styles.headerSubtitle}>
              Compare market-entry pathways, product categorizations, claim sensitivities, and evidence expectations to plan a responsible global launch.
            </p>
          </div>
          <div className={styles.headerActions}>
            <Link href="/assistant" className={styles.actionButton} style={{textDecoration: 'none', color: 'inherit'}}>
              <MessageCircle size={16} /> Ask AYURLEX
            </Link>
            <button className={styles.actionButton} onClick={handleExportCSV}>
              <FileText size={16} /> Export CSV
            </button>
            <button className={styles.actionButton} onClick={handleExportPDF}>
              <Download size={16} /> Export PDF
            </button>
          </div>
        </div>
      </header>

      <main className={styles.mainContent}>
        
        {/* Responsible Regulatory Disclaimer */}
        <div className={styles.disclaimerBanner}>
          <AlertTriangle className={styles.disclaimerIcon} size={20} />
          <div>
            <strong>Orientation Tool Only</strong><br />
            This jurisdiction intelligence interface provides an initial orientation pathway and does not serve as a substitute for current legal, regulatory, or professional advice. Always verify current authority guidance and confirm with qualified regulatory counsel before making market-entry decisions.
          </div>
        </div>

        {/* Selected Pathway Panel */}
        <div className={styles.pathwayPanel}>
          <div className={styles.pathwayInfo}>
            <div className={styles.pathwayHeader}>
              <span className={styles.pathwayTitle}>Primary Market Analysis</span>
              <button className={styles.saveAction} onClick={handleSaveToWorkspace}>
                <Save size={16} /> Save to workspace
              </button>
            </div>
            
            <select 
              className={styles.marketSelector}
              value={selectedMarket}
              onChange={(e) => setSelectedMarket(e.target.value)}
            >
              <option value="India">India</option>
              <option value="European Union">European Union</option>
              <option value="United States">United States</option>
              <option value="Australia">Australia</option>
            </select>

            <div className={styles.postureGrid} style={{marginTop: '2rem'}}>
              <div className={styles.postureItem}>
                <span className={styles.postureLabel}>Product Posture</span>
                <span className={styles.postureValue}>
                  {selectedMarket === "India" ? "AYUSH / Drugs & Cosmetics" : 
                   selectedMarket === "European Union" ? "Food Supplement / Cosmetics" : 
                   selectedMarket === "United States" ? "Dietary Supplement" : "Listed Medicine"}
                </span>
              </div>
              <div className={styles.postureItem}>
                <span className={styles.postureLabel}>Primary Regulator</span>
                <span className={styles.postureValue}>
                  {selectedMarket === "India" ? "Ministry of Ayush" : 
                   selectedMarket === "European Union" ? "EFSA & Member States" : 
                   selectedMarket === "United States" ? "FDA" : "TGA"}
                </span>
              </div>
            </div>

            <div className={styles.marketNote}>
              <strong>Market Note:</strong> {
                selectedMarket === "India" ? "Strong fit for classical formulations and Ayurveda-led positioning under Schedule I authoritative books." :
                selectedMarket === "European Union" ? "High claim substantiation requirements; strictly bounded by Novel Food regulations and EFSA botanical claims on hold." :
                selectedMarket === "United States" ? "Must adhere strictly to structure/function language with rigorous facility controls (cGMP)." :
                "Requires careful ingredient matching with the Permissible Ingredients Determination and strict sponsor evidence dossier holding."
              }
            </div>
          </div>
          
          <div className={styles.readinessWidget}>
            <div className={styles.readinessTitle}>Orientation Readiness</div>
            <div className={styles.readinessScore}>
              {selectedMarket === "India" ? "88" : selectedMarket === "European Union" ? "42" : selectedMarket === "United States" ? "65" : "55"}
            </div>
            <div className={styles.progressContainer}>
              <div 
                className={styles.progressBar} 
                style={{width: selectedMarket === "India" ? "88%" : selectedMarket === "European Union" ? "42%" : selectedMarket === "United States" ? "65%" : "55%"}}
              ></div>
            </div>
            <div className={styles.readinessLabel}>
              Based on formulation and evidence gap analysis
            </div>
          </div>
        </div>

        {/* Comparison Matrix */}
        <div style={{marginTop: '1rem'}}>
          <h2 className={styles.sectionHeading}>
            <Scale size={24} /> Route Comparison Matrix
          </h2>
          <div className={styles.matrixContainer}>
            <div className={styles.matrixWrapper}>
              <table className={styles.matrixTable}>
                <thead>
                  <tr>
                    <th className={styles.matrixTh}>Decision Lens</th>
                    <th className={styles.matrixTh}>
                      <div className="flex items-center gap-2"><Globe size={14}/> India</div>
                    </th>
                    <th className={styles.matrixTh}>
                      <div className="flex items-center gap-2"><Globe size={14}/> European Union</div>
                    </th>
                    <th className={styles.matrixTh}>
                      <div className="flex items-center gap-2"><Globe size={14}/> United States</div>
                    </th>
                    <th className={styles.matrixTh}>
                      <div className="flex items-center gap-2"><Globe size={14}/> Australia</div>
                    </th>
                  </tr>
                </thead>
                <tbody>
                  <tr className={styles.matrixTr}>
                    <td className={styles.matrixTd}>
                      <div className={styles.matrixRowLabel}>Category first question</div>
                    </td>
                    <td className={styles.matrixTd}>Is it a classical formulation or a new proprietary medicine?</td>
                    <td className={styles.matrixTd}>Is the botanical a <span className={styles.termHighlight}>novel food</span> or approved for supplements?</td>
                    <td className={styles.matrixTd}>Is the ingredient an NDI or does it have a history of safe use?</td>
                    <td className={styles.matrixTd}>Is the ingredient pre-cleared for use in listed medicines?</td>
                  </tr>
                  <tr className={styles.matrixTr}>
                    <td className={styles.matrixTd}>
                      <div className={styles.matrixRowLabel}>Claim sensitivity</div>
                    </td>
                    <td className={styles.matrixTd}>High for proprietary; specific rules for classical texts.</td>
                    <td className={styles.matrixTd}>Extremely High; EFSA botanical claims currently on hold.</td>
                    <td className={styles.matrixTd}>Moderate; strictly limited to <span className={styles.termHighlight}>structure/function</span> claims.</td>
                    <td className={styles.matrixTd}>High; requires sponsor to hold evidence dossier.</td>
                  </tr>
                  <tr className={styles.matrixTr}>
                    <td className={styles.matrixTd}>
                      <div className={styles.matrixRowLabel}>Evidence emphasis</div>
                    </td>
                    <td className={styles.matrixTd}>Textual references from Schedule I authoritative books.</td>
                    <td className={styles.matrixTd}>Safety history & pharmacokinetic data.</td>
                    <td className={styles.matrixTd}>Safety & historical use (GRAS/NDI).</td>
                    <td className={styles.matrixTd}>TGA approved evidence requirements based on claim level.</td>
                  </tr>
                  <tr className={styles.matrixTr}>
                    <td className={styles.matrixTd}>
                      <div className={styles.matrixRowLabel}>Early action</div>
                    </td>
                    <td className={styles.matrixTd}>Verify formulation against classical texts.</td>
                    <td className={styles.matrixTd}>Check Novel Food catalogue status.</td>
                    <td className={styles.matrixTd}>Review FDA warning letters for similar ingredients.</td>
                    <td className={styles.matrixTd}>Search TGA ingredient database.</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* Global Market Overview Cards */}
        <div style={{marginTop: '1rem'}}>
          <h2 className={styles.sectionHeading}>
            <MapPin size={24} /> Market Posture Overview
          </h2>
          <div className={styles.marketCardsGrid}>
            
            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> India</div>
                <div className={styles.marketCategory}>AYUSH / Drugs</div>
              </div>
              <p className={styles.marketDescription}>
                Strong fit for classical formulations and Ayurveda-led positioning. Clear pathways exist for both classical and proprietary Ayurvedic medicines under the Drugs & Cosmetics Act.
              </p>
            </div>

            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> European Union</div>
                <div className={styles.marketCategory}>Food Supp / Cosmetics</div>
              </div>
              <p className={styles.marketDescription}>
                Requires high claim substantiation and navigation of member-state nuances. Traditional Herbal Registration (THR) is possible but requires 15 years of EU usage history.
              </p>
            </div>

            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> United States</div>
                <div className={styles.marketCategory}>Dietary Supp</div>
              </div>
              <p className={styles.marketDescription}>
                Operates under DSHEA. Strict boundary requiring structure/function language only. Claims cannot mention disease treatment or prevention. Strong facility controls required.
              </p>
            </div>

            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> Australia</div>
                <div className={styles.marketCategory}>Listed Medicine</div>
              </div>
              <p className={styles.marketDescription}>
                Regulated by the TGA. Ingredients must be on the permissible list. Sponsors bear strict responsibility for holding evidence dossiers to support any made claims.
              </p>
            </div>

            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> United Arab Emirates</div>
                <div className={styles.marketCategory}>Health Product</div>
              </div>
              <p className={styles.marketDescription}>
                Requires a local importer. Classification questions often arise between health supplements and herbal medicines, dictating the registration complexity.
              </p>
            </div>

            <div className={styles.marketCard}>
              <div className={styles.marketCardHeader}>
                <div className={styles.marketName}><Globe size={18} /> Singapore</div>
                <div className={styles.marketCategory}>Health Supplement</div>
              </div>
              <p className={styles.marketDescription}>
                Operates under strict advertising boundaries via the HSA. Requires compiling a safety and quality evidence dossier prior to market entry.
              </p>
            </div>

          </div>
        </div>

      </main>
    </div>
  );
}
