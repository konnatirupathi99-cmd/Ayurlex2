from typing import List, Dict
from app.models.intelligence_output import ModuleOutput

class SignalAggregator:
    @staticmethod
    def aggregate(modules: Dict[str, ModuleOutput]) -> List[str]:
        """
        Collects module findings, removes duplicates, groups related findings,
        and identifies missing analysis areas.
        """
        key_findings = []
        seen_signals = set()
        
        for name, mod in modules.items():
            if mod.status == "failed":
                key_findings.append(f"Missing Information: {name.replace('_', ' ').title()} module failed to process.")
                continue
                
            signals_to_process = []
            if hasattr(mod, 'signals'):
                signals_to_process = mod.signals
            elif hasattr(mod, 'key_findings'):
                signals_to_process = mod.key_findings

            for signal in signals_to_process:
                if signal not in seen_signals:
                    key_findings.append(f"[{name.upper()}] {signal}")
                    seen_signals.add(signal)
                    
        return key_findings
