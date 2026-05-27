# Session 4 — Assignment

---

## Task 1 — Lab Challenges

Pick **two** challenge prompts from any of the four labs and complete them.  
Write the code, run it, and bring the output (screenshot or printed result).

Suggestions:
- Lab 1: Plot the derivative of sin(x) and verify it looks like cos(x)
- Lab 2: Add a hard mode where the secret number changes if you're close
- Lab 3: Add a third chart — goals scored at home vs away for your favourite team
- Lab 4: Roll two dice, plot the sum distribution — explain the triangle shape

---

## Task 2 — Build a Simple Stats Tracker

Write a Python script that:
1. Asks the user to enter 5 match scores for their favourite team (e.g. `3-1, 2-0, 1-1, 0-2, 4-0`)
2. Calculates: total goals scored, total goals conceded, goal difference, wins/draws/losses
3. Prints a summary like:

```
=== Season Summary ===
Goals scored:    10
Goals conceded:  4
Goal difference: +6
Record: W3 D1 L1
Points: 10
```

---

## Task 3 — Explore the Data

Update `lab3_top_scorers.py` with:
- At least **10 players** instead of 5 (5 soccer + 5 basketball)
- Add a **third section**: a horizontal bar chart of minutes played by each soccer player
- Add a line that prints: *"Most efficient scorer: [player] — [goals per 90 minutes]"*
  - You'll need to add `minutes_played` data

---

## Task 4 — Think (connect to Big-O)

The guessing game uses binary search — O(log n).

1. How many guesses does it take to find a number between 1 and 1,000,000?
2. How many guesses to find a number between 1 and 1,000,000,000?
3. If a sorted array has 1 billion records, how many comparisons does binary search need?

Now think: **Why does Google Search return results in under 0.5 seconds for billions of web pages?**  
Write 4–6 sentences connecting your answer to Big-O notation.

---

## Bring to Next Session

- Two completed lab challenges (code + output)
- Match scores stats tracker (Task 2)
- Updated top scorers chart with 10+ players
- Your Big-O / Google Search answer
