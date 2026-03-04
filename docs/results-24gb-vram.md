# 🟢 24GB VRAM — Think vs NoThink Comparison

[← Back to Main Results](../README.md) · [Full Detailed Results →](../RESULTS.md)

All tested with Q4_K_M quantization, KV cache q8_0, on llama.cpp (RTX 3090 / RTX 4090).

| # | Agent Role | 35B-A3B Think | 35B-A3B NoThink | 27B Think | 27B NoThink |
|---|---|---|---|---|---|
| | **Tier 1 — Utility** | | | | |
| 1 | Router / Triage | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 |
| 2 | Input Validator | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 3 | Health Monitor | ⬛ 0 | 🔴 3 | ⬛ 0 | 🔴 3 |
| 4 | Notification | 🟢 8 | 🟢 8 | 🟢 9 | 🟢 8 |
| 5 | Sentiment | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 6 | FAQ Generation | 🟡 6 | 🟡 6 | 🟢 8 | 🟡 6 |
| 7 | Translation | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 10 |
| 8 | Calendar | 🔴 0 | 🔴 0 | ⬛ 0 | 🔴 0 |
| | **Tier 2 — Moderate** | | | | |
| 9 | Research Agent | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 10 | Content Writer | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 11 | Editor | 🟢 9 | 🟢 10 | 🟢 9 | 🟢 10 |
| 12 | Content Planner | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 13 | Email Drafting | ⬛ 0 | 🟢 10 | 🟢 9 | 🟢 10 |
| 14 | Doc Summary | 🟢 8 | 🟢 10 | 🟢 8 | 🟢 10 |
| 15 | Meeting Notes | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 16 | Social Scouting | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 17 | Social Content | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 18 | News Aggregation | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 19 | Shopping | 🟢 10 | 🔴 4 | 🟢 10 | 🔴 4 |
| 20 | Memory Mgmt | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 21 | RAG / Retrieval | 🟡 6 | 🔴 4 | 🟡 6 | 🟡 6 |
| 22 | Data Analysis | 🔴 2 | 🔴 3 | 🔴 2 | 🔴 3 |
| 23 | Web Scraping | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 24 | Image Description | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 25 | Customer Support | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 |
| 26 | Lead Scoring | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 10 |
| 27 | Sprint Summary | ⬛ 0 | 🟡 5 | ⬛ 0 | 🟡 7 |
| 28 | Transaction | 🟢 10 | 🟢 9 | 🟢 10 | 🟢 8 |
| 29 | Home Automation | 🟢 10 | 🟢 9 | 🟢 10 | 🟢 9 |
| 30 | Fitness Tracking | 🟢 9 | 🟡 7 | 🟢 9 | 🟢 9 |
| 31 | Recipe / Cooking | 🟢 10 | 🟢 9 | 🔴 2 | 🔴 2 |
| 32 | Personal Finance | ⬛ 0 | 🔴 4 | 🟡 7 | 🔴 4 |
| 33 | SEO Optimization | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 34 | Landing Page | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 35 | Travel Planning | 🔴 0 | 🟡 7 | ⬛ 0 | 🟡 7 |
| | **Tier 3 — Advanced** | | | | |
| 36 | Code Generation | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 37 | Code Review | 🟢 8 | 🟢 10 | 🟢 10 | 🟢 8 |
| 38 | QA / Test Writing | 🟢 8 | 🟢 10 | 🟢 8 | 🟢 8 |
| 39 | Task Planning | 🟢 9 | 🟢 10 | 🟢 9 | 🟢 9 |
| 40 | Fact-Checking | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 41 | Critic / Review | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 42 | Market Research | ⬛ 0 | 🟡 7 | 🟡 6 | 🟢 8 |
| 43 | Synthesizer | 🟢 9 | 🟢 9 | 🟢 9 | 🟡 7 |
| 44 | Curriculum Design | 🟡 6 | 🟡 6 | 🟡 6 | 🟡 5 |
| 45 | Prototype Gen | 🟡 6 | 🟡 6 | 🟡 5 | 🟡 6 |
| 46 | DevOps | 🟢 10 | 🟢 9 | 🟢 9 | 🟢 10 |
| | **Tier 4 — Expert** | | | | |
| 47 | Math / Logic | 🟡 6 | 🔴 4 | 🟡 6 | 🔴 4 |
| 48 | STEM Analysis | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 49 | Algorithm | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| | **Tier 5 — Senior** | | | | |
| 50 | Orchestrator | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 |
| 51 | Architect | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 52 | Debugger | 🟢 8 | 🟢 10 | ⬛ 0 | 🟢 8 |
| 53 | Legal Review | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 54 | Medical | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 55 | Financial | 🟢 10 | 🟢 10 | 🟡 6 | 🟢 10 |
| 56 | Security | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 57 | SRE / Incident | 🟡 7 | 🔴 3 | 🔴 3 | 🟡 6 |
| 58 | Book Writing | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 59 | Compliance | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 9 |

### Notes

- ⬛ **Thinking overflow:** llama.cpp has no `thinking_budget`, so thinking models can consume all tokens on reasoning before outputting an answer. 35B-Think: 5 overflows (#3, #13, #27, #32, #42), 27B-Think: 3 overflows (#3, #8, #27). These scores would be higher on vLLM/SGLang with proper budget control.
- 📝 Manual review tests default to 5/10 pending human review
- 🔄 **Think vs NoThink tradeoffs:** Thinking helps on Shopping (10 vs 4), Math/Logic (6 vs 4), and RAG (6 vs 4). NoThink avoids overthinking on Recipe (9 vs 0), Market Research (7 vs 0), and Travel (7 vs 0)
- **27B dense vs 35B MoE (both nothink):** Very close overall. 27B beats 35B on RAG (6 vs 4), Lead Scoring (10 vs 8), SRE (6 vs 3), Market Research (8 vs 7). 35B wins on Recipe (9 vs 2), Code Review (10 vs 8), QA (10 vs 8)

### Phase G — Harder Discriminator Tests

Many roles above show identical scores (10/10) across models. [Phase G tests](results-phase-g.md) use harder prompts to differentiate:
- **27B NoThink: 83/110 (75%)** — best at Code Gen (10/10) and Fact-Checking (10/10)
- **35B Think: 51/60 (85%)** on 6 completed tests — Content Planner 8/10 is unique (all NoThink score 1)
- **35B NoThink: 77/110 (70%)**
