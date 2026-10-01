# HiMCM Outstanding-Paper Skill

An evidence-first, model-agnostic skill for building, resuming, auditing, and repairing HiMCM mathematical-modelling papers. It is designed to help a capable team produce an **Outstanding-ready** submission: coherent, decision-complete, reproducible, honestly scoped, and compliant with the applicable contest-year rules.

“Outstanding-ready” is a quality standard, not an award prediction. No prompt or checklist can guarantee an award.

## What makes this different

This repository is not a winning-paper template and not a collection of fashionable model names. It treats a paper as a traceable system:

```text
problem + rules -> decision contract -> model card -> data/code/run
-> result contract -> claim ledger -> figures/tables -> paper -> PDF
```

The workflow was distilled from complete builds and adversarial repairs across many HiMCM problems. The recurring failures were not mostly algebra mistakes. They were silent substitutions, mismatched populations or units, stale model generations, invalid statistical likelihoods, unsupported causal language, local plateaus mistaken for limits, and green validators that had inspected nothing. The skill therefore emphasizes production constraints and independent checks, not self-scoring.

## Contents

- `SKILL.md` — portable entry point and operating contract.
- `references/` — detailed guidance loaded only when relevant.
- `templates/` — machine-readable contracts for rules, inputs, requirements, sources, models, runs, results, claims, and handoff, plus a universal starter prompt.
- `scripts/check_skill.py` — validates this skill package.
- `scripts/check_project.py` — checks whether a paper project has the core evidence chain.
- `tests/` — regression tests and a minimal valid fixture.

## Use with any AI

The skill is plain Markdown and JSON. The AI needs filesystem access to execute the full workflow; a chat-only model can use the reasoning guidance but must not claim that code, sources, or PDFs were verified when it could not inspect them.

### Codex

Clone or copy this repository to:

```text
~/.codex/skills/himcm-o-paper/
```

Then invoke `$himcm-o-paper` or ask Codex to build/audit a HiMCM paper.

### Claude Code

Clone or copy it to:

```text
~/.claude/skills/himcm-o-paper/
```

Ask Claude to read `SKILL.md` before acting.

### DeepSeek or another coding agent

Place the folder in the agent's skill directory if it supports skills. Otherwise attach the repository, tell the agent to read `SKILL.md`, and use [`templates/UNIVERSAL_PROMPT.md`](templates/UNIVERSAL_PROMPT.md).

### Chat-only AI

Upload `SKILL.md` and only the references needed for the current stage. Ask for planning, critique, or a draft. Treat all execution-dependent claims as `NOT_VERIFIED` until a tool-enabled agent runs the code and checks the PDF.

## Quick start

1. Put the problem statement and all supplied attachments in `problem_files/`.
2. Copy [`templates/UNIVERSAL_PROMPT.md`](templates/UNIVERSAL_PROMPT.md) into the agent.
3. Require the agent to create the contracts in `templates/` before writing the paper.
4. Require a LaTeX-to-PDF build, independent recomputation, rendered-page inspection, and a final handoff.

Validate this repository:

```text
python scripts/check_skill.py .
python -m unittest discover -s tests -v
```

The same checks run on every push and pull request through GitHub Actions. The tests include a known-defect mutation so the package gate is observed failing, plus valid and invalid paper-project fixtures.

Validate a paper project:

```text
python scripts/check_project.py path/to/project
```

## Boundaries

- The official problem statement and the applicable year's official rules outrank this skill.
- Historical papers are examples, never answer keys or sources of unstated assumptions.
- The workflow is LaTeX-to-PDF only. It does not require or create DOCX files.
- Raw private session archives, unpublished student work, credentials, and personal information must never be copied into a public project.
- Use only sources and AI assistance allowed by the contest rules in force for the target year.

Licensed under the MIT License.
