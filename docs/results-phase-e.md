# Phase E — 12 Killer Tests (Reasoning, Code, Structured Output, Multi-Turn)

[← Back to Main Results](../README.md) · [Full Detailed Results →](../RESULTS.md)

All scores out of 10.

| # | Test | Category | GPT-OSS Low | GPT-OSS Med | GPT-OSS High | 122B Think | 27B Think | 35B Think | 27B NoThink | 122B NoThink | 35B NoThink |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Precise Counting | Reasoning | 🟡 6 | 🟡 6 | 🟡 6 | 🟢 8 | 🟡 6 | 🔴 4 | 🔴 4 | 🔴 0 | 🔴 4 |
| 2 | Constrained JSON | Structured | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 | 🟢 9 |
| 3 | Logic Grid Puzzle | Reasoning | 🟢 10 | 🟢 10 | 🟡 6 | 🟢 10 | 🟢 10 | 🟢 10 | 🟡 5 | 🟡 5 | 🟡 6 |
| 4 | Multi-Step Math | Reasoning | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 5 | Code Output Prediction | Code | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 |
| 6 | Contradiction Detection | Reasoning | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 | 🟡 5 |
| 7 | Complex Multi-Key Sort | Reasoning | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🟢 8 | 🔴 3 |
| 8 | Regex Construction | Code | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟡 7 |
| 9 | Data Transformation | Structured | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🔴 0 | 🔴 2 | 🔴 2 |
| 10 | Instruction Following | Instruction | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 8 | 🔴 4 | 🔴 2 | 🔴 4 |
| 11 | Multi-Turn Refinement | Multi-Turn | 🟢 10 | 🟢 10 | 🟢 10 | 🟡 7 | 🟢 10 | 🟢 8 | 🟢 10 | 🟢 8 | 🟢 9 |
| 12 | Multi-Turn State Track | Multi-Turn | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 10 | 🟢 9 | 🟡 7 | 🟢 10 | 🟡 7 |
| | **TOTAL** | | **109/120** | **109/120** | **105/120** | **108/120** | **109/120** | **102/120** | **83/120** | **79/120** | **76/120** |
| | **Percentage** | | **90.8%** | **90.8%** | **87.5%** | **90.0%** | **90.8%** | **85.0%** | **69.2%** | **65.8%** | **63.3%** |

### Key Takeaways

- **GPT-OSS-120B ties with 27B Think** at 109/120 (90.8%) — Low and Medium identical
- **GPT-OSS-120B High** drops to 87.5% due to Logic Grid (6/10) — higher reasoning can overthink
- **Thinking provides massive gains** on reasoning tasks: Logic 5→10, Data Transform 2→10, Instruction 2→10
- **Code tasks** are universally strong — all models score 10/10 on Code Output Prediction
- **Contradiction Detection** is hard for all models (ceiling of 5/10)
- **Multi-Turn** performance is generally strong across the board
