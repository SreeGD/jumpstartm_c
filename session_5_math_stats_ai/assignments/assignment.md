# Session 5 — Assignment

---

## Task 1 — Improve the xG Model

Open `labs/xg_model.py` and extend the `estimate_xg` function.

Add at least **two more features** that would make it more accurate:

Ideas:
- **Header vs foot** — headers score at roughly half the rate of shots with the dominant foot
- **Counter-attack** — shots on the break score more often (keeper out of position)
- **Assisted** — shots after a key pass score at higher rate than shots off the dribble

Rerun the famous shots table. Did the estimates change significantly?

Write 3 sentences: which feature had the most impact, and why does that make football sense?

---

## Task 2 — Vector Dot Product

Calculate these dot products **by hand**, then verify with Python:

1. `[3, 4] · [1, 2]`
2. `[1, 0, 0] · [5, 3, 7]`  — what does this tell you about perpendicular vectors?
3. `[2, 3, 1] · [2, 3, 1]`  — what does a vector dotted with itself equal?

Python verification:
```python
import numpy as np
print(np.dot([3, 4], [1, 2]))
```

---

## Task 3 — Correlation in Sports

Use Python to calculate the **Pearson correlation** between goals and xG for a player dataset.

```python
import numpy as np

# 10 players' stats (goals scored, xG for the season)
goals = [22, 18, 15, 27, 12, 31, 8,  24, 19, 14]
xg    = [20, 17, 18, 23, 14, 28, 10, 21, 22, 12]

correlation = np.corrcoef(goals, xg)[0, 1]
print(f"Correlation between Goals and xG: {correlation:.3f}")
```

1. What is the correlation coefficient?
2. What does it mean? (High correlation = goals track xG closely?)
3. A player with 31 goals but only 28 xG — lucky or clinical? How do you decide?
4. Plot goals vs xG as a scatter plot. Add the line y=x (perfect correlation line).

---

## Task 4 — Think

*"Gradient descent finds the minimum of a function by following the slope downhill. But what if there are multiple valleys?"*

In 2 sentences, explain what a **local minimum** vs **global minimum** is — use a sports analogy.  
(Example: a "local minimum" might be like a team that optimises for short-term results but misses the championship.)

---

## Bring to Next Session

- Extended xG model with 2+ new features
- Dot product calculations (by hand + Python)
- Correlation analysis (code + chart)
- Local vs global minimum analogy
