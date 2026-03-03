# 🔴 Small VRAM Models — Phase F (59-Role Evaluation)

[← Back to Main Results](../README.md) · [Phase G Discriminator Tests →](results-phase-g.md)

All tested with Q4_K_M quantization, KV cache q8_0, on llama.cpp (local server).

🟢 = 8-10 &nbsp; 🟡 = 5-7 &nbsp; 🔴 = 0-4 &nbsp; 📝 = Manual review (5)

| # | Agent Role | 0.8B Think | 0.8B NT | 2B Think | 2B NT | 4B Think | 4B NT | 9B Think | 9B NT |
|---|---|---|---|---|---|---|---|---|---|
| | | Qwen3.5-0.8B | Qwen3.5-0.8B | Qwen3.5-2B | Qwen3.5-2B | Qwen3.5-4B | Qwen3.5-4B | Qwen3.5-9B | Qwen3.5-9B |
| | **Tier 1 — Utility** | | | | | | | | |
| 1 | Router / Triage | 🟡 7 | 🟡 7 | — | — | — | — | — | — |
| 2 | Input Validator | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 3 | Health Monitor | 🔴 2 | 🔴 3 | — | — | — | — | — | — |
| 4 | Notification | 🟡 6 | 🟡 6 | — | — | — | — | — | — |
| 5 | Sentiment | 🟡 6 | 🔴 4 | — | — | — | — | — | — |
| 6 | FAQ Generation | 🔴 1 | 🔴 3 | — | — | — | — | — | — |
| 7 | Translation | 🟡 7 | 🟢 9 | — | — | — | — | — | — |
| 8 | Calendar | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| | **Tier 2 — Moderate** | | | | | | | | |
| 9 | Research Agent | 🟡 6 | 🟡 6 | — | — | — | — | — | — |
| 10 | Content Writer | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 11 | Editor | 🟡 7 | 🟡 7 | — | — | — | — | — | — |
| 12 | Content Planner | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 13 | Email Drafting | 🟡 6 | 🔴 4 | — | — | — | — | — | — |
| 14 | Doc Summary | 🟡 6 | 🟢 8 | — | — | — | — | — | — |
| 15 | Meeting Notes | 🟢 9 | 🟢 9 | — | — | — | — | — | — |
| 16 | Social Scouting | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 17 | Social Content | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 18 | News Aggregation | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 19 | Shopping | 🔴 4 | 🔴 2 | — | — | — | — | — | — |
| 20 | Memory Mgmt | 🟢 9 | 🟢 9 | — | — | — | — | — | — |
| 21 | RAG / Retrieval | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 22 | Data Analysis | 🔴 1 | 🔴 0 | — | — | — | — | — | — |
| 23 | Web Scraping | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 24 | Image Description | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 25 | Customer Support | 🟡 6 | 🟡 6 | — | — | — | — | — | — |
| 26 | Lead Scoring | 🔴 2 | 🔴 2 | — | — | — | — | — | — |
| 27 | Sprint Summary | 🔴 2 | 🔴 2 | — | — | — | — | — | — |
| 28 | Transaction | 🔴 1 | 🔴 1 | — | — | — | — | — | — |
| 29 | Home Automation | 🟡 7 | 🟢 10 | — | — | — | — | — | — |
| 30 | Fitness Tracking | 🔴 3 | 🔴 3 | — | — | — | — | — | — |
| 31 | Recipe / Cooking | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 32 | Personal Finance | 🔴 3 | 🔴 3 | — | — | — | — | — | — |
| 33 | SEO Optimization | 🟢 9 | 🟢 9 | — | — | — | — | — | — |
| 34 | Landing Page | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 35 | Travel Planning | 🔴 4 | 🔴 4 | — | — | — | — | — | — |
| | **Tier 3 — Advanced** | | | | | | | | |
| 36 | Code Generation | 🟢 8 | 🟢 8 | — | — | — | — | — | — |
| 37 | Code Review | 🟢 8 | 🟢 10 | — | — | — | — | — | — |
| 38 | QA / Test Writing | 🟢 8 | 🟢 8 | — | — | — | — | — | — |
| 39 | Task Planning | 🟢 9 | 🟡 7 | — | — | — | — | — | — |
| 40 | Fact-Checking | 🟡 5 | 🔴 4 | — | — | — | — | — | — |
| 41 | Critic / Review | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 42 | Market Research | 🔴 4 | 🔴 4 | — | — | — | — | — | — |
| 43 | Synthesizer | 🟢 9 | 🟢 9 | — | — | — | — | — | — |
| 44 | Curriculum Design | 🔴 4 | 🔴 4 | — | — | — | — | — | — |
| 45 | Prototype Gen | 🟡 7 | 🔴 2 | — | — | — | — | — | — |
| 46 | DevOps | 🟢 10 | 🟢 9 | — | — | — | — | — | — |
| | **Tier 4 — Expert** | | | | | | | | |
| 47 | Math / Logic | 🔴 2 | 🔴 2 | — | — | — | — | — | — |
| 48 | STEM Analysis | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 49 | Algorithm | 🟡 5 | 🔴 0 | — | — | — | — | — | — |
| | **Tier 5 — Senior** | | | | | | | | |
| 50 | Orchestrator | 🟢 8 | 🟢 8 | — | — | — | — | — | — |
| 51 | Architect | 🟢 8 | 🟢 9 | — | — | — | — | — | — |
| 52 | Debugger | 🟡 6 | 🟢 10 | — | — | — | — | — | — |
| 53 | Legal Review | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 54 | Medical | 🟢 10 | 🟢 10 | — | — | — | — | — | — |
| 55 | Financial | 🔴 2 | 🔴 1 | — | — | — | — | — | — |
| 56 | Security | 🟡 6 | 🔴 3 | — | — | — | — | — | — |
| 57 | SRE / Incident | 🔴 2 | 🔴 2 | — | — | — | — | — | — |
| 58 | Book Writing | 📝 5 | 📝 5 | — | — | — | — | — | — |
| 59 | Compliance | 🟢 8 | 🟢 8 | — | — | — | — | — | — |
| | **TOTAL** | **339/585 (58%)** | **331/585 (57%)** | — | — | — | — | — | — |

### Notes

- Social Scouting (#16) scored 16/10 due to scoring bug — capped to 10 in totals above
- STEM (#48) scored 0/5 (not 0/10) — model generated degenerate repetitive output filling the token limit
- Think and NoThink perform nearly identically for 0.8B — the model doesn't produce meaningful chain-of-thought at this size

---

## Phase G — Discriminator Tests (Small Models)

| # | Test | 0.8B Think | 0.8B NT | 2B Think | 2B NT | 4B Think | 4B NT | 9B Think | 9B NT |
|---|------|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 36 | Code Gen (RateLimiter) | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 2 | Input Validator (nested) | 🟡 5 | 🟡 5 | — | — | — | — | — | — |
| 5 | Sentiment (hard, 20 items) | 🔴 2 | 🔴 2 | — | — | — | — | — | — |
| 40 | Fact-Checking (plausible) | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 49 | Algorithm (LRU+TTL) | 🔴 3 | 🔴 3 | — | — | — | — | — | — |
| 51 | Architect (trade-offs) | 🟡 7 | 🟡 7 | — | — | — | — | — | — |
| 48 | STEM (multi-step calc) | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| 9 | Research (contradictions) | 🟢 8 | 🟢 8 | — | — | — | — | — | — |
| 12 | Content Planner (15 constraints) | 🔴 1 | 🔴 1 | — | — | — | — | — | — |
| 50 | Orchestrator (multi-agent) | 🟡 7 | 🟡 7 | — | — | — | — | — | — |
| 23 | Web Scraping (messy HTML) | 🔴 0 | 🔴 0 | — | — | — | — | — | — |
| | **TOTAL** | **33/110 (30%)** | **33/110 (30%)** | — | — | — | — | — | — |

---

## Summary — Best Score Per VRAM Tier

| VRAM | Best Model | Phase F | Phase G |
|------|-----------|:---:|:---:|
| **8GB** | Qwen3.5-0.8B Think | 339/585 (58%) | 33/110 (30%) |
| **12GB** | Qwen3.5-2B / 4B | *testing* | *testing* |
| **16GB** | Qwen3.5-9B | *testing* | *testing* |
| **24GB** | Qwen3.5-35B-A3B NT | 433/590 (73%) | 77/110 (70%) |

---

[← Back to Main Results](../README.md)
