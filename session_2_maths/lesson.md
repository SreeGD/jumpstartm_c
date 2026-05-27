# Session 2 — Math Is the Operating System of Reality
## Maths for Computing

**Duration:** 2–3 hours  
**Sree's prep:** Have the Caesar cipher code ready. Have a graph visualisation of Dijkstra's algorithm ready to show (YouTube: "Dijkstra's algorithm visualised").

---

## 🎯 Goal

By the end of this session, Advaith understands:
- Binary arithmetic and number systems
- Boolean algebra — the same as set theory from 12th grade
- What Big-O notation means and how to read it
- Graph theory basics — nodes, edges, centrality
- How these connect to computing and sports analytics

---

## 📖 Sree's Narrative

### Hook

*"You've been doing computing math your entire school life. You just didn't know it had a name."*

Open with this: ask Advaith to find the maximum element in a list of 10 numbers. He scans through them. Ask him: *"How many comparisons did you make? What if the list had a million numbers? A billion?"*

That's Big-O notation. He's been thinking algorithmically without knowing it.

---

### Binary & Number Systems

**Why binary?** Computers use binary because transistors have two states (on/off). We use decimal because humans have ten fingers. Both are just different ways to represent the same numbers.

**Conversion — the key insight:**
In decimal, each position is a power of 10: 1, 10, 100, 1000...  
In binary, each position is a power of 2: 1, 2, 4, 8, 16, 32...

```
Decimal 13 = 8 + 4 + 1
           = 1×2³ + 1×2² + 0×2¹ + 1×2⁰
           = 1101 in binary
```

Let Advaith convert 25, 42, and 100 manually. Then show that `bin(25)` in Python does it instantly — but understanding why is what matters.

**Hexadecimal (base 16)** — used in HTML colours, memory addresses.  
`#e94560` (the red colour from the web lab) is hex: e9=233, 45=69, 60=96 in RGB.

---

### Boolean Algebra

Advaith learned set theory in 12th grade. Boolean algebra is the same thing:

| Set Theory | Boolean Algebra | Python |
|-----------|-----------------|--------|
| A ∩ B (intersection) | A AND B | `a and b` |
| A ∪ B (union) | A OR B | `a or b` |
| A' (complement) | NOT A | `not a` |

*"The logic gates from Session 1.1 are just Boolean algebra made physical in silicon."*

**De Morgan's Laws** — Advaith knows these from sets:
- NOT(A AND B) = NOT(A) OR NOT(B)
- NOT(A OR B) = NOT(A) AND NOT(B)

Computers use these to simplify circuits. The same law that simplifies set expressions also simplifies chip designs.

---

### Big-O Notation — How Algorithms Grow

*"Not all solutions to the same problem are equal. Some are fast for small inputs but catastrophic for large ones. Big-O tells you which."*

Show Advaith a visual: input size (n) on x-axis, time taken on y-axis.

| Notation | Name | Example | Growth |
|----------|------|---------|--------|
| O(1) | Constant | Array lookup by index | Flat line |
| O(log n) | Logarithmic | Binary search | Barely grows |
| O(n) | Linear | Scan a list | Straight diagonal |
| O(n²) | Quadratic | Nested loops | Curves up fast |
| O(2ⁿ) | Exponential | Brute-force chess | Explodes |

**The guessing game connection:** In Session 4's guessing game, Advaith will use binary search — always guess the middle number. With 1000 numbers, you find it in at most 10 guesses. That's O(log n). *That's why it's so powerful.*

**Sports connection:** When Second Spectrum's cameras track 22 football players 25 times per second, they're processing 550 data points per second per match. An O(n²) algorithm on that data would mean comparing every player to every other player — 550² = 302,500 operations per second per match. That's why algorithmic efficiency matters in sports analytics.

---

### Graph Theory — The Math Behind Networks

**A graph:** nodes (vertices) connected by edges.

Real-world graphs:
- **Google Maps** — cities are nodes, roads are edges, weight = distance/time
- **Social networks** — people are nodes, friendships are edges
- **Football passing networks** — players are nodes, passes are edges

**Key concepts:**
- **Degree** — how many connections a node has
- **Path** — a route from one node to another
- **Shortest path** — the fastest route (Dijkstra's algorithm)
- **Centrality** — how "important" a node is in the network

**Dijkstra's algorithm:** Finds the shortest path between two nodes. Used in Google Maps, network routing, and — as Advaith will build in the lab — football passing analysis.

*Show a YouTube visualisation of Dijkstra's running step by step.*

*"Barcelona's tiki-taka style of football is a graph with very high centrality for the midfielders — Xavi, Iniesta, Busquets. The ball flows through them. Analytics confirms what the eye sees."*

---

## ⚡ Wow Moment

Show Dijkstra's algorithm finding a route on Google Maps — then reveal the algorithm is from 1956. It was invented before the internet, before GPS, before smartphones.

*"Edsger Dijkstra wrote this algorithm in 20 minutes, without pen and paper, while sitting in a café in Amsterdam with his fiancée. He waited 3 years to publish it because he didn't think it was significant enough. It's now one of the most used algorithms on Earth."*

---

## 🔑 Key Concepts Checklist

- [ ] Binary — base-2, built on powers of 2
- [ ] Hexadecimal — base-16, used in colours and memory addresses
- [ ] Boolean algebra — AND, OR, NOT (same as set theory)
- [ ] De Morgan's Laws — how to simplify boolean expressions
- [ ] Big-O notation — describes how an algorithm scales with input size
- [ ] O(1), O(log n), O(n), O(n²) — know what each looks like in practice
- [ ] Binary search — O(log n), why it's powerful
- [ ] Graph — nodes + edges
- [ ] Shortest path — Dijkstra's algorithm
- [ ] Centrality — importance of a node in a network

---

## Teaching Notes for Sree

- Don't spend too long on binary conversion — it's a tool, not the point.
- Big-O is crucial. Advaith will need it throughout NITW. Build the intuition carefully.
- The graph theory section leads directly to the football passing network lab — end the theory section there and go straight into the lab.
- The connection to set theory from 12th grade (Boolean algebra) is a major confidence booster. Use it.
