# Session 7 — Assignment

---

## Task 1 — Extend the Stock Analysis

Open `labs/stock_analysis.py` and add two more tickers of your choice.

Good options with sports connections:
- `"NKE"` — Nike (sponsors your favourite clubs/players)
- `"ADDYY"` — Adidas
- `"EA"` — EA Sports (FIFA/FC 25 publisher)
- `"MSGS"` — Madison Square Garden Sports (owns the Knicks + Rangers)
- `"FSK"` — Formula 1 / any sports media company

For each new ticker:
1. Download 3 years of data
2. Calculate annual return, volatility, Sharpe Ratio
3. Add it to the correlation matrix

**Write 3 sentences:** Which new stock has the best risk-adjusted return? Does adding it to a portfolio with MANU reduce or increase overall risk?

---

## Task 2 — The Transfer Budget Model

Imagine you're a sporting director with a £100M transfer budget.  
You're choosing between 3 striker options:

| Player | Fee | Goals/season (last 3 years) | Injury days/year |
|--------|-----|----------------------------|-----------------|
| Player A | £50M | 25, 27, 23 | 10 |
| Player B | £40M | 35, 12, 28 | 45 |
| Player C | £30M | 18, 20, 19 | 5  |

Using Python, calculate:
1. **Mean goals per season** for each player
2. **Standard deviation** (volatility) of goals for each player
3. A **"Sharpe-like ratio"** for each player: `mean_goals / std_goals`
   (More consistent = better ratio)
4. **Goals per million pounds** spent

Print a recommendation: which player would you sign and why?

---

## Task 3 — Research: Renaissance Technologies

Read about the Medallion Fund and Jim Simons.

Answer in 3–5 sentences each:
1. What is the Medallion Fund's average annual return? How does it compare to the S&P 500?
2. Jim Simons was a mathematician and codebreaker before he started the fund. How did his background influence his approach?
3. Why did the fund stop accepting outside investors in 1993?

---

## Task 4 — Connect Finance to AI

In Session 5 you built an xG model. In Session 6 you built an AI agent.  
In Session 7 you learned about quant finance.

Write 6–8 sentences connecting all three:
- How is building an xG model similar to building a trading strategy?
- How could an AI agent (from Session 6) be used in quantitative trading?
- What risks would you worry about if you automated a trading strategy?

---

## Bring to Next Session

- Extended stock analysis with 2 new tickers
- Transfer budget model (code + recommendation)
- Renaissance research answers
- Finance + AI connection essay

---

## Also: Capstone Decision

Before Session 8, think about which capstone track you want to do:

| Track | What You Build |
|-------|---------------|
| 🔮 A — The Oracle | AI-powered stock analysis agent |
| 🧬 B — NeuralNet from Zero | Digit recognition with NumPy |
| 🎓 C — The Tutor Bot | AI that teaches math interactively |
| ⚽🏀 D — The Sports Oracle | Sports analytics dashboard + AI |

**Come to Session 8 with your choice.** Teacher will help you scope it.
