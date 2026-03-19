# 🔵 64–96GB VRAM — GPT-OSS-120B vs Qwen3.5-122B vs Nemotron-3-Super-120B vs Mistral-Small-4-119B

[← Back to Main Results](../README.md) · [Full Detailed Results →](../RESULTS.md)

| # | Agent Role | GPT-OSS-120B Med | 122B Think 16K | Nemotron-3-Super-120B-A12B Think | Nemotron-3-Super-120B-A12B NoThink | Mistral-Small-4-119B Med |
|---|---|---|---|---|---|---|
| | | GPT-OSS-120B · GGUF · llama.cpp | Qwen3.5-122B-A10B · NVFP4 · SGLang | Nemotron-3-Super-120B · NVFP4 · SGLang | Nemotron-3-Super-120B · NVFP4 · SGLang | Mistral-Small-4-119B · NVFP4 · vLLM |
| | **Tier 1 — Utility** | | | | | |
| 1 | Router / Triage | 🟢 9 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 2 | Input Validator | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 3 | Health Monitor | 🟢 8 | 🔴 3 | 🟡 5 | 🔴 0 | 🔴 3 |
| 4 | Notification | 🟢 9 | 🟢 8 | 🟢 9 | 🟢 9 | 🟡 7 |
| 5 | Sentiment | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 6 | FAQ Generation | 🟡 5 | 🟡 5 | 🟢 8 | 🟡 6 | 🟡 7 |
| 7 | Translation | 🟢 9 | 🟢 10 | 🟡 7 | 🟡 5 | 🟢 9 |
| 8 | Calendar | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 |
| | **Tier 2 — Moderate** | | | | | |
| 9 | Research Agent | 🟢 9 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 10 | Content Writer | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 11 | Editor | 🟢 9 | 🟡 7 | 🟢 9 | 🟢 9 | 🟢 9 |
| 12 | Content Planner | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 13 | Email Drafting | 🟢 9 | 🟢 8 | 🟢 9 | 🟢 8 | 🟢 8 |
| 14 | Doc Summary | 🟢 10 | 🟢 8 | 🟢 10 | 🟢 10 | 🟢 10 |
| 15 | Meeting Notes | 🟢 8 | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 16 | Social Scouting | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 17 | Social Content | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 18 | News Aggregation | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 19 | Shopping | 🟢 8 | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 4 |
| 20 | Memory Mgmt | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 21 | RAG / Retrieval | 🟡 6 | 🟡 6 | 🟡 6 | 🟡 6 | 🔴 2 |
| 22 | Data Analysis | 🔴 2 | 🔴 2 | 🔴 2 | 🔴 2 | 🔴 2 |
| 23 | Web Scraping | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 24 | Image Description | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 25 | Customer Support | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 26 | Lead Scoring | 🟢 8 | 🟢 8 | 🟢 10 | 🟢 8 | 🟢 10 |
| 27 | Sprint Summary | 🟢 9 | 🟢 10 | 🟢 9 | 🟢 8 | 🔴 4 |
| 28 | Transaction | 🟢 10 | 🟢 10 | 🟢 9 | 🟢 9 | 🟡 6 |
| 29 | Home Automation | 🟢 9 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 |
| 30 | Fitness Tracking | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 8 |
| 31 | Recipe / Cooking | 🟢 9 | 🔴 2 | 🔴 2 | 🟢 9 | 🟢 9 |
| 32 | Personal Finance | 🟡 5 | 🟡 7 | 🟡 6 | 🟡 7 | 🔴 4 |
| 33 | SEO Optimization | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 | 🟢 9 |
| 34 | Landing Page | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 35 | Travel Planning | 🟡 7 | 🟢 8 | 🟢 10 | 🟢 9 | 🟢 9 |
| | **Tier 3 — Advanced** | | | | | |
| 36 | Code Generation | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 37 | Code Review | 🟢 8 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 38 | QA / Test Writing | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 |
| 39 | Task Planning | 🟢 9 | 🟢 9 | 🟢 10 | 🟢 9 | 🟢 10 |
| 40 | Fact-Checking | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 |
| 41 | Critic / Review | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 42 | Market Research | 🔴 4 | 🔴 0 | 🟢 8 | 🟢 9 | 🟡 6 |
| 43 | Synthesizer | 🟢 10 | 🟡 7 | 🟢 9 | 🟢 9 | 🟢 9 |
| 44 | Curriculum Design | 🟡 7 | 🟡 6 | 🟡 6 | 🟡 5 | 🟡 7 |
| 45 | Prototype Gen | 🟡 5 | 🟡 6 | 🟡 6 | 🟡 5 | 🟡 5 |
| 46 | DevOps | 🟢 10 | 🟡 7 | 🟢 9 | 🟢 10 | 🟢 9 |
| | **Tier 4 — Expert** | | | | | |
| 47 | Math / Logic | 🟢 8 | 🟡 6 | 🟢 8 | 🟡 6 | 🔴 2 |
| 48 | STEM Analysis | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 49 | Algorithm | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| | **Tier 5 — Senior** | | | | | |
| 50 | Orchestrator | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 |
| 51 | Architect | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 | 🟢 10 |
| 52 | Debugger | 🟢 10 | 🟢 10 | 🟢 8 | 🟢 8 | 🟢 10 |
| 53 | Legal Review | 🟢 9 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 54 | Medical | 🟢 9 | 🟡 7 | 🟢 9 | 🟢 10 | 🟢 10 |
| 55 | Financial | 🟢 10 | 🟢 10 | 🟡 6 | 🟡 6 | 🟢 10 |
| 56 | Security | 🟢 10 | 🟡 6 | 🟢 10 | 🟢 10 | 🟢 10 |
| 57 | SRE / Incident | 🟡 6 | 🟡 6 | 🔴 3 | 🔴 4 | 🟡 6 |
| 58 | Book Writing | 📝 5 | 📝 5 | 📝 5 | 📝 5 | 📝 5 |
| 59 | Compliance | 🟢 8 | 🟡 7 | 🟢 8 | 🟢 8 | 🟢 9 |
| | **TOTAL** | **484/590 (82.0%)** | **~439/590 (74.4%)** | **482/590 (81.7%)** | **474/590 (80.3%)** | **464/590 (78.6%)** |

### Notes

- **GPT-OSS-120B** tested at 3 reasoning levels (low/medium/high). Medium shown above as it scored highest overall (484/590 = 82.0%)
- **GPT-OSS-120B** runs on llama-server with GGUF weights (~61GB). Tool calling: 9/10 (90%)
- **Qwen3.5-122B-A10B** runs on SGLang with NVFP4 and 16K thinking budget
- **Nemotron-3-Super-120B-A12B** is a hybrid SSM/Transformer (Mamba) architecture, 69.7 GB model, runs on SGLang with NVFP4, 262K context
- **Mistral-Small-4-119B** tested at 3 reasoning_effort levels (low/medium/high). Medium shown above as it scored highest overall (464/590 = 78.6%). Runs on vLLM with NVFP4
- Nemotron-3-Super-120B-A12B Think excels on: Travel (10), Market Research (8), Task Planning (10), Lead Scoring (10)
- Mistral-Small-4-119B excels on: Lead Scoring (10), Compliance (9), Financial (10), Medical (10), Debugger (10)
- Mistral struggles on: Shopping (4), RAG (2), Math/Logic (2), Sprint Summary (4), Personal Finance (4)

### 122B NoThink (Phase G only)

The 122B was also tested **without thinking** on 11 harder Phase G discriminator tests, scoring **87/110 (79%)** — the best single-config local score before Nemotron. See [Phase G results](results-phase-g.md) for the full comparison.
