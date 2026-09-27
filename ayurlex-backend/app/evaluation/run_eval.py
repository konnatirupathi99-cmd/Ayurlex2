import sys
import os

# Add the root project directory to the path so absolute imports work
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from app.evaluation.evaluator import evaluator

def main():
    print("Starting AYURLEX Evaluation Framework...")
    report = evaluator.evaluate_all()
    
    print("\n--- EVALUATION SUMMARY ---")
    print(f"Total Tests: {report['summary']['total_tests']}")
    print(f"Passed: {report['summary']['passed']}")
    print(f"Failed: {report['summary']['failed']}")
    print(f"Pass Rate: {report['summary']['pass_rate']}")
    
    print("\n--- SYSTEM METRICS ---")
    print(f"Avg Latency: {report['metrics']['average_latency_ms']} ms")
    print(f"Avg Groundedness: {report['metrics']['average_groundedness']}")
    
    if report['failures_and_flags']:
        print("\n--- FLAGS & FAILURES ---")
        for flag in report['failures_and_flags']:
            print(f"- {flag}")
            
    print(f"\nDetailed report written to: {os.path.join(os.path.dirname(__file__), 'evaluation_report.json')}")

if __name__ == "__main__":
    main()
