# ☁️ Cloud Models — Kimi K2.5 (Phase F + Phase G)

[← Back to Main Results](../README.md) · [Phase G Discriminator Tests →](results-phase-g.md)

## Phase F — 59-Role Evaluation

| # | Agent Role | K2.5 Think |
|---|---|---|
| | | moonshotai/Kimi-K2.5 |
| | | Alibaba Coding Plan |
| | **Tier 1 — Utility** | |
| 1 | Router / Triage | 🟢 9 |
| 2 | Input Validator | 🟢 10 |
| 3 | Health Monitor | 🟡 5 |
| 4 | Notification | 🟢 9 |
| 5 | Sentiment | 🟢 10 |
| 6 | FAQ Generation | 🟡 7 |
| 7 | Translation | 🟢 9 |
| 8 | Calendar | 🔴 0 |
| | **Tier 2 — Moderate** | |
| 9 | Research Agent | 🟢 10 |
| 10 | Content Writer | 📝 5 |
| 11 | Editor | 🟢 10 |
| 12 | Content Planner | 🟢 10 |
| 13 | Email Drafting | 🟢 10 |
| 14 | Doc Summary | 🟢 8 |
| 15 | Meeting Notes | 🟢 10 |
| 16 | Social Scouting | 🟢 10 |
| 17 | Social Content | 📝 5 |
| 18 | News Aggregation | 🟢 10 |
| 19 | Shopping | 🟢 10 |
| 20 | Memory Mgmt | 🟢 9 |
| 21 | RAG / Retrieval | 🟡 6 |
| 22 | Data Analysis | 🔴 2 |
| 23 | Web Scraping | 🟢 10 |
| 24 | Image Description | 📝 5 |
| 25 | Customer Support | 🟢 10 |
| 26 | Lead Scoring | 🟢 8 |
| 27 | Sprint Summary | 🟡 7 |
| 28 | Transaction | 🟢 9 |
| 29 | Home Automation | 🟢 10 |
| 30 | Fitness Tracking | 🟢 8 |
| 31 | Recipe / Cooking | 🔴 1 |
| 32 | Personal Finance | 🟡 5 |
| 33 | SEO Optimization | 🟢 9 |
| 34 | Landing Page | 📝 5 |
| 35 | Travel Planning | 🟢 10 |
| | **Tier 3 — Advanced** | |
| 36 | Code Generation | 🟢 10 |
| 37 | Code Review | 🟢 10 |
| 38 | QA / Test Writing | 🟢 8 |
| 39 | Task Planning | 🟢 10 |
| 40 | Fact-Checking | 🟢 10 |
| 41 | Critic / Review | 📝 5 |
| 42 | Market Research | 🟢 8 |
| 43 | Synthesizer | 🟢 9 |
| 44 | Curriculum Design | 🟡 6 |
| 45 | Prototype Gen | 🟡 5 |
| 46 | DevOps | 🟢 10 |
| | **Tier 4 — Expert** | |
| 47 | Math / Logic | 🟢 8 |
| 48 | STEM Analysis | 🟢 10 |
| 49 | Algorithm | 🟢 10 |
| | **Tier 5 — Senior** | |
| 50 | Orchestrator | 🟢 8 |
| 51 | Architect | 🟢 10 |
| 52 | Debugger | 🟢 10 |
| 53 | Legal Review | 🟢 10 |
| 54 | Medical | 🟢 9 |
| 55 | Financial | 🟢 10 |
| 56 | Security | 🟢 10 |
| 57 | SRE / Incident | 🔴 3 |
| 58 | Book Writing | 📝 5 |
| 59 | Compliance | 🟢 8 |
| | **TOTAL** | **483/590 (82%)** |

### Tier Breakdown

| Tier | Score | % |
|------|-------|---|
| 1 — Utility | 59/80 | 74% |
| 2 — Moderate | 222/270 | 82% |
| 3 — Advanced | 91/110 | 83% |
| 4 — Expert | 28/30 | **93%** |
| 5 — Senior | 83/100 | 83% |

### Notes

- Kimi K2.5 tested via Alibaba Coding Plan API (cloud, not local)
- Social Scouting scored 10 (capped from raw 20 due to scoring bug)
- 📝 Manual review tests default to 5/10 pending human review
- Calendar (0/10) and Recipe (1/10) are hard for all models — no model scores well
- **Expert tier (93%)** is the strongest — STEM 10/10, Algorithm 10/10, Math 8/10
- **NoThink results pending** — will be added as second column after testing

---

## Phase G — Discriminator Scores

See [Phase G Results](results-phase-g.md#%EF%B8%8F-cloud-models) for the 11 harder tests:
- **Think: 96/110 (87%)** — No test below 7/10
- **NoThink: 91/110 (83%)**

---

[← Back to Main Results](../README.md)
