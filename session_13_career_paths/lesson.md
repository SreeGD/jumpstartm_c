# Session 13 — Where Do You Go From Here?
## Career Paths in Computing & AI

**Duration:** 1.5–2 hours (mostly discussion)
**Teacher's Prep:** Research current NITW M&C placements. Have real job descriptions ready from Naukri, LinkedIn, and Levels.fyi printed or on screen. Prepare the salary trajectory graph mentally — or draw it live on the whiteboard for effect.

---

## 🎯 Goal

By the end of this session, every student should:
- Be able to name at least 3 real career paths that match their interests and strengths
- Understand what separates students who get exceptional placements from average ones
- Have a concrete, specific plan for their first year at NITW
- Know which skills compound over a career and which ones decay
- Feel genuinely excited about the profession they are entering — not just vaguely optimistic

This session is not about teaching new technical content. It is about giving students an honest map of the territory they are entering.

---

## 📖 Teacher's Narrative

### The Hook — Read This Out Loud

*"In 2010, a software engineer at Google earned ₹15 LPA. In 2025, the same engineer earns ₹80–150 LPA. In 2030, the job description will be unrecognisable. You are entering the most valuable profession in history — during its biggest transformation."*

Pause. Let that land.

Then ask: "How many of you know what job you want when you graduate?" Most hands will not go up. That is fine. Today's session is not about locking in a decision — it is about understanding the landscape well enough to make good early choices.

This curriculum — 13 sessions, from binary to AI agents — has given you a foundation that most NITW freshers will not have when they arrive. That advantage exists right now. It will erode if you do not build on it. Today is about not letting it erode.

---

### Part 1: The Career Landscape — 8 Paths

*Teacher: For each path, try to have one real job description on screen. If you have time, find one NITW M&C alumnus in that role on LinkedIn before class.*

---

#### Path 1: Frontend / UI Engineer

**What they do every day:**
Write the code users actually see and touch. HTML, CSS, JavaScript — the language of every screen, every button, every animation. They collaborate tightly with designers. They obsess over milliseconds, because slow pages lose users. They test on five browsers, three screen sizes, and two operating systems simultaneously.

**Core skills:**
JavaScript and TypeScript. React or Vue (React dominates in 2025). CSS — not just "make it pretty" but layout systems, responsive design, accessibility for users with disabilities. Performance profiling. Testing with Jest or Cypress.

**Entry point:**
₹6–15 LPA in India at a good company. $90–130k USD at a US company or remote-first startup. The range is wide because "frontend" at TCS and "frontend" at a funded startup are completely different jobs.

**5-year trajectory:**
Junior Frontend → Senior Frontend → Tech Lead → Frontend Architect or Engineering Manager

**How AI changes this path:**
Copilot and similar tools write boilerplate HTML and repetitive CSS at roughly a junior level. This does not eliminate frontend engineers — it eliminates the boring parts of their job. What becomes more valuable: product sense, accessibility judgment, performance architecture, and the taste to know when something looks and feels right. Designers and frontend engineers who develop strong product intuition actually benefit from AI tools.

**Is this path for you if:** You are drawn to visual work, you care about how things feel to use, you have patience for debugging subtle visual bugs, you find the intersection of design and code appealing.

---

#### Path 2: Backend Engineer

**What they do every day:**
Build the systems that power applications: APIs, databases, authentication, caching, job queues, payment processing. Users never see backend code directly, but every feature they use depends on it. A backend engineer spends their day writing endpoints, optimising slow database queries, designing schemas, debugging race conditions, and thinking about what happens when 100,000 users hit the system at once.

**Core skills:**
Python, Java, or Go (the three most common in 2025). SQL — essential, not optional. System design: how to structure services so they are fast, reliable, and maintainable. Understanding of caching (Redis), message queues (Kafka), and cloud infrastructure.

**Entry point:**
₹8–18 LPA India. $100–140k USD. Backend roles are among the most consistently available across all company sizes.

**5-year trajectory:**
Junior Backend → Senior Backend → Staff Engineer → Principal Engineer

Staff and Principal engineers at top companies in India earn ₹60–120 LPA. In the US, $200–400k total compensation is realistic.

**How AI changes this path:**
AI writes boilerplate CRUD operations well. What it cannot do well: design systems under novel constraints, reason about distributed failure modes, understand the business context behind a technical decision. Architecture judgment — knowing not just how to build something, but whether to build it at all — becomes the premium skill.

**Is this path for you if:** You like systems, you enjoy figuring out why something is slow, you find databases and data flow intellectually interesting, you prefer correctness and reliability over visual craft.

---

#### Path 3: Full-Stack Engineer

**What they do every day:**
Own a feature end-to-end. They write the frontend, the backend, and the database migration. At a startup, they might also write the deployment script. Full-stack engineers are the most common hire at companies under 200 engineers — they move faster, own more, and require less coordination.

**Core skills:**
Everything from Paths 1 and 2, with less depth in each area initially. The trade-off is deliberate: breadth first, then you specialise over time as you discover what you enjoy most.

**Entry point:**
₹8–20 LPA India. $100–150k USD. The salary ceiling is similar to specialised paths because depth eventually matters.

**Most common job title at:** Product startups, funded early-stage companies, mid-size SaaS companies. Rare at large platform companies (Google, Meta prefer specialists).

**How AI changes this path:**
Full-stack engineers benefit most from AI tools because they have the most surface area to cover. Copilot effectively gives you a junior engineer for each layer. The premium skill becomes product judgment: knowing what to build, in what order, to what quality level.

**Is this path for you if:** You want variety, you prefer owning things end-to-end rather than specialising early, you like startup environments, you are comfortable switching context frequently.

---

#### Path 4: Data Scientist / ML Engineer

**What they do every day:**
Build systems that learn from data. This includes: cleaning data (tedious but essential), building features, training models, running experiments to measure whether an intervention actually works, and deploying models into production. Data scientists answer questions like "does this notification increase retention?" and "which users are likely to churn?" Machine learning engineers focus more on the systems that serve predictions reliably at scale.

**Core skills:**
Python (essential — not optional). Statistics, probability, and linear algebra (Session 4 material is foundational). ML frameworks: scikit-learn for classical methods, PyTorch for deep learning. SQL for data extraction. Experimentation and A/B test design.

**Entry point:**
₹10–25 LPA India. $110–160k USD. Senior ML Engineers at top companies earn ₹40–80 LPA in India.

**5-year trajectory:**
Data Analyst → Data Scientist → Senior DS → Principal DS or Head of AI

**The curriculum connection:**
The xG model in Session 5 is a direct toy version of what data scientists build. You loaded a dataset, engineered a feature (shot distance and angle), trained a logistic regression model, and evaluated it with AUC. Real data scientists do this at 100x the scale with real stakes.

**How AI changes this path:**
AutoML tools handle some model selection. But data scientists who understand why a model works, who can design experiments correctly, and who have domain expertise to ask the right questions are increasingly valuable — not less.

**Is this path for you if:** You enjoyed the xG session, you are drawn to statistics and probability, you want to build things that make predictions, you are comfortable with uncertainty and experimentation.

---

#### Path 5: AI / LLM Engineer (new role, 2023–)

**What they do every day:**
Build products and systems on top of large language models. This includes: designing prompts that reliably produce good outputs, building Retrieval-Augmented Generation (RAG) systems that let LLMs answer questions from private data, fine-tuning models on domain-specific data, building evaluation frameworks to measure whether an AI system is actually working, and designing agentic workflows where LLMs take multi-step actions.

**Core skills:**
Python. LLM APIs (OpenAI, Anthropic, Gemini). Vector databases (Pinecone, Weaviate, pgvector). Prompt engineering and evaluation. Understanding of transformer architecture (not required to implement, but essential to understand). LangChain, LlamaIndex, or similar orchestration frameworks.

**Entry point:**
₹15–35 LPA India. $130–200k USD. This is the highest-entry salary of any engineering role in 2025, driven by extreme demand and limited supply.

**Why NITW M&C students have an edge:**
The Session 6 lab — building an agent with tool use — is direct preparation. You have already written a system prompt, defined tools, and watched an LLM reason through a problem. Most computer science graduates have not done this.

**Honest caveat:**
This field is moving so fast that specific tools you learn today may be obsolete in 18 months. What will not be obsolete: understanding how LLMs work, how to evaluate them, and how to design systems that use them reliably. Learn the fundamentals, not just the current hottest library.

**Is this path for you if:** The Session 6 agent lab made you want to build more, you are genuinely excited about AI, you are comfortable with rapid change and incomplete documentation, you want to work at the frontier.

---

#### Path 6: DevOps / Platform / SRE Engineer

**What they do every day:**
Keep everything running. Deploy code to production. Build and maintain the pipelines that automatically test, build, and ship software. Design infrastructure that scales. Monitor systems for failures. Write postmortems when things break. Reduce the number of times things break.

SRE (Site Reliability Engineering) is Google's term for this role, focused on reliability as an engineering discipline. Platform Engineering is the newer framing — building internal developer tools so software teams can ship faster.

**Core skills:**
Docker and Kubernetes (containerisation and orchestration). Terraform (infrastructure as code). Cloud platforms: AWS, GCP, or Azure. Linux command line fluency. Scripting (Python, Bash). Monitoring tools (Prometheus, Grafana, Datadog).

**Entry point:**
₹8–20 LPA India. $110–160k USD. Senior DevOps/SRE engineers at tier-1 companies earn ₹40–80 LPA in India.

**The curriculum connection:**
Session 9 — servers and deployment — is the beginning of this path. Every time a production server stays up during a traffic spike, there is an SRE who designed the system that made that possible.

**Is this path for you if:** You enjoy systems administration, you are calm under pressure, you find the infrastructure layer intellectually interesting, you like the idea of owning reliability as a measurable outcome.

---

#### Path 7: Quant Developer / Algo Trader

**What they do every day:**
Build mathematical models that predict market movements and execute trades automatically. Write backtesting frameworks to test whether a strategy would have worked on historical data. Build execution systems that trade at millisecond latency. Measure and manage risk. Collaborate with quantitative researchers who design the models.

**Core skills:**
Python for research; C++ for execution systems where microseconds matter. Statistics and probability — this is non-negotiable. Financial mathematics: options pricing, risk models, factor models. Backtesting methodology. SQL and time-series databases.

**Entry point:**
₹15–40 LPA India at prop trading firms. $150–300k USD base at top US firms, plus bonus that can equal or exceed base. This is the highest-compensation engineering role that hires fresh graduates at top firms (Jane Street, Citadel, Two Sigma, D.E. Shaw).

**5-year trajectory:**
Quant Researcher/Developer → Senior Quant → Portfolio Manager or Head of Research

**Why NITW M&C is specifically relevant:**
The mathematics and computer science combination is the exact background quant roles require. Sessions 7 and 8 — financial modelling and the algorithmic trading capstone — are direct preparation. Students who graduate from NITW M&C and continue building trading system projects have a concrete, differentiated application story.

**Honest context:**
Top quant firms hire very selectively. The interview process involves competitive programming-level algorithmic problems, probability puzzles, and mathematical reasoning. It is hard to break into. But for students who are drawn to both math and markets, no other path has a comparable reward structure.

**Is this path for you if:** Sessions 7 and 8 were among your favourites, you find markets and probability genuinely interesting (not just the money), you enjoy rigorous mathematical reasoning, you are willing to invest significantly in competitive programming skills.

---

#### Path 8: Engineering Manager / Technical Product Manager

**What they do every day:**
Not coding — at least not primarily. Engineering Managers lead teams of engineers: hiring, performance, career development, process, and removing blockers. Technical Product Managers define what gets built, why, and in what order — they translate business needs into engineering requirements and vice versa.

**Why it appears here:**
This is not an entry-level path. It typically requires 5–7 years as an individual contributor first. But understanding it now matters because the students who become great managers are the ones who were excellent engineers first, and who developed strong communication and systems-thinking skills alongside their technical depth.

**Core skills:**
Communication — written and verbal. System thinking. Prioritisation and tradeoffs. Technical credibility (you cannot lead engineers without earning their respect). Empathy.

**Entry point:**
Usually a transition from Senior Engineer. Compensation is comparable to or slightly higher than Staff Engineer.

**Is this path for you if:** You find yourself naturally organising projects and people, you care as much about how a team works as what it builds, you are drawn to the product side as much as the technical side.

---

### Part 2: NITW M&C Specifically

#### What the placement landscape looks like — honestly

NITW placements span a wide range. At the lower end: TCS, Infosys, Wipro at ₹3.5–6 LPA (CTC that looks lower once you read the fine print). At the higher end: Goldman Sachs, Microsoft, Google, Walmart Global Tech, and well-funded startups at ₹25–80 LPA for exceptional candidates.

The distribution is not a bell curve. It is heavily skewed — a small number of students get significantly better outcomes than the majority. Understanding why that gap exists is the most practically useful thing you can take from this session.

#### What separates top placements from average ones

It is almost never GPA. This is not an argument against studying — fundamentals matter. But the students who get Goldman Sachs over TCS have one or more of these:

1. **A real project on GitHub** that they can demo and discuss deeply. Not a tutorial project. Something original they built to solve a problem they cared about.
2. **Competitive programming credibility** — Codeforces rating, LeetCode consistency, or ICPC participation.
3. **An internship** that exposed them to production code.
4. **A specific skill** that the company needs and cannot easily find — AI/LLM engineering in 2025 is the clearest example.
5. **The ability to talk about their work clearly** — most candidates cannot explain what their own projects do in plain language.

#### The open-source portfolio argument

One good GitHub project — genuinely novel, well-documented, with clear commits showing real work — matters more for placement than any certificate, any MOOC completion badge, and most academic projects. Why? Because it demonstrates:

- You can build something end-to-end
- You can make technical decisions independently
- You care about the craft enough to do it outside class
- You know how to communicate your work (README, commit messages)

Start building this in Semester 1. It does not have to be impressive at first — it has to be real.

#### The AI advantage — claim it or lose it

Students who arrive at NITW already knowing how to build LLM-based agents, how to think about prompt engineering, how to evaluate AI system outputs — they start 18–24 months ahead of classmates who are encountering these ideas for the first time in their 3rd or 4th year.

That advantage erodes fast. By Semester 3, the students who act on it will be meaningfully ahead. The students who set it aside and focus entirely on curriculum will have lost the gap.

---

### Part 3: What Compounds vs What Decays

This is possibly the most important mental model in the session. Not all skills are equal — some get more valuable the more you have of them, and some get less valuable as tools improve.

#### Skills that compound — invest heavily in these

**System design and architecture thinking:** The ability to look at a complex system and understand how the pieces fit together — what the bottlenecks are, what will break first under load, what the right abstraction is. This skill gets dramatically more valuable with each year of experience. Senior engineers earn 3–5x what junior engineers earn primarily because of this skill.

**Communication and writing:** Technical people who can write clearly and speak persuasively are disproportionately influential. The engineer who writes the design document that convinces the team owns the decision. The engineer who cannot articulate their ideas clearly loses influence relative to their technical ability. This is learnable — start now.

**Debugging and problem decomposition:** The ability to take a system that is not working and systematically find out why. This generalises across every language, framework, and era of technology. It is a thinking skill, not a tool skill.

**Domain depth combined with technical skill:** A developer who understands finance deeply (NITW M&C!) is more valuable to a fintech company than a better pure developer without that context. Domain expertise does not decay — it compounds. Finance + code, biology + code, sports + code. The intersection is where the interesting problems live.

**Understanding how things actually work:** Not just how to use React, but why it re-renders when it does. Not just how to call an API, but what HTTP is. Not just how to use pandas, but why vectorised operations are faster. Deeper understanding takes longer to acquire but does not get obsoleted by the next tool update.

#### Skills that decay — be careful about over-investing

**Specific framework knowledge:** React is dominant today. It was not dominant 10 years ago. In 10 years, something else may dominate. Learning React is still worth doing — but do not learn React as if React is the goal. Learn React while learning the underlying concepts that will transfer.

**Memorising syntax:** AI writes syntax. GitHub Copilot, Claude, and similar tools handle boilerplate at a level that makes memorisation irrelevant. What matters is knowing what to ask for and being able to evaluate whether the output is correct.

**Following tutorials without building original things:** Tutorial completion creates the feeling of learning without most of the actual learning. The hard part — deciding what to build, debugging novel problems, making design decisions without a guide — is where the skill actually forms. Do tutorials to learn syntax, then immediately abandon them to build something of your own.

---

### Part 4: The 10-Year View — AI's Real Impact

Be honest with students here. There is a lot of fear and a lot of hype. The truth is more nuanced.

#### What AI will replace (or substantially automate)

- Writing boilerplate code (CRUD endpoints, standard UI components, test scaffolding)
- Simple, well-defined debugging tasks ("this error means X, here is the fix")
- Documentation — first drafts, at least
- Some testing — generating test cases for known input/output patterns
- Code review for obvious style issues
- Routine data analysis tasks

#### What AI will not replace

**System architecture and design:** Deciding how to structure a system under constraints that are not in the training data, that involve novel business context, and that have consequences measured in years — AI cannot reliably do this. Humans who reason well about systems under uncertainty will be in higher demand, not lower.

**Product judgment:** Deciding what to build is not a coding problem. It requires understanding users, understanding business models, and making bets under uncertainty. This is irreducibly human.

**Novel problem solving:** When the problem has never been solved before, there is no training data. The frontier of what is possible is where humans work.

**Ethics and accountability:** Someone has to be responsible for what a system does. AI systems do not bear responsibility — the humans who design, deploy, and oversee them do.

**Managing uncertainty:** When requirements are unclear, stakeholders disagree, and the right path is genuinely unknown — this is most of actual engineering work at senior levels. AI is a tool within this context, not a replacement for it.

#### The key insight about AI and careers

*"The engineer who uses AI to do 10x more work is not replaced by AI — they replace 9 other engineers."*

Write this on the board. Let students respond. The implication is important: the bar for what a single engineer can produce rises dramatically. This means the premium shifts from "can write code" to "knows what code to write and why." The judgment layer becomes the scarce resource.

The students in this room who learn to use AI tools fluently — not just to write code, but to think through problems, to evaluate solutions, to move faster — will have a durable advantage. The ones who resist AI tools will be slow. The ones who outsource all thinking to AI will produce mediocre work they cannot explain or defend.

The goal: think like an engineer. Use AI as a tool that extends your capability, not a replacement for your judgment.

---

### Part 5: The First Year at NITW — Concrete Advice

This is practical. Read it as a list. Students should write these down.

**Join coding clubs immediately.** NITW has competitive programming clubs and project clubs. Join in the first month of Semester 1, before the social dynamics solidify and before you get behind. The peer group inside these clubs is the highest-leverage network you will build in college.

**Do open-source contributions by Semester 3.** This is a specific, achievable goal. Find a project on GitHub that you use or find interesting. Read the CONTRIBUTING.md. Fix a small bug. Submit a pull request. Repeat. By the time you are interviewing for internships, you have a track record of real commits to real projects.

**Build one real project per semester that you can demo.** Not a tutorial project. Not an academic assignment. Something you built because you wanted it to exist. In 8 semesters, that is 8 projects. At least one of them will be impressive enough to be a centrepiece of your resume.

**Internships are the single highest-leverage thing you can do.** A good internship in Semester 4 or 5 — at a funded startup, at a good product company, at a research lab — will do more for your placement than any combination of other activities. Pursue internships aggressively. Cold email people. Use LinkedIn. Go to hackathons where companies recruit.

**Go to hackathons.** They are not primarily about winning. They are about building things fast under pressure, meeting people who care about similar things, and getting visibility. Many good internships and jobs come from people you meet at hackathons.

**Network with seniors who are placed well.** The information gap between a third-year who has done a Goldman Sachs internship and a first-year is enormous. Buy that senior a coffee. Ask them what they wish they had known in first year. Ask what they did differently. This is freely available information that most students never seek out.

**The curriculum you just completed is 6–18 months ahead of most NITW freshers.** Use that gap. The students who arrive at NITW and spend the first year discovering what you already know — while you are building your first real project — will never catch up if you keep moving.

---

## ⚡ Wow Moment

Draw this on the whiteboard. Call it the "Career Salary Curve."

Year 0 (joining as fresher): All paths start roughly similar — ₹6–20 LPA range.

Year 5: The paths begin to diverge. A TCS engineer might be at ₹12–18 LPA. A good backend engineer at a product company: ₹25–40 LPA. A quant developer: ₹35–60 LPA.

Year 10: The gap is large. Average software engineer at a services company: ₹20–30 LPA. Senior engineer at a good product company: ₹50–90 LPA. Staff/Principal at a top company: ₹80–150 LPA. Quant/AI specialist: ₹80–200 LPA.

Year 20: The divergence is enormous. Senior engineering leadership or quant management: ₹1–3 Cr+ (plus equity). Average career: ₹40–60 LPA.

**The critical insight:** The gap between a great engineer and an average engineer does not narrow over time — it widens. In most professions, experience reduces the gap between the best and the rest. In software engineering, skill and reputation compound. The people at the top of the distribution earn 10–20x more than the median, not 2x.

This is not an argument to be greedy. It is an argument that investing in becoming genuinely excellent — early, consistently — has an unusually high return in this profession. The work you do in the next 4 years at NITW will compound for 20.

---

## 🔑 Key Concepts Checklist

Students should be able to explain these after the session:

- [ ] The difference between frontend, backend, and full-stack engineering
- [ ] What a data scientist does differently from an ML engineer
- [ ] What LLM Engineering is and why it is a new role (post-2022)
- [ ] What SRE/DevOps engineers do and why they are critical
- [ ] Why NITW M&C background is specifically suited to quant/algo trading careers
- [ ] What "compounding skills" means and be able to name 3 examples
- [ ] Why specific framework knowledge "decays" while architecture thinking "compounds"
- [ ] What AI will and will not replace in software engineering
- [ ] The open-source portfolio argument — what it is and why it works
- [ ] At least 3 concrete actions they should take in their first NITW semester

---

## Teaching Notes for Teacher

**On delivery:** This session should feel different from the technical sessions. More conversation, less lecture. After each career path, ask: "Does anyone think they might want this? What excites you about it? What worries you?"

**On salaries:** The salary numbers here are real but ranges are wide. India numbers are based on AmbitionBox/Levels.fyi data for 2024–2025. They vary significantly by city (Bangalore/Hyderabad pay more), company tier (product vs services), and specific role. Do not present these as guarantees — present them as the realistic range if students build good skills.

**On AI:** Some students will be worried. Some will be overconfident. Both reactions are wrong. The accurate message: AI is a powerful tool that raises the baseline for what engineers can produce. Students who use it thoughtfully and build judgment will be significantly more effective than those who either ignore it or outsource their thinking to it.

**On the quant path:** This is genuinely the highest-compensation path available to NITW M&C graduates who pursue it seriously. It is also the hardest to break into. Do not oversell it as easy — be honest that it requires competitive programming investment and mathematical depth. But do not undersell it either.

**If a student says "I don't know what I want to do":** That is the correct answer for most 17-18 year olds. The advice is: do not try to decide now, instead try things. Build projects in multiple areas in your first two semesters. The one you wake up wanting to keep working on — that is the signal.

**The most important thing to leave students with:** This is a profession where your effort and curiosity have a disproportionate impact on your outcomes. You are not in a system where showing up earns you a predictable reward. You are in a system where genuine investment in getting good compounds into something extraordinary. That is a gift, not a burden.

---

## 🧪 Quiz

**1. Multiple Choice**
You enjoy mathematics, probability, and financial markets. You found Sessions 7 and 8 among the most interesting in this curriculum. Which career path is most directly aligned with these interests?

A) Frontend Engineer
B) DevOps / SRE Engineer
C) Quant Developer / Algo Trader
D) Engineering Manager

*Answer: C*

---

**2. Multiple Choice**
Which of the following is an example of a "compounding skill" as discussed in this session?

A) Knowing the syntax of Python 3.10
B) Understanding how React's reconciliation algorithm works under the hood
C) Being proficient with a specific framework that is currently popular
D) Completing online tutorials in multiple programming languages

*Answer: B — understanding why something works (not just how to use it) transfers across tools and compounds over time.*

---

**3. Short Answer**
A student says: "AI will write all the code soon, so why should I bother learning to code?"

In 3–4 sentences, explain why this reasoning is flawed, using what you learned in this session.

*Sample answer: AI automates boilerplate and repetitive coding tasks, but it cannot make system architecture decisions, exercise product judgment, or solve novel problems. The engineers who are replaced are those who only knew how to write routine code — the ones who remain are those who know what to build and why. A student who learns to use AI as a tool to do 10x more work becomes more valuable, not less. The judgment layer — understanding systems, making tradeoffs, knowing what matters — is what cannot be automated.*

---

**4. Multiple Choice**
You are applying for a software engineering internship. You have a 9.2 CGPA but no personal projects and no open-source contributions. Your classmate has a 7.8 CGPA but has a well-documented GitHub project and one merged open-source pull request. For a product company internship, which candidate is likely to have the advantage?

A) You — CGPA is the primary screening criterion
B) Your classmate — the demonstrated work matters more than the GPA
C) Both candidates are equivalent
D) Neither has a sufficient profile

*Answer: B — product companies consistently prioritise demonstrated ability and initiative over academic grades.*

---

**5. Short Answer — NITW Specific**
Name two concrete actions you should take in your first semester at NITW to leverage the advantage this curriculum has given you.

*Sample answers: Join a coding club; start building a real project on GitHub; make your first open-source contribution; attend a hackathon; set up your development environment and write a project README; find a senior NITW student doing the career you want and reach out.*

---

**6. Multiple Choice**
What is the primary reason the salary gap between excellent engineers and average engineers widens over time (rather than converging)?

A) Excellent engineers are better at negotiating salaries
B) Technical skills compound — architecture judgment, domain depth, and reputation grow more valuable with experience
C) Companies pay more for seniority regardless of performance
D) Average engineers tend to leave the industry earlier

*Answer: B*

---

**7. Short Answer — Sports Analytics**
A sports analytics team wants to build a system that predicts which NBA players are likely to improve most over the next season, using historical performance data. Which career path(s) are most directly applicable, and name one skill from this curriculum that would be directly relevant.

*Sample answer: Data Scientist or ML Engineer. Directly relevant skills from this curriculum: logistic regression / supervised learning (Session 5), feature engineering from sports data, model evaluation. The xG model in Session 5 is structurally similar — predicting a probability from features extracted from historical events.*

---

**8. Reflection — No Wrong Answer**
What is the single most important thing you want to build or learn in your first year at NITW? Be specific: not "learn more coding" but "build an AI system that [does X]" or "understand how [Y] works at a deep level."

*This is ungraded. The point is to get students thinking concretely rather than abstractly about their goals.*

---

## 📚 Research Materials

### Salary and Compensation Data
- **Levels.fyi** (levels.fyi) — The most accurate source for software engineering compensation at technology companies globally. Includes India data for Bangalore, Hyderabad, and Mumbai. Essential before any salary negotiation.
- **AmbitionBox** (ambitionbox.com) — India-specific, broader coverage including services companies and mid-tier companies. Good for understanding the full distribution, not just the top end.
- **Glassdoor** (glassdoor.co.in) — Self-reported but useful for understanding culture and interview processes alongside compensation.

### Career Roadmaps
- **roadmap.sh** — The single best free resource for understanding what skills each engineering path requires and in what order to learn them. There are roadmaps for Frontend, Backend, DevOps, Data Science, AI/ML, and more. Every student should bookmark this site immediately.

### People to Follow (for genuine learning, not just inspiration)
- **Swyx (@swyx)** — The best thinker and writer on AI engineering and the LLM ecosystem. His "Latent Space" podcast and writing on "Learning in Public" are essential for anyone entering the AI/LLM path.
- **Addy Osmani** — Google Chrome engineering lead. His writing on frontend performance, JavaScript, and engineering leadership is at a consistently high level. Excellent for frontend and full-stack paths.
- **Kelsey Hightower** — Former Googler, DevOps/Kubernetes thought leader. His talks and writing on platform engineering are the standard reference in the field.
- **Swaminathan Sivasubramanian** — VP of Databases at AWS. Indian engineer who built one of the most important technical organisations in the world. Relevant model for the NITW path to senior engineering leadership.

### Books (Worth Owning)
- **"The Pragmatic Programmer" by David Thomas and Andrew Hunt** — The best book on what it means to be a professional software engineer. Not about any specific language or framework — about how to think about software craft. Read it in your first year.
- **"Designing Data-Intensive Applications" by Martin Kleppmann** — The standard reference for understanding databases, distributed systems, and data architecture. Harder reading, but this is the book that separates engineers who understand systems from those who merely use them. Read it in your second or third year.
- **"Staff Engineer" by Will Larson** — For students who want to understand the senior IC (individual contributor) path in detail. Readable in 4 hours. Gives an honest picture of what it takes to become technically influential at a large company. [Free →](https://staffeng.com/guides/)
- **"The Art of Problem Solving" series** — For students pursuing the quant path. The mathematical reasoning developed here directly prepares for quant interviews.

### Podcasts and Video Channels
- **Lex Fridman Podcast** — Long-form conversations with leading researchers and engineers in AI, robotics, and computer science. Not a tutorial resource — a window into how the best people in the field think.
- **ThePrimeagen** — Former Netflix engineer, now content creator. Excellent for understanding what senior engineering actually looks and feels like. Particularly good on systems programming and performance.
- **Fireship** — 100-second to 10-minute explainers on every technology in the modern stack. Best for quickly understanding what a new technology is and when you would use it.
- **Latent Space Podcast** (swyx and Alessio Fanelli) — The best podcast on AI engineering. More technical than general AI podcasts, focused on what engineers actually build.

### For the Quant Path Specifically
- **Jane Street's Blog and YouTube** — Jane Street publishes genuine technical content about how they think. Reading their materials is one of the best ways to understand what quant trading actually involves.
- **Quantlib** (quantlib.org) — Open-source library for quantitative finance. Contributing to this project is a concrete way to build a portfolio for quant roles.
- **"A Random Walk Down Wall Street" by Burton Malkiel** — Essential context for understanding markets before building trading systems. [Open Library](https://openlibrary.org)
