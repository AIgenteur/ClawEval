"""Phase H Dense Tests — Batch 5: Tests 6, 7, 15, 29, 33, 35, 39, 44, 45, 46, 50, 51, 52, 53, 54, 55, 57, 59
Remaining constraint-based and keyword-detection tests."""

PHASE_H_BATCH5 = [
    # H-6: FAQ GENERATION — 15 constraints
    {
        "id": 6, "role": "FAQ Generation Agent", "tier": 1,
        "scoring_type": "json_values",
        "prompt": """Generate a FAQ section for a SaaS project management tool. Answer these 15 questions exactly. Respond as JSON: {"q1": "answer", ...}. Keep answers to 1-2 sentences.

q1: What is the free plan limit for users?
Answer must state: 5 users

q2: Can I import data from Trello?
Answer must state: Yes, CSV and API import supported

q3: Is there a mobile app?
Answer must state: iOS and Android

q4: What is the uptime SLA?
Answer must state: 99.9%

q5: How is data encrypted?
Answer must state: AES-256 at rest, TLS 1.3 in transit

q6: Can I set up SSO?
Answer must state: SAML 2.0 and OIDC supported on Business plan

q7: What integrations are available?
Answer must state: Slack, GitHub, Jira, Google Workspace, and 50+ via Zapier

q8: What is the maximum file attachment size?
Answer must state: 25MB per file, 10GB per project

q9: Is there a self-hosted option?
Answer must state: Enterprise plan only

q10: How do I cancel my subscription?
Answer must state: Settings > Billing > Cancel, effective end of billing period

q11: Do you offer annual billing discounts?
Answer must state: 20% discount on annual plans

q12: What happens to my data after cancellation?
Answer must state: Data retained for 30 days, then permanently deleted

q13: Is there an API?
Answer must state: RESTful API with rate limit of 1000 requests per minute

q14: What project methodologies are supported?
Answer must state: Kanban, Scrum, Waterfall, and hybrid

q15: How do I contact support?
Answer must state: Email, live chat (business hours), and phone (Enterprise only)""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "q1_users": "5", "q2_import": "yes", "q3_mobile": "iOS and Android",
                "q4_sla": "99.9", "q5_encryption": "AES-256",
                "q6_sso": "SAML", "q7_integrations": "Slack",
                "q8_file_size": "25MB", "q9_self_hosted": "Enterprise",
                "q10_cancel": "Settings", "q11_discount": "20",
                "q12_data_retention": "30 days", "q13_api": "1000",
                "q14_methodologies": "Kanban", "q15_support": "live chat"
            }
        }
    },

    # H-7: TRANSLATION CONSTRAINTS — 15 checks
    {
        "id": 7, "role": "Translation Agent", "tier": 1,
        "scoring_type": "json_values",
        "prompt": """Translate this English marketing copy to Spanish, French, and German. Then verify 15 constraints. Respond as JSON with translations and constraint verification.

English: "Get 30% off your first order! Use code WELCOME30 at checkout. Free shipping on orders over $50. Limited time offer — expires December 31, 2024. Terms and conditions apply."

{"spanish": "...", "french": "...", "german": "...", "checks": {"c1": "yes/no", ...}}

Constraints to verify (answer yes/no):
c1: Spanish translation preserves the 30% number
c2: French translation preserves the code WELCOME30 unchanged
c3: German translation preserves the $50 threshold
c4: Spanish translation includes the expiration date
c5: All three translations preserve the code WELCOME30 exactly (not translated)
c6: French uses formal "vous" form
c7: German translation uses "Geschäftsbedingungen" or equivalent for T&C
c8: Spanish uses exclamation marks at beginning and end (¡...!)
c9: All translations preserve December 31, 2024 date
c10: None of the translations translate the word "WELCOME30"
c11: French translation includes "livraison gratuite" or equivalent for free shipping
c12: German uses "Bestellung" or "Auftrag" for "order"
c13: Spanish translation starts with an imperative or promotional verb
c14: All translations maintain the urgency ("limited time" equivalent)
c15: None of the translations add information not in the original""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "c1": "yes", "c2": "yes", "c3": "yes", "c4": "yes",
                "c5": "yes", "c6": "yes", "c7": "yes", "c8": "yes",
                "c9": "yes", "c10": "yes", "c11": "yes", "c12": "yes",
                "c13": "yes", "c14": "yes", "c15": "yes"
            }
        }
    },

    # H-15: MEETING NOTES — 20 action items
    {
        "id": 15, "role": "Meeting Notes / Transcription Agent", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Extract all 20 action items from this meeting transcript. For each, identify: owner, task, deadline. Respond as JSON: {"actions": [{"id": 1, "owner": "name", "task": "...", "deadline": "..."}, ...]}

Transcript:
"Alice: OK let's go through the items. First, Bob, can you have the API documentation updated by end of this week? Bob: Sure, I'll get that done by Friday. Alice: Great. Carol, we need the Q4 budget proposal. Can you have a draft by March 15? Carol: I'll aim for March 14 actually. Alice: Even better. Dave, the client demo is on March 20 — please prepare the slide deck by March 18. Dave: Got it. Alice: Bob, one more thing — the security audit findings need a response plan. Let's say by next Monday. Bob: Will do.

Carol: I also wanted to mention that we need someone to review the vendor contracts. Alice: Good point. Eve, can you handle that? Deadline is end of month. Eve: Sure. Frank, can you help Eve with the compliance section? Frank: Yes, I'll coordinate with Eve and have my part done by March 22.

Alice: Moving on to engineering. Dave, please set up the staging environment for the new release by March 12. Dave: Already started, will finish by then. Alice: Bob, the load testing results — when can we expect those? Bob: I can have initial results by March 13 and final report by March 16. Alice: Good, both of those please.

Carol: What about the customer survey results? Alice: Right. Carol, please compile the survey report by March 17. Carol: OK. Alice: Eve, we need the onboarding guide updated for new hires starting April 1. Eve: I'll have it done by March 25. Alice: Dave, please update the CI/CD pipeline configs by March 14. Dave: Will do.

Frank: Should I also update the team wiki? Alice: Yes please, Frank, by end of next week. Alice: Bob, we need API rate limiting implemented before the launch. Deadline is March 19. Bob: Tight but doable. Alice: Carol, please schedule the all-hands meeting for March 21. Carol: Done. Alice: And finally, Eve, please order the new equipment by March 11. Eve: I'll do it today. Alice: Dave, one more — please write the release notes by March 18. Dave: Got it."

Find ALL 20 action items with correct owner and deadline.""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "a1_owner": "Bob", "a1_deadline": "Friday",
                "a2_owner": "Carol", "a2_deadline": "March 14",
                "a3_owner": "Dave", "a3_deadline": "March 18",
                "a4_owner": "Bob", "a4_deadline": "Monday",
                "a5_owner": "Eve", "a5_deadline": "end of month",
                "a6_owner": "Frank", "a6_deadline": "March 22",
                "a7_owner": "Dave", "a7_deadline": "March 12",
                "a8_owner": "Bob", "a8_deadline": "March 13",
                "a9_owner": "Bob", "a9_deadline": "March 16",
                "a10_owner": "Carol", "a10_deadline": "March 17",
                "a11_owner": "Eve", "a11_deadline": "March 25",
                "a12_owner": "Dave", "a12_deadline": "March 14",
                "a13_owner": "Frank", "a13_deadline": "end of next week",
                "a14_owner": "Bob", "a14_deadline": "March 19",
                "a15_owner": "Carol", "a15_deadline": "March 21",
                "a16_owner": "Eve", "a16_deadline": "March 11",
                "a17_owner": "Dave", "a17_deadline": "March 18",
                "a18_count": "20"
            }
        }
    },

    # H-39: TASK DECOMPOSITION — 20 subtasks
    {
        "id": 39, "role": "Task Planning / Decomposition", "tier": 3,
        "scoring_type": "json_values",
        "prompt": """Decompose "Migrate a monolithic Django app to microservices" into exactly 20 ordered subtasks with dependencies. Respond as JSON: {"tasks": [{"id": 1, "task": "...", "depends_on": [], "effort_days": N, "team": "backend/frontend/devops/qa"}, ...]}

Requirements:
- Exactly 20 tasks
- Each task must have a team assignment from: backend, frontend, devops, qa
- Dependencies must be valid (no circular deps, can't depend on later tasks)
- Total effort must be between 80-120 days
- At least 3 tasks for each team
- First task must have no dependencies
- Last task must depend on at least 2 other tasks
- At least 2 tasks must be parallelizable (no dependency between them)
- Include database migration, API gateway setup, CI/CD, and testing tasks

Verify your constraints and respond with the task list.""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "task_count": "20",
                "has_backend": "yes", "has_frontend": "yes",
                "has_devops": "yes", "has_qa": "yes",
                "first_no_deps": "yes", "last_multi_deps": "yes",
                "no_circular": "yes", "parallelizable": "yes",
                "has_db_migration": "yes", "has_api_gateway": "yes",
                "has_cicd": "yes", "has_testing": "yes",
                "total_effort_valid": "yes",
                "backend_min_3": "yes", "frontend_min_3": "yes",
                "devops_min_3": "yes", "qa_min_3": "yes"
            }
        }
    },

    # H-46: DEVOPS — 15 issues to detect
    {
        "id": 46, "role": "DevOps Agent", "tier": 3,
        "scoring_type": "json_values",
        "prompt": """Find ALL 15 issues in this Kubernetes deployment config. For each, identify the issue and severity. Respond as JSON: {"issues": [{"line": "...", "issue": "...", "severity": "critical/major/minor"}, ...], "count": 15}

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-api
spec:
  replicas: 1
  selector:
    matchLabels:
      app: web-api
  template:
    metadata:
      labels:
        app: web-api
    spec:
      containers:
      - name: api
        image: myapp:latest
        ports:
        - containerPort: 8080
        resources: {}
        securityContext:
          runAsRoot: true
          privileged: true
        env:
        - name: DB_PASSWORD
          value: "sup3rs3cret!"
        - name: API_KEY
          value: "ak_live_12345"
        volumeMounts:
        - mountPath: /data
          name: data-vol
      - name: sidecar
        image: logger:v1
        resources:
          requests:
            memory: "10Gi"
            cpu: "8"
      volumes:
      - name: data-vol
        hostPath:
          path: /tmp/data
---
apiVersion: v1
kind: Service
metadata:
  name: web-api
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: web-api
```""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "i1": "image uses :latest tag",
                "i2": "only 1 replica - no HA",
                "i3": "no resource limits or requests on api container",
                "i4": "runAsRoot true",
                "i5": "privileged true",
                "i6": "DB_PASSWORD in plaintext",
                "i7": "API_KEY in plaintext",
                "i8": "hostPath volume - not portable",
                "i9": "hostPath in /tmp - insecure",
                "i10": "sidecar requests 10Gi memory - excessive",
                "i11": "sidecar requests 8 CPU - excessive",
                "i12": "no liveness/readiness probes",
                "i13": "no pod disruption budget",
                "i14": "LoadBalancer exposed externally without ingress",
                "i15": "no network policy"
            }
        }
    },

    # H-53: LEGAL REVIEW — 15 issues
    {
        "id": 53, "role": "Legal Document Review", "tier": 5,
        "scoring_type": "json_values",
        "prompt": """Find ALL 15 legal issues in this SaaS service agreement. For each, identify the clause, issue, and risk level. Respond as JSON: {"issues": [{"clause": "...", "issue": "...", "risk": "high/medium/low"}, ...], "count": 15}

Agreement:
"TERMS OF SERVICE
1. LICENSE: Company grants User a perpetual, irrevocable license to use the Software. Company may terminate this license at any time without cause or notice.
2. DATA: All data uploaded by User becomes the exclusive property of Company. Company may use, sell, or share User data with any third party for any purpose without consent.
3. LIABILITY: Company's total liability shall not exceed $100, regardless of the nature of the claim. User waives all rights to consequential, incidental, punitive, or any other damages.
4. INDEMNIFICATION: User shall indemnify Company against any and all claims, including those arising from Company's own negligence or willful misconduct.
5. PAYMENT: Company may increase pricing at any time. Failure to pay within 24 hours of invoice results in immediate account termination and forfeiture of all data.
6. SLA: Company targets 95% uptime but makes no guarantees. Credits will not be issued for any downtime, scheduled or unscheduled.
7. INTELLECTUAL PROPERTY: Any feedback, suggestions, or ideas submitted by User become Company's intellectual property without compensation.
8. DISPUTE RESOLUTION: All disputes shall be resolved exclusively in Company's home jurisdiction. User waives right to jury trial and class action participation.
9. CHANGES: Company may modify these terms at any time. Continued use constitutes acceptance.
10. TERMINATION: Upon termination, Company may delete all User data immediately with no obligation to provide export or backup." """,
        "scoring": {
            "type": "json_values",
            "answers": {
                "i1": "contradictory license terms - perpetual but terminable without notice",
                "i2": "data ownership transfer - user loses rights to own data",
                "i3": "unlimited data sharing with third parties without consent",
                "i4": "liability cap unreasonably low at $100",
                "i5": "waiver of all consequential damages",
                "i6": "indemnification covers company's own negligence",
                "i7": "24-hour payment deadline with data forfeiture",
                "i8": "no SLA guarantees despite being paid service",
                "i9": "no downtime credits",
                "i10": "forced IP assignment for user feedback",
                "i11": "waiver of jury trial rights",
                "i12": "waiver of class action rights",
                "i13": "unilateral price changes without notice",
                "i14": "unilateral term changes without notice",
                "i15": "immediate data deletion on termination with no export"
            }
        }
    },

    # H-54: MEDICAL ANALYSIS — 15 findings
    {
        "id": 54, "role": "Medical / Health Analysis", "tier": 5,
        "scoring_type": "json_values",
        "prompt": """Analyze this patient's lab results and identify ALL 15 findings (normal, abnormal high, abnormal low). Respond as JSON: {"findings": [{"test": "...", "value": N, "status": "normal/high/low", "concern": "..."}, ...]}

Patient: 45-year-old male, BMI 31, Type 2 Diabetes, on Metformin

Lab Results:
1. Fasting Glucose: 185 mg/dL (normal: 70-100)
2. HbA1c: 8.2% (normal: <5.7%, diabetic target: <7%)
3. Total Cholesterol: 265 mg/dL (desirable: <200)
4. LDL Cholesterol: 175 mg/dL (optimal: <100)
5. HDL Cholesterol: 32 mg/dL (normal male: >40)
6. Triglycerides: 290 mg/dL (normal: <150)
7. Blood Pressure: 148/94 mmHg (normal: <120/80)
8. Creatinine: 1.4 mg/dL (normal: 0.7-1.3)
9. eGFR: 58 mL/min (normal: >90)
10. ALT: 52 U/L (normal: 7-35)
11. AST: 28 U/L (normal: 8-33)
12. TSH: 6.8 mIU/L (normal: 0.4-4.0)
13. Vitamin D: 18 ng/mL (normal: 30-100)
14. Hemoglobin: 13.5 g/dL (normal male: 13.5-17.5)
15. Potassium: 3.2 mEq/L (normal: 3.5-5.0)""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1_status": "high", "2_status": "high",
                "3_status": "high", "4_status": "high",
                "5_status": "low", "6_status": "high",
                "7_status": "high", "8_status": "high",
                "9_status": "low", "10_status": "high",
                "11_status": "normal", "12_status": "high",
                "13_status": "low", "14_status": "normal",
                "15_status": "low"
            }
        }
    },

    # H-55: FINANCIAL ANALYSIS — 15 calculations
    {
        "id": 55, "role": "Financial Analysis / Stock Research", "tier": 5,
        "scoring_type": "json_numeric",
        "prompt": """Calculate 15 financial metrics from these company financials. Respond as JSON: {"f1": value, ...}. Round to 2 decimal places.

Income Statement (Annual, $M):
Revenue: 850, COGS: 340, Gross Profit: 510
Operating Expenses: 280, Operating Income: 230
Interest Expense: 15, EBT: 215, Tax (25%): 53.75, Net Income: 161.25
Shares Outstanding: 50M, Dividends Paid: $40M

Balance Sheet ($M):
Total Assets: 1200, Current Assets: 480, Cash: 120
Total Liabilities: 520, Current Liabilities: 200, Long-term Debt: 250
Stockholders' Equity: 680
Accounts Receivable: 95, Inventory: 85

Cash Flow:
Operating Cash Flow: 195, CapEx: 65, Free Cash Flow: 130

Questions:
f1: Gross margin (%)
f2: Operating margin (%)
f3: Net profit margin (%)
f4: EPS ($)
f5: P/E ratio if stock price is $48.00
f6: Return on equity (%)
f7: Return on assets (%)
f8: Current ratio
f9: Debt-to-equity ratio
f10: Dividend per share ($)
f11: Dividend payout ratio (%)
f12: Free cash flow per share ($)
f13: Inventory turnover (COGS/Inventory)
f14: Days sales outstanding (AR/Revenue × 365)
f15: Enterprise value if market cap is $2400M and cash is $120M and debt is $250M ($M)""",
        "scoring": {
            "type": "json_numeric",
            "answers": {
                "f1": 60.0, "f2": 27.06, "f3": 18.97,
                "f4": 3.23, "f5": 14.88, "f6": 23.71,
                "f7": 13.44, "f8": 2.40, "f9": 0.76,
                "f10": 0.80, "f11": 24.81, "f12": 2.60,
                "f13": 4.0, "f14": 40.79, "f15": 2530
            },
            "tolerance": 0.05
        }
    },

    # H-57: SRE / INCIDENT — 15 metrics
    {
        "id": 57, "role": "SRE / Incident Response", "tier": 5,
        "scoring_type": "json_values",
        "prompt": """Analyze this incident timeline and answer 15 questions. Respond as JSON: {"q1": "answer", ...}

Incident Timeline (all times UTC):
02:15 - Monitoring alert: API error rate >5% (threshold: 2%)
02:18 - PagerDuty notifies on-call engineer (Alice)
02:22 - Alice acknowledges alert, begins investigation
02:28 - Alice identifies database connection pool exhaustion
02:30 - Alice attempts connection pool restart — fails
02:35 - Alice escalates to database team (Bob)
02:40 - Bob joins, finds max_connections hit (500/500)
02:45 - Bob identifies runaway query from batch job consuming 200 connections
02:48 - Bob kills the runaway batch job
02:50 - Connection pool begins recovering
02:55 - Error rate drops below 5%
03:00 - Error rate returns to normal (<0.1%)
03:05 - Alice declares incident resolved
03:15 - Alice sends initial incident report to stakeholders
04:00 - Post-incident review scheduled for 10:00

Questions:
q1: Time from alert to acknowledgment (minutes)
q2: Time from alert to resolution (minutes)
q3: Time from detection to root cause identified (minutes)
q4: MTTR — Mean Time to Repair (alert to error rate normal, minutes)
q5: Time to escalate (minutes from ack to escalation)
q6: Who was the incident commander?
q7: What was the root cause?
q8: Time from escalation to fix applied (minutes)
q9: How many connections were consumed by the runaway query?
q10: What was the max connection limit?
q11: Was the initial fix attempt successful? (yes/no)
q12: How long was service degraded (error rate >2%)? (minutes)
q13: Time from fix applied to full recovery (minutes)
q14: Severity based on duration and impact (P1/P2/P3)
q15: Time from resolution to stakeholder communication (minutes)""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "q1": "7", "q2": "50", "q3": "30",
                "q4": "45", "q5": "13", "q6": "Alice",
                "q7": "runaway batch job", "q8": "13",
                "q9": "200", "q10": "500", "q11": "no",
                "q12": "40", "q13": "12", "q14": "P2",
                "q15": "10"
            }
        }
    },

    # H-59: COMPLIANCE — 15 violations
    {
        "id": 59, "role": "Compliance / Regulatory Agent", "tier": 5,
        "scoring_type": "json_values",
        "prompt": """Identify ALL 15 GDPR compliance violations in this data processing description. Respond as JSON: {"violations": [{"id": 1, "article": "...", "violation": "...", "severity": "critical/major/minor"}, ...], "count": 15}

Company Data Processing Description:
"1. We collect user email, name, phone, location, browsing history, purchase history, and social media profiles when they visit our website, even before they create an account or consent to anything.
2. Our privacy policy is 47 pages long and written in legal jargon. It was last updated in 2019.
3. We share all user data with 340 advertising partners. Users can opt out by sending a notarized letter to our legal department.
4. When a user requests data deletion, we mark their record as 'inactive' but retain all data indefinitely for 'business analytics.'
5. We process children's data (ages 8-15) the same way as adult data. No special protections or parental consent required.
6. Our data is stored on servers in 12 countries, including some without adequacy decisions. No Standard Contractual Clauses are in place.
7. We experienced a data breach affecting 50,000 users in January. We notified affected users 6 months later via a blog post.
8. Our Data Protection Officer is a marketing intern who started last week.
9. Users cannot download their data in a machine-readable format. We only provide PDF summaries upon written request.
10. We use automated decision-making for credit scoring and loan approvals with no option for human review." """,
        "scoring": {
            "type": "json_values",
            "answers": {
                "v1": "collecting data without consent before account creation",
                "v2": "privacy policy not clear or accessible",
                "v3": "outdated privacy policy (2019)",
                "v4": "sharing with 340 partners without valid consent",
                "v5": "opt-out requires notarized letter - not freely given",
                "v6": "not actually deleting data on deletion request",
                "v7": "no special protection for children's data",
                "v8": "no parental consent for minors",
                "v9": "cross-border transfers without adequacy or SCCs",
                "v10": "72-hour breach notification not met",
                "v11": "breach notification via blog post not direct",
                "v12": "DPO not qualified",
                "v13": "data portability not in machine-readable format",
                "v14": "automated decision-making without human review option",
                "v15": "no lawful basis established for processing"
            }
        }
    },
]
