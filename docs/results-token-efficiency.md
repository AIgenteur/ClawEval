# ⚡ Token Efficiency — Which Models Waste the Fewest Tokens?

[← Back to Main Results](../README.md) · [Full Detailed Results →](../RESULTS.md)

Two models both score 10/10 — but one used 500 tokens and the other used 5,000. **The efficient model saves 10× on compute, cost, and latency.** This page ranks models by how many tokens they need to earn each point.

> 💡 **Lower is better.** A model scoring 400 points using 30,000 tokens (75 tok/point) is far more efficient than one scoring 440 points using 300,000 tokens (682 tok/point) — even though it scored lower.

### How We Measure

- **Tokens/Point** = Total output tokens ÷ Total score (excluding manual-review tests)
- This metric is **hardware-independent** — it measures model verbosity, not GPU speed
- Thinking/reasoning tokens count against efficiency (they consume compute even if stripped from output)

---

## 🏆 Token Efficiency Leaderboard — Phase F

Only models with full 53-test runs (excluding 6 manual tests). Sorted by Tokens/Point (lower = more efficient).

| Rank | Model | VRAM Tier | Score | Tokens | Tok/Point | Verdict |
|------|-------|-----------|-------|--------|-----------|---------|
| 🥇 1 | **Trinity-Large** | ☁️ Cloud | 414 | 16,214 | **39** | Ultra-lean |
| 🥈 2 | **Mistral-Small-4-119B NT** | 🔵 64-96GB | 419 | 20,703 | **49** | Ultra-lean |
| 🥉 3 | **Mistral-Small-4-119B Think** | 🔵 64-96GB | 421 | 21,165 | **50** | Ultra-lean |
| 4 | Mistral-Small-4-119B Med | 🔵 64-96GB | 425 | 24,484 | **58** | Lean |
| 5 | GLM-5 NoThink | ☁️ Cloud | 421 | 25,800 | **61** | Lean |
| 6 | Qwen3.5-Plus NT | ☁️ Cloud | 442 | 28,024 | **63** | Lean |
| 7 | Qwen3.5-35B-A3B NT | 🟢 24GB | 432 | 32,685 | **76** | Efficient |
| 8 | Qwen3.5-9B NT | 🟡 16GB | 404 | 31,220 | **77** | Efficient |
| 9 | Qwen3.5-9B Think | 🟡 16GB | 393 | 31,524 | **80** | Efficient |
| 10 | Kimi K2.5 Think | ☁️ Cloud | 443 | 35,559 | **80** | Efficient |
| 11 | Kimi K2.5 NT | ☁️ Cloud | 439 | 36,693 | **84** | Efficient |
| 12 | Ministral-14B | 🟡 16GB | 398 | 33,667 | **85** | Efficient |
| 13 | Qwen3.5-2B NT | 🔴 8GB | 354 | 31,231 | **88** | Moderate |
| 14 | Qwen3.5-4B Think | 🔴 8GB | 400 | 35,481 | **89** | Moderate |
| 15 | Qwen3.5-4B NT | 🔴 8GB | 402 | 36,196 | **90** | Moderate |
| 16 | Ministral-3B | 🔴 8GB | 368 | 37,200 | **101** | Moderate |
| 17 | Ministral-8B | 🟠 12GB | 391 | 40,689 | **104** | Moderate |
| 18 | Qwen3.5-0.8B Think | 🔴 8GB | 303 | 42,547 | **140** | Verbose |
| 19 | GPT-OSS-120B Med | 🔵 64-96GB | 444 | 68,267 | **154** | Verbose |
| 20 | GPT-OSS-120B Low | 🔵 64-96GB | 435 | 69,085 | **159** | Verbose |
| 21 | GPT-OSS-120B High | 🔵 64-96GB | 435 | 71,976 | **166** | Verbose |
| 22 | Qwen3.5-0.8B NT | 🔴 8GB | 295 | 50,893 | **173** | Verbose |
| 23 | Gemma-4-E4B | 🔴 8GB | 429 | 87,620 | **204** | Heavy |
| 24 | Gemma-4-E2B | 🔴 8GB | 421 | 86,669 | **206** | Heavy |
| 25 | Nemotron-120B NT | 🔵 64-96GB | 435 | 94,314 | **217** | Heavy |
| 26 | Nemotron-120B Think | 🔵 64-96GB | 443 | 106,300 | **240** | Heavy |
| 27 | MiniMax-M2.5 Think | ☁️ Cloud | 420 | 118,253 | **282** | Heavy |
| 28 | Gemma-4-31B | 🟢 24GB | 439 | 147,652 | **336** | Very Heavy |
| 29 | GLM-5 Think | ☁️ Cloud | 426 | 168,639 | **396** | Very Heavy |
| 30 | MiniMax-M2.7 Med | ☁️ Cloud | 377 | 149,865 | **398** | Very Heavy |
| 31 | Qwen3.6-Plus | ☁️ Cloud | 439 | 239,555 | **546** | Extremely Heavy |
| 32 | **Qwen3.6-35B-A3B** | 🟢 24GB | 430 | 299,171 | **696** | Extremely Heavy |
| 33 | Qwen3.5-Plus Think | ☁️ Cloud | 426 | 311,200 | **731** | Extremely Heavy |
| 34 | Qwen3.5-27B Think | 🟢 24GB | 406 | 375,609 | **925** | Extremely Heavy |
| 35 | Qwen3.5-35B-A3B Think | 🟢 24GB | 395 | 602,132 | **1,524** | Extremely Heavy |

> ⚠️ Models with incomplete runs (partial tests, crashed results) are excluded.
>
> 💡 **Key insight:** Thinking/reasoning models consistently use 3-10× more tokens than their NoThink counterparts for similar scores. For cost-sensitive agent pipelines, NoThink variants are dramatically more efficient.

---

## 📊 Best Efficiency Per VRAM Tier

| VRAM Tier | Most Efficient Model | Score | Tok/Point |
|-----------|---------------------|-------|-----------|
| 🔴 8GB | Qwen3.5-2B NT | 354 | **88** |
| 🟠 12GB | Ministral-8B | 391 | **104** |
| 🟡 16GB | Qwen3.5-9B NT | 404 | **77** |
| 🟢 24GB | Qwen3.5-35B-A3B NT | 432 | **76** |
| 🔵 64-96GB | Mistral-Small-4-119B NT | 419 | **49** |
| ☁️ Cloud | Trinity-Large | 414 | **39** |

> 🏆 **Trinity-Large** is the most token-efficient model we've tested at just 39 tokens per point — but it's cloud-only. For local deployment, **Qwen3.5-35B-A3B NT** at 76 tok/point offers the best balance of quality and efficiency on 24GB hardware.

---

## 🔍 Think vs NoThink Efficiency Gap

| Model Family | NoThink Tok/Pt | Think Tok/Pt | Think Overhead |
|-------------|---------------|-------------|----------------|
| Qwen3.5-35B-A3B | 76 | 1,524 | **20.1×** |
| Qwen3.5-27B | 65 | 925 | **14.2×** |
| Qwen3.5-Plus | 63 | 731 | **11.6×** |
| GLM-5 | 61 | 396 | **6.5×** |
| Qwen3.5-9B | 77 | 80 | **1.04×** |
| Kimi K2.5 | 84 | 80 | **0.95×** |
| Mistral-119B | 49 | 50 | **1.02×** |

> 💡 **Massive insight:** For Qwen 3.5 local models, thinking mode uses **10-20× more tokens** with minimal score improvement. Kimi K2.5 and Mistral-119B show virtually no efficiency penalty from thinking — their reasoning is already baked in.
