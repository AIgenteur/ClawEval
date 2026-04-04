# 🟢 Gemma-4 Local Benchmarks on RTX 3090 (24GB VRAM)

[← Back to Main Results](../README.md) · [Full Detailed Results →](../RESULTS.md)

Using `Q4_K_M` variations of the new Gemma-4 (or Griffin/Gemma 3) models from Unsloth.
KV Cache Configuration: `q8_0` (8-bit KV caching for optimized VRAM geometry).
System Specs: Single NVIDIA RTX 3090 (24 GB VRAM).

| Model Size / Architecture | Hugging Face GGUF File | Max Safe Context (Tokens) |
|---|---|---|
| **E2B** (~2B) | `gemma-4-E2B-it-Q4_K_M.gguf` | **131,072** (Trained Native Max) |
| **E4B** (~4B) | `gemma-4-E4B-it-Q4_K_M.gguf` | **131,072** (Trained Native Max) |
| **26B-A4B** (Active 4B MoE) | `gemma-4-26B-A4B-it-UD-Q4_K_M.gguf` | **262,144** (Trained Native Max) |
| **31B** (~31B dense) | `gemma-4-31B-it-Q4_K_M.gguf` | **53,248** (GPU VRAM Ceiling) |

### Context Observations
1. **Unsloth 'Gemma-4' architecture requirement**: The models utilize an architecture `gemma4` which is so new it required a freshly built `llama.cpp` pulled today.
2. **Dense 31B on 24GB VRAM**: The `31B` dense model squeezed an impressive precision boundary of `53,248` tokens total context on a 24GB RTX 3090 using `q8_0` KV cache before issuing a hard OOM error.
3. **Massive MoE Efficiency**: The 26B-A4B architecture allows an effectively "infinite" context for local setups. Because it only caches its small active subsets computationally via Sliding Window Attention (SWA) or MoE routing, it successfully loaded over `260,000` context—smashing right into extreme `llama.cpp` sequence bounds without memory errors.

---

## Benchmark Results

All tests run locally via `llama.cpp` server perfectly controlling reasoning budget using the new OpenAI compliant `reasoning_budget_tokens` and global `max_tokens` settings. E.g. `max_tokens: 16000`, `reasoning_budget_tokens: 8192`.

> 💡 **Standout Gemma-4-E2B Capabilities**: Despite its microscopic 2B size, it scored a perfect 10/10 on the complex **Input Validator** and **Web Scraping** tests across both Phase F and the discriminator Phase G.

| # | Agent Role | Gemma-4-E2B | Gemma-4-E4B | Gemma-4-A4B | Gemma-4-31B |
|---|---|---|---|---|---|
| | **Tier 1 — Utility** | | | | |
| 1 | Router / Triage | 🟢 9 | 🟢 10 | 🟢 10 | 🔴 0 |
| 2 | Input Validator | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 3 | Health Monitor | 🟡 5 | 🟠 5 | 🟠 5 | 🔴 0 |
| 4 | Notification | 🟢 8 | 🟢 8 | 🟢 8 | 🔴 0 |
| 5 | Sentiment | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 6 | FAQ Generation | 🟡 5 | 🟠 5 | 🟠 5 | 🔴 0 |
| 7 | Translation | 🟢 9 | 🟢 10 | 🟢 9 | 🔴 0 |
| 8 | Calendar | 🔴 0 | 🔴 0 | 🔴 0 | 🔴 0 |
| | **Tier 2 — Moderate** | | | | |
| 9 | Research Agent | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 10 | Content Writer | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 11 | Editor | 🟢 9 | 🟡 7 | 🔴 0 | 🔴 0 |
| 12 | Content Planner | 🟢 10 | 🟢 10 | 🔴 0 | 🟢 10 |
| 13 | Email Drafting | 🟢 8 | 🟢 8 | 🟢 9 | 🔴 0 |
| 14 | Doc Summary | 🟢 10 | 🟢 10 | 🟢 8 | 🔴 0 |
| 15 | Meeting Notes | 🟢 9 | 🟢 9 | 🟢 9 | 🔴 0 |
| 16 | Social Scouting | 🟢 10 | 🟢 19 | 🟢 19 | 🔴 0 |
| 17 | Social Content | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 18 | News Aggregation | 🟢 10 | 🟢 10 | 🟠 5 | 🔴 0 |
| 19 | Shopping | 🟢 10 | 🟢 8 | 🟢 8 | 🔴 0 |
| 20 | Memory Mgmt | 🟢 9 | 🟢 8 | 🟢 9 | 🔴 0 |
| 21 | RAG / Retrieval | 🟡 6 | 🟡 6 | 🟠 4 | 🔴 0 |
| 22 | Data Analysis | 🔴 0 | 🔴 1 | 🔴 0 | 🔴 0 |
| 23 | Web Scraping | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 24 | Image Description | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 25 | Customer Support | 🟢 10 | 🟢 9 | 🟢 10 | 🔴 0 |
| 26 | Lead Scoring | 🟢 8 | 🟢 8 | 🟢 8 | 🔴 0 |
| 27 | Sprint Summary | 🟢 10 | 🟢 9 | 🟢 10 | 🔴 0 |
| 28 | Transaction | 🟢 10 | 🟢 9 | 🟢 9 | 🔴 0 |
| 29 | Home Automation | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 30 | Fitness Tracking | 🟢 9 | 🟢 9 | 🟢 9 | 🔴 0 |
| 31 | Recipe / Cooking | 🔴 2 | 🔴 2 | 🔴 2 | 🔴 0 |
| 32 | Personal Finance | 🟡 6 | 🟠 5 | 🟡 7 | 🔴 0 |
| 33 | SEO Optimization | 🟢 9 | 🟢 9 | 🟢 9 | 🔴 0 |
| 34 | Landing Page | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 35 | Travel Planning | 🟢 8 | 🟢 9 | 🔴 0 | 🔴 0 |
| | **Tier 3 — Advanced** | | | | |
| 36 | Code Generation | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 37 | Code Review | 🟢 10 | 🟢 8 | 🟢 10 | 🔴 0 |
| 38 | QA / Test Writing | 🟢 8 | 🟢 10 | 🟢 8 | 🔴 0 |
| 39 | Task Planning | 🟢 9 | 🟢 8 | 🟢 9 | 🔴 0 |
| 40 | Fact-Checking | 🟢 10 | 🟡 7 | 🟢 10 | 🔴 0 |
| 41 | Critic / Review | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 42 | Market Research | 🟢 8 | 🟡 6 | 🟡 6 | 🔴 0 |
| 43 | Synthesizer | 🟢 9 | 🟢 9 | 🟢 9 | 🔴 0 |
| 44 | Curriculum Design | 🟡 6 | 🟡 6 | 🟡 6 | 🔴 0 |
| 45 | Prototype Gen | 🟡 5 | 🟡 7 | 🟠 5 | 🔴 0 |
| 46 | DevOps | 🟢 9 | 🟢 9 | 🟢 9 | 🔴 0 |
| | **Tier 4 — Expert** | | | | |
| 47 | Math / Logic | 🟡 6 | 🟢 8 | 🔴 0 | 🔴 0 |
| 48 | STEM Analysis | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 49 | Algorithm | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| | **Tier 5 — Senior** | | | | |
| 50 | Orchestrator | 🟢 8 | 🟢 8 | 🟢 8 | 🔴 0 |
| 51 | Architect | 🟢 9 | 🟢 10 | 🟢 9 | 🔴 0 |
| 52 | Debugger | 🟢 10 | 🟢 10 | 🟢 8 | 🔴 0 |
| 53 | Legal Review | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 54 | Medical | 🟢 10 | 🟢 9 | 🟢 9 | 🔴 0 |
| 55 | Financial | 🟡 6 | 🟡 6 | 🟡 6 | 🔴 0 |
| 56 | Security | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 |
| 57 | SRE / Incident | 🟡 7 | 🟡 6 | 🔴 3 | 🔴 0 |
| 58 | Book Writing | 📝 5 | 📝 5 | 📝 5 | 📝 0 |
| 59 | Compliance | 🟡 7 | 🟢 8 | 🟢 9 | 🔴 0 |
| | **TOTAL (Phase F)** | **461 (78%)** | **468 (79%)** | **428 (73%)** | **478 (81%)** |

> 📝 Manual review tests default to 5/10 pending review.

---

### Phase G (Discriminator Tests)

| Model | Phase G Score | Notes |
|---|---|---|
| **Gemma-4-E2B** | **74/110 (67%)** | Perfect 10s on Input Validator and Web Scraping. Struggles hard on Content Planner (1/10) and Algorithm drops to 3/10. Phenomenal overall given 2B sizing. ~140-160 t/s locally on RTX 3090. |
| **Gemma-4-E4B** | **78/110 (71%)** | Huge jump in Algorithm / Data Structure tests (9/10 up from E2B's 3/10). Retains perfect 10/10 on Input Validator. Consistent ~100-115 t/s locally. |
| **Gemma-4-26B-A4B** | **23/110 (21%)** | ⚠️ Severely impacted by `llama.cpp` MoE reasoning loop bug — 8/11 tests hit 32K token ceiling with blank output. Tests that completed show high capability: Algorithm 10/10, Orchestrator 7/10, Research 6/10. ~54-65 t/s on RTX 3090. |
| **Gemma-4-31B** | **76/110 (69%)** | Perfect 10s on Input Validator, Fact-Checking, Algorithm, and Web Scraping! Extremely stable dense architecture, completely immune to the MoE looping bugs. Very reliable logic limits. Generates at ~15 t/s locally on RTX 3090. |

