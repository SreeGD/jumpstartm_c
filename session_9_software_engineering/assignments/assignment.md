# Session 9 — Assignment

---

## Task 1 — Build Something with Docker (Conceptual)

You don't need to run Docker yet. But understand what it does.

Read: https://docs.docker.com/get-started/overview/  
Watch: Search "Docker in 100 seconds" by Fireship on YouTube (2 minutes)

Then answer:
1. What problem does Docker solve? (In your own words, not copied)
2. What is the difference between a Docker image and a Docker container?
3. If the student's `sports_analyst.py` was put into a Docker container, what would need to be included in the container for it to run?

---

## Task 2 — Design a Microservices Architecture

Imagine you're building a "Sports Oracle" app (your capstone, scaled up) as a real product with 10,000 daily users.

Sketch the microservices architecture on paper:
- What services would you split it into? (at least 4)
- What does each service do?
- How do they communicate? (REST APIs between them)
- What database does each service need?

Draw a diagram (boxes and arrows — doesn't need to be beautiful).

**Example to get started:**
- `user-service` — handles login, profiles
- `stats-service` — fetches and caches sports data
- `ai-service` — calls Claude API, returns analysis
- `notification-service` — sends alerts when a player scores

Add your own ideas.

---

## Task 3 — Cloud Costs Research

AWS, GCP, and Azure all have pricing calculators.

Using AWS's pricing page (aws.amazon.com/pricing), estimate the monthly cost to run:
- 1 small virtual machine running 24/7 (t3.micro EC2)
- 10GB of file storage (S3)
- A database with 1GB of data (RDS)

Then: what would it cost to serve 1,000 users per day?  
(Hint: Lambda charges per request — look at Lambda pricing)

Write your estimates + 3 sentences on why cloud pricing can surprise startups.

---

## Task 4 — The AI Engineer Essay

Write 300–400 words answering:

*"You are entering software engineering in 2026 — the AI-native era. What skills do you think will matter most in 10 years? What won't matter? And what do you think AI will never be able to do in software engineering?"*

No research needed. This is what Student actually thinks. Teacher will challenge the answer.

---

## Task 5 — Glossary

Create a personal glossary of the 15 key concepts from Session 9's checklist.  
For each term, write:
- One sentence definition (in your own words)
- One real-world example (an app, company, or situation)

This becomes a reference card for NITW.

---

## Bring to Next Session

- App tech stack map (Part 1 of lab)
- Job description analysis (Part 3 of lab)
- Your learning roadmap ranking with reasons
- Docker explanation (Task 1)
- Microservices diagram (Task 2)
- The AI Engineer essay (Task 4)
- Glossary (Task 5)
