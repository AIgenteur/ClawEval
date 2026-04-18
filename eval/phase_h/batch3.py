"""Phase H Dense Tests — Batch 3: Tests 19-32 (Shopping, Memory, RAG, Data, Scraping, Customer, Lead, Sprint, Transaction, Home, Fitness, Recipe, Finance)"""

PHASE_H_BATCH3 = [
    # H-19: SHOPPING / PRICE COMPARISON — 15 products
    {
        "id": 19, "role": "Shopping / Price Comparison", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Compare these 15 products across 3 stores and identify the best deal for each. Respond as JSON: {"1": {"best_store": "...", "best_price": N.NN, "savings_pct": N}, ...}

Products and prices (Store A / Store B / Store C):
1. Wireless Mouse: $29.99 / $24.99 / $27.49
2. USB-C Hub: $45.00 / $42.50 / $39.99
3. Mechanical Keyboard: $89.99 / $94.99 / $79.99
4. Monitor Stand: $34.99 / $34.99 / $39.99
5. Webcam 1080p: $59.99 / $49.99 / $54.99
6. Laptop Sleeve 15": $19.99 / $22.99 / $18.49
7. Desk Lamp LED: $42.00 / $38.50 / $41.00
8. Mouse Pad XL: $14.99 / $16.99 / $12.99
9. USB Microphone: $69.99 / $64.99 / $67.50
10. HDMI Cable 6ft: $8.99 / $12.99 / $7.49
11. Wireless Charger: $19.99 / $17.99 / $19.49
12. Bluetooth Speaker: $39.99 / $44.99 / $37.99
13. Power Strip 6-outlet: $15.99 / $14.49 / $16.99
14. Screen Protector 2-pack: $9.99 / $11.99 / $8.99
15. Laptop Stand Aluminum: $54.99 / $49.99 / $52.99""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1_best_store": "B", "2_best_store": "C", "3_best_store": "C",
                "4_best_store": "A", "5_best_store": "B", "6_best_store": "C",
                "7_best_store": "B", "8_best_store": "C", "9_best_store": "B",
                "10_best_store": "C", "11_best_store": "B", "12_best_store": "C",
                "13_best_store": "B", "14_best_store": "C", "15_best_store": "B"
            }
        }
    },

    # H-20: MEMORY / KNOWLEDGE MANAGEMENT — 20 queries
    {
        "id": 20, "role": "Memory / Knowledge Management", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Given this knowledge base, answer 20 queries with TRUE or FALSE. Respond as JSON: {"1": "TRUE/FALSE", ...}

Knowledge Base:
- Project Alpha: Started Jan 2024. Team: Alice (lead), Bob, Carol. Stack: Python, PostgreSQL, Redis. Status: In production. Budget: $120K.
- Project Beta: Started Mar 2024. Team: Dave (lead), Eve, Frank. Stack: Go, MongoDB, Kafka. Status: Development. Budget: $85K.
- Project Gamma: Started Jun 2024. Team: Alice (lead), Grace, Henry. Stack: Rust, PostgreSQL, gRPC. Status: Planning. Budget: $200K.
- Alice is a Senior Engineer. She manages 2 projects simultaneously.
- Bob transferred from Project Beta to Project Alpha in Feb 2024.
- Carol went on leave in Aug 2024. Replaced by Ivy.
- Frank left the company in Jul 2024. Not replaced yet.

Queries:
1. Alice leads exactly 2 projects.
2. Bob has always been on Project Alpha.
3. Project Beta uses PostgreSQL.
4. Project Gamma has the largest budget.
5. Dave's team currently has 3 members.
6. Carol is currently active on Project Alpha.
7. Alice works with PostgreSQL on at least one project.
8. All three projects use the same database.
9. Project Alpha is the oldest project.
10. Frank is still on Project Beta.
11. Project Beta is in production.
12. Ivy joined Project Alpha.
13. Bob was originally on Project Beta.
14. Project Gamma uses Go.
15. The total budget across all projects exceeds $400K.
16. Alice and Dave work on the same project.
17. Project Alpha uses Redis for caching.
18. Henry works on Project Gamma.
19. Eve is on a project that uses Kafka.
20. Carol's replacement (Ivy) works on the same project Carol was on.""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1": "TRUE", "2": "FALSE", "3": "FALSE",
                "4": "TRUE", "5": "FALSE", "6": "FALSE",
                "7": "TRUE", "8": "FALSE", "9": "TRUE",
                "10": "FALSE", "11": "FALSE", "12": "TRUE",
                "13": "TRUE", "14": "FALSE", "15": "TRUE",
                "16": "FALSE", "17": "TRUE", "18": "TRUE",
                "19": "TRUE", "20": "TRUE"
            }
        }
    },

    # H-21: RAG / RETRIEVAL — 15 questions
    {
        "id": 21, "role": "RAG / Retrieval Agent", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Given these 5 document chunks, answer 15 questions. Respond as JSON: {"1": "answer", ...}. Keep answers concise (1-3 words or a number).

Chunk 1 (Employee Handbook v4.2, Section 3): "Employees accrue 15 days PTO annually for the first 3 years. After 3 years: 20 days. After 7 years: 25 days. Maximum carryover: 5 days. Unused PTO beyond carryover is forfeited on Jan 1. Sick leave is separate: 10 days per year, non-accruing."
Chunk 2 (IT Policy, Rev 2024-03): "All employees must use company-issued laptops. Personal devices may not access internal systems. VPN is mandatory for remote work. Password policy: minimum 14 characters, changed every 90 days. Two-factor authentication required for all cloud services."
Chunk 3 (Travel Policy, Updated Sep 2024): "Economy class for flights under 6 hours. Business class permitted for flights over 6 hours. Hotel: max $200/night domestic, $300/night international. Per diem: $75/day domestic, $100/day international. Expenses over $500 require VP approval."
Chunk 4 (Remote Work Policy, v2.0): "Employees may work remotely up to 3 days per week. Full remote requires Director approval. Remote workers must be available 9am-3pm in their local time zone (core hours). Home office stipend: $500 one-time for equipment."
Chunk 5 (Benefits Summary 2024): "Health insurance: company pays 80% of premium. Dental: company pays 50%. Vision: company pays 100%. 401k match: 100% up to 4% of salary, then 50% up to 6%. Vesting: immediate for company match."

Questions:
1. How many PTO days does a 5-year employee get?
2. What is the maximum PTO carryover?
3. Must VPN be used for remote work?
4. What is the minimum password length?
5. Can an employee fly business class on a 4-hour flight?
6. What is the international hotel max per night?
7. How many days per week can an employee work remotely?
8. What are the core hours for remote workers?
9. What percentage of health insurance does the company pay?
10. What is the 401k match on the first 4% of salary?
11. How many sick days per year?
12. How often must passwords be changed?
13. What approval is needed for full remote work?
14. What is the home office stipend amount?
15. Is the 401k company match vesting immediate?""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1": "20", "2": "5", "3": "yes",
                "4": "14", "5": "no", "6": "300",
                "7": "3", "8": "9am-3pm", "9": "80",
                "10": "100", "11": "10", "12": "90 days",
                "13": "Director", "14": "500", "15": "yes"
            }
        }
    },

    # H-22: DATA ANALYSIS — 15 calculations
    {
        "id": 22, "role": "Data Analysis Agent", "tier": 2,
        "scoring_type": "json_numeric",
        "prompt": """Analyze this sales data and answer 15 questions. Respond as JSON: {"q1": answer, ...}. Round to 2 decimal places.

Monthly Sales Data (2024):
| Month | Revenue | Units | Returns | Ad Spend | New Customers |
|-------|---------|-------|---------|----------|---------------|
| Jan   | 45200   | 452   | 23      | 5000     | 89            |
| Feb   | 38900   | 389   | 18      | 4500     | 72            |
| Mar   | 52100   | 498   | 31      | 6000     | 105           |
| Apr   | 48700   | 487   | 25      | 5500     | 98            |
| May   | 61300   | 590   | 42      | 7000     | 134           |
| Jun   | 55800   | 530   | 35      | 6500     | 112           |
| Jul   | 42100   | 421   | 19      | 4000     | 78            |
| Aug   | 49500   | 495   | 28      | 5200     | 95            |
| Sep   | 58200   | 564   | 38      | 6800     | 121           |
| Oct   | 63400   | 617   | 44      | 7500     | 142           |
| Nov   | 71200   | 685   | 52      | 8000     | 158           |
| Dec   | 78500   | 742   | 61      | 9000     | 175           |

q1: Total annual revenue
q2: Average monthly revenue
q3: Average price per unit (total revenue / total units)
q4: Total units sold
q5: Total returns
q6: Return rate percentage (returns / units * 100)
q7: Total ad spend
q8: Revenue per ad dollar (total revenue / total ad spend)
q9: Total new customers
q10: Customer acquisition cost (total ad spend / total new customers)
q11: Best month by revenue (month number 1-12)
q12: Worst month by revenue (month number 1-12)
q13: Q4 (Oct-Dec) revenue
q14: H1 (Jan-Jun) vs H2 (Jul-Dec) revenue difference
q15: Month-over-month growth from Nov to Dec in percentage""",
        "scoring": {
            "type": "json_numeric",
            "answers": {
                "q1": 664900, "q2": 55408.33, "q3": 99.09,
                "q4": 6470, "q5": 416, "q6": 6.43,
                "q7": 75000, "q8": 8.87, "q9": 1379,
                "q10": 54.39, "q11": 12, "q12": 2,
                "q13": 213100, "q14": 60900, "q15": 10.25
            },
            "tolerance": 0.02
        }
    },

    # H-25: CUSTOMER SUPPORT — 20 tickets
    {
        "id": 25, "role": "Customer Support Agent", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Classify 20 customer support tickets by: urgency (p1/p2/p3/p4), category (bug/feature/billing/account/how-to), and suggested_action (escalate/respond/automate). Respond as JSON: {"1": {"urgency": "...", "category": "...", "action": "..."}, ...}

Tickets:
1. "App won't start at all since the update. Getting error code E-5001. I'm a Premium subscriber."
2. "How do I export my data to CSV?"
3. "I was charged $49.99 but I'm on the $29.99 plan"
4. "Would be nice to have keyboard shortcuts for common actions"
5. "Can't login — says my account is locked but I didn't do anything wrong"
6. "Your website is showing my private profile to other users! This is a privacy violation!"
7. "The color theme doesn't save when I switch to dark mode"
8. "Cancel my subscription effective immediately"
9. "PDF export cuts off the right side of tables on A4 paper"
10. "Please add integration with Slack"
11. "Forgot my password, reset email never arrived, checked spam"
12. "The search function returns results from 2019 when I filter for 2024"
13. "Your competitor has better pricing. Can you match it?"
14. "Getting 500 Internal Server Error when uploading files over 10MB"
15. "How do I add a second user to my account?"
16. "My data appears to be missing — 3 months of records just disappeared"
17. "Why does the mobile app drain my battery so fast?"
18. "Invoice shows wrong company name and tax ID"
19. "Can you add multi-language support? We need Spanish and German."
20. "App crashes every time I try to print a report" """,
        "scoring": {
            "type": "json_values",
            "answers": {
                "1_urgency": "p2", "1_category": "bug", "1_action": "escalate",
                "2_urgency": "p4", "2_category": "how-to", "2_action": "automate",
                "3_urgency": "p2", "3_category": "billing", "3_action": "escalate",
                "4_urgency": "p4", "4_category": "feature", "4_action": "respond",
                "5_urgency": "p2", "5_category": "account", "5_action": "escalate",
                "6_urgency": "p1", "6_category": "bug", "6_action": "escalate",
                "7_urgency": "p3", "7_category": "bug", "7_action": "respond",
                "8_urgency": "p3", "8_category": "account", "8_action": "respond",
                "9_urgency": "p3", "9_category": "bug", "9_action": "respond",
                "10_urgency": "p4", "10_category": "feature", "10_action": "respond",
                "11_urgency": "p2", "11_category": "account", "11_action": "escalate",
                "12_urgency": "p2", "12_category": "bug", "12_action": "escalate",
                "13_urgency": "p3", "13_category": "billing", "13_action": "respond",
                "14_urgency": "p2", "14_category": "bug", "14_action": "escalate",
                "15_urgency": "p4", "15_category": "how-to", "15_action": "automate",
                "16_urgency": "p1", "16_category": "bug", "16_action": "escalate",
                "17_urgency": "p3", "17_category": "bug", "17_action": "respond",
                "18_urgency": "p2", "18_category": "billing", "18_action": "escalate",
                "19_urgency": "p4", "19_category": "feature", "19_action": "respond",
                "20_urgency": "p2", "20_category": "bug", "20_action": "escalate"
            }
        }
    },

    # H-26: LEAD SCORING — 15 leads
    {
        "id": 26, "role": "Lead Scoring / Prospecting", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Score these 15 sales leads from 1-100 and classify as: hot (70+), warm (40-69), cold (0-39). Respond as JSON: {"1": {"score": N, "tier": "hot/warm/cold"}, ...}

Leads:
1. VP of Engineering at Fortune 500, visited pricing page 5 times this week, downloaded whitepaper, requested demo
2. Student at community college, signed up for free tier, no further activity
3. CTO of 200-person startup, attended webinar, asked 4 questions, connected on LinkedIn
4. Marketing intern at small agency, opened 1 email out of 5 sent
5. CEO of mid-market company ($50M revenue), replied to cold email saying "send more info"
6. Anonymous visitor, viewed blog post once, bounced after 30 seconds
7. Director of IT at hospital chain, filled out contact form, budget confirmed $100K+
8. Freelance developer, uses free tier actively for 6 months, never opened upgrade emails
9. CFO of public company, downloaded ROI calculator, viewed case studies, has upcoming contract renewal
10. HR manager at 20-person startup, clicked email link once, no further engagement
11. VP of Sales at competitor, likely competitive intelligence
12. Head of Product at Series B startup, requested custom demo, mentioned timeline of "next quarter"
13. Recent college graduate, applied for a job at our company, also signed up for product trial
14. Procurement director at government agency, submitted RFI, requires compliance documentation
15. Existing customer's colleague from different department, referred by current champion user""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1_tier": "hot", "2_tier": "cold", "3_tier": "hot",
                "4_tier": "cold", "5_tier": "warm", "6_tier": "cold",
                "7_tier": "hot", "8_tier": "cold", "9_tier": "hot",
                "10_tier": "cold", "11_tier": "cold", "12_tier": "hot",
                "13_tier": "cold", "14_tier": "warm", "15_tier": "warm"
            }
        }
    },

    # H-28: TRANSACTION / APPROVAL — 20 transactions
    {
        "id": 28, "role": "Transaction / Approval Agent", "tier": 2,
        "scoring_type": "json_values",
        "prompt": """Review 20 transactions and decide: approve, flag, or reject. Rules:
- Transactions over $10,000 require VP approval (flag)
- International transactions over $5,000 require compliance review (flag)
- Transactions to sanctioned countries: reject
- Duplicate amounts to same vendor within 24hrs: flag
- Round-number transactions over $5,000: flag (potential fraud pattern)
- Transactions from suspended accounts: reject
- Weekend transactions over $20,000: flag

Respond as JSON: {"1": "approve/flag/reject", ...}

Transactions:
1. $3,200 to Office Supplies Inc, domestic, Tuesday, active account
2. $15,000 to Cloud Services Corp, domestic, Monday, active account
3. $4,800 to London Marketing Ltd, international (UK), Wednesday, active account
4. $7,500 to Berlin Tech GmbH, international (Germany), Thursday, active account
5. $500 to Catering Express, domestic, Friday, active account
6. $12,000 to same Cloud Services Corp, domestic, Monday (same day as #2), active account
7. $3,000 to vendor in North Korea, international, Monday, active account
8. $8,000 to Consulting Partners, domestic, Saturday, active account
9. $10,000.00 to Marketing Agency, domestic, Tuesday, active account (round number)
10. $2,100 to Office Supplies Inc, domestic, Friday, suspended account
11. $450 to Coffee Shop, domestic, Wednesday, active account
12. $25,000 to IT Infrastructure vendor, domestic, Sunday, active account
13. $6,000 to Tokyo Design Studio, international (Japan), Monday, active account
14. $5,000.00 to Freelancer, domestic, Thursday, active account (round number)
15. $1,200 to vendor in Cuba, international, Tuesday, active account
16. $9,500 to Legal Services LLC, domestic, Wednesday, active account
17. $3,500 to Paris Agency, international (France), Friday, active account
18. $50,000 to Enterprise Software vendor, domestic, Monday, active account
19. $750 to Uber for Business, domestic, Thursday, active account
20. $11,000 to Recruitment Agency, domestic, Tuesday, suspended account""",
        "scoring": {
            "type": "json_values",
            "answers": {
                "1": "approve", "2": "flag", "3": "approve",
                "4": "flag", "5": "approve", "6": "flag",
                "7": "reject", "8": "approve", "9": "flag",
                "10": "reject", "11": "approve", "12": "flag",
                "13": "flag", "14": "flag", "15": "reject",
                "16": "approve", "17": "approve", "18": "flag",
                "19": "approve", "20": "reject"
            }
        }
    },

    # H-30: FITNESS / HEALTH — 15 metrics
    {
        "id": 30, "role": "Fitness / Health Tracking", "tier": 2,
        "scoring_type": "json_numeric",
        "prompt": """Calculate these 15 fitness metrics from the weekly data. Respond as JSON: {"m1": value, ...}. Round to 1 decimal place.

Weekly Activity Log:
| Day | Steps | Calories Burned | Active Min | Sleep Hrs | Heart Rate Avg | Distance km |
|-----|-------|----------------|------------|-----------|---------------|-------------|
| Mon | 8420  | 2100           | 45         | 7.5       | 72            | 6.3         |
| Tue | 12350 | 2800           | 78         | 6.8       | 85            | 9.2         |
| Wed | 6100  | 1750           | 30         | 8.0       | 68            | 4.5         |
| Thu | 9800  | 2350           | 55         | 7.2       | 76            | 7.4         |
| Fri | 11200 | 2650           | 72         | 6.5       | 82            | 8.4         |
| Sat | 15400 | 3200           | 95         | 8.5       | 88            | 11.6        |
| Sun | 4200  | 1500           | 20         | 9.0       | 65            | 3.1         |

Questions:
m1: Total weekly steps
m2: Average daily steps
m3: Total calories burned for the week
m4: Average daily active minutes
m5: Total sleep hours for the week
m6: Average sleep per night
m7: Average resting heart rate
m8: Total distance in km
m9: Day with most steps (1=Mon, 7=Sun)
m10: Day with least active minutes (1-7)
m11: Calories per step (total calories / total steps)
m12: Steps per km (total steps / total distance)
m13: How many days exceeded 10,000 steps?
m14: Weekend (Sat+Sun) total steps
m15: Weekday (Mon-Fri) average steps""",
        "scoring": {
            "type": "json_numeric",
            "answers": {
                "m1": 67470, "m2": 9638.6, "m3": 16350,
                "m4": 56.4, "m5": 53.5, "m6": 7.6,
                "m7": 76.6, "m8": 50.5, "m9": 6,
                "m10": 7, "m11": 0.2, "m12": 1335.6,
                "m13": 3, "m14": 19600, "m15": 9574.0
            },
            "tolerance": 0.02
        }
    },

    # H-32: PERSONAL FINANCE — 15 calculations
    {
        "id": 32, "role": "Personal Finance Tracking", "tier": 2,
        "scoring_type": "json_numeric",
        "prompt": """Calculate 15 personal finance metrics from this monthly data. Respond as JSON: {"f1": value, ...}. Round to 2 decimal places.

Monthly Budget (March 2024):
Income:
- Salary (after tax): $5,800
- Freelance work: $1,200
- Investment dividends: $150

Expenses:
- Rent: $1,800
- Utilities: $180
- Groceries: $520
- Dining out: $340
- Transportation: $280
- Insurance (health+car): $450
- Phone+Internet: $130
- Subscriptions: $85
- Clothing: $120
- Entertainment: $200
- Gym: $50
- Student loan payment: $380
- Credit card payment: $250 (of which $45 is interest)
- Savings transfer: $500
- Emergency fund: $200

Questions:
f1: Total monthly income
f2: Total monthly expenses (including savings/emergency transfers)
f3: Net cash flow (income - expenses)
f4: Savings rate percentage (savings+emergency / income * 100)
f5: Housing cost percentage (rent+utilities / income * 100)
f6: Total food spending (groceries + dining)
f7: Discretionary spending (dining+entertainment+clothing+subscriptions)
f8: Debt payments total (student loan + credit card)
f9: Fixed expenses total (rent+utilities+insurance+phone+gym+loans)
f10: Variable expenses total (groceries+dining+transport+clothing+entertainment+subscriptions)
f11: Essential vs non-essential ratio (fixed / variable)
f12: If income drops 20%, what is the new net cash flow?
f13: Months of expenses that savings ($12,000) can cover
f14: Annual projected savings (monthly savings * 12)
f15: Interest paid as percentage of credit card payment""",
        "scoring": {
            "type": "json_numeric",
            "answers": {
                "f1": 7150, "f2": 5485, "f3": 1665,
                "f4": 9.79, "f5": 27.69, "f6": 860,
                "f7": 745, "f8": 630, "f9": 3270,
                "f10": 1545, "f11": 2.12, "f12": 235,
                "f13": 2.19, "f14": 8400, "f15": 18.0
            },
            "tolerance": 0.05
        }
    },
]
