# ☁️ Cloud Models — Kimi K2.5 (Phase F + Phase G)

[← Back to Main Results](../README.md) · [Phase G Discriminator Tests →](results-phase-g.md)

## Phase F — 59-Role Evaluation

| # | Agent Role | K2.5 Think | K2.5 NoThink |
|---|---|---|---|
| | | moonshotai/Kimi-K2.5 | moonshotai/Kimi-K2.5 |
| | | Alibaba Coding Plan | `thinking: False` |
| | **Tier 1 — Utility** | | |
| 1 | Router / Triage | 🟢 9 | 🟢 9 |
| 2 | Input Validator | 🟢 10 | 🟢 10 |
| 3 | Health Monitor | 🟡 5 | 🟡 5 |
| 4 | Notification | 🟢 9 | 🟢 9 |
| 5 | Sentiment | 🟢 10 | 🟢 10 |
| 6 | FAQ Generation | 🟡 **7** | 🟡 6 |
| 7 | Translation | 🟢 9 | 🟢 9 |
| 8 | Calendar | 🔴 0 | 🔴 0 |
| | **Tier 2 — Moderate** | | |
| 9 | Research Agent | 🟢 10 | 🟢 10 |
| 10 | Content Writer | 📝 5 | 📝 5 |
| 11 | Editor | 🟢 **10** | 🟢 9 |
| 12 | Content Planner | 🟢 10 | 🟢 10 |
| 13 | Email Drafting | 🟢 **10** | 🟢 9 |
| 14 | Doc Summary | 🟢 8 | 🟢 8 |
| 15 | Meeting Notes | 🟢 10 | 🟢 10 |
| 16 | Social Scouting | 🟢 10 | 🟢 10 |
| 17 | Social Content | 📝 5 | 📝 5 |
| 18 | News Aggregation | 🟢 10 | 🟢 10 |
| 19 | Shopping | 🟢 10 | 🟢 10 |
| 20 | Memory Mgmt | 🟢 9 | 🟢 9 |
| 21 | RAG / Retrieval | 🟡 6 | 🟡 6 |
| 22 | Data Analysis | 🔴 2 | 🔴 2 |
| 23 | Web Scraping | 🟢 10 | 🟢 10 |
| 24 | Image Description | 📝 5 | 📝 5 |
| 25 | Customer Support | 🟢 10 | 🟢 10 |
| 26 | Lead Scoring | 🟢 8 | 🟢 8 |
| 27 | Sprint Summary | 🟡 **7** | 🟡 5 |
| 28 | Transaction | 🟢 9 | 🟢 9 |
| 29 | Home Automation | 🟢 10 | 🟢 10 |
| 30 | Fitness Tracking | 🟢 8 | 🟢 8 |
| 31 | Recipe / Cooking | 🔴 1 | 🔴 1 |
| 32 | Personal Finance | 🟡 5 | 🟡 5 |
| 33 | SEO Optimization | 🟢 9 | 🟢 9 |
| 34 | Landing Page | 📝 5 | 📝 5 |
| 35 | Travel Planning | 🟢 10 | 🟢 10 |
| | **Tier 3 — Advanced** | | |
| 36 | Code Generation | 🟢 10 | 🟢 10 |
| 37 | Code Review | 🟢 10 | 🟢 10 |
| 38 | QA / Test Writing | 🟢 8 | 🟢 8 |
| 39 | Task Planning | 🟢 10 | 🟢 10 |
| 40 | Fact-Checking | 🟢 10 | 🟢 10 |
| 41 | Critic / Review | 📝 5 | 📝 5 |
| 42 | Market Research | 🟢 8 | 🟢 8 |
| 43 | Synthesizer | 🟢 9 | 🟢 **10** |
| 44 | Curriculum Design | 🟡 6 | 🟡 **7** |
| 45 | Prototype Gen | 🟡 5 | 🟡 5 |
| 46 | DevOps | 🟢 10 | 🟢 10 |
| | **Tier 4 — Expert** | | |
| 47 | Math / Logic | 🟢 8 | 🟢 8 |
| 48 | STEM Analysis | 🟢 10 | 🟢 10 |
| 49 | Algorithm | 🟢 10 | 🟢 10 |
| | **Tier 5 — Senior** | | |
| 50 | Orchestrator | 🟢 8 | 🟢 8 |
| 51 | Architect | 🟢 **10** | 🟢 9 |
| 52 | Debugger | 🟢 10 | 🟢 10 |
| 53 | Legal Review | 🟢 10 | 🟢 10 |
| 54 | Medical | 🟢 9 | 🟢 9 |
| 55 | Financial | 🟢 10 | 🟢 10 |
| 56 | Security | 🟢 10 | 🟢 10 |
| 57 | SRE / Incident | 🔴 **3** | 🔴 2 |
| 58 | Book Writing | 📝 5 | 📝 5 |
| 59 | Compliance | 🟢 8 | 🟢 **9** |
| | **TOTAL** | **473/590 (80%)** | **469/590 (80%)** |

### Tier Breakdown

| Tier | Think | NoThink |
|------|-------|---------|
| 1 — Utility | 59/80 (74%) | 58/80 (73%) |
| 2 — Moderate | 222/270 (82%) | 218/270 (81%) |
| 3 — Advanced | 91/110 (83%) | 93/110 (85%) |
| 4 — Expert | 28/30 (**93%**) | 28/30 (**93%**) |
| 5 — Senior | 83/100 (83%) | 82/100 (82%) |

### Think vs NoThink Comparison

Only 9 out of 59 tests differ — Kimi K2.5 is remarkably consistent regardless of thinking mode.

**Think wins (5 tests):**
- Sprint Summarizer: 7 vs 5 (+2)
- Editor: 10 vs 9
- Email Drafting: 10 vs 9
- Architect: 10 vs 9
- FAQ Gen: 7 vs 6

**NoThink wins (3 tests):**
- Synthesizer: 10 vs 9
- Curriculum Design: 7 vs 6
- Compliance: 9 vs 8

**Tied on 50/59 tests** including all Expert and most Senior roles.

### Notes

- Kimi K2.5 tested via Alibaba Coding Plan API (cloud, not local)
- Social Scouting scored 10 (capped from raw score due to scoring bug)
- 📝 Manual review tests default to 5/10 pending human review
- Calendar (0/10) and Recipe (1/10) are hard for all models
- **Expert tier (93%)** is the strongest — STEM 10/10, Algorithm 10/10, Math 8/10

---

## Phase G — Discriminator Scores (Harder Tests)

See [Phase G Results](results-phase-g.md#%EF%B8%8F-cloud-models) for the 11 harder tests:
- **Think: 96/110 (87%)** — No test below 7/10
- **NoThink: 91/110 (83%)**

Key Phase G difference: Content Planner Think 7/10 vs NoThink 1/10 — thinking genuinely helps for complex constraint satisfaction.

---

[← Back to Main Results](../README.md)
