# Session 3 — The Family Tree of Programming Languages
## Introduction to Programming Languages

**Duration:** 1.5–2 hours  
**Sree's prep:** Have side-by-side code comparisons ready. Install Python and VS Code before this session.

---

## 🎯 Goal

By the end of this session, Advaith understands:
- Why so many programming languages exist
- The key distinctions: compiled vs interpreted, high vs low level
- Where Python fits and why it dominates AI and data science
- He writes his first standalone Python file

---

## 📖 Sree's Narrative

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

## Teaching Notes for Sree

- The history is a story — tell it as one. Don't list facts.
- The side-by-side comparison is the centrepiece. Spend time on it.
- By the end of this session, Python should be installed and VS Code open.
- Advaith types the Fibonacci code himself — first time with a real IDE.
- If he asks "which language should I learn after Python?" — answer: Python deeply first, then JavaScript for web, then C for systems/understanding.
