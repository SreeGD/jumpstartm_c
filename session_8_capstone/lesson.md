# Session 8 — Build Something Real
## Capstone Project

**Duration:** 5–7 days total  
**Structure:** Day 1–2 (Scope together) · Day 3–5 (Advaith builds) · Day 6 (Code review) · Day 7 (Demo)

---

## 🎯 Goal

Advaith builds one complete, working project that:
- Connects at least 3 sessions of learning
- Can be demonstrated in 5 minutes
- He is genuinely proud of

---

## 📖 How This Session Works

This is different from all other sessions. Sree doesn't teach — Sree coaches.

**Day 1–2: Scope and Scaffold (together)**
- Advaith presents his chosen track
- Sree helps scope it down to what's achievable in 3 days
- Together they create the file structure and a working "skeleton" with placeholder functions
- Advaith should leave Day 2 with code that runs (even if it doesn't do much yet)

**Day 3–5: Advaith Builds Independently**
- Advaith works on his own
- Sree is available for "unblocking" — not writing code, but answering questions
- Advaith should commit working code at the end of each day

**Day 6: Code Review (together)**
- Sree reviews the code like a senior engineer
- Focus: does it work? Is it readable? What's one thing to improve?
- Advaith makes the improvements

**Day 7: Demo**
- Advaith presents the project to Sree (and anyone else who wants to watch)
- 5 minutes max
- Sree plays devil's advocate: asks hard questions about the code and the results

---

## The Four Tracks

---

### 🔮 Track A — The Oracle
**AI-Powered Stock Analysis Agent**

Connect: Sessions 4, 6, 7

**What it does:**
- User inputs a stock ticker (e.g., "MANU")
- Downloads 1 year of price data using yfinance
- Calculates: return, volatility, Sharpe ratio
- Feeds the stats to Claude API
- Claude generates a plain-English "investment thesis" (3 paragraphs: what the data says, risks, recommendation)

**Skeleton:**
```python
def get_stock_stats(ticker: str) -> dict: ...
def generate_thesis(ticker: str, stats: dict) -> str: ...
def main():
    ticker = input("Enter ticker: ")
    stats = get_stock_stats(ticker)
    print_stats(stats)
    thesis = generate_thesis(ticker, stats)
    print(thesis)
```

**3-day plan:**
- Day 3: `get_stock_stats()` working, stats printing correctly
- Day 4: `generate_thesis()` working with Claude API
- Day 5: Polish output, add error handling for bad tickers

---

### 🧬 Track B — NeuralNet from Zero
**Digit Recognition with Pure NumPy**

Connect: Sessions 4, 5

**What it does:**
- Trains a 2-layer neural network on the MNIST dataset (handwritten digits)
- Uses only NumPy — no PyTorch, no TensorFlow
- Achieves >85% accuracy
- Shows a grid of 25 test digits with predicted labels

**Skeleton:**
```python
# Layer sizes: 784 input (28x28 pixels) → 64 hidden → 10 output (digits 0-9)
def forward(X, W1, b1, W2, b2): ...
def backward(X, y, W1, b1, W2, b2, Z1, A1, Z2, A2): ...
def train(X_train, y_train, epochs=500): ...
def evaluate(X_test, y_test): ...
```

**3-day plan:**
- Day 3: Forward pass working, loss printing correctly
- Day 4: Backpropagation working, accuracy improving
- Day 5: Training done, visualisation of test predictions

---

### 🎓 Track C — The Tutor Bot
**AI That Teaches Math Interactively**

Connect: Sessions 4, 6

**What it does:**
- User chooses a math topic (e.g., "derivatives", "probability", "linear algebra")
- AI explains the concept at the right level
- AI generates a practice problem
- User submits their answer
- AI gives feedback and adjusts difficulty

**Skeleton:**
```python
def explain_concept(topic: str) -> str: ...
def generate_problem(topic: str, difficulty: str) -> tuple[str, str]: ...
def check_answer(problem: str, answer: str, correct: str) -> str: ...
def run_session(topic: str): ...
```

**3-day plan:**
- Day 3: `explain_concept()` and `generate_problem()` working
- Day 4: `check_answer()` with feedback and difficulty adjustment
- Day 5: Full session loop working, 3+ topics supported

---

### ⚽🏀 Track D — The Sports Oracle (Recommended for Advaith)
**Sports Analytics Dashboard + AI Commentary**

Connect: Sessions 2, 4, 5, 6

**What it does:**
- Loads pre-built CSV data for soccer + basketball (Sree provides this)
- Computes: top scorers, most consistent players, goals vs xG comparison
- Plots 3 charts: bar chart, scatter (goals vs assists), xG comparison
- AI analyst comments on the standout finding in the data

**Skeleton:**
```python
def load_data(sport: str) -> pd.DataFrame: ...
def compute_stats(df: pd.DataFrame) -> dict: ...
def plot_dashboard(df: pd.DataFrame): ...
def ai_commentary(stats: dict) -> str: ...
def main():
    for sport in ['soccer', 'basketball']:
        df = load_data(sport)
        stats = compute_stats(df)
        plot_dashboard(df)
        print(ai_commentary(stats))
```

**3-day plan:**
- Day 3: `load_data()` and `compute_stats()` working, basic prints
- Day 4: All 3 charts plotting correctly
- Day 5: AI commentary connected, full demo ready

---

## Demo Day Structure (Day 7)

Advaith presents for 5 minutes:
1. **Show it working** (2 minutes) — live demo
2. **Explain one piece of code** (1 minute) — pick the part he's most proud of
3. **What surprised him** (1 minute) — something unexpected during building
4. **What he'd add next** (1 minute) — one feature he didn't have time for

Sree asks 3 questions:
- *"Walk me through what happens when [specific input] is given"*
- *"What would break this if the data was different?"*
- *"Which session did you use most in this project?"*

---

## Sree's Coaching Principles

- **Unblock, don't write.** If Advaith is stuck, help him think — don't touch the keyboard.
- **Celebrate small wins.** Getting the first chart to appear is worth celebrating.
- **Embrace broken code.** Errors are information. "Read the error message out loud."
- **Scope ruthlessly.** If he's behind, cut features — not quality.
- **Ask "what do you want it to do next?"** — let him drive direction.

---

## What Success Looks Like

Not: perfect code.  
Not: a sophisticated project.  

Success: Advaith can sit down in front of a keyboard, write a Python program that does something real, and explain every line he wrote.

That's the whole goal.
