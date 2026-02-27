# Phase E: Killer Evaluation Comparison — Qwen3.5-35B-A3B MoE Q4_K_M

**Date:** 2026-02-26  
**Test Suite:** 12 tests (10 single-shot + 2 multi-turn agentic)  
**Scoring:** 100% automated, binary sub-checks  

---

## Head-to-Head: Thinking (32K budget) vs No-Think (4K budget)

| # | Test | Category | No-Think | Think | Δ |
|---|------|----------|:--------:|:-----:|:---:|
| 1 | Precise Counting | reasoning | 4 | 4 | = |
| 2 | Constrained JSON | structured | 9 | **10** | +1 |
| 3 | Logic Grid Puzzle | reasoning | 6 | **10** | **+4** |
| 4 | Multi-Step Math | reasoning | 10 | 10 | = |
| 5 | Code Output Prediction | code | 10 | 10 | = |
| 6 | Contradiction Detection | reasoning | 5 | 5 | = |
| 7 | Complex Multi-Key Sort | reasoning | 3 | **8** | **+5** |
| 8 | Regex Construction | code | 7 | **10** | **+3** |
| 9 | Data Transformation | structured | 2 | **10** | **+8** |
| 10 | Instruction Following | instruction | 4 | **8** | **+4** |
| 11 | Multi-Turn Code Refinement | multi_turn | **9** | 8 | -1 |
| 12 | Multi-Turn State Tracking | multi_turn | 7 | **9** | +2 |
| | **TOTAL** | | **76 (63.3%)** | **102 (85.0%)** | **+26** |

---

## Category Breakdown

| Category | No-Think | Think | Winner |
|----------|:--------:|:-----:|:------:|
| Code | 85% | **100%** | Think |
| Multi-Turn (Agentic) | 80% | **85%** | Think |
| Reasoning | 56% | **74%** | Think |
| Structured Output | 55% | **100%** | Think |
| Instruction Following | 40% | **80%** | Think |

---

## Resource Usage

| Metric | No-Think | Think |
|--------|:--------:|:-----:|
| Total tokens | ~3K | ~92K |
| Total time | ~30s | ~15min |
| Avg speed | ~85 t/s | ~95 t/s |
| Token budget | 4,000 | 32,000 |

---

## Key Findings

> [!IMPORTANT]
> Phase E is the **first eval that clearly differentiates thinking vs no-think**.
> Previous phases (A, D) actually scored *better* without thinking.

**Where thinking helps most (Δ ≥ +3):**
- Data Transformation: +8 (2→10) — step-by-step pipeline execution
- Complex Sorting: +5 (3→8) — multi-key tie-breaking requires tracking
- Logic Grid Puzzle: +4 (6→10) — constraint propagation benefits from reasoning
- Instruction Chain: +4 (4→8) — sequential operations on text
- Regex Construction: +3 (7→10) — edge case handling in pattern design

**Where thinking doesn't help (Δ = 0):**
- Precise Counting: 4=4 — both modes struggle equally with counting
- Multi-Step Math: 10=10 — both perfect
- Code Output: 10=10 — both perfect
- Contradictions: 5=5 — both partial (scorer limitation)

**Where nothink wins (Δ < 0):**
- Multi-Turn Code Refinement: 9>8 — thinking produced too many assertions, missed count constraint

## Recommendation for OpenClaw

For agentic workflows, a **hybrid approach** would be optimal:
- Use **no-think** for simple routing, format, tool-call tasks (fast, efficient)
- Use **thinking** for complex reasoning: data transforms, logic puzzles, multi-constraint problems
- The model's multi-turn capability is strong in both modes (80-85%)
