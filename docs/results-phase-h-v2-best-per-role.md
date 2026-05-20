# ClawEval v2 — Best Model per Agent Role (Enhanced Tests)

59 agent roles, 1,220 constraint checkpoints, **47 open-weight models** tested.
Use this table to pick the best model for each specific agent task.

> Proprietary models are ranked separately — see the [Proprietary Models leaderboard](../README.md#-clameval-v2-leaderboard--proprietary-models) in the README.

## Tier 1

| Test | Agent Role | Best Score | Best Model(s) |
|------|-----------|------------|---------------|
| H-1 | Router / Triage Agent | 30/30 (100%) ✅ | Cobuddy, GLM-5 NT +8 |
| H-2 | Input Validator / Sanitizer | 29/30 (97%) | Cobuddy, GLM-5 NT +23 |
| H-3 | Heartbeat / Health Monitor | 15/15 (100%) ✅ | Gemma-31B, Gemma-31B TQ3 +6 |
| H-4 | Notification / Alert Agent | 27/30 (90%) | Nem-Super NT |
| H-5 | Sentiment Analysis Agent | 29/30 (97%) | GLM-5 NT, GLM-5 T +2 |
| H-6 | FAQ Generation Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +38 |
| H-7 | Translation Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +34 |
| H-8 | Calendar / Scheduling Agent | 14/20 (70%) | Gemma-31B cloud |

## Tier 2

| Test | Agent Role | Best Score | Best Model(s) |
|------|-----------|------------|---------------|
| H-9 | Research / Web Search Agent | 30/30 (100%) ✅ | Cobuddy, GLM-5 NT +6 |
| H-10 | Content Writer / Blog Writer | 20/20 (100%) ✅ | GLM-5 NT, Granite-8B +8 |
| H-11 | Editor Agent | 29/30 (97%) | Cobuddy, Gemma-31B TQ3 +11 |
| H-12 | Content Planner / Strategist | 26/30 (87%) | Cobuddy, Kimi K2.5 T +2 |
| H-13 | Email Drafting / Summarization | 45/45 (100%) ✅ | Kimi K2.5 T, Qwen3.6-27B |
| H-14 | Document Summarization Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +42 |
| H-15 | Meeting Notes / Transcription Agent | 35/35 (100%) ✅ | Gemma-31B cloud, Granite-3B +16 |
| H-16 | Social Media Scouting / Monitoring | 58/60 (97%) | Qwen3.5-122B |
| H-17 | Social Media Content Agent | 20/20 (100%) ✅ | GPT-OSS-120B, Gemma-31B +13 |
| H-18 | News Aggregation Agent | 7/7 (100%) ✅ | Cobuddy, GLM-5 NT +35 |
| H-19 | Shopping / Price Comparison | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +42 |
| H-20 | Memory / Knowledge Management | 20/20 (100%) ✅ | Cobuddy, GLM-5 NT +29 |
| H-21 | RAG / Retrieval Agent | 13/15 (87%) | GPT-OSS-120B, GPT-OSS-20B +6 |
| H-22 | Data Analysis Agent | 14/15 (93%) | Cobuddy, GLM-5 NT +16 |
| H-23 | Website Scraping / Understanding | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +38 |
| H-24 | Image Description / Understanding | 20/20 (100%) ✅ | Cobuddy, GLM-5 NT +43 |
| H-25 | Customer Support Agent | 55/60 (92%) | MM-M2.7 Med |
| H-26 | Lead Scoring / Prospecting | 15/15 (100%) ✅ | MM-M2.7 Med, Ministral-14B T |
| H-27 | Sprint / Project Summarizer | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +28 |
| H-28 | Transaction / Approval Agent | 20/20 (100%) ✅ | Granite-8B, Laguna-M.1 +2 |
| H-29 | Home Automation Agent | 10/20 (50%) | Qwen3.5-122B |
| H-30 | Fitness / Health Tracking | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +22 |
| H-31 | Recipe / Cooking Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +25 |
| H-32 | Personal Finance Tracking | 15/15 (100%) ✅ | GLM-5 NT, GLM-5 T +11 |
| H-33 | SEO Optimization Agent | 9/15 (60%) | Gemma-E4B |
| H-34 | Landing Page Generator | 20/20 (100%) ✅ | Cobuddy, GLM-5 NT +34 |
| H-35 | Travel Planning Agent | 12/15 (80%) | Ministral-14B, Ministral-8B cloud |

## Tier 3

| Test | Agent Role | Best Score | Best Model(s) |
|------|-----------|------------|---------------|
| H-36 | Code Generation Agent | 30/30 (100%) ✅ | Cobuddy, GLM-5 NT +38 |
| H-37 | Code Review Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +25 |
| H-38 | QA / Test Writing Agent | 14/15 (93%) | Ministral-14B, Ministral-14B cloud +4 |
| H-39 | Task Planning / Decomposition | 13/18 (72%) | Ministral-8B, Mistral-Large-3 |
| H-40 | Fact-Checking Agent | 30/30 (100%) ✅ | Ministral-8B T, Nem-Super NT |
| H-41 | Critic / Review Agent | 20/20 (100%) ✅ | Cobuddy, GLM-5 NT +39 |
| H-42 | Market Research Agent | 14/15 (93%) | Cobuddy, GLM-5 NT +22 |
| H-43 | Synthesizer / Aggregator | 15/15 (100%) ✅ | Qwen3.6-27B |
| H-44 | Curriculum / Course Designer | 10/15 (67%) | Mistral-Large-3, Trinity-Large |
| H-45 | Prototype Generator | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +36 |
| H-46 | DevOps Agent | 11/15 (73%) | Qwen3.6-27B |

## Tier 4

| Test | Agent Role | Best Score | Best Model(s) |
|------|-----------|------------|---------------|
| H-47 | Math / Logic Reasoning | 14/15 (93%) | Cobuddy, GLM-5 NT +25 |
| H-48 | STEM Research Analyst | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +20 |
| H-49 | Algorithm / Data Structure Explorer | 30/30 (100%) ✅ | GLM-5 NT, GLM-5 T +24 |

## Tier 5

| Test | Agent Role | Best Score | Best Model(s) |
|------|-----------|------------|---------------|
| H-50 | Orchestrator / Manager Agent | 13/15 (87%) | Cobuddy, Qwen3.6-35B |
| H-51 | Software Architect Agent | 8/15 (53%) | Mistral-Large-3 |
| H-52 | Complex Debugger Agent | 15/15 (100%) ✅ | Cobuddy, GLM-5 T +6 |
| H-53 | Legal Document Review | 8/15 (53%) | Laguna-M.1, Nem-Nano-30B +2 |
| H-54 | Medical / Health Analysis | 15/15 (100%) ✅ | Cobuddy, GLM-5 NT +41 |
| H-55 | Financial Analysis / Stock Research | 15/15 (100%) ✅ | GPT-OSS-120B, GPT-OSS-20B +11 |
| H-56 | Security Analyst Agent | 15/15 (100%) ✅ | GLM-5 NT, GPT-OSS-120B +16 |
| H-57 | SRE / Incident Response | 13/15 (87%) | GLM-5 NT, GLM-5 T +6 |
| H-58 | Book / Long-Form Writing | 20/20 (100%) ✅ | GLM-5 NT, GLM-5 T +33 |
| H-59 | Compliance / Regulatory Agent | 8/15 (53%) | GLM-5 NT |
