# Writing, LaTeX, and PDF production

## 1. Write the argument, not the workflow history

The contest paper should let a judge answer:

1. What decision/problem is being solved?
2. What evidence and assumptions define it?
3. What model was selected and why?
4. How does it work?
5. What are the quantitative answers?
6. Why should those answers be trusted?
7. What could change them?
8. What should the stakeholder do?

Do not narrate every failed attempt, correction round, internal gate, or skill. Keep rejected alternatives only when they justify the final choice or reveal structural uncertainty.

## 2. Summary Sheet

The Summary Sheet must stand alone and agree with the body. Include:

- the problem/decision in plain language;
- chosen architecture and distinctive insight;
- principal numerical answers in prompt units;
- validation/uncertainty that calibrates trust;
- recommendation and important condition/limitation.

Avoid background padding, undefined acronyms, unsupported superlatives, and unexplained precision. If rules require one physical page, assert it on the rendered PDF.

## 3. Section architecture

Organize around the problem's logic, not a universal chapter count. A common structure is:

- Summary Sheet and keywords if appropriate;
- Table of Contents if required/valuable;
- problem interpretation and requirement map;
- assumptions with reasons and consequences;
- variables/parameters with units and provenance;
- system diagram and model architecture;
- formulation/algorithm;
- results answering each task;
- validation and uncertainty/sensitivity;
- strengths, limitations, conclusion/recommendation;
- requested memo/letter/article/presentation;
- references and appendices according to the year's rules.

Use an explicit final-model statement. Do not make the judge reconstruct which of several models is current.

## 4. Equations and notation

- Define every symbol before or immediately after use.
- State domain, unit, and interpretation.
- Explain why the equation answers the decision.
- Keep notation stable across text, code, tables, and figures.
- Distinguish indices, decisions, states, parameters, observations, and random variables.
- State solver/algorithm when a closed-form equation is not the implementation.

## 5. Evidence-bound prose

Generate model outputs from result contracts into LaTeX macros or complete tables. Avoid hand-typing values.

Generate or verify relational language when possible:

```text
higher/lower, faster/slower, increases/decreases,
best/worst, inside/outside, above/below, meets/fails
```

Every causal word—because, causes, drives, saves, prevents, explains—needs a mechanistic or identified comparison. Otherwise use association/joint-effect language.

Quantifiers must match provenance: one run, representative case, all tested scenarios, Monte Carlo replications, or universal proof are different scopes.

## 6. Tables and figures

Every table/figure must:

- answer a question or support a claim;
- have readable labels, units, legend, and caption;
- state scenario/sample size/provenance where relevant;
- be cited and interpreted in the text;
- use the current model generation;
- avoid decorative duplication of a nearby table.

Validate plot data and geometry separately. Confirm coordinate systems, bar endpoints/widths, baselines, ticks (especially logarithmic), confidence bands, color/greyscale legibility, and reference lines.

Do not draw zero-width sensitivity bars as though they were visible evidence. Report zero effects in prose and explain the active regime.

## 7. LaTeX controls

- Compile directly to PDF; no Word/DOCX stage.
- Generate command names using letters only; TeX control sequences end before digits.
- Use consistent font encoding (for example T1 with a compatible font) and inspect special symbols in the PDF text layer.
- Treat overfull/underfull boxes, unresolved references/citations, missing glyphs, and float placement warnings as an inspection list.
- Keep result generation separate from LaTeX compilation.
- Do not manually edit the final PDF.

## 8. PDF verification

After every meaningful manuscript/artifact change:

1. compile enough passes for references/page totals;
2. fail on LaTeX errors, unresolved references/citations, and forbidden placeholders;
3. confirm PDF freshness against source/generated artifacts;
4. extract the text layer and compare headline values/claims;
5. verify page count, headers, anonymity, font sizes, and named-deliverable page spans;
6. render every page to images;
7. visually inspect equations, tables, figures, captions, page breaks, glyphs, whitespace, references, and transitions.

Text extraction cannot detect clipping or misleading visual geometry. Rendering cannot prove logical field data or numerical provenance. Use both.

## 9. Compression under a page limit

Verify the actual year's page contract before cutting. Compress in this order:

1. remove repeated background and correction history;
2. combine redundant prose/table presentations;
3. shorten captions while keeping scope/units/provenance;
4. improve figure/table layout;
5. move nonessential derivations/code according to allowed appendices;
6. remove analysis only when it does not support a requirement, validation, uncertainty, or decision.

After compression, compare requirement coverage, citations, figures/tables, claims, and model content against the baseline. A shorter PDF that silently loses a required deliverable is a failure.

