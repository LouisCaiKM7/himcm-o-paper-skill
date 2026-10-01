# Audit and repair protocol

## 1. Reconstruct before judging

Do not begin from the author's correction list. Independently reconstruct:

- prompt requirements and applicable rules;
- current model identities and component interfaces;
- data/parameter provenance;
- headline results and their run IDs;
- claim ownership;
- final PDF structure and deliverables.

Then compare the reconstruction with what the paper says.

## 2. Audit passes

### Pass A — prompt and rules

- Every subquestion answered explicitly?
- Requested stakeholder artifact present and usable?
- Correct population, time, geography, units, and scenario?
- Correct year's page, anonymity, header, file, citation, and AI rules?
- Historical source cutoff respected?

### Pass B — model validity

- Objective/metric matches the decision contract?
- Variables and system boundary mean what the prose says?
- Proxy/substitution registered and tested?
- Assumptions sufficient and directionally analyzed?
- Likelihood/data-generating process valid?
- Optimization feasibility/bounds/claims valid?
- Multiple changed inputs protected from causal over-attribution?

### Pass C — implementation and results

- Code implements the stated equations/algorithm?
- Indexing, signs, units, denominators, and aggregation correct?
- Solver/run complete and official result unambiguous?
- Output overwritten or scenario files mixed?
- Independent recomputation agrees?

### Pass D — continuity

Compare model cards, code, results, tables, figures, captions, abstract, body, conclusion, and requested communication. Search for old model IDs, obsolete numbers/equations, stale figure labels, and contradictory recommendations.

Trace integers as well as decimals. Scan relation/quantifier words in context.

### Pass E — uncertainty and decision

- Validation capable of failing?
- Sensitivity can change the recommendation?
- Structural uncertainty considered?
- Limitations say how the answer could move?
- Recommendation conditional where evidence is conditional?

### Pass F — rendered artifact

Inspect the final PDF, not only source. Verify physical page spans, clipping, glyphs, tables/plots, headers, anonymity, citations, references, and visual consistency.

## 3. Finding format

For each finding record:

```text
ID and severity
Exact location/artifact
Observed evidence
Why it is wrong or risky
Effect on answer/recommendation
Earliest faulty upstream artifact
Repair and descendants to regenerate
Verification required
Status
```

Separate confirmed errors from plausible risks and optional enhancements.

## 4. Repair order

1. binding rule and prompt interpretation;
2. data/parameter/source;
3. objective/definition/model card;
4. algorithm/code;
5. official run/result contract;
6. independent verification;
7. claim ledger;
8. tables/figures/macros;
9. prose;
10. PDF and readiness report.

Never reverse this order by editing a conclusion first.

## 5. Audit the repair

Repairs are high-risk because they are often authored inside the same faulty frame. After repairing:

- identify every output written by the changed function/script;
- regenerate all descendants;
- compare before/after on intended and invariant quantities;
- run synthetic and real-artifact tests;
- plant a relevant defect to verify the gate;
- have an independent implementation/reviewer examine the repaired claim;
- read the rendered PDF again.

## 6. Completion language

Use:

- `REPAIRED_AND_VERIFIED` only when the current artifact and descendants were checked;
- `PARTIALLY_REPAIRED` when some dependent evidence remains stale;
- `DISCLOSED_LIMITATION` when no justified repair exists and the claim is narrowed;
- `BLOCKED` only when a named external input/authority is required.

Do not use “fixed” for prose-only changes around an invalid model. Do not use “unfixable” for an unattempted method.

## 7. Handoff

The handoff must tell the next agent what is current, not preserve the audit chronology. Include:

- direct answers to every requirement;
- model architecture and IDs;
- defects repaired and why;
- exact reproduction order;
- verification/gate coverage;
- current hashes/page count;
- remaining limitations and blockers;
- transferable lessons without case-specific numbers in the reusable skill.

