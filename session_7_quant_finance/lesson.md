# Session 7 — Hedge Funds Are Just Applied Math
## General Overview of Quant Finance

**Duration:** 2–3 hours  
**Sree's prep:** `pip install yfinance` done. Man United ticker confirmed working. Data pre-downloaded if internet is unreliable.

---

## 🎯 Goal

By the end of this session, Advaith understands:
- What quantitative finance is and why it's relevant
- How stock prices, returns, and volatility work
- Why portfolio theory (Markowitz) is just linear algebra
- How to download and visualise real financial data
- The connection between sports analytics and quant finance

---

## 📖 Sree's Narrative

### Hook

*"In 1988, a group of mathematicians and scientists left academia to start a hedge fund. No traders. No finance backgrounds. Just math people. By 2022, their Medallion Fund had returned over 66% per year for 30 years. No other fund has come close. Their secret? They treated the market like a physics problem and let the math trade."*

That fund is Renaissance Technologies. *"What did they know that everyone else didn't? The same math you've been learning."*

---

### What Is Quantitative Finance?

The application of mathematics, statistics, and computing to financial markets.

Three main areas:
1. **Quantitative trading** — use math to find patterns in prices and trade on them
2. **Risk management** — use probability and statistics to measure and limit exposure
3. **Derivatives pricing** — use calculus and stochastic processes to price complex instruments

*"The same skills that power AI — linear algebra, probability, Python — are the skills that power quant finance. The tools are identical. The data is different."*

---

### The Basic Building Blocks

**Stock price** — what someone is willing to pay for a share of a company right now.  
**Return** — how much a stock gained or lost over a period.
```
Daily return = (price today - price yesterday) / price yesterday
```

**Volatility** — how much a stock's returns vary (standard deviation of returns).  
High volatility = the stock swings a lot = riskier.

*"Standard deviation — Advaith knows this from stats. In finance, it IS risk. Low std dev = stable investment. High std dev = roller coaster."*

**Sports connection:** *"A player who scores 25 goals every season has low volatility. A player who scores 45 one season and 8 the next has high volatility. Would you sign a striker with high volatility? Depends on the price and your squad's needs. Same logic as portfolio construction."*

---

### Portfolio Theory — Markowitz (1952)

Harry Markowitz won the Nobel Prize in Economics for one idea: **diversification reduces risk without reducing expected return.**

If you own one stock and it crashes, you lose everything.  
If you own 20 uncorrelated stocks, one crash barely affects you.

The math: portfolio return = weighted average of individual returns.  
Portfolio risk = **not** the weighted average of individual risks — it's lower because of correlation.

*"If Man United stock falls when Man City wins the league, and you hold both Man United AND a company that benefits from Man City winning, the losses offset. That's diversification."*

The **Sharpe Ratio** — return per unit of risk:
```
Sharpe Ratio = (Portfolio Return - Risk-Free Rate) / Portfolio Volatility
```
Higher Sharpe = better risk-adjusted return. Renaissance Medallion Fund: Sharpe ratio of ~2.0. The S&P 500: ~0.5.

---

### The Man United Thought Experiment

Man United (ticker: MANU) is publicly listed. The Glazer family bought the club for £790 million. The club is now worth £2.5 billion.

*"Was it a good investment?"*
- For the Glazers: Yes. 3× their money.
- For the fans: The debt they loaded onto the club drained transfer budgets for a decade.

*"Same numbers. Completely different answer depending on your perspective. This is why finance isn't just math — it's incentives and stakeholders."*

---

### Black-Scholes — The Equation Worth a Nobel Prize

In 1973, Fischer Black and Myron Scholes published a formula to price options (the right to buy a stock at a fixed price in the future).

Show the formula — don't derive it. Just point to each symbol:
- The exponential and logarithm — Advaith knows these
- The normal distribution — covered in Session 5
- The partial derivatives — 12th-grade calculus

*"Every symbol in this formula is something you know. This equation is worth a Nobel Prize and runs a $10 trillion market. It's your maths, dressed up in finance."*

---

## ⚡ Wow Moment

Run the lab live. Download 5 years of real Man United stock data in 3 lines of Python. Plot it.  
Find the exact date the Glazers announced they were considering selling (November 2022) — watch the price spike on the chart.

*"You just downloaded and visualised 5 years of real financial data in under 60 seconds. A Bloomberg terminal costs $24,000 per year for the same thing."*

---

## 🔑 Key Concepts Checklist

- [ ] Stock — a share of ownership in a company
- [ ] Return — percentage change in price over a period
- [ ] Volatility — standard deviation of returns; measure of risk
- [ ] Portfolio — a collection of assets held together
- [ ] Diversification — owning uncorrelated assets reduces total risk
- [ ] Sharpe Ratio — return divided by risk; measures efficiency
- [ ] Markowitz — portfolio optimisation using mean-variance analysis
- [ ] Correlation — how two assets move together (−1 to +1)
- [ ] Options — the right (not obligation) to buy/sell at a fixed price
- [ ] Black-Scholes — formula to price options using calculus + statistics

---

## Teaching Notes for Sree

- Connect everything to the math Advaith already knows. Don't introduce new math — reveal that familiar math has financial applications.
- The Man United example is personal and accessible. Use it as the thread.
- Don't go deep on derivatives pricing — Black-Scholes is a "here's what the math enables" moment, not a derivation.
- The Sharpe Ratio is the one formula worth memorising — it's used in every performance discussion.
- Best question at the end: *"If you were managing a £100m transfer budget like a portfolio, how would you apply what we learned today?"*
