# Session 4 — Python: Math with Superpowers
## Get Started with Python

**Duration:** 3–4 hours (can split across 2 sittings)  
**the teacher's prep:** Python + VS Code installed. All 4 lab files ready. `pip install matplotlib numpy pandas` done.

---

## 🎯 Goal

By the end of this session, Student can:
- Write and run Python programs independently
- Use variables, loops, conditionals, and functions
- Plot graphs using matplotlib
- Work with lists and basic data
- See Python as "math that runs"

---

## 📖 the teacher's Narrative

### Hook

*"Python was named after Monty Python's Flying Circus — a British comedy show. Its inventor wanted programming to be fun. By the end of today, you'll have built four working programs. Let's find out if he was right."*

---

### The Python Mental Model — Connect to Math

Everything Student knows from 12th grade has a direct Python equivalent:

| Math Concept | Python Equivalent |
|-------------|------------------|
| Variable: x = 5 | `x = 5` |
| Function: f(x) = x² | `def f(x): return x**2` |
| Set: A = {1,2,3} | `A = {1, 2, 3}` |
| Sequence: aₙ | `a = [a0, a1, a2, ...]` |
| Summation: Σ | `sum(list)` |
| For all x in A | `for x in A:` |
| If condition | `if condition:` |

*"Python isn't a foreign language — it's math with slightly different notation."*

---

### Core Concepts to Cover (teach as you go through labs)

**Variables and Types**
```python
name = "Student"        # string
goals = 24              # integer
average = 24.5          # float
is_champion = True      # boolean
```

**Lists** — ordered sequences (like arrays in math)
```python
players = ["Messi", "Ronaldo", "Mbappe"]
scores = [34, 27, 24]
players[0]     # → "Messi" (0-indexed!)
len(players)   # → 3
```

**Loops** — repeat an action
```python
for player in players:
    print(player)

for i in range(5):
    print(i)   # 0, 1, 2, 3, 4
```

**Conditionals** — decisions
```python
if goals > 25:
    print("Golden Boot contender")
elif goals > 15:
    print("Quality season")
else:
    print("Need to improve")
```

**Functions** — reusable blocks (just like f(x) in math)
```python
def rate_season(goals, assists):
    total = goals + assists
    if total > 30:
        return "Exceptional"
    elif total > 20:
        return "Good"
    else:
        return "Average"
```

---

## Teaching Flow — 4 Labs, 4 Concepts

**Lab 1 (math_waves.py):** Variables, imports, matplotlib basics  
*Teach: variables, imports, function calls, plotting*

**Lab 2 (guessing_game.py):** Loops, conditionals, user input  
*Teach: while loops, if/elif/else, input(), random module*  
*Key insight: Binary search → O(log n) — connects to Session 2*

**Lab 3 (top_scorers.py):** Lists, sorting, bar charts  
*Teach: lists, sorted(), zip(), matplotlib bar charts*  
*Key insight: Student fills in his own players — makes it personal*

**Lab 4 (dice_simulator.py):** Loops, randomness, histograms  
*Teach: list comprehensions, random module, histograms*  
*Key insight: Law of large numbers — more rolls = flatter distribution*

---

## ⚡ Wow Moments

**Lab 1:** The sin and cos waves appear instantly. *"You just plotted a wave in 6 lines. This took me an hour in C."*

**Lab 2:** Student beats 7 guesses using binary search. *"You just implemented an O(log n) algorithm. Computers use this to search through billions of sorted records."*

**Lab 3:** His own player stats appear as a beautiful chart. *"This is what ESPN's stat team does — except they do it for 500 players a night."*

**Lab 4:** 10 dice rolls looks lumpy. 10,000 looks perfectly flat. *"That's the law of large numbers. In probability theory, this is why insurance companies never go bankrupt."*

---

## 🔑 Key Concepts Checklist

- [ ] Variables and types (int, float, str, bool)
- [ ] Lists — indexing, append, len, sorted
- [ ] For loops and while loops
- [ ] If / elif / else
- [ ] Functions — def, parameters, return
- [ ] import — using external libraries
- [ ] matplotlib — plt.plot(), plt.bar(), plt.hist(), plt.show()
- [ ] random — random.randint(), random.choice()
- [ ] List comprehensions — `[x**2 for x in range(10)]`

---

## Teaching Notes for Teacher

- Go slow on indexing (0-indexed). It trips up everyone at first.
- The guessing game is the most satisfying lab — let Student play it a few times.
- Encourage Student to break things. "What happens if you type a letter instead of a number in the guessing game?"
- Don't worry about explaining everything perfectly — curiosity > completeness.
- At the end, ask: *"What would you build if you could build anything with Python?"* That's his Session 8 capstone.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** What does `players[0]` return if `players = ["Messi", "Ronaldo", "Mbappe"]`?
- A) `"Ronaldo"`
- B) `1`
- C) `"Messi"` ✓
- D) `"Mbappe"`

**Q2.** What is the Python equivalent of the mathematical summation Σ applied to a list?
- A) `total(list)`
- B) `sum(list)` ✓
- C) `add(list)`
- D) `sigma(list)`

**Q3.** What does `range(5)` produce in a for loop?
- A) The numbers 1, 2, 3, 4, 5
- B) The numbers 0, 1, 2, 3, 4 ✓
- C) Five random numbers
- D) The numbers 0, 1, 2, 3, 4, 5

**Q4.** Write the Python function definition for the mathematical function f(x) = x² + 3.

**Q5.** In Lab 4 (dice simulator), rolling 10 dice looked lumpy but 10,000 rolls looked flat and even. What principle explains this?

**Q6.** A footballer's goals per season are stored as `goals = [32, 28, 35, 29, 31]`. Write one line of Python that prints how many seasons are in this list.

**Q7.** What is the key difference between a `for` loop and a `while` loop? Give a real-world scenario where you would choose each.

**Q8 (explain in your own words).** A friend says "Python is a completely different language from math — it's just code." Based on what you learned today, how would you explain to them that Python and math are actually very closely connected?

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** C — Lists in Python are zero-indexed, so index 0 gives the first element, "Messi".

**Q2.** B — Python's built-in `sum()` function computes the total of all elements in a list, directly equivalent to Σ in mathematics.

**Q3.** B — `range(5)` generates integers starting at 0 and stopping before 5: 0, 1, 2, 3, 4.

**Q4.** `def f(x): return x**2 + 3` — the `**` operator means "to the power of" in Python.

**Q5.** The Law of Large Numbers — as the number of trials increases, the observed frequencies converge toward the true theoretical probabilities (each face of a fair die has a 1/6 chance).

**Q6.** `print(len(goals))` — `len()` returns the number of elements in a list, which here is 5.

**Q7.** A `for` loop is used when you know in advance how many times to repeat (e.g., process each player in a squad of 20). A `while` loop is used when you repeat until a condition changes (e.g., keep asking for a guess until the user guesses correctly, as in the guessing game lab).

**Q8.** Model answer: Python variables, functions, loops, and conditions map directly to mathematical notation. `x = 5` is the same as assigning a variable, `def f(x): return x**2` is exactly f(x) = x², `for x in A:` means "for all x in set A", and `sum(list)` is Σ. Python is essentially math with a slightly different spelling — the logic is identical.

---

## 📚 Research Materials

> 💡 **Start here:** Work through the official Python tutorial at https://docs.python.org/3/tutorial — specifically chapters 3–5 covering numbers, strings, lists, and control flow. It is written by Guido's team, takes about 2 hours, and consolidates everything from this session.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *Moneyball* | 2011 | The analytics team's work is essentially what Lab 3 (top_scorers.py) models at small scale — Python and pandas power modern versions of exactly this analysis |
| *AlphaGo* | 2017 | DeepMind documentary; all the visualisations of neural network training are built with Python's data visualisation stack — matplotlib and seaborn at industrial scale |
| *The Social Dilemma* | 2020 | Shows recommendation algorithms and data pipelines; the Python data science workflow from this session is the foundation of those systems |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "Python Tutorial for Beginners" — Programming with Mosh | https://www.youtube.com/watch?v=kqtD5dpn9C8 | Six-hour complete Python course; use it to reinforce whichever concepts from the session need more practice |
| "Matplotlib Tutorial" — Corey Schafer | https://www.youtube.com/watch?v=UO98lJQ3QGI | Best YouTube series on matplotlib; covers plt.plot, bar charts, and histograms — exactly the functions from the labs |
| "NumPy Tutorial" — Keith Galli | https://www.youtube.com/watch?v=GB9ByFAIAH4 | Covers arrays and vectorised operations; the bridge between basic Python and the data science tools in Session 5 |
| "Python List Comprehensions" — Corey Schafer | https://www.youtube.com/watch?v=3dt4OGnU5sM | Deep-dives list comprehensions used in Lab 4; clear and concise |
| "Python for Data Science" — freeCodeCamp | https://www.youtube.com/watch?v=LHBE6Q9XlzI | Four-hour course covering Python, NumPy, Pandas, and matplotlib together |

### 📖 Books

| Title | Author | Level | Covers | Free |
|-------|--------|-------|--------|------|
| *Python Crash Course* | Eric Matthes | Easy | Best beginner Python book; projects include data visualisation with matplotlib — directly mirrors this session's labs | — |
| *Automate the Boring Stuff with Python* | Al Sweigart | Easy | Free online; shows Python as a practical tool for everyday tasks — great for building coding habits after this session | [Free →](https://automatetheboringstuff.com) |
| *Python Data Science Handbook* | Jake VanderPlas | Medium | Free online; covers NumPy, Pandas, matplotlib, and machine learning — the natural continuation after Session 4 | [Free →](https://jakevdp.github.io/PythonDataScienceHandbook/) |
| *Learning Python* | Mark Lutz | Medium–Hard | Comprehensive 1,600-page reference; use it to look up anything rather than read cover to cover | [Open Library](https://openlibrary.org) |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| Official Python Tutorial | https://docs.python.org/3/tutorial | Written by Guido's team; chapters 3–5 directly reinforce this session |
| Matplotlib Gallery | https://matplotlib.org/stable/gallery | Every chart type with source code; find the chart you want and copy the pattern |
| Kaggle — Python Course | https://www.kaggle.com/learn/python | Free interactive Python exercises in the browser; no setup required |
| FBref (Football Statistics) | https://fbref.com | Real football data you can download and analyse using the Python skills from this session |
| Google Colab | https://colab.research.google.com | Free cloud Jupyter notebooks; run Python with NumPy and matplotlib pre-installed — no local setup |

### 🔗 People to Look Up

- **Guido van Rossum** — Creator of Python; his design philosophy of "readability counts" and "programmer time is more valuable than computer time" shapes every aspect of the language learned in this session.
- **Travis Oliphant** — Created NumPy (originally Numeric) in the mid-2000s; the array operations that make Python fast enough for science are largely his engineering work.
- **Wes McKinney** — Created Pandas in 2008 while working as a quantitative analyst; the DataFrame structure he designed is used in virtually every data analysis pipeline.
- **John Hunter** — Created matplotlib in 2003; built it to replicate MATLAB's plotting capabilities in Python — the charts produced in Labs 1 and 3 use his library directly.
- **Jake VanderPlas** — Author of the Python Data Science Handbook and creator of widely-used visualisation tools; his work bridges academic science and practical Python data analysis.
