"""Phase H Dense Tests — Batch 7: Tests 10, 17, 24, 34, 41, 58 (previously manual-review, now automated)
Uses h_content_check scorer: checks for keyword presence in raw model output."""

PHASE_H_BATCH7 = [
    # H-10: CONTENT WRITER — 20 structural constraints
    {
        "id": 10, "role": "Content Writer / Blog Writer", "tier": 2,
        "scoring_type": "h_content_check",
        "prompt": """Write a blog post about "Why Remote Work Is Here to Stay in 2025". 

ALL 20 constraints must be met:
1. Title must contain "Remote Work" and "2025"
2. Must have exactly 5 sections with H2 headings
3. Include at least 3 specific statistics with sources (e.g., "According to Gallup...")
4. Total word count between 800-1200 words
5. Include an introduction paragraph (before first H2)
6. Include a conclusion paragraph (after last H2)
7. Mention at least 3 specific companies by name (e.g., Google, Microsoft)
8. Include at least 2 counterarguments (challenges of remote work)
9. Each section must have at least 2 paragraphs
10. Use at least 3 bullet or numbered lists
11. Include at least 2 quotes (real or attributed to a named person/title)
12. Mention productivity data or research
13. Mention mental health or work-life balance
14. Mention technology tools (at least 2 specific tools like Zoom, Slack)
15. Include a call-to-action in the conclusion
16. Use transition phrases between sections (e.g., "Moreover", "However", "Furthermore")
17. Mention cost savings (for employees or companies)
18. Reference the COVID-19 pandemic as a catalyst
19. Include at least 1 comparison (e.g., "compared to", "vs", "unlike")
20. No section should be fewer than 100 words

Respond in markdown format with clear H2 headings.""",
        "scoring": {
            "checks": {
                "has_remote_work_title": ["remote work"],
                "has_2025_title": ["2025"],
                "has_h2_sections": ["## "],
                "has_statistics": ["according to", "survey", "study found", "research shows", "percent"],
                "has_introduction": ["introduction", "in recent years", "the rise of", "over the past"],
                "has_conclusion": ["conclusion", "in conclusion", "looking ahead", "moving forward"],
                "mentions_companies": ["google", "microsoft", "amazon", "meta", "apple", "twitter", "slack", "zoom"],
                "has_counterarguments": ["challenge", "drawback", "downside", "however", "obstacle", "concern", "difficult"],
                "has_bullet_lists": ["- ", "* ", "1."],
                "has_quotes": ['"', "said", "stated", "noted", "according to"],
                "mentions_productivity": ["productivity", "output", "performance", "efficiency"],
                "mentions_mental_health": ["mental health", "work-life balance", "well-being", "wellbeing", "burnout"],
                "mentions_tech_tools": ["zoom", "slack", "teams", "notion", "asana", "trello", "google meet"],
                "has_call_to_action": ["start", "try", "consider", "embrace", "take the", "begin"],
                "has_transitions": ["moreover", "however", "furthermore", "additionally", "in addition", "on the other hand"],
                "mentions_cost_savings": ["cost", "savings", "save", "expense", "commut"],
                "mentions_covid": ["covid", "pandemic", "coronavirus", "lockdown"],
                "has_comparison": ["compared to", " vs ", "unlike", "whereas", "in contrast"],
                "mentions_remote_flexibility": ["flexibility", "flexible", "anywhere", "hybrid"],
                "has_substantive_content": ["employee", "employer", "organization", "workforce"]
            }
        }
    },

    # H-17: SOCIAL MEDIA CONTENT — 20 post constraints
    {
        "id": 17, "role": "Social Media Content Agent", "tier": 2,
        "scoring_type": "h_content_check",
        "prompt": """Create a 5-day social media content calendar for a SaaS project management tool called "TaskFlow". Respond as JSON:
{"days": [{"day": 1, "platform": "...", "post_type": "...", "content": "...", "hashtags": [...], "cta": "...", "time": "..."}]}

ALL 20 constraints must be met:
1. Exactly 5 days of content
2. Must cover at least 3 different platforms (Twitter/X, LinkedIn, Instagram, TikTok, Facebook)
3. Each post must include 3-5 relevant hashtags
4. Each post must have a clear call-to-action (CTA)
5. Include at least 1 video content post
6. Include at least 1 carousel/infographic post
7. Include at least 1 user testimonial or social proof post
8. Each post must specify optimal posting time (e.g., "10:00 AM EST")
9. At least 1 post must mention a competitor comparison
10. Include at least 1 educational/how-to post
11. At least 1 post must include emoji usage
12. Include at least 1 promotional/discount post
13. No two consecutive days should use the same platform
14. At least 1 post must reference a trending topic or industry news
15. Each content piece must be under 280 characters (Twitter-compatible length)
16. Include at least 1 poll or question-based engagement post
17. Hashtags must include #ProjectManagement or #Productivity in at least 3 posts
18. At least 1 post must target enterprise/B2B audience
19. Include at least 1 behind-the-scenes or team culture post
20. CTA must vary (not the same CTA repeated)""",
        "scoring": {
            "checks": {
                "has_5_days": ["day 1", "day 2", "day 3", "day 4", "day 5", "\"day\": 1", "\"day\": 5"],
                "has_twitter": ["twitter", "x.com", "\"x\""],
                "has_linkedin": ["linkedin"],
                "has_instagram": ["instagram"],
                "has_hashtags": ["#taskflow", "#projectmanagement", "#productivity", "#saas"],
                "has_cta": ["sign up", "try", "click", "learn more", "get started", "visit", "download"],
                "has_video": ["video", "reel", "tiktok"],
                "has_carousel": ["carousel", "infographic", "slide"],
                "has_testimonial": ["testimonial", "customer", "review", "said", "love using", "transformed"],
                "has_posting_time": [" am", " pm", "est", "pst"],
                "has_competitor": ["competitor", "compared to", "unlike", "vs", "alternative"],
                "has_educational": ["how to", "how-to", "tip", "guide", "tutorial", "learn"],
                "has_emoji": ["🚀", "💡", "✅", "📊", "🎯", "💪", "🔥", "⭐"],
                "has_promo": ["discount", "free trial", "offer", "% off", "deal", "promo"],
                "has_trending": ["trending", "trend", "2025", "news", "latest", "industry"],
                "has_poll": ["poll", "question", "what do you think", "vote", "which"],
                "has_pm_hashtag": ["#projectmanagement", "#productivity"],
                "has_b2b": ["enterprise", "b2b", "business", "team", "organization"],
                "has_behind_scenes": ["behind", "team", "culture", "day in the life", "meet"],
                "mentions_taskflow": ["taskflow"]
            }
        }
    },

    # H-24: IMAGE DESCRIPTION — 20 analysis checkpoints
    {
        "id": 24, "role": "Image Description / Understanding", "tier": 2,
        "scoring_type": "h_content_check",
        "prompt": """You are an image description agent. Given this detailed scene description, produce a comprehensive accessibility description and analysis. Respond as JSON:
{"description": "...", "objects": [...], "colors": [...], "mood": "...", "composition": "...", "accessibility_alt_text": "...", "detailed_analysis": {...}}

Scene to describe (imagine you are seeing this photograph):
A busy Tokyo street crossing (Shibuya-style) at dusk. Neon signs in Japanese and English cover buildings on both sides. A large digital billboard shows an anime advertisement. Dozens of pedestrians cross in multiple directions — some carrying umbrellas (it's lightly raining). A yellow taxi waits at the crossing. Street lights reflect off wet pavement. A convenience store (7-Eleven) is visible on the corner. Power lines cross overhead. A businessman in a dark suit checks his phone while walking. A group of school students in uniforms stand at the corner.

ALL 20 analysis points must be covered:
1. Mention the location (Tokyo/Shibuya crossing)
2. Time of day (dusk/evening)
3. Weather condition (rain)
4. Count of major object categories (people, vehicles, buildings, signs)
5. Dominant colors (neon, wet reflections)
6. Mood/atmosphere (busy, urban, vibrant)
7. The taxi (color and position)
8. The 7-Eleven store
9. The anime billboard
10. The businessman with phone
11. The school students in uniforms
12. The umbrellas
13. The wet pavement reflections
14. Power lines
15. Japanese and English text on signs
16. Composition analysis (foreground/midground/background)
17. Lighting analysis (artificial neon + natural dusk)
18. Cultural elements (Japanese urban culture)
19. Accessibility alt-text (concise, under 125 characters)
20. Suggested image tags for SEO (at least 8 tags)""",
        "scoring": {
            "checks": {
                "mentions_tokyo": ["tokyo", "shibuya"],
                "mentions_dusk": ["dusk", "evening", "twilight", "sunset"],
                "mentions_rain": ["rain", "drizzle", "wet"],
                "has_object_count": ["pedestrian", "people", "vehicle", "building"],
                "mentions_neon_colors": ["neon", "glow", "vibrant", "illuminate"],
                "mentions_busy_atmosphere": ["busy", "bustling", "crowded", "vibrant", "energetic"],
                "mentions_taxi": ["taxi", "cab"],
                "mentions_7eleven": ["7-eleven", "7eleven", "convenience store", "konbini"],
                "mentions_anime_billboard": ["anime", "billboard", "advertisement"],
                "mentions_businessman": ["businessman", "business man", "suit", "phone"],
                "mentions_students": ["student", "uniform", "school"],
                "mentions_umbrellas": ["umbrella"],
                "mentions_reflections": ["reflection", "reflect", "wet pavement", "glistening"],
                "mentions_power_lines": ["power line", "power lines", "overhead", "cables", "wires"],
                "mentions_bilingual": ["japanese", "english", "bilingual", "kanji"],
                "has_composition": ["foreground", "midground", "background", "composition"],
                "has_lighting": ["lighting", "neon light", "artificial", "natural light"],
                "mentions_culture": ["japanese", "culture", "urban", "japan"],
                "has_alt_text": ["alt", "alt_text", "alt-text", "accessibility"],
                "has_seo_tags": ["tag", "keyword", "seo"]
            }
        }
    },

    # H-34: LANDING PAGE GENERATOR — 20 structural elements
    {
        "id": 34, "role": "Landing Page Generator", "tier": 2,
        "scoring_type": "h_content_check",
        "prompt": """Generate the complete HTML structure for a SaaS landing page for an AI writing assistant called "QuillAI". Respond with the full HTML code.

ALL 20 structural constraints must be met:
1. Must include a hero section with headline, subheadline, and CTA button
2. Include a navigation bar with at least 4 links (Features, Pricing, Testimonials, Contact)
3. Features section with at least 4 feature cards, each with an icon placeholder, title, and description
4. Pricing section with exactly 3 tiers (Free, Pro, Enterprise) with prices
5. Testimonials section with at least 3 testimonials including name, role, and quote
6. FAQ section with at least 5 question-answer pairs
7. Footer with copyright, social media links, and legal links (Privacy, Terms)
8. Must include a <meta name="description"> tag
9. Must include a <title> tag containing "QuillAI"
10. At least 1 email signup/newsletter form with input field and submit button
11. Mobile-responsive viewport meta tag
12. At least 2 CTA buttons with different text (e.g., "Start Free Trial", "Get Started")
13. Include social proof (e.g., "Trusted by 10,000+ users" or company logos section)
14. Include a "How it Works" section with at least 3 steps
15. Use semantic HTML elements (header, nav, main, section, footer)
16. Include at least 1 anchor link that scrolls to a section
17. Contact section or link with email address
18. Must mention AI or artificial intelligence in the hero section
19. Include accessibility attributes (alt text on images, aria labels)
20. Include at least 1 comparison or "before/after" element""",
        "scoring": {
            "checks": {
                "has_hero_section": ["hero"],
                "has_navbar": ["<nav", "features", "pricing"],
                "has_features": ["feature"],
                "has_pricing": ["free", "pro", "enterprise"],
                "has_testimonials": ["testimonial"],
                "has_faq": ["faq", "frequently asked", "question"],
                "has_footer": ["<footer", "copyright", "©"],
                "has_meta_description": ["meta name=\"description\"", "meta name='description'"],
                "has_title_quillai": ["quillai"],
                "has_email_form": ["<input", "<form", "email", "newsletter", "subscribe"],
                "has_viewport": ["viewport"],
                "has_cta_buttons": ["get started", "start free", "try free", "sign up", "free trial"],
                "has_social_proof": ["trusted by", "users", "companies trust", "join"],
                "has_how_it_works": ["how it works", "step 1", "step 2", "step 3"],
                "has_semantic_html": ["<header", "<section", "<footer", "<main", "<nav"],
                "has_anchor_links": ["href=\"#", "href='#"],
                "has_contact": ["contact", "email", "@"],
                "has_ai_mention": ["ai", "artificial intelligence", "ai-powered"],
                "has_accessibility": ["alt=", "aria-", "role="],
                "has_comparison": ["before", "after", "compared", "without", "with quillai"]
            }
        }
    },

    # H-41: CRITIC / REVIEW AGENT — 20 review checkpoints
    {
        "id": 41, "role": "Critic / Review Agent", "tier": 3,
        "scoring_type": "h_content_check",
        "prompt": """Write a comprehensive critical review of this Python code repository structure. Respond as JSON:
{"overall_score": N, "categories": [{...}], "critical_issues": [...], "recommendations": [...]}

Repository structure and key files:
```
myapp/
├── app.py (500 lines, all routes + business logic + DB queries in one file)
├── config.py (hardcoded DB_PASSWORD = "admin123", API_KEY = "sk-xxx")
├── utils.py (200 lines, mix of string helpers, date parsing, API calls, file I/O)
├── test_app.py (50 lines, only 3 test functions, no mocking)
├── requirements.txt (flask, requests, sqlalchemy — no version pinning)
├── README.md (empty except "TODO: add docs")
├── .env.example (missing)
├── Dockerfile (FROM python:3.8, uses root user, no multi-stage build)
├── database.py (raw SQL queries with string formatting: f"SELECT * FROM users WHERE id={user_id}")
└── deploy.sh (contains AWS credentials inline, chmod 777 on all files)
```

ALL 20 review points must be addressed:
1. Score overall code quality (1-10 with justification)
2. Identify the SQL injection vulnerability in database.py
3. Flag the hardcoded credentials in config.py
4. Critique the monolithic app.py (separation of concerns)
5. Flag the lack of version pinning in requirements.txt
6. Critique the insufficient test coverage
7. Flag the security issue in deploy.sh (inline AWS credentials)
8. Flag the chmod 777 security issue
9. Critique the outdated Python 3.8 in Dockerfile
10. Flag running as root in Dockerfile
11. Critique the missing .env.example
12. Critique the empty README
13. Critique the mixed responsibilities in utils.py
14. Suggest proper project structure (blueprints/modules)
15. Recommend parameterized queries for SQL
16. Recommend secrets management (environment variables or vault)
17. Recommend CI/CD pipeline additions
18. Recommend minimum test coverage percentage
19. Recommend Dockerfile improvements (multi-stage, non-root)
20. Rate severity of each issue (critical/high/medium/low)""",
        "scoring": {
            "checks": {
                "has_overall_score": ["overall_score", "overall score", "score:", "/10", "out of 10"],
                "identifies_sql_injection": ["sql injection", "sql inject", "string format", "f-string", "user_id"],
                "flags_hardcoded_credentials": ["hardcoded", "hard-coded", "admin123", "credential", "password"],
                "critiques_monolithic": ["monolithic", "single file", "500 lines", "separation of concern", "too large"],
                "flags_no_version_pinning": ["version pin", "pinning", "==", "requirements"],
                "critiques_test_coverage": ["test coverage", "insufficient test", "only 3 test", "mock", "testing"],
                "flags_deploy_credentials": ["aws credential", "inline credential", "deploy.sh", "secret"],
                "flags_chmod_777": ["chmod 777", "777", "permission"],
                "critiques_python_38": ["python 3.8", "outdated", "end of life", "eol", "upgrade python"],
                "flags_root_docker": ["root user", "non-root", "rootless", "user root", "as root"],
                "critiques_missing_env": [".env", "env.example", "environment variable"],
                "critiques_empty_readme": ["readme", "documentation", "empty readme", "todo"],
                "critiques_mixed_utils": ["utils.py", "mixed responsibilit", "single responsibility", "helper"],
                "suggests_structure": ["blueprint", "module", "package", "restructur", "refactor"],
                "recommends_parameterized": ["parameterized", "prepared statement", "placeholder", "bind variable"],
                "recommends_secrets": ["secret management", "vault", "environment variable", "dotenv", ".env"],
                "recommends_cicd": ["ci/cd", "ci cd", "pipeline", "github action", "continuous integration"],
                "recommends_test_coverage": ["coverage", "80%", "90%", "pytest", "test suite"],
                "recommends_dockerfile": ["multi-stage", "non-root", "slim", "alpine", "dockerfile"],
                "has_severity_ratings": ["critical", "high", "medium", "low", "severity"]
            }
        }
    },

    # H-58: BOOK / LONG-FORM WRITING — 20 structural constraints
    {
        "id": 58, "role": "Book / Long-Form Writing", "tier": 5,
        "scoring_type": "h_content_check",
        "prompt": """Write a detailed outline for a non-fiction book titled "The AI Revolution in Small Business: A Practical Guide for 2025". Respond as JSON:
{"title": "...", "subtitle": "...", "chapters": [{"number": N, "title": "...", "sections": [...], "key_takeaway": "...", "estimated_pages": N}], "appendices": [...], "total_chapters": N, "target_audience": "...", "word_count_estimate": N}

ALL 20 constraints must be met:
1. Exactly 12 chapters
2. Each chapter must have 3-5 sections
3. Chapter 1 must be an introduction/overview
4. Chapter 12 must be a conclusion/future outlook
5. Include at least 2 chapters on specific AI tools (ChatGPT, Midjourney, etc.)
6. Include at least 1 chapter on ROI/financial impact
7. Include at least 1 chapter on ethics/risks of AI
8. Include at least 1 chapter on implementation/getting started
9. Each chapter must have a key_takeaway
10. Each chapter must have estimated_pages (5-25 range)
11. Total estimated pages must be 200-350
12. Include at least 2 appendices (glossary, resource list, etc.)
13. Specify target audience
14. Include at least 1 chapter on case studies or real examples
15. Include at least 1 chapter on hiring/team building with AI
16. Chapter progression must be logical (basics → advanced → future)
17. Include at least 1 chapter on marketing/sales with AI
18. Include at least 1 chapter on customer service/support with AI
19. Total word count estimate must be 50,000-80,000
20. Include at least 1 chapter addressing common fears/objections about AI""",
        "scoring": {
            "checks": {
                "has_12_chapters": ["chapter 12", "\"number\": 12", "chapter twelve"],
                "has_sections": ["section", "sections"],
                "ch1_is_introduction": ["introduction", "overview", "getting started", "chapter 1"],
                "ch12_is_conclusion": ["conclusion", "future", "outlook", "looking ahead"],
                "has_ai_tools": ["chatgpt", "midjourney", "dall-e", "copilot", "gemini", "claude"],
                "has_roi": ["roi", "return on investment", "financial impact", "cost", "revenue"],
                "has_ethics": ["ethics", "ethical", "risk", "bias", "privacy", "responsible"],
                "has_implementation": ["implementation", "getting started", "deploy", "adopt", "integration"],
                "has_key_takeaways": ["key_takeaway", "key takeaway", "takeaway"],
                "has_page_estimates": ["estimated_pages", "pages", "page count"],
                "has_appendices": ["appendix", "appendices", "glossary", "resource"],
                "has_target_audience": ["target_audience", "target audience", "small business", "entrepreneur"],
                "has_case_studies": ["case study", "case studies", "real-world", "example", "success story"],
                "has_hiring": ["hiring", "team building", "talent", "recruit", "workforce"],
                "has_marketing": ["marketing", "sales", "advertising", "lead generation"],
                "has_customer_service": ["customer service", "customer support", "chatbot", "helpdesk"],
                "has_word_count": ["word_count", "word count", "50,000", "60,000", "70,000", "80,000", "50000", "60000", "70000"],
                "has_fears": ["fear", "objection", "concern", "myth", "misconception", "worry"],
                "has_book_title": ["ai revolution", "small business"],
                "has_structured_json": ["\"chapters\"", "\"title\"", "\"number\""]
            }
        }
    },
]
