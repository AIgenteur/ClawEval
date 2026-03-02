# Phase G — Discriminator Tests (Harder Tests That Separate Model Quality)

[← Back to main README](../README.md)

## Why Phase G?

Phase F tests showed identical scores (10/10) across all models for ~15 roles, meaning the tests were too easy to differentiate model quality. Phase G uses **harder, multi-constraint tests** designed to reveal real differences between 27B, 35B, and 120B+ models.

## Scoring Legend

🟢 = 8-10 &nbsp; 🟡 = 5-7 &nbsp; 🔴 = 0-4

## Results

| # | Test | 122B NoThink | 27B NoThink | GPT-OSS-120B | 35B NoThink |
|---|------|:----------:|:----------:|:----------:|:----------:|
| | | Qwen3.5-122B-A10B | Qwen3.5-27B | GPT-OSS-120B Med | Qwen3.5-35B-A3B |
| | | NVFP4 · SGLang | Q4_K_M · llama.cpp | GGUF · llama.cpp | Q4_K_M · llama.cpp |
| 36 | Code Gen (RateLimiter) | 🟢 8 | 🟢 **10** | 🟡 7 | 🟢 9 |
| 2 | Input Validator (nested) | 🟢 **10** | 🟢 **10** | 🟢 9 | 🟢 9 |
| 5 | Sentiment (hard, 20 items) | 🟢 **8** | 🟢 **8** | 🟡 6 | 🟢 **8** |
| 40 | Fact-Checking (plausible) | 🟢 **10** | 🟢 **10** | 🟢 9 | 🟢 9 |
| 49 | Algorithm (LRU Cache + TTL) | 🟢 **10** | 🟢 9 | 🟢 **10** | 🟡 5 |
| 51 | Architect (trade-offs) | 🟢 **10** | 🟢 9 | 🟢 9 | 🟢 9 |
| 48 | STEM (multi-step calc) | 🟡 **5** | 🔴 2 | 🟡 **5** | 🔴 1 |
| 9 | Research (contradictions) | 🟢 8 | 🟢 **9** | 🟢 **9** | 🟢 **9** |
| 12 | Content Planner (15 constraints) | 🔴 1 | 🔴 1 | 🔴 1 | 🔴 1 |
| 50 | Orchestrator (multi-agent) | 🟡 **7** | 🟡 **7** | 🟡 **7** | 🟡 **7** |
| 23 | Web Scraping (messy HTML) | 🟢 **10** | 🟢 8 | 🟢 **10** | 🟢 **10** |
| | **TOTAL** | **87/110 (79%)** | **83/110 (75%)** | **82/110 (75%)** | **77/110 (70%)** |

## Key Findings

1. **122B NoThink is the overall winner** (87/110) — best at algorithm, architecture, and multi-step reasoning
2. **27B NoThink is the best 24GB model** (83/110) — surprisingly aces Code Generation (10/10) where both 120B+ models score lower
3. **GPT-OSS-120B is a strong all-rounder** (82/110) — ties 122B on Algorithm and STEM
4. **35B NoThink is solid but 4th** (77/110) — weakest on Algorithm (5/10) and STEM (1/10)
5. **Content Planner** (1/10 for all) — the keyword-based scorer is too strict for this test; all models likely meet constraints but the automated checker can't parse them

## What Makes Phase G Different from Phase F?

| Aspect | Phase F | Phase G |
|--------|---------|---------|
| Code Gen test | `merge_intervals()` — simple | `RateLimiter` class — 8 requirements, 10 test cases |
| Input Validator | 10 flat errors | 15 nested errors + cross-field dependencies |
| Sentiment | 10 statements | 20 with nested sarcasm + ambiguity |
| Fact-Checking | 10 well-known facts | 20 plausible falsehoods |
| Algorithm | Single function | LRU Cache with TTL — 15 test cases |
| Scoring | Binary pass/fail | Graduated (partial credit) |

## Thinking Mode Results

Thinking mode on SGLang causes issues: the model spends too many tokens on chain-of-thought reasoning and runs out of output budget before producing the actual answer. This affects both 122B Think (45/110) and 35B Think (51/110). These scores are **not representative** of model quality — they reflect a token budget problem, not capability.

> ⭐ Star this repo to get notified when new models are added.

---

[← Back to main README](../README.md)
