# Session 4 — Python: Math with Superpowers
## Get Started with Python

**Duration:** 3–4 hours (can split across 2 sittings)  
**Sree's prep:** Python + VS Code installed. All 4 lab files ready. `pip install matplotlib numpy pandas` done.

---

## 🎯 Goal

By the end of this session, Advaith can:
- Write and run Python programs independently
- Use variables, loops, conditionals, and functions
- Plot graphs using matplotlib
- Work with lists and basic data
- See Python as "math that runs"

---

## 📖 Sree's Narrative

### Hook

*"Python was named after Monty Python's Flying Circus — a British comedy show. Its inventor wanted programming to be fun. By the end of today, you'll have built four working programs. Let's find out if he was right."*

---

### The Python Mental Model — Connect to Math

Everything Advaith knows from 12th grade has a direct Python equivalent:

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
name = "Advaith"        # string
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
*Key insight: Advaith fills in his own players — makes it personal*

**Lab 4 (dice_simulator.py):** Loops, randomness, histograms  
*Teach: list comprehensions, random module, histograms*  
*Key insight: Law of large numbers — more rolls = flatter distribution*

---

## ⚡ Wow Moments

**Lab 1:** The sin and cos waves appear instantly. *"You just plotted a wave in 6 lines. This took me an hour in C."*

**Lab 2:** Advaith beats 7 guesses using binary search. *"You just implemented an O(log n) algorithm. Computers use this to search through billions of sorted records."*

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

## Teaching Notes for Sree

- Go slow on indexing (0-indexed). It trips up everyone at first.
- The guessing game is the most satisfying lab — let Advaith play it a few times.
- Encourage Advaith to break things. "What happens if you type a letter instead of a number in the guessing game?"
- Don't worry about explaining everything perfectly — curiosity > completeness.
- At the end, ask: *"What would you build if you could build anything with Python?"* That's his Session 8 capstone.
