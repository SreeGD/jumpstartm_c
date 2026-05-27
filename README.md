# NITW M&C Prep — 2-Month Curriculum

A hook-first computing curriculum for students entering engineering college, built for **one-on-one teaching**. Covers hardware, Python, AI, quant finance, full stack development, and career planning — starting from zero code experience.

**Student:** *(your student's name)*  
**Teacher:** *(your name)*  
**Duration:** 8 weeks · 13 sessions  
**Goal:** Build genuine understanding of computing, math, and AI — not surface familiarity.

---

## What's in Each Session

Every session folder contains:

```
session_X/
├── lesson.md        ← teacher's narrative guide (hook, concepts, wow moments,
│                      quiz with answers, research materials)
├── labs/            ← runnable code and activities (do together in session)
└── assignments/     ← student's independent work before the next session
```

Each `lesson.md` includes:
- 📖 **Narrative** — story-first teaching guide with questions to ask
- ⚡ **Wow Moment** — the one thing that makes it click
- 🔑 **Key Concepts Checklist**
- 🧪 **Quiz** — 8 questions per session (multiple choice + short answer + explain-in-your-own-words), answers included
- 📚 **Research Materials** — curated films, YouTube, books, articles, and people to look up

---

## Teaching Philosophy

> Every session opens with a story or demo that creates a question. Then answers it.

No session starts with "today we learn X."  
Every session starts with something that makes the student *want* to understand X.

```
HOOK      → Teacher opens with a story or surprising demo
EXPLAIN   → Teacher walks through the concept live
DEMO      → Teacher runs real code or a visualisation
PRACTICE  → Teacher and student build it together
WOW       → The moment it all clicks
HOMEWORK  → Student continues independently before the next session
```

---

## Session Map

| # | Session | Theme | Lab |
|---|---------|-------|-----|
| 1 | [History of Computing](./session_1_history/) | From Ada Lovelace to ChatGPT — the thriller behind every device you own | Timeline research |
| 1.1 | [Building Blocks](./session_1_1_building_blocks/) | Transistors, binary, logic gates, CPU, GPU | Logic gates in Python |
| 1.2 | [How the Web Works](./session_1_2_web/) | What actually happens when you open Instagram | Build your first webpage |
| 2 | [Maths for Computing](./session_2_maths/) | Binary, Boolean algebra, Big-O, graph theory — math you already know with meaning | Caesar cipher + passing network |
| 3 | [Programming Languages](./session_3_languages/) | The family tree: FORTRAN → C → Java → Python → TypeScript → Go | Fibonacci in Python |
| 4 | [Python](./session_4_python/) | Math with superpowers — waves, games, NBA charts, probability | 4 labs: waves, guessing game, scorers, dice |
| 5 | [Math & Stats for AI](./session_5_math_stats_ai/) | Vectors, gradient descent, probability, correlation, xG model | Build an Expected Goals model |
| 6 | [Agentic AI](./session_6_agentic_ai/) | Rules → ML → Transformers → LLMs → Agents. Build one. | Sports analyst agent with Claude API |
| 7 | [Quant Finance](./session_7_quant_finance/) | Hedge funds are just applied math — Sharpe ratio, Markowitz, Black-Scholes | Analyse Man United + NVDA stocks |
| 8 | [Capstone Project](./session_8_capstone/) | Build something real. Four tracks to choose from. | Sports Oracle (recommended) |
| 9 | [Software Engineering Landscape](./session_9_software_engineering/) | How the profession evolved: 2010 → 2026 | Career map + job description analysis |
| 10 | [How Instagram Works](./session_10_instagram/) | CDN, feed algorithm, fan-out, Redis, microservices — the billion-dollar app explained | Instagram feed algorithm simulator |
| 11 | [Full Stack: Frontend](./session_11_fullstack_frontend/) | HTML/CSS/JS, React, responsive design, the 2026 frontend stack | NBA dashboard (pure JS, no frameworks) |
| 12 | [Full Stack: Backend](./session_12_fullstack_backend/) | Servers, REST APIs, SQL, NoSQL, auth, deployment | Build a working sports REST API with Flask |
| 13 | [Career Paths](./session_13_career_paths/) | 8 tracks, India + global salary bands, NITW strategy, the 10-year view | Career self-assessment + LinkedIn research |

---

## Company Thread

Every major company is woven into the sessions where they genuinely belong:

| Company | Where it appears |
|---------|-----------------|
| **IBM** | Mainframes (S1), FORTRAN (S3), enterprise Java (S9) |
| **Microsoft** | MS-DOS deal (S1), TypeScript + VS Code (S3, S9), GitHub + OpenAI $10B (S6, S9) |
| **Apple** | PC revolution + 1984 ad (S1), iPhone (S1) |
| **Google** | PageRank as graph theory (S2), Go language (S3), TensorFlow (S5), DeepMind + AlphaGo (S6), React/Angular/Kubernetes (S9) |
| **Meta / Facebook** | Social graph (S1), PyTorch (S5), LLaMA open-source (S6), React (S9, S11), Instagram architecture (S10) |
| **Amazon / AWS** | Cloud origin story (S1), cloud market share (S9) |
| **Oracle** | Relational databases (S1, S2), Java acquisition + lawsuits (S3) |
| **Yahoo** | Web portal era + decline (S1), Yahoo Finance as quant data source (S7) |
| **Netflix** | Recommendation system + matrix factorisation (S5), microservices + Chaos Monkey (S9) |
| **OpenAI** | Founding story 2015 (S1), GPT → ChatGPT (S1, S6), $10B Microsoft investment (S6) |
| **Anthropic** | Founded 2021 (S1), Constitutional AI, Claude named after Claude Shannon (S1, S6) |
| **Bloomberg** | Terminal as quant data layer — $24k/year, 325k subscribers (S7) |
| **Two Sigma / Citadel** | Quant career destinations (S7) |
| **Spotify / Stripe / Twitter** | API design standards (S9) |
| **Docker / HashiCorp** | Container and IaC origins (S9) |

---

## Software Engineering Era Map (Session 9)

| Year | Era | Key Company |
|------|-----|-------------|
| 2010 | Java, OOP & Web Fundamentals | Oracle (Java), IBM (enterprise) |
| 2012 | Python & JavaScript | Dropbox, Joyent (Node.js), npm |
| 2014 | SPA & TypeScript | Meta (React), Google (Angular), Microsoft (TypeScript, VS Code) |
| 2015 | Spring Boot & REST APIs | Twitter, Stripe, Twilio |
| 2016 | Microservices & DevOps | Netflix, Amazon, Docker |
| 2017 | Cloud Engineering | AWS (32%), Azure (22%), GCP (11%) |
| 2020 | Kubernetes & Observability | Google (K8s), Datadog, HashiCorp |
| 2023 | Platform Engineering | Spotify (Backstage), Vercel, IBM |
| 2026 | AI-Assisted Engineering | Microsoft (Copilot), Anthropic (Claude Code), Cursor |

---

## Career Tracks (Session 13)

| Track | Core Skills | Entry (India) | Entry (US) |
|-------|-------------|---------------|-----------|
| Frontend Engineer | JS/TS, React, CSS | ₹6–15 LPA | $90–130k |
| Backend Engineer | Python/Java/Go, SQL | ₹8–18 LPA | $100–140k |
| Full-Stack Engineer | Front + back end | ₹8–20 LPA | $100–150k |
| Data Scientist / ML | Python, stats, PyTorch | ₹10–25 LPA | $110–160k |
| AI / LLM Engineer | LLM APIs, RAG, agents | ₹15–35 LPA | $130–200k |
| DevOps / SRE | Docker, K8s, cloud | ₹8–20 LPA | $110–160k |
| Quant Developer | Python/C++, finance, math | ₹15–40 LPA | $150–300k |
| Engineering Manager | Leadership + technical credibility | 5–7 years IC first | — |

---

## Generated Resources

| File | What it is |
|------|-----------|
| `curriculum_advaith.html` | Full printable curriculum — open in Chrome, `Cmd+P → Save as PDF` |
| `curriculum_advaith.pptx` | 105-slide deck — one idea per slide, colour-coded by session |
| `generate_pdf.py` | Regenerates the HTML from source markdown |
| `generate_pptx.py` | Regenerates the PowerPoint deck |

---

## Setup

**Before Session 4:**
- Python 3.11+ → https://python.org
- VS Code → https://code.visualstudio.com
- Extensions: Python (Microsoft), Pylance

**Python libraries** (install as needed):
```bash
pip install matplotlib numpy pandas yfinance anthropic flask
```

**API key** (for Session 6 and Capstone):
- Get an Anthropic API key → https://console.anthropic.com
- Set it: `export ANTHROPIC_API_KEY="sk-ant-..."`

---

## Student Profile (adapt to your student)

- Just finished 12th PCM
- Loves math — scored well, genuinely enjoyed it
- Zero programming experience
- Loves basketball and soccer
- 2 months of free time
