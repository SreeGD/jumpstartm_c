# Session 2 — Math Is the Operating System of Reality
## Maths for Computing

**Duration:** 2–3 hours  
**the teacher's prep:** Have the Caesar cipher code ready. Have a graph visualisation of Dijkstra's algorithm ready to show (YouTube: "Dijkstra's algorithm visualised").

---

## 🎯 Goal

By the end of this session, Student understands:
- Binary arithmetic and number systems
- Boolean algebra — the same as set theory from 12th grade
- What Big-O notation means and how to read it
- Graph theory basics — nodes, edges, centrality
- How these connect to computing and sports analytics

---

## 📖 the teacher's Narrative

### Hook

*"You've been doing computing math your entire school life. You just didn't know it had a name."*

Open with this: ask Student to find the maximum element in a list of 10 numbers. He scans through them. Ask him: *"How many comparisons did you make? What if the list had a million numbers? A billion?"*

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

Let Student convert 25, 42, and 100 manually. Then show that `bin(25)` in Python does it instantly — but understanding why is what matters.

**Hexadecimal (base 16)** — used in HTML colours, memory addresses.  
`#e94560` (the red colour from the web lab) is hex: e9=233, 45=69, 60=96 in RGB.

---

### Boolean Algebra

Student learned set theory in 12th grade. Boolean algebra is the same thing:

| Set Theory | Boolean Algebra | Python |
|-----------|-----------------|--------|
| A ∩ B (intersection) | A AND B | `a and b` |
| A ∪ B (union) | A OR B | `a or b` |
| A' (complement) | NOT A | `not a` |

*"The logic gates from Session 1.1 are just Boolean algebra made physical in silicon."*

**De Morgan's Laws** — Student knows these from sets:
- NOT(A AND B) = NOT(A) OR NOT(B)
- NOT(A OR B) = NOT(A) AND NOT(B)

Computers use these to simplify circuits. The same law that simplifies set expressions also simplifies chip designs.

One level up from circuits, Boolean algebra became the engine of databases. SQL — the language used to query every database on the planet — is Boolean algebra applied to tables of data. `SELECT * FROM patients WHERE age > 60 AND diagnosis = 'diabetes'` is an AND operation on rows. Every bank query, every hospital record, every airline booking runs this logic billions of times a day. **Oracle** built a $40 billion business on exactly this insight: Larry Ellison bet in 1977 that relational databases — rows, columns, and Boolean queries — would run the world's institutions. He was right.

---

### Big-O Notation — How Algorithms Grow

*"Not all solutions to the same problem are equal. Some are fast for small inputs but catastrophic for large ones. Big-O tells you which."*

Show Student a visual: input size (n) on x-axis, time taken on y-axis.

| Notation | Name | Example | Growth |
|----------|------|---------|--------|
| O(1) | Constant | Array lookup by index | Flat line |
| O(log n) | Logarithmic | Binary search | Barely grows |
| O(n) | Linear | Scan a list | Straight diagonal |
| O(n²) | Quadratic | Nested loops | Curves up fast |
| O(2ⁿ) | Exponential | Brute-force chess | Explodes |

**The guessing game connection:** In Session 4's guessing game, Student will use binary search — always guess the middle number. With 1000 numbers, you find it in at most 10 guesses. That's O(log n). *That's why it's so powerful.*

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

**Dijkstra's algorithm:** Finds the shortest path between two nodes. Used in Google Maps, network routing, and — as Student will build in the lab — football passing analysis.

*Show a YouTube visualisation of Dijkstra's running step by step.*

Dijkstra is about the shortest path. But there is another question you can ask of a graph: which node is the most important? That measure is called **centrality** — and it is the mathematical idea behind one of the most consequential algorithms ever written. Larry Page and Sergey Brin were Stanford PhD students who asked: what if you modelled the entire web as a directed graph, with every hyperlink as an edge? A link from one page to another is a vote. A page that receives many links from other highly-linked pages ranks higher. They called it **PageRank**. It was graph centrality applied at web scale. The algorithm from this session became a $200 billion per year business — **Google**.

*"Barcelona's tiki-taka style of football is a graph with very high centrality for the midfielders — Xavi, Iniesta, Busquets. The ball flows through them. Analytics confirms what the eye sees. And the same mathematics — applied to a different graph — is how you find things on the internet."*

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

## Teaching Notes for Teacher

- Don't spend too long on binary conversion — it's a tool, not the point.
- Big-O is crucial. Student will need it throughout NITW. Build the intuition carefully.
- The graph theory section leads directly to the football passing network lab — end the theory section there and go straight into the lab.
- The connection to set theory from 12th grade (Boolean algebra) is a major confidence booster. Use it.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** Convert the decimal number 25 to binary. Show your working.
- A) 10110
- B) 11001 ✓
- C) 10101
- D) 11010

**Q2.** De Morgan's Laws come from Boolean algebra (and set theory). Write out both laws and give one example of where a computer uses them.

**Q3.** An algorithm that scans every element in a list of n items has Big-O complexity O(n). If the same algorithm is run on a list of 1 million items instead of 1,000, roughly how many times more operations will it require?
- A) 10 times more
- B) 100 times more
- C) 1,000 times more ✓
- D) 1,000,000 times more

**Q4.** Explain in your own words why O(log n) is dramatically better than O(n) for large datasets. Use the guessing game (binary search) as your example.

**Q5.** In football analytics, Barcelona's tiki-taka style can be modelled as a passing network graph. Xavi, Iniesta, and Busquets have very high "betweenness centrality" in this graph. What does high betweenness centrality mean, and why does it matter tactically?
- A) High centrality means a player attempts the most shots per game
- B) High centrality means a player sits at many of the shortest paths between teammates — the ball flows through them, so disrupting these players disrupts the whole team's network ✓
- C) High centrality means a player covers the most ground in kilometres per match
- D) High centrality means a player has the highest passing accuracy percentage

**Q6.** What is a graph in the mathematical sense? Give one example from each of: mapping/navigation, social media, and sport.

**Q7.** Dijkstra's algorithm was written in 1956 — decades before GPS and smartphones. How does it work conceptually, and name one modern application where it runs billions of times per day?
- A) It uses brute force to try all possible paths; used in email spam filtering
- B) It finds the shortest path between nodes by iteratively visiting the nearest unvisited node; used in Google Maps routing ✓
- C) It sorts a list by repeatedly swapping adjacent elements; used in database indexing
- D) It compresses data by removing repeated patterns; used in file storage systems

**Q8.** Second Spectrum's cameras track 22 football players 25 times per second. An O(n²) algorithm compares every player to every other player. How many comparisons per second would that produce — and why does this illustrate the importance of choosing efficient algorithms?

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — 25 = 16 + 8 + 1 = 1×2⁴ + 1×2³ + 0×2² + 0×2¹ + 1×2⁰ = 11001. Work right to left: 25 is odd so the last bit is 1, 25÷2=12 remainder 1; 12 is even so next bit is 0; 12÷2=6 remainder 0; 6÷2=3 remainder 0; 3÷2=1 remainder 1; 1÷2=0 remainder 1. Reading remainders bottom-up: 11001.

**Q2.** Law 1: NOT(A AND B) = NOT(A) OR NOT(B). Law 2: NOT(A OR B) = NOT(A) AND NOT(B). Computers use these to simplify logic gate arrangements — a NAND gate (NOT AND) can replace a NOT followed by an OR, reducing chip complexity and saving transistors.

**Q3.** C — O(n) means operations scale linearly with input size. 1,000,000 ÷ 1,000 = 1,000. The algorithm requires 1,000 times more operations for a list 1,000 times larger.

**Q4.** Binary search always guesses the middle value and eliminates half the remaining possibilities. With 1,000 numbers, you find the answer in at most 10 guesses (2¹⁰ = 1,024). With 1 billion numbers, you need only 30 guesses (2³⁰ ≈ 1 billion). O(n) linear search on 1 billion items could take 1 billion steps. The difference between 30 and 1,000,000,000 is why O(log n) is transformative.

**Q5.** B — Betweenness centrality measures how often a node lies on the shortest path between other nodes. In football, a high-centrality midfielder is the conduit for most passing combinations. Opponents who press or neutralise these players collapse the team's passing structure — which is precisely the tactical philosophy behind high pressing against possession teams.

**Q6.** A graph is a mathematical structure of nodes (vertices) connected by edges. Navigation example: cities are nodes, roads are edges, weights are distances or travel times. Social media example: users are nodes, follows/friendships are edges. Sport example: players are nodes, successful passes are directed edges with weights representing frequency.

**Q7.** B — Dijkstra's algorithm starts at the source node, always visits the nearest unvisited node next, and records the shortest known distance to each node encountered. It guarantees the shortest path without examining every possible route. Google Maps (and all major mapping services) run variants of it continuously.

**Q8.** 22 players tracked 25 times per second = 550 data points per second. An O(n²) algorithm produces 550² = 302,500 comparisons per second, per match. Across thousands of matches analysed simultaneously, this becomes hundreds of billions of operations per day. Choosing an O(n log n) algorithm instead might reduce that to roughly 550 × 9 ≈ 5,000 comparisons — a 60× improvement that means the difference between real-time analysis and a system that can't keep up.

---

## 📚 Research Materials

> 💡 **Start here:** Watch "Big-O Notation in 100 Seconds" by Fireship (https://www.youtube.com/watch?v=g2o22C3CRfU) — it gives you the visual intuition for algorithm complexity in under 2 minutes, making the growth curves from this session immediately tangible.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *The Man Who Knew Infinity* | 2015 | Biographical film about Ramanujan; beautiful portrayal of mathematical thinking and the intuition behind abstract structures like graph theory |
| *Moneyball* | 2011 | Brad Pitt film about using statistics and data to build a baseball team; the graph-theoretic network of player value relationships drives every decision |
| *Connected: The Hidden Science of Everything* | 2020 | Netflix documentary series; Episode 1 on social networks is essentially an applied graph theory lecture |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "Big-O Notation in 100 Seconds" — Fireship | https://www.youtube.com/watch?v=g2o22C3CRfU | Visual growth curves for O(1), O(log n), O(n), O(n²) — fastest possible introduction |
| "Dijkstra's Algorithm — Step by Step" — Spanning Tree | https://www.youtube.com/watch?v=EFg3u_E6eHU | Clear animated walkthrough of exactly how Dijkstra finds shortest paths |
| "Graph Theory for Beginners" — TED-Ed | https://www.youtube.com/watch?v=tWVWeAqZ0WU | The Seven Bridges of Königsberg — Euler's original graph problem explained as a story |
| "Boolean Algebra" — The Organic Chemistry Tutor | https://www.youtube.com/watch?v=EPJf4owqwdA | Connects Boolean algebra to circuit design; reinforces the set theory link from this session |
| "Binary Search in 4 Minutes" — Michael Sambol | https://www.youtube.com/watch?v=fDKIpRe8GW4 | Concise animation of binary search — directly connects O(log n) to the guessing game |
| "How Barcelona's Tiki-Taka Works" — Tifo Football | *search "Tifo Football tiki-taka explained"* | Tactical breakdown of Barcelona's passing game; view through the lens of centrality from this session |

### 📖 Books

| Title | Author | Level | Covers |
|-------|--------|-------|--------|
| *Grokking Algorithms* | Aditya Bhargava | Easy | Illustrated introduction to algorithms and Big-O; binary search, sorting, graphs — all covered with hand-drawn visuals |
| *The Man from the Future: The Visionary Life of John von Neumann* | Ananyo Bhattacharya | Easy–Medium | Biography weaving together Boolean logic, computing theory, and the mathematical foundations of the digital world |
| *Introduction to Graph Theory* | Richard Trudeau | Easy–Medium | Gentle introduction to graph theory starting from Euler's bridges; no advanced maths required |
| *The Art of Problem Solving* (Vol. 1) | Lehoczky & Rusczyk | Medium | Competition mathematics including number theory and combinatorics — sharpens the mathematical reasoning behind Big-O thinking |
| *Networks, Crowds, and Markets* | Easley & Kleinberg | Medium–Hard | How graph theory explains social networks, markets, and the internet; free PDF available from Cornell |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| VisuAlgo — Algorithm Visualiser | https://visualgo.net/en | Interactive animations for sorting, graphs, Dijkstra's — run algorithms step by step in a browser |
| Big-O Cheat Sheet | https://www.bigocheatsheet.com | Reference card for Big-O of all common data structures and algorithms |
| Six Degrees of Kevin Bacon — Oracle of Bacon | https://oracleofbacon.org | Live demonstration of small-world graph theory using movie connections |
| StatsBomb — Open Data & Passing Networks | https://statsbomb.com/articles/soccer/statsbomb-open-data | Free football data including passing networks; build the analysis from this session with real data |
| "The Mathematics of Football" — Plus Magazine | https://plus.maths.org/content/os/issue14/features/football/index | Academic article exploring graph theory and statistics in football analytics |

### 🔗 People to Look Up

- **George Boole** — Victorian mathematician who created Boolean algebra in 1854; had no idea it would become the logical foundation of every computer ever built.
- **Leonhard Euler** — 18th-century Swiss mathematician who solved the Seven Bridges of Königsberg problem in 1736, founding graph theory as a discipline.
- **Edsger Dijkstra** — Dutch computer scientist who invented his shortest-path algorithm in 20 minutes in 1956 without pen and paper; it now runs in Google Maps billions of times daily.
- **Claude Shannon** — Bell Labs engineer who founded information theory in 1948, formalising how binary digits (bits) can encode any information and connecting Boolean algebra to electronic circuits.
- **Andres Iniesta / Xavi Hernandez** — Barcelona midfielders whose tiki-taka style is the most cited real-world example of high-centrality nodes in a football passing network graph.
