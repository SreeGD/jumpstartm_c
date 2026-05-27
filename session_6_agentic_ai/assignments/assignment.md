# Session 6 — Assignment

---

## Task 1 — Extend the Sports Analyst

Open `labs/sports_analyst.py` and add two new features:

**Feature A — Debate Mode**
```python
def debate(player1: str, player2: str) -> str:
    """Agent argues for player1 over player2"""
    # Write the system prompt and API call
    # The agent should: pick a side, give 3 arguments, acknowledge weaknesses
```

Test it: `debate("Mbappe", "Haaland")` and `debate("Luka", "SGA")`

**Feature B — Match Prediction**
```python
def predict_match(home_team: str, away_team: str) -> str:
    """Agent predicts score and gives a reason"""
    # Your system prompt should ask for: predicted score, key player, tactical reason
```

Test it with 3 upcoming or recent fixtures you care about.

---

## Task 2 — Feed It Real Data

Take the stats from your `lab3_top_scorers.py` (Session 4) and pass them to the analyst:

```python
stats = {
    "Haaland":  {"goals": 27, "assists": 5,  "xG": 24.3},
    "Mbappe":   {"goals": 24, "assists": 8,  "xG": 20.1},
    "Vini Jr":  {"goals": 22, "assists": 11, "xG": 18.3},
}

# Ask the analyst to explain what the xG column means
# and identify who is most and least clinical
response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=400,
    messages=[{
        "role": "user",
        "content": f"Here are the stats: {stats}. Who is over/under-performing their xG and why?"
    }]
)
```

Write 3 sentences on what the AI said and whether you agree.

---

## Task 3 — System Prompt Engineering

The system prompt is a "personality dial." Try 3 completely different personas for the same player analysis:

1. A **Spanish football journalist** writing for Marca
2. A **data scientist** who only cares about numbers, not narratives
3. A **12-year-old fan** who just watched their first match

For the same question ("Analyse Vini Jr"), compare the three responses.  
Write: which response was most useful? Which was most entertaining? Why does the persona matter?

---

## Task 4 — Think

*"GPT-4 passed the bar exam, scored in the top 10% of the SAT, and can write working code. Does that mean it understands those things?"*

Write 4–6 sentences with your view. Is there a difference between "performing a task well" and "understanding" it? Does it matter for practical purposes?

---

## Bring to Next Session

- Debate mode and match prediction functions (code + example outputs)
- Stats-connected analysis (Task 2 code + your 3 sentences)
- Three system prompt outputs (Task 3 comparison)
- Your answer to Task 4
