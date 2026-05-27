# Session 9 — How Software Engineering Grew Up
## The Complete Landscape: 2010 → 2026

**Duration:** 2–3 hours  
**Format:** Narrative overview + discussion. No heavy coding.  
**the teacher's prep:** Pull up real examples for each era as you go — GitHub, AWS console, a Kubernetes dashboard, a Copilot demo.

---

## 🎯 Goal

By the end of this session, Student can:
- Describe what software engineers do at each layer of a modern system
- Understand why the field evolved the way it did (each era solved a real problem)
- Name the key technologies in each era and what they replaced
- Know where AI-Assisted Engineering fits — and why it's the era he's entering

---

## 📖 the teacher's Narrative

### Hook

*"If you joined a software team in 2010, you'd write Java in a text editor and deploy by copying files to a server manually. If you joined in 2026, you'd have an AI pair programmer, deploy to a cloud that auto-scales to millions of users, and your infrastructure would rebuild itself if it broke. Same job title — completely different reality. Here's how it happened."*

---

## Era 1 — 2010: Java, OOP & Web Fundamentals
### *"Learn to speak to a machine in full sentences"*

**The world in 2010:** Smartphones were 3 years old. The cloud barely existed. Most software ran on servers companies owned in-house.

**What engineers learned:**
- **Java** — the dominant enterprise language. Verbose but reliable. Still runs most of the world's banking and insurance systems.
- **OOP (Object-Oriented Programming)** — organise code around objects (a `Player` has `goals` and can `shoot()`). The dominant paradigm for 30 years.
- **HTML/CSS/JavaScript** — the front end: what users actually see and click.
- **Server-side basics** — a web server receives requests, queries a database, sends back HTML. The model behind 99% of websites.

**The key insight:** Software engineering in 2010 was about learning *one* language deeply and one paradigm (OOP) thoroughly. Mastery mattered more than breadth.

**Who owned this era:** **Oracle** owns Java and has since its acquisition of Sun Microsystems in 2010. The **Spring Framework** — the toolkit that made large Java applications manageable — came from Pivotal (later acquired by VMware). **IBM** dominated enterprise contracts, selling the consulting services and hardware that ran Java applications in banks and insurance companies. That world hasn't gone away — every major bank and insurance company still runs Java at its core. It's the "boring but extremely well-paid" end of engineering.

**What Student already knows from this curriculum:**  
Session 1.2 (how the web works), Session 3 (programming languages), Session 4 (Python — same OOP principles apply in Java)

---

## Era 2 — 2012: Python & JavaScript
### *"Scripting your way to productivity"*

**The problem it solved:** Java is powerful but slow to write. Every experiment takes days to set up. Scientists, data analysts, and web startups needed something faster.

**What engineers learned:**
- **Python** — Student knows this. Scripting, automation, data analysis. The language that ate research.
- **JavaScript (Node.js)** — JavaScript escaped the browser. Now you could run it as a server. One language, everywhere.
- **Backend basics** — routing requests, connecting to databases, building simple APIs.
- **Frontend foundations** — making web pages dynamic without reloading.

**The shift:** Speed of development started to matter as much as raw performance. "Ship it fast, improve it later" became viable.

**Who drove this era:** **Dropbox** famously rewrote its entire backend from Java to Python — a signal to the industry that Python was production-ready. **Node.js** was created at **Joyent** by Ryan Dahl in 2009, with the explicit goal of handling thousands of simultaneous connections without the overhead of Java threading. The **npm** registry (Node Package Manager) became the single largest software registry in the world — millions of reusable packages, free for anyone.

**Sports parallel:** *"It's like the difference between a methodical possession team (Java) and a high-press counter-attacking side (Python). Both can win. Different contexts."*

---

## Era 3 — 2014: SPA & TypeScript
### *"The web becomes an app"*

**The problem it solved:** Every click reloading the whole page felt clunky. Gmail, Google Maps, and Facebook had proven that web apps could feel like native desktop apps.

**What engineers learned:**
- **Single-Page Applications (SPAs)** — the page loads once. User interactions swap content dynamically via API calls without reloading. (Student saw this in the DevTools lab — those XHR requests are SPAs talking to servers.)
- **Angular / React / Vue** — frameworks that manage the complexity of SPAs.
- **TypeScript** — JavaScript with type hints, created by **Microsoft** (Anders Hejlsberg, 2012). Catches bugs before the code runs. Scales better in large teams. Microsoft also released **VS Code** (2015) — a free editor built in TypeScript, now the most-used editor in the world.

**The shift:** Frontend engineering became a serious specialisation. "Full-stack" became a thing — one engineer who could do both front and back end.

**The framework wars — and how they ended:** **Google** open-sourced Angular in 2010. **Facebook** open-sourced React in 2013. React won. Today it powers Meta's own products, plus Airbnb, Netflix, and Atlassian — and it's the default choice for most new frontend projects worldwide. (TypeScript and VS Code, as noted above, are Microsoft's contributions to this era.)

**What it looks like today:** Instagram, YouTube, Gmail — all SPAs. When you scroll your feed and new posts load without the page refreshing, that's an SPA making API calls.

---

## Era 4 — 2015: Spring Boot & REST APIs
### *"Backend becomes a factory"*

**The problem it solved:** Building a backend from scratch for every project took months. Teams needed standard patterns they could rely on.

**What engineers learned:**
- **Spring Boot (Java)** — a framework that wires up a backend server with minimal configuration. Annotations do the heavy lifting. A REST API in a few dozen lines.
- **REST APIs** — Student knows this from Session 1.2. HTTP verbs (GET, POST, PUT, DELETE) as a standard contract between frontend and backend. The universal language of the modern web.
- **Enterprise patterns** — dependency injection, ORMs (translate between code and databases), middleware.

**The shift:** Backend development became about assembling well-designed components, not building from scratch. Most of a typical backend is now framework code; engineers focus on the business logic.

**The companies that set the standard:** **Twitter's** public API in this era was studied by every backend engineer — it established the vocabulary for how REST APIs should behave. **Stripe** took it further: their API documentation became the industry benchmark for how to design developer-facing APIs (clear, consistent, testable). **Twilio** made the most important point of all — that an API *itself* could be a business model. You didn't need an app; you could sell access to a capability over HTTP and charge per call.

**A real example:** When the student's `sports_analyst.py` calls the Claude API, it's making a REST POST request to Anthropic's backend — which almost certainly runs on a framework like this.

---

## Era 5 — 2016: SOA, Microservices & DevOps
### *"Break the monolith. Ship every day."*

**The problem it solved:** As teams grew, one giant codebase became a nightmare. Netflix deploying a new feature required every team to coordinate. Deployments were terrifying events that happened once a month.

**What engineers learned:**

**Microservices** — instead of one big app, split it into many small services. Netflix has ~700 microservices. Each does one thing: one for authentication, one for recommendations, one for video streaming. Each team owns their service. Each deploys independently.

**SOA (Service-Oriented Architecture)** — the architectural pattern that microservices refined. Services communicate over networks, each exposing APIs.

**DevOps** — previously: developers wrote code, a separate "operations" team deployed it. DevOps: the same team does both. Automation handles the repetitive parts.

**CI/CD (Continuous Integration / Continuous Deployment):**
```
Developer pushes code
  → automated tests run
  → if tests pass, code auto-deploys to production
  → in production in minutes, not months
```

**Docker** — package your app and all its dependencies into a "container." *"Works on my machine"* becomes *"works everywhere."*

**The shift:** Software stopped being released in big versions and started being released continuously. Netflix deploys new code thousands of times per day.

**The pioneers:** **Netflix** didn't just use microservices — they invented the playbook. They broke a single monolith into 700+ independent services, and then went further: they built **Chaos Monkey**, a tool that *deliberately kills random services in production* to test whether the rest of the system can survive. The philosophy: if failure is inevitable, practise it constantly. **Amazon** made the architectural shift even earlier — around 2002, Jeff Bezos issued his famous internal "API mandate" memo, requiring every team to expose their data through APIs and communicate only that way. Bezos added the line: "Anyone who doesn't do this will be fired." That mandate is the origin story of AWS. **Docker** was created by Solomon Hykes at a startup called dotCloud in 2013 — originally an internal tool, demonstrated in a five-minute PyCon lightning talk, and immediately recognised as something the whole industry needed.

**Sports parallel:** *"This is like changing from a squad of 11 generalists to 11 specialists — a goalkeeper specialist coach, a set-piece coach, a fitness coach. Each expert in their lane. Faster to improve each part."*

---

## Era 6 — 2017: Cloud Engineering
### *"Someone else's computer — but infinitely scalable"*

**The problem it solved:** Running your own servers is expensive, slow, and brittle. You need a data centre, hardware procurement, power, cooling, maintenance. For a startup, this kills you before you even start.

**What engineers learned:**

**AWS / Azure / GCP** — rent compute, storage, networking, databases from Amazon/Microsoft/Google. Pay per second of use. Scale to millions of users without buying a single server.

**Key cloud services:**
| Service | What it does | Real example |
|---------|-------------|--------------|
| EC2 / Compute VMs | Virtual machines | Run your Python server |
| S3 / Blob Storage | Store any file | Store user photos |
| RDS | Managed databases | PostgreSQL without the admin |
| Lambda | Run code without a server | Respond to an API call |
| CDN | Serve files from nearest location | Fast video loading |

**Infrastructure as Code** — describe your infrastructure in code (Terraform, CloudFormation). Same version control, review, and automation as software. Rebuild your entire production environment in minutes.

**The shift:** A two-person startup could now serve millions of users on the same infrastructure as Netflix. The playing field levelled.

**The big three — and the numbers:** **AWS** (Amazon) launched in 2006, giving it a ten-year head start on rivals. Today it holds ~32% of the cloud market. **Azure** (Microsoft) is at ~22%, and **GCP** (Google) at ~11%. Google's contribution that changed everything wasn't just cloud compute — in 2014 they open-sourced **Kubernetes**, the container orchestration system they had built internally under the name Borg. It became the standard way to run microservices across every cloud provider.

**the student's connection:** Every API he's called in this curriculum (Claude, yfinance) runs on cloud infrastructure. The Anthropic API is deployed on AWS or GCP. He's been a cloud user since Session 6.

---

## Era 7 — 2020: Kubernetes & Observability
### *"Managing the chaos of microservices at scale"*

**The problem it solved:** Microservices and Docker were great — until you had 700 of them. How do you restart a crashed container? How do you deploy a new version with zero downtime? How do you scale when traffic spikes? You need an orchestrator.

**What engineers learned:**

**Kubernetes (K8s)** — the operating system for containers. You declare: *"I want 5 copies of this service running at all times."* Kubernetes makes it happen — starts containers, restarts crashed ones, routes traffic, scales up and down.

```yaml
# Tell Kubernetes: run 3 copies of the API
# If one crashes, automatically restart it
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sports-api
spec:
  replicas: 3
  ...
```

**Observability** — when your system is 700 microservices, how do you know what's broken?
- **Logs** — every service writes what it did (structured text)
- **Metrics** — numbers over time (requests/second, error rate, response time)
- **Tracing** — follow one user request across all 12 services it touched

**The shift:** Reliability became a first-class concern. Teams started having SLOs (Service Level Objectives) — "99.9% of requests will respond in under 200ms." Engineers who could run and monitor systems at scale became the most valuable people in tech.

**The tooling ecosystem:** **Datadog** and **Grafana** became the commercial dashboards every engineering team lived inside. **Prometheus** — open-source, created at **SoundCloud** in 2012 — became the standard for collecting metrics. The observability market is now worth $3B/year. For infrastructure itself, **HashiCorp** built **Terraform**, making "infrastructure as code" mainstream: describe your entire cloud setup in a text file, version-control it, and rebuild your production environment from scratch in minutes.

---

## Era 8 — 2023: Platform Engineering & Security
### *"Build the roads, not just the cars"*

**The problem it solved:** Every team building its own CI/CD pipeline, its own logging, its own deployment workflow created massive duplication. Developers spent more time on infrastructure toil than on actual features.

**What engineers learned:**

**Platform Engineering** — build an internal developer platform (IDP). A "golden path" — an opinionated, pre-built way to do common things. New developer joins → clones a template → runs one command → has a fully configured, deployable service.

*"Platform engineers are the people who build the tools that other developers use. They make everyone else go faster."*

**Shift-Left Security** — historically, security was tested at the end ("pen testing" before release). Shift-left means: find security issues as early as possible — in the IDE, in CI/CD, before code reaches production. Automated scanners check every pull request.

**Golden paths give teams:**
- Standard Dockerfiles
- Pre-configured CI/CD pipelines  
- Automatic security scanning
- Observability baked in

**The shift:** The best engineers in 2023 weren't just building features — they were building the platform that made everyone else more productive. This is "10x engineer" done right.

**The companies that defined this era:** **Spotify** built an internal developer portal called **Backstage** to manage their hundreds of microservices — and then open-sourced it in 2020, where it became the blueprint for how companies build IDPs. **Vercel** and **Netlify** solved the same problem for frontend teams: deploy a web app by pushing to Git, full stop. And the era ended with a landmark acquisition: **IBM bought HashiCorp for $6.4 billion in 2024** — a sign that infrastructure tooling had become valuable enough for the old enterprise giants to want it back.

---

## Era 9 — 2026: AI-Assisted Software Engineering
### *"The era Student is entering"*

**The problem it solved:** Even with all the tooling above, writing software is still slow. Boilerplate, tests, documentation, debugging, code review — most of an engineer's time isn't on hard problems, it's on repetitive ones.

**What engineers are learning now:**

**Code Copilots** — AI that writes code alongside you. **GitHub Copilot** (Microsoft + OpenAI, 2021) was first — trained on billions of lines of code from GitHub, which Microsoft acquired for $7.5B in 2018. **Cursor** arrived next, built on Claude (Anthropic's model). **JetBrains AI** — embedded in the IDE most professional Java and Kotlin developers already use — draws on multiple models. **Amazon CodeWhisperer** targets developers already inside the AWS ecosystem. Over 1 million developers use Copilot daily, and that number is growing across all the tools. You describe what you want; the AI writes a first draft. You review, refine, redirect.

**Agentic Workflows** — AI that takes multi-step actions autonomously. "Review this PR, run the tests, fix the failing ones, update the documentation." Student built a simple agent in Session 6. Production systems now have agents managing entire workflows.

**LLM Apps** — applications where the AI IS the core feature, not an add-on. The sports analyst, the tutor bot — those are LLM apps. Every company is building them now.

**AI-Native Development** — designing systems from the start assuming AI is part of the team. Different architecture choices, different testing strategies, different cost models.

**The honest reality:**
- AI doesn't replace software engineers. It removes toil.
- An engineer using AI tools writes 2–5× more code per day.
- The engineers who adapt fast will be the most valuable.
- The skills that matter more: system design, problem decomposition, judgment, debugging, knowing when the AI is wrong.

*"Student is entering engineering at the exact moment it's being reinvented. He doesn't have to unlearn 10 years of habits. He gets to start native."*

---

## ⚡ Wow Moment — The Full Stack of a Modern System

Draw this on a whiteboard (or show it as a diagram):

```
  USER                                          
    │                                           
    ▼                                           
[SPA / React]          ← Era 3 (2014)           
    │                                           
    ▼ REST API call                             
[API Gateway]          ← Era 4 (2015)           
    │                                           
    ├──► [Auth Service]                         
    ├──► [Player Stats Service]    ← Era 5 (2016) microservices
    ├──► [AI Analysis Service]     ← Era 9 (2026)
    └──► [Notification Service]    
              │                                 
              ▼                                 
   [Kubernetes cluster]            ← Era 7 (2020)
              │                                 
              ▼                                 
   [AWS / GCP]                     ← Era 6 (2017)
              │                                 
              ▼                                 
   [Logs / Metrics / Traces]       ← Era 7 (2020)
```

*"When Student uses Instagram, his request travels through every single one of these layers. Now he knows what each one is called, why it exists, and when it was invented."*

---

## 🔑 Key Concepts Checklist

- [ ] OOP — organise code around objects with data and behaviour
- [ ] REST API — standard HTTP-based contract between services
- [ ] SPA — web app that loads once and updates dynamically
- [ ] TypeScript — JavaScript with type safety
- [ ] Microservices — break a large app into small, independent services
- [ ] Docker — package apps into containers that run anywhere
- [ ] CI/CD — automated testing and deployment pipeline
- [ ] Cloud (AWS/GCP/Azure) — rent infrastructure, pay per use
- [ ] Kubernetes — orchestrates containers at scale
- [ ] Observability — logs + metrics + tracing
- [ ] Platform engineering — build tools that make other devs faster
- [ ] Shift-left security — catch vulnerabilities early, in the pipeline
- [ ] Code copilots — AI pair programmers
- [ ] Agentic workflows — AI taking multi-step autonomous actions
- [ ] LLM apps — applications built around large language models

---

## Teaching Notes for Teacher

- This is a *map*, not a deep dive. The goal is orientation, not mastery.
- For each era, ask: *"Have you heard of any of these? Where?"* — Student may know Docker from YouTube or AWS from news.
- The strongest connection: Student has already used Era 9 tools (Claude API in Session 6). Go backwards from what he knows.
- Best question at the end: *"If you were joining a software team at NITW placement, which era's skills would be expected? Which would make you stand out?"*
- Honest answer: Eras 1-5 are table stakes at placement. Era 6-7 (cloud, K8s) makes you stand out. Era 9 (AI-native) is the frontier.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** What problem did microservices solve that the "monolith" architecture struggled with?
- A) Monoliths were too slow to write code in
- B) As teams grew, one giant codebase made coordination and independent deployments nearly impossible ✓
- C) Monoliths could not connect to the internet
- D) Monoliths required too many programming languages

**Q2.** What is a Docker container, and what problem does it solve?
- A) A database that stores application logs
- B) A virtual machine that runs a full operating system
- C) A packaged bundle of an application and all its dependencies that runs consistently anywhere ✓
- D) A cloud storage service for files

**Q3.** What does CI/CD stand for, and what does it automate?
- A) Cloud Integration / Cloud Deployment — automating server purchases
- B) Continuous Integration / Continuous Deployment — automating testing and releasing code to production ✓
- C) Code Inspection / Code Delivery — automating code reviews
- D) Container Integration / Container Deployment — automating Docker builds

**Q4.** Kubernetes is described as "the operating system for containers." What two specific problems does it solve that plain Docker alone cannot handle?

**Q5.** A startup is choosing between renting servers on AWS or buying their own physical servers. Give two advantages of the cloud option for an early-stage company.

**Q6.** What is "platform engineering" and how does it differ from regular software engineering?
- A) It is engineering for gaming platforms like PlayStation
- B) It involves building the internal tools and "golden paths" that make other developers more productive ✓
- C) It means writing code for cloud providers like AWS
- D) It is the same as DevOps — just a new name for an old role

**Q7.** The session describes AI copilots as "removing toil, not replacing engineers." What specific skills does the session say become MORE important in the AI-assisted era?

**Q8 (explain in your own words).** A football club's data engineering team runs a monolith: one giant codebase handles scouting data, squad planning, match analytics, and ticketing. The team is now 15 engineers and deployments are slow and risky. Using concepts from this session, explain what architectural change you would recommend and what specific benefits it would bring.

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — In a monolith, all features are tightly coupled. When Netflix grew to hundreds of engineers, one team's change could break another's, and releasing required everyone to coordinate. Microservices gave each team ownership of one service they deploy independently.

**Q2.** C — Docker containers bundle the application code with every library and configuration it needs. This eliminates the "works on my machine but not on the server" problem — the container behaves identically in development, testing, and production.

**Q3.** B — CI (Continuous Integration) automatically runs tests every time code is pushed. CD (Continuous Deployment) automatically releases code to production if tests pass. Together they let teams ship safely multiple times per day instead of once a month.

**Q4.** Kubernetes handles automatic restart of crashed containers (self-healing) and auto-scaling — spinning up more copies when traffic spikes and fewer when traffic drops. Docker alone just runs containers; Kubernetes orchestrates fleets of them.

**Q5.** Any two of: pay only for what you use (no upfront hardware cost); scale instantly to handle traffic spikes; no need for a physical data centre, power, or cooling; faster to get started; global infrastructure already built.

**Q6.** B — Platform engineers build the shared internal developer platform: standard CI/CD pipelines, Dockerfiles, monitoring, and deployment tools. Rather than shipping user-facing features, they multiply the productivity of every other engineer on the team.

**Q7.** The session names: system design, problem decomposition, judgment, debugging, and knowing when the AI is wrong. These are the higher-order skills that AI cannot yet replace.

**Q8.** Model answer: Recommend splitting into microservices — for example, a separate scouting-service, analytics-service, squad-planning-service, and ticketing-service. Each team can develop and deploy their service independently using CI/CD pipelines, which eliminates the coordination bottleneck. Docker containers ensure each service runs consistently across environments. Kubernetes can manage the services in production, restarting any that crash and scaling the analytics-service during peak usage (match nights). The overall result is faster releases, fewer cross-team breakages, and the ability to update the ticketing system without any risk to the match analytics pipeline.

---

## 📚 Research Materials

> 💡 **Start here:** Watch Fireship's "Docker in 100 Seconds" followed by "Kubernetes Explained in 100 Seconds" on YouTube — they are the fastest possible mental model for how containers and orchestration work before diving deeper.

### 🎬 Films & Documentaries

| Title | Year | What to watch for |
|---|---|---|
| [The Internet's Own Boy](https://www.imdb.com/title/tt3268458/) | 2014 | The story of Aaron Swartz; touches on open-source culture, the ethos behind GitHub, and the politics of software infrastructure |
| [General Magic](https://www.generalmagicthemovie.com/) | 2018 | The forgotten Silicon Valley project that incubated the engineers who later built the cloud infrastructure we use today |
| [lo and behold: Reveries of the Connected World](https://www.imdb.com/title/tt5ourselves/) | 2016 | Werner Herzog documentary on the internet's origins and infrastructure — excellent background on how the cloud came to exist |

### 📺 YouTube

| Channel | Video | Link |
|---|---|---|
| Fireship | Docker in 100 Seconds | [youtube.com/watch?v=Gjnup-PuquQ](https://www.youtube.com/watch?v=Gjnup-PuquQ) |
| Fireship | Kubernetes Explained in 100 Seconds | [youtube.com/watch?v=PziYflu8cB8](https://www.youtube.com/watch?v=PziYflu8cB8) |
| TechWorld with Nana | Docker Tutorial for Beginners — Full Course | [youtube.com/watch?v=3c-iBn73dDE](https://www.youtube.com/watch?v=3c-iBn73dDE) |
| TechWorld with Nana | Kubernetes Tutorial for Beginners — Full Course | [youtube.com/watch?v=X48VuDVv0do](https://www.youtube.com/watch?v=X48VuDVv0do) |
| Fireship | CI/CD Explained in 100 Seconds | *search "Fireship CI CD 100 seconds"* |
| AWS | AWS re:Invent — Werner Vogels Keynote (any recent year) | *search "Werner Vogels AWS re:Invent keynote"* |

### 📖 Books

| Title | Author | Level | What it covers |
|---|---|---|---|
| *The Phoenix Project* | Gene Kim, Kevin Behr & George Spafford | Easy | A novel about a fictional IT disaster; teaches DevOps, CI/CD, and platform engineering principles through story |
| *Building Microservices* | Sam Newman | Medium | The definitive practical guide to designing, building, and deploying microservices architectures |
| *Docker Deep Dive* | Nigel Poulton | Easy | Concise, practical introduction to Docker containers; widely used as a first Docker text |
| *Kubernetes Up and Running* | Brendan Burns, Joe Beda & Kelsey Hightower | Medium | Written by the creators of Kubernetes; the authoritative hands-on guide |
| *Accelerate* | Nicole Forsgren, Jez Humble & Gene Kim | Medium | Data-driven research on what separates high-performing engineering teams; makes the case for CI/CD with evidence |

### 🌐 Articles & Interactive Resources

| Resource | Link | What it covers |
|---|---|---|
| Play with Docker | [labs.play-with-docker.com](https://labs.play-with-docker.com) | Free browser-based Docker playground — run real containers without installing anything |
| Kubernetes Interactive Tutorial | [kubernetes.io/docs/tutorials/kubernetes-basics/](https://kubernetes.io/docs/tutorials/kubernetes-basics/) | Official step-by-step tutorial in your browser; deploys and scales a real app |
| Martin Fowler — Microservices | [martinfowler.com/articles/microservices.html](https://martinfowler.com/articles/microservices.html) | The original 2014 article that defined the term and the architectural pattern |
| GitHub Actions Documentation | [docs.github.com/en/actions](https://docs.github.com/en/actions) | Official docs for the most widely used CI/CD platform; includes worked examples for Python projects |
| The Twelve-Factor App | [12factor.net](https://12factor.net) | Methodology for building scalable, maintainable cloud-native applications — the principles behind every modern microservice |

### 🔗 People to Look Up

- **Solomon Hykes** — Creator of Docker; his 2013 PyCon lightning talk "The Future of Linux Containers" is the moment Docker was introduced to the world
- **Kelsey Hightower** — Principal Engineer at Google and one of the most respected Kubernetes educators; known for making complex infrastructure concepts genuinely accessible
- **Martin Fowler** — Chief Scientist at ThoughtWorks; coined or popularised "microservices", "continuous integration", and "refactoring"; his website martinfowler.com is an essential reference
- **Werner Vogels** — CTO of Amazon; architect of AWS; his philosophy "you build it, you run it" is the origin of DevOps culture in cloud computing
- **Linus Torvalds** — Creator of Linux (the OS inside every Docker container and cloud server) and Git (the version control system underpinning every CI/CD pipeline)
- **Nicole Forsgren** — Researcher whose DORA metrics (from the *Accelerate* book) are the industry standard for measuring software delivery performance
