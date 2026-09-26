"use client";

import React, { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { useLanguage, LANGUAGE_NAMES } from "@/components/LanguageProvider";
import { 
  ArrowRight, 
  ArrowLeft, 
  X, 
  CheckCircle2, 
  Globe2, 
  Flag, 
  Wand2,
  Check,
  Circle,
  Loader2
} from "lucide-react";

type Step = 1 | 2 | 3 | 4 | 'processing';

export default function NewAnalysisWizard() {
  const router = useRouter();
  const [step, setStep] = useState<Step>(1);
  
  // Form State
  const [innovationName, setInnovationName] = useState("");
  const [description, setDescription] = useState("");
  const [category, setCategory] = useState("");
  const [purpose, setPurpose] = useState("");
  
  const [ingredients, setIngredients] = useState<string[]>([]);
  const [ingredientInput, setIngredientInput] = useState("");
  
  const [jurisdiction, setJurisdiction] = useState<string>("");
  const { t, language: globalLangCode, languageName: globalLangName } = useLanguage();

  const [processingStage, setProcessingStage] = useState(0);

  const processingStages = [
    "Understanding Innovation",
    `Detecting Language (Detected: ${globalLangCode})`,
    "Normalizing Ayurvedic Terminology",
    "Classifying Formulation Context",
    "Searching Knowledge Base",
    "Reviewing IP Context",
    "Reviewing Traditional Knowledge",
    "Checking ABS Context",
    "Reviewing Regulatory Context",
    "Validating Evidence",
    "Preparing Intelligence Report"
  ];

  // Processing Animation Simulation
  useEffect(() => {
    if (step === 'processing') {
      const interval = setInterval(() => {
        setProcessingStage(prev => {
          if (prev < processingStages.length - 1) return prev + 1;
          clearInterval(interval);
          // Pass the mocked API context to the report
          sessionStorage.setItem('ayurlex_mock_report_lang', globalLangCode);
          setTimeout(() => router.push('/analysis/demo-id-123'), 1000); // Redirect to report
          return prev;
        });
      }, 1500);
      return () => clearInterval(interval);
    }
  }, [step, router, globalLangCode, processingStages.length]);

  const handleAddIngredient = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter' && ingredientInput.trim() !== '') {
      e.preventDefault();
      if (!ingredients.includes(ingredientInput.trim())) {
        setIngredients([...ingredients, ingredientInput.trim()]);
      }
      setIngredientInput("");
    }
  };

  const removeIngredient = (tag: string) => {
    setIngredients(ingredients.filter(i => i !== tag));
  };

  const nextStep = () => setStep((s) => typeof s === 'number' && s < 4 ? (s + 1) as Step : s);
  const prevStep = () => setStep((s) => typeof s === 'number' && s > 1 ? (s - 1) as Step : s);

  if (step === 'processing') {
    return (
      <div className="max-w-3xl mx-auto py-12 flex flex-col items-center">
        <h1 className="text-3xl font-bold text-stone-900 text-center mb-2">{t('wizard.processingTitle')}</h1>
        <p className="text-stone-500 text-center mb-12">{t('wizard.processingDesc')}</p>

        <div className="flex w-full gap-12">
          {/* Visual Animation */}
          <div className="w-1/2 flex justify-center items-start pt-8">
            <div className="relative flex flex-col items-center">
              <div className="w-16 h-16 rounded-2xl bg-botanical-100 border-2 border-botanical-200 flex items-center justify-center animate-pulse">
                <Wand2 className="w-8 h-8 text-botanical-600" />
              </div>
              <div className="h-16 w-0.5 bg-gradient-to-b from-botanical-200 to-transparent my-2 animate-pulse"></div>
              <div className="w-16 h-16 rounded-full border-4 border-dashed border-stone-200 flex items-center justify-center animate-[spin_4s_linear_infinite]">
                 <div className="w-8 h-8 rounded-full bg-botanical-50"></div>
              </div>
            </div>
          </div>

          {/* Timeline */}
          <div className="w-1/2 space-y-4">
            {processingStages.map((stage, idx) => {
              const isCompleted = idx < processingStage;
              const isCurrent = idx === processingStage;
              return (
                <div key={idx} className={`flex items-center gap-3 transition-opacity duration-500 ${idx > processingStage + 1 ? 'opacity-30' : 'opacity-100'}`}>
                  {isCompleted ? (
                    <CheckCircle2 className="w-5 h-5 text-botanical-600 shrink-0" />
                  ) : isCurrent ? (
                    <Loader2 className="w-5 h-5 text-botanical-600 animate-spin shrink-0" />
                  ) : (
                    <Circle className="w-5 h-5 text-stone-300 shrink-0" />
                  )}
                  <span className={`text-sm ${isCompleted ? 'text-stone-500 line-through' : isCurrent ? 'text-botanical-700 font-medium' : 'text-stone-400'}`}>
                    {stage}
                  </span>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="max-w-3xl mx-auto pb-12">
      {/* Header & Progress */}
      <div className="mb-10 text-center">
        <h1 className="text-2xl font-bold text-stone-900 mb-6">{t('wizard.title')}</h1>
        <div className="flex items-center justify-center gap-2 sm:gap-4 text-sm font-medium">
           {[t('wizard.step1'), t('wizard.step2'), t('wizard.step3'), t('wizard.step4')].map((label, idx) => (
             <React.Fragment key={label}>
               <span className={`${step === idx + 1 ? 'text-botanical-700 font-bold' : step > idx + 1 ? 'text-botanical-600' : 'text-stone-400'}`}>
                 {label}
               </span>
               {idx < 3 && <ArrowRight className="w-4 h-4 text-stone-300" />}
             </React.Fragment>
           ))}
        </div>
      </div>

      {/* Form Container */}
      <div className="bg-white rounded-2xl border border-stone-200 shadow-sm p-6 sm:p-10">
        
        {/* STEP 1: INNOVATION */}
        {step === 1 && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div>
              <label className="block text-sm font-semibold text-stone-900 mb-2">{t('wizard.innovationName')}</label>
              <input 
                type="text" 
                value={innovationName}
                onChange={e => setInnovationName(e.target.value)}
                className="w-full px-4 py-3 rounded-lg border border-stone-300 focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-colors bg-stone-50"
                placeholder="e.g. Ashwagandha & Turmeric Immunity Blend"
              />
            </div>
            <div>
              <label className="block text-sm font-semibold text-stone-900 mb-2">{t('wizard.innovationDesc')}</label>
              <textarea 
                rows={4}
                value={description}
                onChange={e => setDescription(e.target.value)}
                className="w-full px-4 py-3 rounded-lg border border-stone-300 focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-colors bg-stone-50"
                placeholder="Describe your Ayurvedic formulation, product, research idea, or innovation..."
              />
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
              <div>
                <label className="block text-sm font-semibold text-stone-900 mb-2">{t('wizard.category')}</label>
                <select 
                  value={category}
                  onChange={e => setCategory(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg border border-stone-300 focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-colors bg-stone-50"
                >
                  <option value="" disabled>Select a category</option>
                  <option value="Ayurvedic Product">Ayurvedic Product</option>
                  <option value="Herbal Wellness Product">Herbal Wellness Product</option>
                  <option value="Cosmetic">Cosmetic</option>
                  <option value="Food / Ayurveda Aahar">Food / Ayurveda Aahar</option>
                  <option value="Research Innovation">Research Innovation</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div>
                <label className="block text-sm font-semibold text-stone-900 mb-2">{t('wizard.purpose')} <span className="text-stone-400 font-normal">(Optional)</span></label>
                <input 
                  type="text" 
                  value={purpose}
                  onChange={e => setPurpose(e.target.value)}
                  className="w-full px-4 py-3 rounded-lg border border-stone-300 focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-colors bg-stone-50"
                  placeholder="e.g. Immunity boosting"
                />
              </div>
            </div>
          </div>
        )}

        {/* STEP 2: INGREDIENTS */}
        {step === 2 && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <div>
              <h2 className="text-xl font-bold text-stone-900 mb-2">{t('wizard.addIngredients')}</h2>
              <p className="text-sm text-stone-500 mb-6">Enter ingredient names and press Enter to add. You can enter names in your preferred supported language.</p>
              
              <div className="relative">
                <input 
                  type="text" 
                  value={ingredientInput}
                  onChange={e => setIngredientInput(e.target.value)}
                  onKeyDown={handleAddIngredient}
                  className="w-full px-4 py-3 rounded-lg border border-stone-300 focus:ring-2 focus:ring-botanical-500/20 focus:border-botanical-500 transition-colors bg-stone-50"
                  placeholder="Type ingredient and press Enter..."
                />
              </div>

              <div className="mt-6 flex flex-wrap gap-2">
                {ingredients.length === 0 && <span className="text-stone-400 text-sm italic">No ingredients added yet.</span>}
                {ingredients.map(ing => (
                  <span key={ing} className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-full bg-botanical-100 text-botanical-800 text-sm font-medium border border-botanical-200">
                    {ing}
                    <button onClick={() => removeIngredient(ing)} className="text-botanical-600 hover:text-botanical-900">
                      <X className="w-3.5 h-3.5" />
                    </button>
                  </span>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 3: JURISDICTION */}
        {step === 3 && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <h2 className="text-xl font-bold text-stone-900 mb-6">{t('wizard.selectJurisdiction')}</h2>
            <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
              <button 
                onClick={() => setJurisdiction('India')}
                className={`p-6 rounded-xl border-2 text-left transition-all ${jurisdiction === 'India' ? 'border-botanical-600 bg-botanical-50' : 'border-stone-200 hover:border-botanical-300'}`}
              >
                <Flag className={`w-8 h-8 mb-4 ${jurisdiction === 'India' ? 'text-botanical-600' : 'text-stone-400'}`} />
                <h3 className="font-bold text-stone-900 mb-1">India</h3>
                <p className="text-xs text-stone-500">India-focused regulatory and IP analysis context.</p>
              </button>
              <button 
                onClick={() => setJurisdiction('International')}
                className={`p-6 rounded-xl border-2 text-left transition-all ${jurisdiction === 'International' ? 'border-botanical-600 bg-botanical-50' : 'border-stone-200 hover:border-botanical-300'}`}
              >
                <Globe2 className={`w-8 h-8 mb-4 ${jurisdiction === 'International' ? 'text-botanical-600' : 'text-stone-400'}`} />
                <h3 className="font-bold text-stone-900 mb-1">International</h3>
                <p className="text-xs text-stone-500">Broader international IP and research context.</p>
              </button>
              <button 
                onClick={() => setJurisdiction('Auto')}
                className={`p-6 rounded-xl border-2 text-left transition-all ${jurisdiction === 'Auto' ? 'border-botanical-600 bg-botanical-50' : 'border-stone-200 hover:border-botanical-300'}`}
              >
                <Wand2 className={`w-8 h-8 mb-4 ${jurisdiction === 'Auto' ? 'text-botanical-600' : 'text-stone-400'}`} />
                <h3 className="font-bold text-stone-900 mb-1">Auto Detect</h3>
                <p className="text-xs text-stone-500">Allow AYURLEX to determine most relevant context.</p>
              </button>
            </div>
          </div>
        )}

        {/* STEP 4: REVIEW */}
        {step === 4 && (
          <div className="space-y-6 animate-in fade-in slide-in-from-bottom-4 duration-500">
            <h2 className="text-xl font-bold text-stone-900 mb-6">{t('wizard.reviewDetails')}</h2>
            
            <div className="bg-stone-50 p-6 rounded-xl border border-stone-200 space-y-4 text-sm">
              <div className="grid grid-cols-3 gap-4 border-b border-stone-200 pb-4">
                <span className="text-stone-500 font-medium">{t('wizard.innovationName')}</span>
                <span className="col-span-2 text-stone-900 font-semibold">{innovationName || 'Not provided'}</span>
              </div>
              <div className="grid grid-cols-3 gap-4 border-b border-stone-200 pb-4">
                <span className="text-stone-500 font-medium">Description</span>
                <span className="col-span-2 text-stone-900">{description || 'Not provided'}</span>
              </div>
              <div className="grid grid-cols-3 gap-4 border-b border-stone-200 pb-4">
                <span className="text-stone-500 font-medium">Product Category</span>
                <span className="col-span-2 text-stone-900">{category || 'Not selected'}</span>
              </div>
              <div className="grid grid-cols-3 gap-4 border-b border-stone-200 pb-4">
                <span className="text-stone-500 font-medium">Ingredients</span>
                <span className="col-span-2 text-stone-900">
                  {ingredients.length > 0 ? ingredients.join(", ") : 'None added'}
                </span>
              </div>
              <div className="grid grid-cols-3 gap-4 border-b border-stone-200 pb-4">
                <span className="text-stone-500 font-medium">Jurisdiction</span>
                <span className="col-span-2 text-stone-900">{jurisdiction || 'Not selected'}</span>
              </div>
              <div className="grid grid-cols-3 gap-4">
                <span className="text-stone-500 font-medium">Language</span>
                <span className="col-span-2 text-stone-900">{globalLangName}</span>
              </div>
            </div>
          </div>
        )}

        {/* Form Actions */}
        <div className="mt-10 flex items-center justify-between pt-6 border-t border-stone-100">
          <button 
            onClick={prevStep}
            disabled={step === 1}
            className={`px-6 py-2.5 rounded-lg font-medium transition-colors ${step === 1 ? 'opacity-0 pointer-events-none' : 'text-stone-600 hover:bg-stone-100'}`}
          >
            {t('wizard.back')}
          </button>
          
          {step < 4 ? (
            <button 
              onClick={nextStep}
              className="px-6 py-2.5 rounded-lg bg-botanical-700 hover:bg-botanical-800 text-white font-medium flex items-center gap-2 shadow-sm transition-colors"
            >
              {t('wizard.continue')} <ArrowRight className="w-4 h-4" />
            </button>
          ) : (
            <button 
              onClick={() => setStep('processing')}
              className="px-8 py-3 rounded-lg bg-botanical-700 hover:bg-botanical-800 text-white font-bold flex items-center gap-2 shadow-md hover:shadow-lg transition-all"
            >
              <Wand2 className="w-5 h-5" /> {t('wizard.startAnalysis')}
            </button>
          )}
        </div>

      </div>
    </div>
  );
}
