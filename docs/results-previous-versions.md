# Previous Versions — Superseded Models

[← Back to Main Results](../README.md)

When a newer version of a model family is tested on the same deployment type (cloud or local) at a comparable size, the older versions move here so the main leaderboard shows only current models. **Scores are unchanged** and every result directory is still in the repo. All rows are ClawEval v2 (59 agents, 1,220 checkpoints).

| Model | Provider | Score | % | Perfect | Replaced by | Results |
|-------|----------|-------|---|---------|-------------|---------|
| **DeepSeek family** | | | | | | |
| DeepSeek V4 Flash | ☁️ DeepSeek | 1054/1220 | **86.4%** | 23 | DeepSeek V4.1 Flash | [`DeepSeek-V4-Flash`](../eval/test_results/DeepSeek-V4-Flash/phase_h/) |
| **GLM family** | | | | | | |
| GLM-5.1 | ☁️ Ollama | 1020/1220 | **83.6%** | 26 | GLM-5.3 | [`GLM-5.1`](../eval/test_results/GLM-5.1/phase_h/) |
| GLM-5.2 | ☁️ Ollama | 957/1220 | **78.4%** | 23 | GLM-5.3 | [`GLM-5.2-Think`](../eval/test_results/GLM-5.2-Think/phase_h/) |
| GLM-5 NoThink | ☁️ Ollama | 948/1220 | **77.7%** | 25 | GLM-5.3 | [`glm-5-nothink`](../eval/test_results/glm-5-nothink/phase_h/) |
| GLM-5 Think | ☁️ Ollama | 927/1220 | **76.0%** | 23 | GLM-5.3 | [`glm-5-think`](../eval/test_results/glm-5-think/phase_h/) |
| **Kimi family** | | | | | | |
| Kimi K2.5 Think | ☁️ Ollama | 1048/1220 | **85.9%** | 24 | Kimi K2.7 Code | [`kimi-k2.5-think`](../eval/test_results/kimi-k2.5-think/phase_h/) |
| Kimi K2.7 Code | ☁️ Ollama | 1038/1220 | **85.1%** | 24 | Kimi K3 | [`Kimi-K2.7-Code`](../eval/test_results/Kimi-K2.7-Code/phase_h/) |
| Kimi K2.6 | ☁️ Ollama | 1028/1220 | **84.3%** | 24 | Kimi K2.7 Code | [`Kimi-K2.6`](../eval/test_results/Kimi-K2.6/phase_h/) |
| Kimi K2.5 NoThink | ☁️ Ollama | 935/1220 | **76.6%** | 21 | Kimi K2.7 Code | [`kimi-k2.5-nothink`](../eval/test_results/kimi-k2.5-nothink/phase_h/) |
| **MiniMax family** | | | | | | |
| MiniMax-M2.7 Medium | ☁️ Ollama | 1014/1220 | **83.1%** | 20 | MiniMax-M3 | [`MiniMax-M2.7-Medium`](../eval/test_results/MiniMax-M2.7-Medium/phase_h/) |
| MiniMax-M2.7 Think | ☁️ Ollama | 993/1220 | **81.4%** | 19 | MiniMax-M3 | [`MiniMax-M2.7-Think`](../eval/test_results/MiniMax-M2.7-Think/phase_h/) |
| **Qwen family** | | | | | | |
| Qwen3.6-27B (TurboQuant4) | 🖥️ Local TQ4 | 1012/1220 | **83.0%** | 26 | Qwen3.8-27B | [`Qwen3.6-27B-Local`](../eval/test_results/Qwen3.6-27B-Local/phase_h/) |

> Rule: same family + same deployment type + comparable size, newer version tested → older rows move here. Local and cloud entries are tracked separately, so a local small model is only superseded by a newer local model of similar size.
