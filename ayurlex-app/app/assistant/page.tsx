"use client";

import React, { useState } from "react";
import { useLanguage, LANGUAGE_NAMES } from "@/components/LanguageProvider";
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
  const { language, t } = useLanguage();

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
            <h1 className={styles.headerTitle}>{t('assistant.headerTitle')}</h1>
            <p className={styles.headerSubtitle}>
              {t('assistant.headerSubtitle')}
            </p>
          </div>
          <div className={styles.statusBadge}>
            <div className={styles.statusIndicator}></div>
            {t('assistant.citationOnline')}
          </div>
        </header>

        {/* Chat Toolbar */}
        <div className={styles.chatToolbar}>
          <div className={styles.toolbarLeft}>
            <div className={styles.toolbarItem}>
              <Leaf size={14} className="text-botanical-600" />
              <strong>{t('assistant.assistantName')}</strong>
            </div>
            <div className={styles.toolbarItem}>
              <Globe size={14} />
              <span className={styles.contextValueSelect} style={{ background: 'transparent', border: 'none', padding: 0 }}>
                {LANGUAGE_NAMES[language]}
              </span>
            </div>
            <div className={styles.toolbarItem}>
              <ShieldAlert size={14} />
              <span>{t('assistant.scopeBadge')}</span>
            </div>
          </div>
          <div className={styles.toolbarItem}>
            <CheckCircle2 size={14} className="text-botanical-600" />
            {t('assistant.liveCitation')}
          </div>
        </div>

        {/* Conversation Area */}
        <div className={styles.conversationArea}>
          {language === 'hi' ? (
            <>
              {/* User Message */}
              <div className={`${styles.message} ${styles.messageUser}`}>
                <div className={`${styles.avatar} ${styles.avatarUser}`}>
                  <User size={18} />
                </div>
                <div className={styles.messageContent}>
                  क्या आप अश्वगंधा (Ashwagandha) का उपयोग करके मेरे पुराने जोड़ों के दर्द का निदान करने में मदद कर सकते हैं?
                </div>
              </div>

              {/* Assistant Guardrail Message */}
              <div className={styles.message}>
                <div className={`${styles.avatar} ${styles.avatarAssistant}`}>
                  <Leaf size={18} />
                </div>
                <div className={`${styles.messageContent} ${styles.messageGuardrail}`}>
                  <AlertTriangle className={styles.guardrailIcon} size={18} />
                  {t('assistant.guardrailText')}
                  <br/><br/>
                  <em>{t('assistant.guardrailDisclaimer')}</em>
                </div>
              </div>

              {/* User Message 2 */}
              <div className={`${styles.message} ${styles.messageUser}`}>
                <div className={`${styles.avatar} ${styles.avatarUser}`}>
                  <User size={18} />
                </div>
                <div className={styles.messageContent}>
                  मैं यूरोपीय संघ (EU) के बाज़ार में अतिरंजित दावे किए बिना हल्दी (Turmeric) के नवाचार (Innovation) को कैसे अलग कर सकता हूँ?
                </div>
              </div>

              {/* Assistant Response Message */}
              <div className={styles.message}>
                <div className={`${styles.avatar} ${styles.avatarAssistant}`}>
                  <Leaf size={18} />
                </div>
                <div className={styles.messageContent}>
                  <p>यूरोपीय संघ के बाज़ार में हल्दी (<em>Curcuma longa</em>) योग (Formulation) को अलग करने के लिए पारंपरिक ज्ञान का लाभ उठाने और EFSA स्वास्थ्य दावा नियमों का पालन करने के बीच एक सावधानीपूर्वक संतुलन की आवश्यकता होती है।</p>
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">प्रमाण (Evidence)</h3>
                  <p className="text-sm">यूरोपीय संघ में, पारंपरिक हर्बल पंजीकरण (THR) लंबे समय से उपयोग के आधार पर विशिष्ट दावों की अनुमति देता है। <em>सुश्रुत संहिता</em> (Suśruta Saṁhitā) जैसे शास्त्रीय ग्रंथ इसे <em>विषघ्न</em> (viṣaghna, विषनाशक) और <em>कुष्ठघ्न</em> (kuṣṭhaghna, त्वचा-रोग नाशक) के रूप में प्रलेखित करते हैं <a href="#citation-1" className="text-botanical-600 hover:underline font-medium">[1]</a>।</p>
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">नवाचार (Innovation)</h3>
                  <p className="text-sm">अनधिकृत दावों के बिना अलग करने के लिए, आधुनिक फार्माकोकाइनेटिक अध्ययनों द्वारा समर्थित जैव-उपलब्धता वृद्धि (उदा. पिपेरिन/काली मिर्च) पर ध्यान दें <a href="#citation-2" className="text-botanical-600 hover:underline font-medium">[2]</a>। आप प्रत्यक्ष रोग-उपचार दावों को करने के बजाय "पारंपरिक रूप से उपयोग की जाने वाली हल्दी शामिल है..." का दावा कर सकते हैं, जो खाद्य पूरक के लिए सख्त वर्जित हैं।</p>
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">खुले प्रश्न (Open Questions)</h3>
                  <ul className="list-disc pl-5 text-sm space-y-1">
                    <li>आप हल्दी के लिए किस विशिष्ट बायोएक्टिव निष्कर्षण विधि का उपयोग कर रहे हैं?</li>
                    <li>क्या आपके पास इस सटीक तैयारी के लिए यूरोपीय संघ के भीतर 15 वर्षों के प्रलेखित उपयोग का इतिहास है?</li>
                  </ul>

                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">अगला कदम (Next Action)</h3>
                  <p className="text-sm">अपने विशिष्ट अर्क के लिए फार्माकोकाइनेटिक डेटा संकलित करें और अपने लक्षित यूरोपीय संघ के सदस्य राज्य के लिए THR दस्तावेज़ीकरण आवश्यकताओं को सत्यापित करें।</p>
                  
                  <div className={styles.messageMetadata}>
                    <span className="flex items-center gap-1"><BookOpen size={12}/> {t('assistant.citations.source')}: नियामक दिशानिर्देश और शास्त्रीय ग्रंथ</span>
                    <span className="flex items-center gap-1"><Globe size={12}/> {t('workspace.projects.jurisdiction')}: यूरोपीय संघ (EFSA)</span>
                    <span className="flex items-center gap-1"><Info size={12}/> उद्धरण (Citations): 2 जुड़े हुए</span>
                  </div>
                </div>
              </div>
            </>
          ) : (
            <>
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
                  {t('assistant.guardrailText')}
                  <br/><br/>
                  <em>{t('assistant.guardrailDisclaimer')}</em>
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
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">Evidence</h3>
                  <p className="text-sm">In the EU, Traditional Herbal Registration (THR) allows for specific claims based on long-standing use. Classical texts like the <em>Suśruta Saṁhitā</em> document its use as a <em>viṣaghna</em> (विषघ्न, anti-toxic) and <em>kuṣṭhaghna</em> (कुष्ठघ्न, skin-alleviating) agent <a href="#citation-1" className="text-botanical-600 hover:underline font-medium">[1]</a>.</p>
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">Innovation</h3>
                  <p className="text-sm">To differentiate without unauthorized claims, focus on bioavailability enhancements (e.g., Piperine/Black Pepper) supported by modern pharmacokinetic studies <a href="#citation-2" className="text-botanical-600 hover:underline font-medium">[2]</a>. You can claim "contains Turmeric, traditionally used..." rather than making direct disease-treatment claims which are strictly prohibited for food supplements.</p>
                  
                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">Open Questions</h3>
                  <ul className="list-disc pl-5 text-sm space-y-1">
                    <li>What specific bioactive extraction method are you utilizing for the Turmeric?</li>
                    <li>Do you have 15 years of documented usage history within the EU for this exact preparation?</li>
                  </ul>

                  <h3 className="text-sm font-semibold mt-4 mb-2 text-stone-900 border-b border-stone-100 pb-1">Next Action</h3>
                  <p className="text-sm">Compile the pharmacokinetic data for your specific extract and verify the THR documentation requirements for your target EU member state.</p>
                  
                  <div className={styles.messageMetadata}>
                    <span className="flex items-center gap-1"><BookOpen size={12}/> Source: Regulatory Guidelines & Classical Texts</span>
                    <span className="flex items-center gap-1"><Globe size={12}/> Jurisdiction: European Union (EFSA)</span>
                    <span className="flex items-center gap-1"><Info size={12}/> Citations: 2 Linked</span>
                  </div>
                </div>
              </div>
            </>
          )}

        </div>

        {/* Composer Area */}
        <div className={styles.composerContainer}>
          <div className={styles.suggestions}>
            <button className={styles.suggestionChip}>
              {language === 'hi' ? '"मैं अतिरंजित दावे किए बिना हल्दी नवाचार को कैसे अलग कर सकता हूँ?"' : '"How can I differentiate a turmeric innovation without overclaiming?"'}
            </button>
            <button className={styles.suggestionChip}>
              {language === 'hi' ? '"भारत और यूरोपीय संघ के लिए एक आयुर्वेदिक योग मैप करें।"' : '"Map an Ayurvedic formulation for India and the EU."'}
            </button>
            <button className={styles.suggestionChip}>
              {language === 'hi' ? '"सामुदायिक ज्ञान के साथ काम करने से पहले मुझे क्या दस्तावेज़ करना चाहिए?"' : '"What should I document before working with community knowledge?"'}
            </button>
          </div>

          <div className={styles.composerInputWrapper}>
            <div className={styles.scopeLabel}>
              <Leaf size={12} /> {t('common.ayurvedaScope')}
            </div>
            <textarea 
              className={styles.composerInput}
              placeholder={t('assistant.composerPlaceholder')}
              value={inputText}
              onChange={(e) => setInputText(e.target.value)}
              onKeyDown={handleKeyDown}
              rows={2}
            />
            <div className={styles.composerActions}>
              <button className={styles.sendButton}>
                <Send size={16} />
              </button>
              <span className={styles.composerHint}>{t('assistant.shiftEnter')}</span>
            </div>
          </div>
        </div>
      </div>

      {/* Context and Evidence Sidebar */}
      <div className={styles.sidebar}>
        
        {/* Context Lens */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <Scale size={16} /> {t('assistant.lens.title')}
          </div>
          <div className={styles.contextList}>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>{t('assistant.lens.jurisdiction')}</span>
              <select className={styles.contextValueSelect}>
                <option>European Union (EFSA)</option>
                <option>India (Ayush)</option>
                <option>US (FDA / DSHEA)</option>
                <option>UK (MHRA)</option>
              </select>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>{t('assistant.lens.pathway')}</span>
              <span className={styles.contextValue}>
                <span className={styles.statusIndicator} style={{backgroundColor: 'var(--color-amber)'}}></span> Moderate (65/100)
              </span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>{t('assistant.lens.category')}</span>
              <span className={styles.contextValue}>Food Supplement / Botanicals</span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>{t('assistant.lens.claimSensitivity')}</span>
              <span className={styles.contextValue} style={{color: 'var(--color-terracotta)'}}>High (Restricted)</span>
            </div>
            <div className={styles.contextItem}>
              <span className={styles.contextLabel}>{t('assistant.lens.expectedEvidence')}</span>
              <span className={styles.contextValue}>History of Safe Use, Pharmacokinetics</span>
            </div>
          </div>
        </div>

        {/* Answer Quality Panel */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <CheckCircle2 size={16} /> {t('assistant.quality.title')}
          </div>
          <div className={styles.qualityPanel}>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>{t('assistant.quality.coverage')}</span>
              <span className={styles.contextValue}>Comprehensive</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>{t('assistant.quality.classical')}</span>
              <span className={styles.contextValue}>Verified (Suśruta)</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>{t('assistant.quality.journal')}</span>
              <span className={styles.contextValue}>Europe PMC Synced</span>
            </div>
            <div className={styles.qualityItem}>
              <span className={styles.contextLabel}>{t('assistant.quality.openQuestions')}</span>
              <span className={styles.contextValue}>Pending formulation details</span>
            </div>
          </div>
        </div>

        {/* Live Citation Panel */}
        <div className={styles.sidebarSection}>
          <div className={styles.sidebarTitle}>
            <BookOpen size={16} /> {t('assistant.citations.title')}
          </div>
          
          <div className={styles.citationCard}>
            <div className={styles.citationHeader}>
              <span className={`${styles.citationType} ${styles.citationTypeClassical}`}>{t('assistant.citations.classicalType')}</span>
              <CheckCircle2 size={14} className={styles.verifiedBadge} />
            </div>
            <div className={styles.citationTitle}>Suśruta Saṁhitā, Sūtrasthāna</div>
            <div className={styles.citationMeta}>{t('assistant.citations.author')}: Suśruta | {t('assistant.citations.chapter')} 38 (Dravyasaṅgrahaṇīya)</div>
            <div className={styles.citationExcerpt}>
              "Haridrā (Turmeric) is indicated in the Haridrādi Gaṇa for alleviating skin conditions (Kuṣṭha) and acting as an anti-toxic (Viṣaghna)."
            </div>
            <Link href="/library" className={styles.citationLink}>
              <ExternalLink size={12} /> {t('assistant.citations.viewOriginal')}
            </Link>
          </div>

          <div className={styles.citationCard}>
            <div className={styles.citationHeader}>
              <span className={styles.citationType}>{t('assistant.citations.journalType')}</span>
              <CheckCircle2 size={14} className={styles.verifiedBadge} />
            </div>
            <div className={styles.citationTitle}>Bioavailability of Curcumin: Problems and Promises</div>
            <div className={styles.citationMeta}>Anand P, et al. | {t('assistant.citations.year')}: 2007 | {t('assistant.citations.source')}: Europe PMC</div>
            <div className={styles.citationExcerpt}>
              "Piperine enhances the serum concentration, extent of absorption and bioavailability of curcumin in both rats and humans with no adverse effects."
            </div>
            <Link href="/library" className={styles.citationLink}>
              <ExternalLink size={12} /> {t('assistant.citations.verifySource')}
            </Link>
          </div>

          <div style={{fontSize: '0.625rem', color: 'var(--color-text-light)', marginTop: '0.5rem', fontStyle: 'italic'}}>
            {t('assistant.citations.note')}
          </div>
        </div>

        {/* Responsible Use Note */}
        <div className={styles.sidebarSection} style={{borderBottom: 'none'}}>
          <div className={styles.responsibleUse}>
            <Info className="flex-shrink-0" size={16} style={{color: 'var(--color-botanical-green)'}} />
            <div>
              {t('assistant.responsibleUse')}
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
