# TurboQuant KV-Cache Experiment

## What is TurboQuant?

[TurboQuant](https://arxiv.org/abs/2504.19874) (Zandieh et al., ICLR 2026) compresses the attention KV cache using a Walsh–Hadamard transform followed by Lloyd–Max optimal scalar quantization. **Model weights are never touched** — only the per-layer KV cache that grows linearly with context length.

Key properties:
- Reduces KV cache from 8-bit (`q8_0`) to 2/3/4-bit per dimension
- 72–78% VRAM savings on the KV cache
- <10% throughput overhead
- Enables massive context expansion on consumer GPUs

## Why a Separate Section?

The variable being studied is **KV-cache precision**, not model capability. TurboQuant runs use the exact same GGUF weights as the baseline — the only difference is how the attention cache is stored in VRAM. Any quality delta comes purely from the KV-cache encoding.

## Hardware

- **GPU**: NVIDIA RTX 3090 (24GB)
- **Backend**: [TheTom/llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant), branch `feature/turboquant-kv-cache`, commit `11a241d`
- **Endpoint**: `http://192.168.0.187:8080` (LAN, OpenAI-compatible)

## Results

### Gemma-4-31B-it (Q4_K_M weights)

| KV Mode | Context | Score | % | Avg t/s | Notes |
|---------|---------|-------|---|---------|-------|
| q8_0 (baseline) | 53,248 | 927/1220 | 76.0% | 28.1 | Standard llama.cpp |
| turbo3 (3-bit) | 262,144 | 1014/1220 | 83.1% | 27.1 | TurboQuant fork — **+7.1% score, −3.6% speed for 4.9× context** |

**Context expansion**: 53K → 262K = **4.9× improvement** on the same 24GB GPU.

> ⚠️ The original turbo3 run scored 75.0% (915/1220), but 5 of those tests hit `500 Server Error` infrastructure failures. After retesting those 5 tests with stable infra, the corrected score is **83.1%** (1014/1220) — actually **exceeding** the q8₀ baseline. The +7.1% delta likely reflects longer-context benefits on some tests rather than KV precision gains, since the KV compression itself should be near-lossless.

> Note: This benchmark uses short prompts (Phase H tests are 8K–32K context). TurboQuant's impact may differ at longer contexts (>100K) where distant-token recall matters more.

## Methodology

- Same 59 Phase H v2 tests, same scoring, same `run_phase_h.py` harness
- `max_tokens=32000`, `reasoning_budget_tokens=4000` (thinking model)
- Baseline comparison: `Gemma-4-31B` Local Q4 run (standard llama.cpp, q8_0 KV, 53K context)

## References

- **Paper**: [TurboQuant — arXiv:2504.19874](https://arxiv.org/abs/2504.19874)
- **Upstream tracking**: [llama.cpp Discussion #20969](https://github.com/ggml-org/llama.cpp/discussions/20969)
- **Fork**: [TheTom/llama-cpp-turboquant](https://github.com/TheTom/llama-cpp-turboquant)
