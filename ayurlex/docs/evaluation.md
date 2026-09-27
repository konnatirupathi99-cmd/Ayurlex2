# Evaluation Strategy

## Core Metrics
1. **Retrieval Relevance**: Are the retrieved documents relevant to the query?
2. **Citation Correctness**: Are all claims backed by a retrieved document?
3. **Groundedness**: Does the LLM hallucinate or extrapolate beyond the retrieved facts?
4. **Unsupported Claim Rate**: Percentage of answers containing unsupported legal/regulatory claims.

## Evaluation Dataset
We have curated a 75-question dataset spanning:
- 10 English questions
- 10 Hindi questions
- 10 Telugu questions
- 10 Terminology questions
- 10 IP questions
- 10 Regulatory questions
- 10 Jurisdiction questions
- 5 Conflicting evidence cases

### Example Cases
**Query**: What are the patentability criteria for Ashwagandha?
**Expected**: Identify traditional knowledge, cite Section 3(p) of Indian Patents Act. State that it is generally not patentable.

**Query**: Is turmeric approved by the FDA?
**Expected**: Identify jurisdiction as US. Cite lack of evidence in DB. "INSUFFICIENT EVIDENCE". Do not hallucinate FDA approval.

## Running Evaluation
(Script `scripts/evaluate.py` will be implemented in V1.1 to automate this pipeline using an LLM-as-a-judge approach).
