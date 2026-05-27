# Session 3 — The Family Tree of Programming Languages
## Introduction to Programming Languages

**Duration:** 1.5–2 hours  
**the teacher's prep:** Have side-by-side code comparisons ready. Install Python and VS Code before this session.

---

## 🎯 Goal

By the end of this session, Student understands:
- Why so many programming languages exist
- The key distinctions: compiled vs interpreted, high vs low level
- Where Python fits and why it dominates AI and data science
- He writes his first standalone Python file

---

## 📖 the teacher's Narrative

### Hook

*"There are over 700 programming languages. Why? Was that necessary? The answer tells you everything about how computing evolved — and why Python won."*

---

### Every Language Solved a Problem

**1950s — Machine Code**  
The first computers were programmed in binary. Literally flipping switches and entering 1s and 0s. Painful, error-prone, nearly impossible to maintain.

**1954 — FORTRAN (IBM)**  
Scientists at IBM had a problem: mathematicians wanted to write `E = M * C**2`, not `01001101 00101010`. John Backus created FORTRAN — the first high-level language. "Formula Translation." It let scientists write math-like code that compiled to machine code automatically.

*"The idea that a computer could translate human-ish instructions into machine code was revolutionary. Nobody believed it would work at the speed needed. Backus proved them wrong."*

**1972 — C (Bell Labs)**  
Dennis Ritchie needed a language to write an operating system (Unix). C gave programmers direct control over memory and hardware — it's close to the machine but readable by humans. Still used today in operating systems, embedded systems, and anywhere performance is critical.

**1983 — C++**  
C with "objects" — a way of organising code around real-world things (a `Player` object with attributes like `goals` and methods like `shoot()`).

**1991 — Python**  
*"Guido van Rossum was a Dutch programmer who was frustrated with every language he used. They were either too slow to write or too hard to read. Over Christmas 1989, he started writing a new language. He named it after Monty Python's Flying Circus because he wanted it to be fun."*

Python's philosophy: code should be readable — almost like English. It should be quick to write. The programmer's time is more valuable than the computer's time.

**1995 — Java**  
Sun Microsystems wanted code that could run anywhere — "Write once, run anywhere." Java runs on a virtual machine (JVM) that sits between the code and the hardware.

**1995 — JavaScript**  
Brendan Eich was hired by Netscape to add interactivity to web browsers. He wrote JavaScript in 10 days. It became the language of the web — every browser runs it, no installation needed. Now it runs servers too (Node.js).

**2012 — TypeScript (Microsoft)**  
JavaScript was written in 10 days and it shows — no types, no guardrails, errors only visible at runtime. Fine for a small web page. Catastrophic for a 500,000-line codebase with 200 engineers. Microsoft's Anders Hejlsberg (who also designed C#) created TypeScript: JavaScript with type annotations that catch bugs before the code runs. Today TypeScript is the default for any serious web project.

Microsoft also built **VS Code** (2015) — a free, open-source code editor written in TypeScript — and released it to the world. It became the most-used code editor on the planet. The tool you'll use throughout this curriculum is a Microsoft product.

---

### Key Distinctions

**Compiled vs Interpreted:**
- **Compiled** (C, C++, Rust): Translated to machine code *before* running. Faster to execute.
- **Interpreted** (Python, JavaScript): Translated line by line *while* running. Slower but more flexible, easier to test.

*"Python is interpreted. That's why you can open a Python REPL and type one line at a time and see the result instantly. That's also why it's slower than C for heavy computation — but with NumPy and GPU support, it doesn't matter for AI work."*

**High-level vs Low-level:**
- **Low-level** (C, Assembly): Close to hardware. You manage memory manually. Fast but hard.
- **High-level** (Python, JavaScript): Abstracts away hardware. Slower but much easier to write.

*Python is so high-level that `sorted([3,1,2])` just works — you don't need to know how sorting works internally.*

---

### Why Python Won AI

Three reasons:

1. **Readable** — research code is written once, read many times. Python reads like English. Scientists adopted it.

2. **Libraries** — NumPy (1995), SciPy (2001), Matplotlib (2003), Pandas (2008), Scikit-learn (2007), TensorFlow (2015), PyTorch (2016). Every AI/data library was built for Python first.

3. **Community** — the AI research community standardised on Python. Sharing code (GitHub), papers (arXiv), tutorials (YouTube) — all in Python. The network effect made it unstoppable.

*"If you learn Python, you can read every AI paper's code, contribute to every open-source AI library, and build anything from a web app to a neural network. That's why we're learning Python."*

---

## ⚡ Wow Moment — Same Problem, Different Languages

Show the Fibonacci sequence in four languages:

**Assembly (x86)** — ~40 lines of incomprehensible symbols  
**C** — 10 lines, still pretty opaque  
**Java** — 15 lines, lots of boilerplate  
**Python** — 4 lines, almost English

Then: `sorted([5, 2, 8, 1, 9])` in Python — one function call.  
The same in C — 20+ lines of memory management.

*"Python is fast to write. For building AI and data tools, the bottleneck is never Python — it's your ideas."*

---

## 🔑 Key Concepts Checklist

- [ ] Why languages exist — each solved a specific frustration
- [ ] FORTRAN — first high-level language, let scientists write math
- [ ] C — system programming, still used in OS kernels
- [ ] Python — readable, rich libraries, dominates AI/data science
- [ ] JavaScript — the language of the web
- [ ] Compiled vs interpreted — translate before or during execution
- [ ] High-level vs low-level — abstraction vs hardware control
- [ ] Why Python won AI — readability + libraries + community

---

## Teaching Notes for Teacher

- The history is a story — tell it as one. Don't list facts.
- The side-by-side comparison is the centrepiece. Spend time on it.
- By the end of this session, Python should be installed and VS Code open.
- Student types the Fibonacci code himself — first time with a real IDE.
- If he asks "which language should I learn after Python?" — answer: Python deeply first, then JavaScript for web, then C for systems/understanding.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** FORTRAN was created in 1954. What specific frustration was it designed to solve, and what made it revolutionary compared to what came before?
- A) Scientists had to write code in binary (machine code); FORTRAN let them write math-like expressions that a compiler translated to machine code automatically ✓
- B) Programs couldn't share code between projects; FORTRAN introduced reusable libraries
- C) Computers could only run one program at a time; FORTRAN added multitasking
- D) Memory had to be managed character by character; FORTRAN introduced automatic garbage collection

**Q2.** What is the difference between a compiled language and an interpreted language? Give one example of each from the session, and state one practical trade-off between them.

**Q3.** Python was started by Guido van Rossum over Christmas 1989. What was his core design philosophy — and how does `sorted([3,1,2])` demonstrate it compared to doing the same thing in C?
- A) Python prioritises execution speed above all else; sorted() is faster than C's qsort()
- B) Python prioritises programmer productivity and readability; sorted() is a single readable call that hides the 20+ lines of memory management required in C ✓
- C) Python prioritises portability; sorted() compiles to identical machine code on any platform
- D) Python prioritises security; sorted() validates inputs automatically in ways C cannot

**Q4.** Three reasons are given for why Python won AI. Name all three and briefly explain which you think was most important and why.

**Q5.** JavaScript was written by Brendan Eich in 10 days and became the language of the web. Today, every basketball stats website — NBA.com, Basketball Reference, Second Spectrum's dashboards — uses JavaScript. Why is JavaScript unavoidable for any interactive web application, regardless of what language the backend uses?
- A) JavaScript is faster than all other languages for number-crunching, which stats dashboards require
- B) JavaScript is the only language all web browsers can execute natively — so any interactivity in a browser (clicking, live chart updates, filtering stats) must eventually run as JavaScript ✓
- C) JavaScript has the best charting libraries, which happen to be the only ones browsers support
- D) JavaScript was chosen as a web standard because Netscape owned the dominant browser market in 1995

**Q6.** Explain in your own words the difference between a high-level language and a low-level language. Why would an engineer writing code for a Formula 1 car's engine management system choose C over Python?

**Q7.** Java's design philosophy was "Write once, run anywhere." What does the Java Virtual Machine (JVM) do, and why does that achieve portability?
- A) The JVM compiles Java code to C before running it, so it works on any system that has a C compiler
- B) The JVM is a software layer that runs on each machine and executes Java bytecode — the same compiled output runs unchanged on Windows, Mac, and Linux because the JVM handles the hardware differences ✓
- C) The JVM stores all Java programs in the cloud so they can be accessed from any device
- D) The JVM translates Java into Python, which is already cross-platform

**Q8.** A friend says: "Python is slow, so I'll learn C instead for my AI project." Based on what you learned in this session, explain why this reasoning is flawed.

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** A — Before FORTRAN, programmers wrote in machine code or assembly — binary patterns or symbolic representations of hardware instructions. FORTRAN (Formula Translation) let scientists write expressions like `E = M * C**2` and have the compiler convert them to machine code automatically. It was the first proof that a program could translate human-readable code into efficient machine instructions.

**Q2.** Compiled languages (e.g. C) translate the entire source code to machine code before execution — the result runs fast but must be recompiled for changes. Interpreted languages (e.g. Python) translate and execute code line by line at runtime — slower to execute but you can test one line at a time and see results immediately, making development faster.

**Q3.** B — Guido van Rossum's philosophy was that the programmer's time is more valuable than the computer's time. `sorted([3,1,2])` is immediately readable. The equivalent in C requires allocating memory, writing a comparison function, calling qsort, and managing memory cleanup — roughly 20+ lines of code. Python hides all of that so you can focus on the problem, not the plumbing.

**Q4.** Readability (research code is read many more times than it is written; Python reads like English, making it easy for scientists to share and review), Libraries (NumPy, Pandas, TensorFlow, PyTorch — every major AI/data library was built for Python first), and Community (the AI research community standardised on Python, creating a powerful network effect through GitHub, arXiv papers, and tutorials). The most important is arguably libraries — even a beautiful language dies without a rich ecosystem.

**Q5.** B — Browsers are the universal application runtime of the web. They execute HTML, CSS, and JavaScript. There is no other language you can run in a browser without first compiling it to JavaScript (or WebAssembly). So regardless of whether the backend is Python, Java, or anything else, any interactive behaviour the user sees must be driven by JavaScript in the browser.

**Q6.** High-level languages abstract away hardware details — Python handles memory, data types, and system calls for you. Low-level languages like C give the programmer direct control over memory addresses, pointers, and hardware registers. A Formula 1 engine management system runs on a microcontroller with kilobytes of memory, no operating system, and microsecond timing requirements. Python's interpreter overhead and automatic memory management would make it too slow and unpredictable. C gives deterministic, near-hardware-speed execution.

**Q7.** B — Java source code is compiled not to native machine code but to "bytecode" — a platform-neutral intermediate format. The JVM on each machine reads this bytecode and handles the translation to that machine's actual processor instructions. One compiled `.class` file works on any machine with a JVM installed, without recompilation.

**Q8.** Python's interpreted speed disadvantage doesn't matter for AI work for two reasons. First, the computationally heavy parts (matrix multiplications in NumPy, TensorFlow, or PyTorch) are implemented in C or CUDA and run at full native speed — Python just orchestrates them. Second, the bottleneck in building AI systems is the researcher's ability to iterate quickly on ideas, not raw execution speed. Python's readability and ecosystem make that iteration fast. Learning C to avoid Python's "slowness" would give up the entire AI library ecosystem and make development far harder.

---

## 📚 Research Materials

> 💡 **Start here:** Watch "The History of Programming Languages" by Fireship (https://www.youtube.com/watch?v=Og847HVwRSI) — it covers the entire lineage from Assembly to Python in 12 minutes with the same narrative arc as this session, making it the perfect companion video.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *Pirates of Silicon Valley* | 1999 | Dramatised history of Apple and Microsoft; shows the era when C and assembly were the only options and how software abstraction changed everything |
| *The Social Network* | 2010 | While dramatised, shows Python-era engineering culture — the speed of writing ideas in high-level languages is what enabled Zuckerberg's legendary two-week build |
| *Code Rush* | 2000 | Documentary following Netscape engineers (including the JavaScript team) during the browser wars; shows the birth of JavaScript in a real engineering context |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "The History of Programming Languages" — Fireship | https://www.youtube.com/watch?v=Og847HVwRSI | 12-minute visual history from Assembly to Python — mirrors this session's narrative |
| "Guido van Rossum: Python" — Lex Fridman Podcast | https://www.youtube.com/watch?v=ghwaIiE3Nd8 | 2.5-hour interview with Python's creator; hear his original design philosophy directly |
| "Compiled vs Interpreted Languages" — Computerphile | https://www.youtube.com/watch?v=_C5AHaS1mOA | Clear explanation of the compile/interpret distinction with real examples |
| "Why Python is Slow" — Jake VanderPlas | https://www.youtube.com/watch?v=7wr9Q22bLGg | Explains exactly why Python feels slow and why it doesn't matter for data science |
| "C Programming in 100 Seconds" — Fireship | https://www.youtube.com/watch?v=U3aXWizDbQ4 | Contrast with Python to feel the difference in verbosity and control |

### 📖 Books

| Title | Author | Level | Covers |
|-------|--------|-------|--------|
| *The C Programming Language* | Kernighan & Ritchie | Medium | The original C textbook, written by Dennis Ritchie himself; brief, dense, and essential context for understanding why Python was such a relief |
| *Fluent Python* | Luciano Ramalho | Medium | Deep dive into Python's design; explains why Python works the way it does — a book for after the basics are solid |
| *The Pragmatic Programmer* | Hunt & Thomas | Medium | Language-agnostic guide to thinking like a software engineer; highly relevant to "why languages exist" from this session |
| *Coders* | Clive Thompson | Easy | Profiles of working programmers; readable narrative of how different languages shaped different computing cultures |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| "The Evolution of Programming Languages" — InfoQ | https://www.infoq.com/articles/programming-language-history | Timeline with context on why each language emerged when it did |
| TIOBE Language Popularity Index | https://www.tiobe.com/tiobe-index | Live ranking of programming language usage — see Python's rise to the top in real time |
| "Python's Story" — Python.org | https://www.python.org/doc/essays/foreword | Guido van Rossum's own foreword explaining Python's design goals |
| Compiler Explorer (Godbolt) | https://godbolt.org | Type code in C, C++, or Python and see the compiled machine code output — makes "compiled vs interpreted" tangible |
| "Why Python is Popular for AI" — Towards Data Science | https://towardsdatascience.com/why-python-is-the-go-to-language-for-machine-learning-4e43d96db207 | Data-backed explanation of the library ecosystem advantage |

### 🔗 People to Look Up

- **Grace Hopper** — US Navy rear admiral who created the first compiler in 1952 and championed COBOL; her insight that code could be written in English-like syntax is the ancestor of every high-level language including Python.
- **Dennis Ritchie** — Bell Labs engineer who created C in 1972 and co-created Unix; the operating systems on virtually every device in the world descend from his work.
- **James Gosling** — Canadian engineer who created Java at Sun Microsystems in 1995; the JVM's "write once, run anywhere" idea influenced how Python's interpreter was later positioned.
- **Guido van Rossum** — Dutch programmer who created Python over Christmas 1989 and served as its Benevolent Dictator for Life until 2018; his philosophy of readability over cleverness shaped the entire language.
- **Brendan Eich** — Created JavaScript in 10 days in 1995; later co-founded Mozilla; JavaScript is now the most widely deployed programming language on Earth.
