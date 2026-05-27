# Session 8 — Build Something Real
## Capstone Project

**Duration:** 5–7 days total  
**Structure:** Day 1–2 (Scope together) · Day 3–5 (Student builds) · Day 6 (Code review) · Day 7 (Demo)

---

## 🎯 Goal

Student builds one complete, working project that:
- Connects at least 3 sessions of learning
- Can be demonstrated in 5 minutes
- He is genuinely proud of

---

## 📖 How This Session Works

This is different from all other sessions. Teacher doesn't teach — Teacher coaches.

**Day 1–2: Scope and Scaffold (together)**
- Student presents his chosen track
- Teacher helps scope it down to what's achievable in 3 days
- Together they create the file structure and a working "skeleton" with placeholder functions
- Student should leave Day 2 with code that runs (even if it doesn't do much yet)

**Day 3–5: Student Builds Independently**
- Student works on his own
- Teacher is available for "unblocking" — not writing code, but answering questions
- Student should commit working code at the end of each day

**Day 6: Code Review (together)**
- Teacher reviews the code like a senior engineer
- Focus: does it work? Is it readable? What's one thing to improve?
- Student makes the improvements

**Day 7: Demo**
- Student presents the project to Teacher (and anyone else who wants to watch)
- 5 minutes max
- Teacher plays devil's advocate: asks hard questions about the code and the results

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

### ⚽🏀 Track D — The Sports Oracle (Recommended for Student)
**Sports Analytics Dashboard + AI Commentary**

Connect: Sessions 2, 4, 5, 6

**What it does:**
- Loads pre-built CSV data for soccer + basketball (Teacher provides this)
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

Student presents for 5 minutes:
1. **Show it working** (2 minutes) — live demo
2. **Explain one piece of code** (1 minute) — pick the part he's most proud of
3. **What surprised him** (1 minute) — something unexpected during building
4. **What he'd add next** (1 minute) — one feature he didn't have time for

Teacher asks 3 questions:
- *"Walk me through what happens when [specific input] is given"*
- *"What would break this if the data was different?"*
- *"Which session did you use most in this project?"*

---

## the teacher's Coaching Principles

- **Unblock, don't write.** If Student is stuck, help him think — don't touch the keyboard.
- **Celebrate small wins.** Getting the first chart to appear is worth celebrating.
- **Embrace broken code.** Errors are information. "Read the error message out loud."
- **Scope ruthlessly.** If he's behind, cut features — not quality.
- **Ask "what do you want it to do next?"** — let him drive direction.

---

## What Success Looks Like

Not: perfect code.  
Not: a sophisticated project.  

Success: Student can sit down in front of a keyboard, write a Python program that does something real, and explain every line he wrote.

That's the whole goal.

---

## 📚 Research Materials

> 💡 **Start here:** Work through the official [Python.org Beginner's Guide](https://wiki.python.org/moin/BeginnersGuide) alongside your project — it is concise, trustworthy, and structured exactly for someone writing their first real programs.

### 🎬 Films & Documentaries

| Title | Year | What to watch for |
|---|---|---|
| [General Magic](https://www.generalmagicthemovie.com/) | 2018 | Documentary about a forgotten 1990s startup whose alumni founded or shaped Google, eBay, Android, and LinkedIn — a masterclass in what makes or breaks a product vision |
| [The Inventor: Out for Blood in Silicon Valley](https://www.imdb.com/title/tt8488126/) | 2019 | HBO documentary on Theranos; sobering lesson on the dangers of demo culture over working product |
| [Indie Game: The Movie](https://www.imdb.com/title/tt1942884/) | 2012 | Three indie developers building and launching their first commercial games; captures the emotional reality of a solo build project |

### 📺 YouTube

| Channel | Video | What it covers |
|---|---|---|
| Tech With Tim | Build a Stock Price Tracker in Python | *search "Tech With Tim Python stock price tracker"* — Stock Oracle track |
| 3Blue1Brown | Neural Networks series (Chapters 1–4) | [youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) — Neural Net track |
| Sentdex | Python for Finance — Pulling Stock Data with yfinance | *search "Sentdex yfinance tutorial"* — Stock Oracle track |
| Tech With Tim | Build a Chatbot with Python and the OpenAI API | *search "Tech With Tim Python chatbot OpenAI API"* — Tutor Bot track |
| Coding Is Fun | Build a Sports Data App with Python | *search "Python sports data API project tutorial"* — Sports Oracle track |
| Corey Schafer | Python OOP Tutorial — Classes and Objects | [youtube.com/watch?v=ZDa-Z5JzLYM](https://www.youtube.com/watch?v=ZDa-Z5JzLYM) — All tracks: structuring a real project |

### 📖 Books

| Title | Author | Level | What it covers | Free |
|---|---|---|---|---|
| *Automate the Boring Stuff with Python* | Al Sweigart | Easy | Free online; teaches Python through real projects (web scraping, working with files, APIs) — ideal capstone companion | [Free →](https://automatetheboringstuff.com) |
| *Python Crash Course* | Eric Matthes | Easy | Project-based introduction; Part II walks through three complete projects from scratch | — |
| *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* | Aurélien Géron | Medium | The standard practical ML book; Chapter 10–12 covers neural networks with working code examples | [Open Library](https://openlibrary.org) |
| *Flask Web Development* | Miguel Grinberg | Medium | Build and deploy a real Flask web application; directly applicable to adding a web front end to any capstone track | — |
| *The Pragmatic Programmer* | Hunt & Thomas | Medium | Timeless advice on software craftsmanship, debugging, and writing code that actually works in the real world | — |

### 🌐 Articles & Interactive Resources

| Resource | Link | What it covers |
|---|---|---|
| yfinance Documentation | [pypi.org/project/yfinance/](https://pypi.org/project/yfinance/) | Python library to pull live and historical stock data from Yahoo Finance — essential for Stock Oracle and Sports Oracle tracks |
| Anthropic Claude API Quickstart | [docs.anthropic.com/en/docs/quickstart](https://docs.anthropic.com/en/docs/quickstart) | 10-minute guide to sending your first API request — essential for Tutor Bot track |
| Scikit-learn Getting Started | [scikit-learn.org/stable/getting_started.html](https://scikit-learn.org/stable/getting_started.html) | Official tutorial for building ML models in Python; relevant to Neural Net track |
| Real Python | [realpython.com](https://realpython.com) | High-quality tutorials on specific Python topics (APIs, data visualisation, web scraping) — great for unblocking specific problems |
| GitHub Student Developer Pack | [education.github.com/pack](https://education.github.com/pack) | Free access to hosting, domains, and developer tools for students |

### 🔗 People to Look Up (by Capstone Track)

**All tracks — Software Engineering Process**
- **Jon Skeet** — Legendary Stack Overflow contributor; his answers on debugging and clean code are a model for how to think through problems
- **Martin Fowler** — Author of *Refactoring*; his writing on clean, maintainable code is the best practical guide for structuring a project that actually works

**Stock Oracle & Sports Oracle**
- **Siraj Raval** — YouTube educator known for fast-paced Python and ML project tutorials; good for rapid inspiration (verify his code carefully)
- **Sentdex (Harrison Kinsley)** — YouTube channel dedicated to Python finance, trading, and data science projects with complete code walkthroughs

**Tutor Bot**
- **Andrej Karpathy** — His lectures on LLMs give the deepest understanding of what is happening inside the chatbot you are building
- **Simon Willison** — Developer and writer who publishes extensively on practical, responsible use of LLM APIs in real projects at [simonwillison.net](https://simonwillison.net)
