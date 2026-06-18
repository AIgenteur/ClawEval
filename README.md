# 🦞 ClawEval — Can Your Local or Cloud LLM Actually Do the Job?

[![AIgenteur](https://img.shields.io/badge/AIgenteur-cofounder%20OSS-e7c14b)](https://github.com/AIgenteur/aigenteur)

**The only deterministic benchmark that tests LLMs as real AI agents** — not trivia, not chat, not vibes. 59 specialized roles. Hard, verifiable tasks. Every score is reproducible. Built for [OpenClaw](https://github.com/AIgenteur/ClawEval), [Hermes Agent](https://github.com/NousResearch/hermes-agent), and any model-agnostic agent framework.

> 🔥 **New models added regularly.** Star ⭐ this repo to get notified when new results drop.
>
> 📬 **[Subscribe to AIgenteur Dispatch](https://aigenteurdispatch.substack.com/)** — benchmark results, local AI guides, and agent workflows in your inbox.
>
> 🎓 **[Join AIgenteur Launchpad (free)](https://www.skool.com/aigenteur-academy-9764)** — community for freelancers and entrepreneurs putting AI agents to work. Want a model tested? Post your request in the community.
>
> 🤖 **Sister project: [AIgenteur](https://github.com/AIgenteur/aigenteur)** — open-source AI cofounder for solopreneurs. ClawEval grades the agents it dispatches.

> 💡 **You'd be surprised** how well some small, fast models handle sub-agent tasks — even on an RTX 3090 (we got ours for $799). Before you rent cloud GPUs, check the scores below.

### Why ClawEval?

Most benchmarks tell you a model is "smart." ClawEval tells you if it can **do the work** — route tickets, review code, analyze financials, draft legal docs, plan sprints, and 54 more agent roles. Each test has an exact expected answer. No LLM-as-judge. No vibes.

**Built for agent frameworks like [OpenClaw](https://github.com/AIgenteur/ClawEval) and [Hermes Agent](https://github.com/NousResearch/hermes-agent)** — any system where you need to pick the right LLM backend for specialized sub-agent roles. If your framework is model-agnostic, ClawEval shows you exactly which model to plug in for each job.

### ⚡ NEW: Token Efficiency Leaderboard

> 🏆 **[Which models waste the fewest tokens? →](docs/results-token-efficiency.md)**
>
> Two models both score 10/10 — but one used 500 tokens, the other 5,000. The efficient one saves **10× on compute, cost, and latency.** We rank 35 models by tokens-per-point. Think modes use 10–20× more tokens for marginal gains. **This metric is hardware-independent.**

### 🚀 NEW: ClawEval v2 — 59 Agents, 1,220 Checkpoints, Zero Ceiling Effects

> 🏆 **[The definitive dense evaluation →](docs/results-phase-h.md)**
>
> Phase F scored x/10 — everyone got 8+. **ClawEval v2 upgrades all 59 agents** to 15–30 checkpoints each with adversarial traps, sarcasm, and near-truths. Real separation, real rankings. **First results (Kimi K2.6, GLM-5.1) dropping now.**

### 🖥️ LOCAL Models — Run on YOUR Hardware

> 📄 **[OpenClaw Backend: Local on 3090 — The Complete Guide (PDF)](docs/OpenClaw_Backend_Local_on_3090.pdf)** — An interactive walkthrough of running the full OpenClaw backend locally on an RTX 3090. Covers setup, model selection, and performance tips with step-by-step calls to action.

We test quantized open-source models that fit on hardware you already own. Find out which model is best for each agent role **before you commit your VRAM.** We're also testing smaller models for max context and usability — even a 16GB GPU can run capable sub-agents.

| 🔴 8GB VRAM | 🟠 12GB VRAM | 🟡 16GB VRAM | 🟢 24GB VRAM | 🔵 64–96GB VRAM |
|---|---|---|---|---|
| Qwen3.5-0.8B Q4_K_M | Qwen3.5-9B Q4_K_M | Qwen3.5-9B Q4_K_M | Qwen3.6-35B-A3B Q4_K_M | Qwen3.5-122B-A10B NVFP4 |
| Qwen3.5-2B Q4_K_M | | | Qwen3.5-35B-A3B Q4_K_M | GPT-OSS-120B GGUF |
| Qwen3.5-4B Q4_K_M (250K ctx) | | | Qwen3.5-27B Q4_K_M | |
| ✅ Tested | ✅ Tested | llama.cpp | llama.cpp · SGLang · vLLM | SGLang · vLLM · llama.cpp |

> 📖 **VRAM Guides:** [8–16GB Small Models](docs/results-small-vram.md) · [16GB](docs/OpenClaw%2016GB%20VRAM%20Local%20LLM%20Subagents.md) · [24GB](docs/The%2024GB%20VRAM%20Tier_%20Where%20Local%20AI%20Agents%20Get%20Serious.md) · [32GB](docs/openclaw-model-selection-32gb-tier.md) · [48GB](docs/openclaw-48gb-tier.md) · [64GB](docs/openclaw-64gb-tier.md) · [96GB](docs/openclaw-96gb-tier.md) — Which models fit, context limits, speed estimates

#### 🧩 Which Tested Models Fit on Your Hardware?

No discrete GPU? Unified-memory devices can run these models directly. Estimates are **conservative** — they account for OS overhead (~4–8 GB) and KV cache for reasonable context windows.

| Model (as tested) | Weights | Mac Mini M4 (16 GB) | Mac Mini M4 Pro (24 GB) | Mac Mini M4 Pro (48 GB) | Strix Halo (96 GB GPU) | DGX Spark (96 GB GPU) |
|---|---|:---:|:---:|:---:|:---:|:---:|
| Qwen3.5-0.8B Q4_K_M | ~0.5 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3.5-2B Q4_K_M | ~1.5 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma-4-E2B Q4_K_M | ~1.5 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3.5-4B Q4_K_M | ~2.8 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Gemma-4-E4B Q4_K_M | ~2.5 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ministral-3B Q4_K_M | ~2 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ministral-8B Q4_K_M | ~5 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Qwen3.5-9B Q4_K_M | ~6 GB | ✅ | ✅ | ✅ | ✅ | ✅ |
| Ministral-14B Q4_K_M | ~9 GB | ⚠️ tight | ✅ | ✅ | ✅ | ✅ |
| Gemma-4-26B-A4B Q4_K_M | ~15 GB | ❌ | ⚠️ tight | ✅ | ✅ | ✅ |
| Qwen3.5-27B Q4_K_M | ~17 GB | ❌ | ⚠️ tight | ✅ | ✅ | ✅ |
| Gemma-4-31B Q4_K_M | ~19 GB | ❌ | ⚠️ tight | ✅ | ✅ | ✅ |
| Qwen3.5-35B-A3B NVFP4 | ~20 GB | ❌ | ❌ | ✅ | ✅ | ✅ |
| Qwen3.6-35B-A3B Q4_K_M | ~20 GB | ❌ | ❌ | ✅ | ✅ | ✅ |
| GPT-OSS-120B GGUF | ~61 GB | ❌ | ❌ | ❌ | ✅ | ✅ |
| Qwen3.5-122B-A10B NVFP4 | ~70 GB | ❌ | ❌ | ❌ | ✅ | ✅ |
| Nemotron-3-Super-120B-A12B NVFP4 | ~70 GB | ❌ | ❌ | ❌ | ✅ | ✅ |
| Mistral-Small-4-119B NVFP4 | ~70 GB | ❌ | ❌ | ❌ | ✅ | ✅ |

> ⚠️ **tight** = model loads but leaves little room for KV cache / long context. Short prompts only.
>
> **Strix Halo** = AMD Ryzen AI Max (128 GB LPDDR5X total, up to 96 GB allocatable to GPU). **DGX Spark** = NVIDIA GB10 (128 GB LPDDR5X unified, ~96 GB GPU-usable). Both can run 120B-class models with room for KV cache.
>
> Mac Mini M4 Pro 64 GB and M4 Max 128 GB configs exist but are not listed — they slot between the columns above.

### ☁️ CLOUD Models — Run via API

Don't have a GPU? We also test open-source models hosted on cloud providers so you can compare **local vs cloud performance at every agent role.** Same tests, same scoring — find out if paying for cloud is worth it, or if your local setup already matches.

| Provider | Models | Status |
|---|---|---|
| Alibaba Coding Plan | **Qwen3.5-Plus** — 🥇 472/590 (80%) Phase F, 86/110 (78%) Phase G | ✅ Tested |
| Alibaba Coding Plan | **Kimi K2.5** — 473/590 (80%) Phase F, 96/110 (87%) Phase G | ✅ Tested |
| Alibaba Coding Plan | **GLM-5** — 456/590 (77%) Phase F, 80/110 (73%) Phase G | ✅ Tested |
| Alibaba Coding Plan | **MiniMax-M2.5** — 455/590 (77%) Phase F, 78/110 (71%) Phase G | ✅ Tested |
| Ollama Cloud | **MiniMax-M2.7** — 473/590 (80%) Phase F, 83/110 (75%) Phase G | ✅ Tested |
| OpenRouter | **Step-3.5-Flash** — 438/590 (74%) Phase F, 66/110 (60%) Phase G | ✅ Tested |
| OpenRouter | **Trinity-Large** — 444/590 (75%) Phase F, 73/110 (66%) Phase G | ✅ Tested |
| OpenRouter | **Nemotron-3-Nano-30B** — 453/590 (77%) Phase F, 70/110 (64%) Phase G | ✅ Tested |
| OpenRouter | **Qwen3.6-Plus** — 469/590 (79%) Phase F, 91/110 (83%) Phase G | ✅ Tested |

> 💡 **Kimi K2.5 leads Phase F** at 473/590 (80%), closely followed by M2.7 and Qwen3.5-Plus. M2.7's reasoning tokens count against `max_tokens`, requiring 16-24k to avoid truncation.
>
> 📊 **Detailed cloud comparisons:**
> - [☁️ Full cloud model comparison (all scores per role) →](docs/results-cloud.md)
> - [🆕 Phase G — Discriminator Tests (harder tests) →](docs/results-phase-g.md)

## ⚡ Token Efficiency — Which Models Waste the Fewest Tokens?

Two models both score 10/10 — but one used 500 tokens, the other 5,000. **The efficient one saves 10× on compute, cost, and latency.** This is hardware-independent: it measures model behavior, not GPU speed.

| Rank | Model | VRAM | Score | Tokens/Point | Verdict |
|------|-------|------|-------|-------------|---------|
| 🥇 | **Trinity-Large** | ☁️ | 414 | **39** | Ultra-lean |
| 🥈 | **Mistral-119B NT** | 🔵 64GB | 419 | **49** | Ultra-lean |
| 🥉 | **GLM-5 NT** | ☁️ | 421 | **61** | Lean |
| 4 | **Qwen3.5-Plus NT** | ☁️ | 442 | **63** | Lean |
| 5 | **Qwen3.5-35B-A3B NT** | 🟢 24GB | 432 | **76** | Efficient |
| 6 | **Kimi K2.5 Think** | ☁️ | 443 | **80** | Efficient |
| | ... | | | | |
| 32 | **Qwen3.6-35B-A3B** | 🟢 24GB | 430 | **696** | Heavy |
| 35 | **Qwen3.5-35B-A3B Think** | 🟢 24GB | 395 | **1,524** | Extremely Heavy |

> 💡 **Key insight:** Thinking models use **10–20× more tokens** than NoThink variants for similar scores. For cost-sensitive agent pipelines, NoThink wins massively on efficiency.
>
> 📊 **[Full Token Efficiency Leaderboard (35 models) →](docs/results-token-efficiency.md)** — complete rankings, Think vs NoThink gaps, best per VRAM tier

---

## 🚀 ClawEval v2 — Full 59-Agent Dense Evaluation

> **The next generation of ClawEval testing.** Every agent role now has a dense constraint test with **15–30 checkpoints** — no more x/10 ceiling effects. This is the definitive leaderboard.

Phase F gave every model 8–10/10 on most roles. ClawEval v2 replaces that with **granular percentage scoring** across all 59 agents. Same roles, dramatically harder prompts, real separation between models.

| Metric | Phase F (v1) | ClawEval v2 |
|--------|-------------|-------------|
| Tests | 59 roles × 10 pts | **59 roles × 15–30 checkpoints** |
| Total checkpoints | 590 | **1,220** |
| Scoring | x/10 (ceiling effect) | **Raw % (fine-grained)** |
| Manual-only tests | 6 | **0 — fully automated** |
| Discriminating power | Low (everyone scores 8+) | **High (real spread)** |

### 🏅 ClawEval v2 Leaderboard — Open-Weight Models

| Rank | Model | Provider | Score | % | Perfect |
|------|-------|----------|-------|---|---------|
| 🥇 | **DeepSeek V4 Pro** | ☁️ DeepSeek | 1060/1220 | **86.9%** | 26 |
| 🥈 | **DeepSeek V4 Flash** | ☁️ DeepSeek | 1054/1220 | **86.4%** | 23 |
| 🥉 | **Kimi K2.5 Think** | ☁️ Ollama | 1048/1220 | **85.9%** | 24 |
| 4 | **Kimi K2.7 Code** | ☁️ Ollama | 1038/1220 | **85.1%** | 24 |
| 5 | **Laguna-M.1** | ☁️ OpenRouter | 1034/1220 | **84.8%** | 25 |
| 6 | **Qwen3.5-Plus** | ☁️ Alibaba | 1031/1220 | **84.5%** | 26 |
| 7 | **Qwen3.6-35B-A3B** | 🖥️ Local | 1029/1220 | **84.3%** | 24 |
| 8 | **Kimi K2.6** | ☁️ Ollama | 1028/1220 | **84.3%** | 24 |
| 9 | **Qwen3.5-122B-A10B** | ☁️ Ollama | 1025/1220 | **84.0%** | 21 |
| 10 | **Gemma-4-31B** | ☁️ Ollama | 1024/1220 | **83.9%** | 25 |
| 11 | **Cobuddy** | ☁️ OpenRouter | 1023/1220 | **83.9%** | 21 |
| 12 | **Mistral-Large-3** | ☁️ Ollama | 1021/1220 | **83.7%** | 25 |
| 13 | **GLM-5.1** | ☁️ Ollama | 1020/1220 | **83.6%** | 26 |
| 14 | **Nemotron-3-Super Think** | ☁️ Ollama | 1016/1220 | **83.3%** | 20 |
| 15 | **MiniMax-M2.7 Medium** | ☁️ Ollama | 1014/1220 | **83.1%** | 20 |
| 16 | **Qwen3.6-27B** | 🖥️ Local TQ4 | 1012/1220 | **83.0%** | 26 |
| 17 | **Nemotron-3-Super NoThink** | ☁️ Ollama | 996/1220 | **81.6%** | 21 |
| 18 | **MiniMax-M2.7 Think** | ☁️ Ollama | 993/1220 | **81.4%** | 19 |
| 19 | **Nemotron-3-Nano-Omni** | ☁️ OpenRouter | 991/1220 | **81.2%** | 20 |
| 20 | **Gemma-4-E2B** | 🖥️ Local | 981/1220 | **80.4%** | 14 |
| 21 | **GPT-OSS-120B** | ☁️ Ollama | 979/1220 | **80.2%** | 19 |
| 22 | **Gemini-3.5-Flash** | ☁️ Google (OpenRouter) | 978/1220 | **80.2%** | 22 |
| 23 | **Phi-4** | 🖥️ Local Q8 | 977/1220 | **80.1%** | 17 |
| 24 | **GLM-5.2** | ☁️ Ollama | 957/1220 | **78.4%** | 23 |
| 25 | **Laguna-XS.2** | ☁️ OpenRouter | 950/1220 | **77.9%** | 20 |
| 26 | **GLM-5 NoThink** | ☁️ Ollama | 948/1220 | **77.7%** | 25 |
| 27 | **Nemotron-Nano-Omni** | 🖥️ Local IQ4 | 948/1220 | **77.7%** | 20 |
| 28 | **Kimi K2.5 NoThink** | ☁️ Ollama | 935/1220 | **76.6%** | 21 |
| 29 | **Granite-4.1 30B** | 🖥️ Local TQ4 | 929/1220 | **76.1%** | 15 |
| 30 | **Granite-4.1 8B** | 🖥️ Local Q4 | 929/1220 | **76.1%** | 14 |
| 31 | **Gemma-4-31B** | 🖥️ Local Q4 | 927/1220 | **76.0%** | 25 |
| 32 | **GLM-5 Think** | ☁️ Ollama | 927/1220 | **76.0%** | 23 |
| 33 | **Nemotron-Nano-Omni** | 🖥️ Local Q4 | 925/1220 | **75.8%** | 19 |
| 34 | **Nemotron-3-Nano-30B** | ☁️ Ollama | 914/1220 | **74.9%** | 19 |
| 35 | **Trinity-Large-Think** | ☁️ OpenRouter | 914/1220 | **74.9%** | 21 |
| 36 | **Ministral-3 8B** | ☁️ Ollama | 906/1220 | **74.3%** | 18 |
| 37 | **Ministral-3 14B** | ☁️ Ollama | 888/1220 | **72.8%** | 17 |
| 38 | **GPT-OSS-20B** | ☁️ Ollama | 885/1220 | **72.5%** | 19 |
| 39 | **Ministral-3 8B** | 🖥️ Local Q4 | 884/1220 | **72.5%** | 16 |
| 40 | **Ministral-3 14B** | 🖥️ Local Q4 | 877/1220 | **71.9%** | 18 |
| 41 | **Gemma-4-E4B** | 🖥️ Local | 867/1220 | **71.1%** | 15 |
| 42 | **Ministral-3 14B Think** | 🖥️ Local Q4 | 858/1220 | **70.3%** | 19 |
| 43 | **Granite-4.1 3B** | 🖥️ Local Q4 | 846/1220 | **69.3%** | 12 |
| 44 | **Ministral-3 3B** | ☁️ Ollama | 844/1220 | **69.2%** | 14 |
| 45 | **Ministral-3 8B Think** | 🖥️ Local Q4 | 791/1220 | **64.8%** | 10 |
| 46 | **Ministral-3 3B** | 🖥️ Local Q4 | 760/1220 | **62.3%** | 12 |
| 47 | **RNJ-1-8B** | ☁️ Ollama | 750/1220 | **61.5%** | 18 |
| 48 | **Ministral-3 3B Think** | 🖥️ Local Q4 | 704/1220 | **57.7%** | 10 |
| 49 | **Gemma-4-A4B** | 🖥️ Local | 622/1220 | **51.0%** | 10 |
| 50 | **Qwen3.5-9B** | 🖥️ Local | 543/1220 | **44.5%** | 6 |
| 51 | **Qwen3.5-4B** | 🖥️ Local | 374/1220 | **30.7%** | 4 |
| 52 | **LFM2.5-350M** | 🖥️ Local | 308/1220 | **25.2%** | 2 |
| 53 | **Qwen3.5-0.8B** | 🖥️ Local | 58/1220 | **4.8%** | 0 |
| 54 | **Qwen3.5-2B** | 🖥️ Local | 50/1220 | **4.1%** | 0 |

#### 📋 Gemini-3.5-Flash — Full 59-Agent Breakdown

> Per-role performance across all 59 ClawEval v2 agents. **978/1,220 checkpoints (80.2%)** — 22 roles at 100%, 12 roles below 50%.

| Test | Agent Role | Score | % |
|------|-----------|-------|---|
| H-01 | Router / Triage Agent | 29/30 | 97% |
| H-02 | Input Validator / Sanitizer | 29/30 | 97% |
| H-03 | Heartbeat / Health Monitor | 14/15 | 93% |
| H-04 | Notification / Alert Agent | 21/30 | 70% |
| H-05 | Sentiment Analysis Agent | 29/30 | 97% |
| H-06 | FAQ Generation Agent | 15/15 | 100% |
| H-07 | Translation Agent | 15/15 | 100% |
| H-08 | Calendar / Scheduling Agent | 12/20 | 60% |
| H-09 | Research / Web Search Agent | 30/30 | 100% |
| H-10 | Content Writer / Blog Writer | 18/20 | 90% |
| H-11 | Editor Agent | 29/30 | 97% |
| H-12 | Content Planner / Strategist | 0/30 | 0% |
| H-13 | Email Drafting / Summarization | 43/45 | 96% |
| H-14 | Document Summarization Agent | 15/15 | 100% |
| H-15 | Meeting Notes / Transcription Agent | 35/35 | 100% |
| H-16 | Social Media Scouting / Monitoring | 57/60 | 95% |
| H-17 | Social Media Content Agent | 19/20 | 95% |
| H-18 | News Aggregation Agent | 7/7 | 100% |
| H-19 | Shopping / Price Comparison | 15/15 | 100% |
| H-20 | Memory / Knowledge Management | 20/20 | 100% |
| H-21 | RAG / Retrieval Agent | 4/15 | 27% |
| H-22 | Data Analysis Agent | 14/15 | 93% |
| H-23 | Website Scraping / Understanding | 15/15 | 100% |
| H-24 | Image Description / Understanding | 20/20 | 100% |
| H-25 | Customer Support Agent | 33/60 | 55% |
| H-26 | Lead Scoring / Prospecting | 12/15 | 80% |
| H-27 | Sprint / Project Summarizer | 15/15 | 100% |
| H-28 | Transaction / Approval Agent | 19/20 | 95% |
| H-29 | Home Automation Agent | 9/20 | 45% |
| H-30 | Fitness / Health Tracking | 15/15 | 100% |
| H-31 | Recipe / Cooking Agent | 15/15 | 100% |
| H-32 | Personal Finance Tracking | 15/15 | 100% |
| H-33 | SEO Optimization Agent | 4/15 | 27% |
| H-34 | Landing Page Generator | 20/20 | 100% |
| H-35 | Travel Planning Agent | 6/15 | 40% |
| H-36 | Code Generation Agent | 30/30 | 100% |
| H-37 | Code Review Agent | 15/15 | 100% |
| H-38 | QA / Test Writing Agent | 13/15 | 87% |
| H-39 | Task Planning / Decomposition | 1/18 | 6% |
| H-40 | Fact-Checking Agent | 28/30 | 93% |
| H-41 | Critic / Review Agent | 20/20 | 100% |
| H-42 | Market Research Agent | 14/15 | 93% |
| H-43 | Synthesizer / Aggregator | 13/15 | 87% |
| H-44 | Curriculum / Course Designer | 7/15 | 47% |
| H-45 | Prototype Generator | 15/15 | 100% |
| H-46 | DevOps Agent | 8/15 | 53% |
| H-47 | Math / Logic Reasoning | 14/15 | 93% |
| H-48 | STEM Research Analyst | 15/15 | 100% |
| H-49 | Algorithm / Data Structure Explorer | 30/30 | 100% |
| H-50 | Orchestrator / Manager Agent | 1/15 | 7% |
| H-51 | Software Architect Agent | 4/15 | 27% |
| H-52 | Complex Debugger Agent | 13/15 | 87% |
| H-53 | Legal Document Review | 6/15 | 40% |
| H-54 | Medical / Health Analysis | 15/15 | 100% |
| H-55 | Financial Analysis / Stock Research | 14/15 | 93% |
| H-56 | Security Analyst Agent | 0/15 | 0% |
| H-57 | SRE / Incident Response | 13/15 | 87% |
| H-58 | Book / Long-Form Writing | 19/20 | 95% |
| H-59 | Compliance / Regulatory Agent | 2/15 | 13% |

---


## 📦 Evaluation Phases

ClawEval evaluates models across multiple phases of increasing difficulty:

| Phase | Focus | Tests | Scoring |
|---|---|---|---|
| **A–C** | Basic role evaluation | 59 roles × system prompts | Quality review |
| **D** | Hard prompts | 59 roles × adversarial prompts | Automated |
| **E** | Killer tests | 12 precision tasks | Deterministic (JSON, code exec, regex) |
| **F** | Role-specific hard tests | 59 roles × deterministic prompts | Deterministic (15+ scoring types) |

### Phase F — 59 Roles Across 5 Tiers
- **Tier 1** (8 roles): Router, Validator, Health Monitor, Notification, Sentiment, FAQ, Translation, Calendar
- **Tier 2** (27 roles): Research, Writer, Editor, Email, Summarization, Customer Support, Data Analysis, etc.
- **Tier 3** (11 roles): Code Gen, Code Review, QA Testing, Task Planning, Fact-Checking, Market Research, etc.
- **Tier 4** (3 roles): Math/Logic Reasoning, STEM Analysis, Algorithm Exploration
- **Tier 5** (10 roles): Orchestrator, Architect, Debugger, Legal, Medical, Financial, Security, SRE, etc.

### Scoring Types
`exact_json` · `json_numeric` · `keyword_detection` · `code_exec` · `constraint_check` · `error_count` · `action_items` · `news_dedup` · `recipe_scaling` · `compliance_issues` · `architecture_constraints` · `manual_review` · and more

## 🚀 Quick Start

### Prerequisites
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install requests
```

### Run Phase E (12 killer tests)
```bash
# Against llama.cpp server
python eval/run_phase_e.py \
  --base-url http://localhost:8080/v1 \
  --model my-model-name \
  --max-tokens 4000

# Against SGLang server (with thinking)
python eval/run_phase_e.py \
  --base-url http://192.168.1.2:8000/v1 \
  --model Qwen3.5-122B-think \
  --api-model /path/to/weights \
  --thinking-budget 16384 \
  --max-tokens 32000

# Disable thinking
python eval/run_phase_e.py \
  --base-url http://192.168.1.2:8000/v1 \
  --model Qwen3.5-122B-nothink \
  --api-model /path/to/weights \
  --nothink
```

### Run Phase F (59 role tests)
```bash
python eval/run_phase_f.py \
  --base-url http://localhost:8080/v1 \
  --model my-model-name \
  --max-tokens 4000

# Run specific tests or tiers
python eval/run_phase_f.py ... --test-ids 1 2 3
python eval/run_phase_f.py ... --tier 3
```

### Results
Results are saved to `eval/test_results/<model-name>/phase_e/` and `phase_f/` directories, including:
- Individual response text files per test
- `phase_e_scores.json` / `phase_f_scores.json` with full scoring breakdown

## 🔧 Key Features

- **OpenAI-compatible API**: Works with any server exposing `/v1/chat/completions` (llama.cpp, SGLang, vLLM, etc.)
- **SGLang thinking control**: `--thinking-budget` and `--nothink` flags for reasoning token management
- **Think-tag stripping**: Automatically strips `<think>` tags from responses for clean scoring
- **Flexible JSON scoring**: Case-insensitive keys, nested dict traversal, numeric tolerance
- **Deterministic**: Every test has an exact expected answer — no LLM-as-judge

## 📁 Repo Structure

```
ClawEval/
├── eval/
│   ├── run_phase_e.py          # Phase E runner (12 killer tests)
│   ├── run_phase_f.py          # Phase F runner (59 role tests)
│   ├── phase_e_prompts.py      # Phase E test definitions
│   ├── phase_f/                # Phase F test definitions (5 tiers)
│   │   ├── __init__.py
│   │   ├── tier1.py ... tier5.py
│   ├── role_prompts.py         # 59 role system prompts
│   ├── hard_prompts.py         # Phase D adversarial prompts
│   └── test_results/           # All model evaluation results
├── docs/                       # VRAM tier guides & model selection
│   ├── 16GB, 24GB, 32GB, 48GB, 64GB, 96GB tier guides
│   └── Subagent type reference
├── RESULTS.md                  # Detailed per-role score comparison
└── README.md
```

## 🗺️ Model Testing Roadmap

This is a living benchmark. We're continuously adding new models as they release. Here's what's on the radar — and we take requests.

**16GB VRAM tier (coming soon)**
- Qwen3-8B, Qwen3.5-14B
- Phi-4 14B, Phi-4-mini 3.8B
- Mistral Small 3.1 24B (tight fit)
- GPT-OSS-20B MXFP4
- Gemma 3 12B
- Ministral 3B (ultra-fast routing/triage)

**24GB VRAM tier**
- ✅ Qwen3.5-35B-A3B Q4_K_M (tested)
- ✅ Qwen3.5-27B Q4_K_M (tested)
- Gemma 3 27B QAT
- More MoE models as they release

**64–96GB VRAM tier**
- ✅ Qwen3.5-122B-A10B NVFP4 (tested)
- ✅ GPT-OSS-120B GGUF · llama.cpp (tested — 3 reasoning levels)
- More large models coming

**Cloud (open-source via API)**
- Open-source models via OpenRouter, Alibaba, and other affordable providers

> 💬 **Want us to test a specific model?** [Open an issue](https://github.com/AIgenteur/ClawEval/issues) or drop a comment — we prioritize community requests. New models are added as they release.

## 📄 License

MIT

## 🔗 Links

- **Newsletter**: [AIgenteur Dispatch](https://aigenteurdispatch.substack.com/) — subscribe for new benchmark results and AI agent guides
- **Community**: [AIgenteur Launchpad (free)](https://www.skool.com/aigenteur-academy-9764) — discuss results, get help, share what's working
- **Sister project**: [AIgenteur](https://github.com/AIgenteur/aigenteur) — main cofounder repo. ClawEval is the eval harness it grades itself with.
- **GitHub**: [github.com/AIgenteur/ClawEval](https://github.com/AIgenteur/ClawEval)
