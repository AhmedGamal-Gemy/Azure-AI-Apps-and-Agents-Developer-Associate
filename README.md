# AI-103 Cert Prep — Azure AI Apps and Agents Developer Associate

> **Microsoft Certified: Azure AI Apps and Agents Developer Associate (Beta)**
> Exam code: AI-103 | Passing score: 700/1000 | Duration: 120 min
> **Voucher deadline: 18 August 2026** | Target exam date: 14–16 Aug 2026

## ⚠️ Important

- Register with a **personal MSA account** — not your work/school AAD account
- Practice Assessment not available yet (beta) — use mscertquiz.com + Udemy practice tests
- Exam has **interactive components** — the labs in this repo are exam prep, not optional

---

## Progress

### Learning Paths

| Path | Title | Hours | Modules | Branch | Status |
|------|-------|-------|---------|--------|--------|
| 1 | Develop Generative AI Apps in Azure | 6h 52m | 6 | `path/01-generative-ai-apps` | ⬜ |
| 2 | Develop AI Agents on Azure | 9h 52m | 9 | `path/02-ai-agents` | ⬜ |
| 3 | Develop Natural Language Solutions in Azure | 5h 46m | 7 | `path/03-natural-language` | ⬜ |
| 4 | Extract Insights from Visual Data on Azure | 7h 06m | 8 | `path/04-visual-data` | ⬜ |
| — | Final Review | — | — | `review/final` | ⬜ |

**Total: ~29h 30min across 30 modules**

**Status keys:** ⬜ not started · 🔄 in progress · ✅ merged to main

---

### Domain Weights

| Domain | Topic | Weight |
|--------|-------|--------|
| 1 | Plan and manage an Azure AI solution | 10–15% |
| 2 | Implement generative AI and agentic solutions | 35–40% |
| 3 | Implement computer vision solutions | 15–20% |
| 4 | Implement text analysis solutions | 15–20% |
| 5 | Implement information extraction solutions | 10–15% |

---

## Repo Structure

```
ai103-cert-prep/
├── README.md
├── tracker.md              # daily log + practice Q scores
├── cheatsheet.md           # built in Week 8, one page per domain
└── path-01/
    ├── notes/
    │   ├── 01-foundry-setup.md
    │   └── 02-prompt-engineering.md
    ├── labs/
    │   ├── deploy_model.py
    │   └── prompt_flow_basic/
    └── practice-qs.md      # questions + your answers + correct answers
```

---

## Branching Rules

- One branch per learning path: `path/01` → `path/04`
- Merge to `main` only when: notes + labs + practice-qs.md all committed
- `review/final` branch created in Week 7 — weak spots, mock scores, cheatsheet

## Commit Convention

```
feat:   add path01 module02 prompt engineering notes
lab:    deploy gpt-4o-mini via foundry sdk
fix:    correct chunking strategy notes in path02
review: add mock exam 1 score + wrong answers
```

---

## Weekly Study Plan

| Week | Book Path | Cert Focus | Key Lab | Dates |
|------|-----------|------------|---------|-------|
| 1 | Path 1 (mod 1–3) | Domain 1 — plan & manage | Deploy GPT-4o-mini, content filters | 22–28 Jun |
| 2 | Path 1 (mod 4–6) | Domain 2 — gen AI, Prompt Flow | Build Prompt Flow + eval node | 29 Jun–5 Jul |
| 3 | Path 2 (mod 1–5) | Domain 2 — agents, function calling | Foundry agent + 2 custom tools | 6–12 Jul |
| 4 | Path 2 (mod 6–9) | Domain 2 — RAG, AI Search | Full RAG pipeline | 13–19 Jul |
| 5 | Path 2 finish + Path 3 start | Domain 2 — multi-agent, eval runs | LLM-as-judge eval run | 20–26 Jul |
| 6 | Path 3 finish | Domain 4 — NLP, CLU, Speech | CLU project + Speech SDK | 27 Jul–2 Aug |
| 7 | Path 4 | Domain 3 + 5 — vision, doc intel | Doc Intelligence vs Content Understanding | 3–9 Aug |
| 8 | Review only | All domains — weak spots | Cheatsheet, mock exam 2 | 10–18 Aug |

---

## Mock Exam Log

| # | Date | Score | Weak Domains | Notes |
|---|------|-------|-------------|-------|
| 1 | (Sat Week 7) | — | — | — |
| 2 | (Mon Week 8) | — | — | — |

---

## Key Traps to Watch

- **Doc Intelligence vs Content Understanding** — know when to use each
- **PTUs vs PAYG** — provisioned throughput vs consumption billing
- **AI Search tier selection** — semantic ranker availability per tier
- **Private endpoints + CMK encryption** — compliance scenario questions
- **CLU vs LUIS** — LUIS is retired, CLU is the replacement

---

*Morning slot: 6:45–9:50 daily (Sun–Thu) · Sat: full mock exam (Week 7+)*