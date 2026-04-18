# 🔬 Phase H — Dense Constraint Tests

[← Back to Main Results](../README.md)

## What Is Phase H?

Phase H is the **ceiling-breaker** for ClawEval. In Phase F, most strong models score 8–10 out of 10 on many tests — making it impossible to rank them. Phase H solves this by using **30–50 checkpoints per test** instead of 10, creating real spread between models that Phase F can't distinguish.

**Same roles. Same task types. Much harder.**

## How It Differs From Phase F

| | Phase F | Phase H |
|---|---|---|
| **Checkpoints per test** | ~10 | 30–50 |
| **Score scale** | /10 per test | Raw count (e.g., 29/30) |
| **Purpose** | Baseline capability | Fine-grained ranking |
| **Difficulty** | Standard | Adversarial edge cases, traps, sarcasm, near-truths |
| **Which models** | All models | Top-tier models only |

## How Tests Are Scored

Each test has a fixed answer key. Scores are **raw checkpoint counts** — not normalized to 10. A model scoring 26/30 on Sentiment is objectively weaker at sarcasm detection than one scoring 29/30. In Phase F, both would score 10/10.

**Scoring types used:**
- **json_values** — exact match on JSON key-value pairs (Input Validator, Sentiment, Research, Fact-Checking)
- **json_numeric** — numeric match within tolerance (STEM Analysis)
- **code_exec** — Python code execution against test cases (Code Generation, Algorithm)
- **content_planner** — structural constraint verification on generated calendars
- **news_errors** — factual error detection in news headlines
- **security_vulns** — vulnerability identification in code samples

## How To Run

```bash
# Basic run
python3 run_phase_h.py \
  --base-url http://YOUR_SERVER:8080/v1 \
  --model "Your-Model-Name" \
  --api-model "actual-model-filename.gguf" \
  --max-tokens 16000 \
  --timeout 600

# With reasoning budget (for llama.cpp / thinking models)
python3 run_phase_h.py \
  --base-url http://YOUR_SERVER:8080/v1 \
  --model "Your-Model-Name" \
  --api-model "actual-model-filename.gguf" \
  --max-tokens 16000 \
  --reasoning-budget-tokens 8192 \
  --timeout 1200

# Run specific tests only
python3 run_phase_h.py \
  --base-url http://YOUR_SERVER:8080/v1 \
  --model "Your-Model-Name" \
  --test-ids 2 5 36
```

**Key flags:**
- `--max-tokens 16000` — higher than Phase F (4000) because dense prompts produce longer responses
- `--timeout 600` — longer timeout for complex multi-part problems
- `--test-ids` — run specific tests by their Phase F ID (e.g., 2 = Input Validator)

**Runtime:** ~10–20 minutes for all 10 tests on a fast model (~75 t/s).

## The 10 Tests

| ID | Role | Checkpoints | What It Tests |
|----|------|------------|---------------|
| H-2 | Input Validator | 30 | Email, phone, URL, date, integer, username validation with unicode, injection, overflow traps |
| H-5 | Sentiment Analysis | 30 | Posts with sarcasm, passive-aggression, backhanded compliments, mixed signals |
| H-9 | Research Agent | 30 | Common misconceptions, near-truths, temporal tricks, half-truths |
| H-12 | Content Planner | 30 | 30 interlocking calendar constraints with cross-dependencies |
| H-18 | News Aggregation | 7 | Subtle factual errors in 20 news headlines (wrong airline, wrong planet, wrong year) |
| H-36 | Code Generation | 30 | 3 functions × 10 test cases: interval merging, RPN evaluator, deep flatten |
| H-40 | Fact-Checking | 30 | Science, tech, and CS claims with adversarial near-truths |
| H-48 | STEM Analysis | 15 | Multi-step physics, chemistry, and CS problems with unit conversion traps |
| H-49 | Algorithm | 30 | 3 data structures × 10 test cases: LRU Cache, MinStack, running median |
| H-56 | Security Analyst | 15 | 15 vulnerabilities in a realistic Flask web app |

**Total: 217 checkpoints** across 10 tests.

---

## Results

### Qwen3.6-35B-A3B (24GB VRAM, llama.cpp Q4_K_M, ~77 t/s)

*First model tested on Phase H.*

| Test | Score | % | Phase F | Notes |
|------|-------|---|---------|-------|
| H-2 Input Validator | 29/30 | 97% | 10/10 | Missed: 1-555-123-4567 classified as INVALID |
| H-5 Sentiment | 26/30 | 87% | 10/10 | Weak on sarcasm (#6, #11), passive-aggression (#15) |
| H-9 Research | 28/30 | 93% | 10/10 | Missed: human-banana DNA similarity, bacterial cell count |
| H-12 Content Planner | 25/30 | 83% | 10/10 | LinkedIn count off by 1, some constraints unverifiable |
| H-18 News Aggregation | 7/7 | 100% | 10/10 | Found all 7 headline errors perfectly |
| H-36 Code Generation | 30/30 | 100% | 10/10 | Perfect on all 3 functions × 10 test cases |
| H-40 Fact-Checking | 29/30 | 97% | 9/10 | Missed: Mercury as only liquid metal (gallium also melts near RT) |
| H-48 STEM Analysis | 15/15 | 100% | 10/10 | Perfect on all 15 multi-step STEM problems |
| H-49 Algorithm | 30/30 | 100% | 10/10 | Perfect: LRU Cache, MinStack, running median all passed |
| H-56 Security Analyst | 15/15 | 100% | 10/10 | Found all 15 vulnerabilities in Flask app |
| **Total** | **234/247** | **94.7%** | | |

> 💡 **Key finding:** Phase H creates real spread. Tests that were 10/10 in Phase F now show 83–97%, revealing genuine model weaknesses in sarcasm detection, obscure facts, and complex constraint satisfaction. Meanwhile, code generation and STEM remain at 100% — proving the model is genuinely strong there, not just coasting on easy tests.
