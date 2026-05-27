# Session 3 — Assignment

---

## Task 1 — Fibonacci Challenges

Open `labs/fibonacci.py` and complete the challenges:

**Challenge A:** Time both versions for `n=35`.  
Add this to the file:
```python
import time

start = time.time()
fibonacci_loop(35)
print(f"Loop took: {time.time() - start:.6f} seconds")

start = time.time()
fibonacci_recursive(35)
print(f"Recursive took: {time.time() - start:.6f} seconds")
```
Which is faster? By how much? **Why?** (Connect to Big-O from Session 2)

**Challenge B:** Find the first Fibonacci number greater than 1,000,000.  
How many numbers in the sequence before you reach it?

---

## Task 2 — Language Research

Find out what language powers these apps. For each, write:
- The primary language used
- One reason why that language was chosen (performance? speed of development? existing team skills?)

| App | Language | Why? |
|-----|----------|------|
| WhatsApp backend | ? | ? |
| Instagram backend | ? | ? |
| Netflix recommendation engine | ? | ? |
| Google Search | ? | ? |
| The NASA Mars Rover software | ? | ? |

---

## Task 3 — Python Setup Check

Make sure these work on your machine. Run each in a Python file:

```python
# Check Python version
import sys
print(sys.version)

# Check these libraries are installed
import math
print(math.pi)
print(math.sqrt(2))

# Install if needed: pip install matplotlib numpy
import matplotlib
import numpy
print("All good!")
```

If anything fails, note the error. Bring it to Session 4.

---

## Task 4 — Think

Guido van Rossum said: *"Code is read more often than it is written."*

Write 4–6 sentences explaining what you think this means and why it influenced Python's design.

---

## Before Session 4

Make sure you have installed:
- [ ] Python 3.11+ from python.org
- [ ] VS Code from code.visualstudio.com
- [ ] VS Code Python extension (search "Python" in Extensions tab)
- [ ] Run in terminal: `pip install matplotlib numpy pandas`

Bring all Task answers to Session 4.
