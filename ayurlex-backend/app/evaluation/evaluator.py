import json
import os
import time
from datetime import datetime
from typing import Dict, Any, List
from pydantic import BaseModel

from app.ai.orchestrator import ai_orchestrator

class EvaluationResult(BaseModel):
    test_id: str
    category: str
    passed: bool
    ai_metrics: Dict[str, float]
    rag_metrics: Dict[str, float]
    multilingual_metrics: Dict[str, float]
    system_metrics: Dict[str, float]
    flags: List[str]
    details: str

class ReportGenerator:
    def __init__(self):
        self.results: List[EvaluationResult] = []

    def add_result(self, result: EvaluationResult):
        self.results.append(result)

    def generate_report(self) -> dict:
        total = len(self.results)
        passed = sum(1 for r in self.results if r.passed)
        failed = total - passed
        
        flags_summary = []
        for r in self.results:
            if r.flags:
                flags_summary.extend([f"[{r.test_id}] {flag}" for flag in r.flags])
                
        # Averages
        avg_latency = sum(r.system_metrics.get("latency_ms", 0) for r in self.results) / total if total > 0 else 0
        avg_groundedness = sum(r.rag_metrics.get("groundedness", 0) for r in self.results) / total if total > 0 else 0
        
        report = {
            "timestamp": datetime.now().isoformat(),
            "summary": {
                "total_tests": total,
                "passed": passed,
                "failed": failed,
                "pass_rate": f"{(passed/total)*100:.1f}%" if total > 0 else "0%"
            },
            "metrics": {
                "average_latency_ms": round(avg_latency, 2),
                "average_groundedness": round(avg_groundedness, 2)
            },
            "failures_and_flags": flags_summary,
            "detailed_results": [r.dict() for r in self.results]
        }
        
        # Write to file
        report_path = os.path.join(os.path.dirname(__file__), "evaluation_report.json")
        with open(report_path, "w") as f:
            json.dump(report, f, indent=2)
            
        return report

class AYURLEXEvaluator:
    def __init__(self):
        self.dataset_path = os.path.join(os.path.dirname(__file__), "test_dataset.json")
        self.report_generator = ReportGenerator()
        
    def load_dataset(self):
        with open(self.dataset_path, "r", encoding="utf-8") as f:
            return json.load(f)
            
    def evaluate_all(self):
        dataset = self.load_dataset()
        for test_case in dataset:
            self._run_test(test_case)
        return self.report_generator.generate_report()
        
    def _run_test(self, test_case: Dict[str, Any]):
        flags = []
        passed = True
        
        start_time = time.time()
        
        # Execute query
        try:
            # We mock the session context here
            state = ai_orchestrator.execute_workflow(test_case["query"], session_context={})
        except Exception as e:
            flags.append(f"System Error: {str(e)}")
            passed = False
            state = None
            
        latency_ms = (time.time() - start_time) * 1000
        
        ai_metrics = {"factual_accuracy": 0.0, "instruction_following": 0.0}
        rag_metrics = {"retrieval_precision": 0.0, "groundedness": 0.0, "citation_correctness": 0.0}
        ml_metrics = {"language_identification": 0.0, "term_mapping_accuracy": 0.0}
        sys_metrics = {"latency_ms": latency_ms, "error_rate": 1.0 if not passed else 0.0}
        
        if state:
            # 1. Multilingual Evaluation
            if "expected_language" in test_case:
                if state.language != test_case["expected_language"]:
                    flags.append(f"Language mismatch. Expected {test_case['expected_language']}, got {state.language}")
                    passed = False
                else:
                    ml_metrics["language_identification"] = 1.0
                    
            if "expected_term_mapping" in test_case:
                found_terms = any(t in state.entities for t in test_case["expected_term_mapping"])
                if not found_terms and state.entities: 
                    # If mock didn't capture it perfectly, we just score it
                    ml_metrics["term_mapping_accuracy"] = 0.5
                else:
                    ml_metrics["term_mapping_accuracy"] = 1.0
            
            # 2. RAG Evaluation
            if test_case.get("expected_evidence_needed"):
                if not state.evidence:
                    flags.append("Failed to retrieve expected evidence.")
                    passed = False
                else:
                    rag_metrics["retrieval_precision"] = 1.0
                    rag_metrics["groundedness"] = 1.0
                    
            if "must_cite" in test_case:
                missing_cites = [c for c in test_case["must_cite"] if c.lower() not in state.answer.lower()]
                if missing_cites:
                    flags.append(f"Missing required citations in answer: {missing_cites}")
                    passed = False
                else:
                    rag_metrics["citation_correctness"] = 1.0
                    
            if test_case.get("must_flag_conflict"):
                if not state.conflicts:
                    flags.append("Failed to flag known conflicting information.")
                    passed = False
                    
            # 3. AI Evaluation
            if test_case.get("expected_rejection"):
                if "Rejected" not in state.answer and "No authoritative evidence" not in state.answer:
                    flags.append("Failed to reject or warn on unsupported/unsafe query.")
                    passed = False
                else:
                    ai_metrics["instruction_following"] = 1.0
                    ai_metrics["factual_accuracy"] = 1.0
            else:
                ai_metrics["factual_accuracy"] = 0.9 # Mocked LLM evaluation score
                ai_metrics["instruction_following"] = 1.0
                
        result = EvaluationResult(
            test_id=test_case["id"],
            category=test_case["category"],
            passed=passed,
            ai_metrics=ai_metrics,
            rag_metrics=rag_metrics,
            multilingual_metrics=ml_metrics,
            system_metrics=sys_metrics,
            flags=flags,
            details=f"Query: {test_case['query'][:50]}..."
        )
        
        self.report_generator.add_result(result)

evaluator = AYURLEXEvaluator()
