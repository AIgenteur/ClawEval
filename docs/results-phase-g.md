# Phase G — Discriminator Tests (Harder Tests That Separate Model Quality)

[← Back to main README](../README.md)

## Why Phase G?

Phase F tests showed identical scores (10/10) across all models for ~15 roles, meaning the tests were too easy to differentiate model quality. Phase G uses **harder, multi-constraint tests** designed to reveal real differences between 27B, 35B, and 120B+ models.

## Scoring Legend

🟢 = 8-10 &nbsp; 🟡 = 5-7 &nbsp; 🔴 = 0-4

## Results

| # | Test | 35B Best | 122B NoThink | 27B NoThink | GPT-OSS-120B |
|---|------|:--------:|:----------:|:----------:|:----------:|
| | | Qwen3.5-35B-A3B | Qwen3.5-122B-A10B | Qwen3.5-27B | GPT-OSS-120B Med |
| | | Q4_K_M / NVFP4 | NVFP4 · SGLang | Q4_K_M · llama.cpp | GGUF · llama.cpp |
| | | **Best of Think + NoThink** | **NoThink** | **NoThink** | **Medium reasoning** |
| 36 | Code Gen (RateLimiter) | 🟢 9 | 🟢 8 | 🟢 **10** | 🟡 7 |
| 2 | Input Validator (nested) | 🟢 **10** | 🟢 **10** | 🟢 **10** | 🟢 9 |
| 5 | Sentiment (hard, 20 items) | 🟢 **8** | 🟢 **8** | 🟢 **8** | 🟡 6 |
| 40 | Fact-Checking (plausible) | 🟢 **10** | 🟢 **10** | 🟢 **10** | 🟢 9 |
| 49 | Algorithm (LRU Cache + TTL) | 🟢 9 | 🟢 **10** | 🟢 9 | 🟢 **10** |
| 51 | Architect (trade-offs) | 🟢 9 | 🟢 **10** | 🟢 9 | 🟢 9 |
| 48 | STEM (multi-step calc) | 🔴 2 | 🟡 **5** | 🔴 2 | 🟡 **5** |
| 9 | Research (contradictions) | 🟢 **10** | 🟢 8 | 🟢 9 | 🟢 9 |
| 12 | Content Planner (15 constraints) | 🟢 **8** | 🔴 1 | 🔴 1 | 🔴 1 |
| 50 | Orchestrator (multi-agent) | 🟡 **7** | 🟡 **7** | 🟡 **7** | 🟡 **7** |
| 23 | Web Scraping (messy HTML) | 🟢 **10** | 🟢 **10** | 🟢 8 | 🟢 **10** |
| | **TOTAL** | **92/110 (84%)** | **87/110 (79%)** | **83/110 (75%)** | **82/110 (75%)** |

## Key Findings

1. **35B Best-of-Think+NoThink is the overall winner** (92/110) — mixing Think for reasoning tasks and NoThink for structured output gives the best results
2. **122B NoThink is the best single-config model** (87/110) — best at algorithm, architecture, and STEM
3. **27B NoThink is the best pure 24GB model** (83/110) — aces Code Generation (10/10) where 120B+ models score lower
4. **GPT-OSS-120B is a strong all-rounder** (82/110) — ties 122B on Algorithm and STEM
5. **Content Planner** — 35B Think scored 8/10 while all NoThink configs score 1/10, showing thinking mode genuinely helps for complex constraint satisfaction

## What Makes Phase G Different from Phase F?

| Aspect | Phase F | Phase G |
|--------|---------|---------|
| Code Gen test | `merge_intervals()` — simple | `RateLimiter` class — 8 requirements, 10 test cases |
| Input Validator | 10 flat errors | 15 nested errors + cross-field dependencies |
| Sentiment | 10 statements | 20 with nested sarcasm + ambiguity |
| Fact-Checking | 10 well-known facts | 20 plausible falsehoods |
| Algorithm | Single function | LRU Cache with TTL — 15 test cases |
| Scoring | Binary pass/fail | Graduated (partial credit) |

## Think vs NoThink on SGLang

The 35B model benefits from mixing modes:
- **Think wins on:** Content Planner (8 vs 1), Input Validator (10 vs 9), Research (10 vs 9)
- **NoThink wins on:** Code Gen (9 vs 0*), Algorithm (9 vs 0*), Fact-Checking (10 vs 0*), STEM (2 vs 0*), Web Scraping (8 vs 0*)

\* Think-mode failures were due to thinking tokens consuming the entire output budget, leaving no room for the actual answer. This is a token budget issue, not a capability issue.

> ⭐ Star this repo to get notified when new models are added.

---

[← Back to main README](../README.md)
