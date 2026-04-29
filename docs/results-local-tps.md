# Local Model TPS — RTX 3090 (24GB)

Phase H benchmark throughput on NVIDIA RTX 3090, measured across 59 tests.

| Model | Quant | Params | Avg t/s | Min t/s | Max t/s | Score | % |
|-------|-------|--------|---------|---------|---------|-------|---|
| LFM2.5-350M | Q4_K_M | 350M | 628.3 | 178.9 | 712.2 | 308/1220 | 25.2% |
| Gemma-4-E2B | BF16 | 2B | 101.1 | 98.9 | 111.7 | 981/1220 | 80.4% |
| Qwen3.6-35B-A3B | UD-Q4_K_M | 35B MoE (3B active) | 99.3 | 94.8 | 108.6 | 1029/1220 | 84.3% |
| Gemma-4-A4B | UD-Q4_K_M | 26B MoE (4B active) | 89.6 | 82.5 | 106.4 | 622/1220 | 51.0% |
| Gemma-4-E4B | BF16 | 4B | 61.8 | 59.7 | 66.0 | 867/1220 | 71.1% |
| Gemma-4-31B | Q4_K_M | 31B | 28.1 | 25.9 | 33.7 | 927/1220 | 76.0% |

> **🏆 Best local model**: Qwen3.6-35B-A3B — 99 t/s with 84.3% accuracy, ties Kimi K2.6 cloud!
>
> **Best value**: Gemma-4-E2B — 101 t/s with 80.4%, beats 120B cloud models.
>
> **Thinking model tax**: Gemma-4-A4B runs fast (90 t/s) but wastes tokens on CoT, scoring only 51%.
> Gemma-4-31B on Ollama Cloud (better quant) scored 83.9% vs 76.0% local Q4_K_M.
