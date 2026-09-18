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

            for raw_signal in signals_to_process:
                # Handle both string and complex signal objects
                signal_text = raw_signal
                if hasattr(raw_signal, 'signal'):
                    signal_text = raw_signal.signal
                elif isinstance(raw_signal, dict) and 'signal' in raw_signal:
                    signal_text = raw_signal['signal']
                    
                if signal_text not in seen_signals:
                    key_findings.append(f"[{name.upper()}] {signal_text}")
                    seen_signals.add(signal_text)
                    
        return key_findings
