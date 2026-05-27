# Session 7 — Hedge Funds Are Just Applied Math
## General Overview of Quant Finance

**Duration:** 2–3 hours  
**the teacher's prep:** `pip install yfinance` done. Man United ticker confirmed working. Data pre-downloaded if internet is unreliable.

---

## 🎯 Goal

By the end of this session, Student understands:
- What quantitative finance is and why it's relevant
- How stock prices, returns, and volatility work
- Why portfolio theory (Markowitz) is just linear algebra
- How to download and visualise real financial data
- The connection between sports analytics and quant finance

---

## 📖 the teacher's Narrative

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

All of this runs on data — and for 40 years the data layer has been Bloomberg. Michael Bloomberg built the Bloomberg Terminal in 1981 after being fired from Merrill Lynch with a $10 million severance cheque. He used it to build the financial information system that every bank, hedge fund, and trading desk in the world relies on. Bloomberg LP now generates around $10 billion a year in revenue. A single terminal subscription costs $24,000 per year, and there are roughly 325,000 active subscribers globally. The terminal is so entrenched that most people in finance consider it a non-negotiable overhead, like electricity.

---

### The Basic Building Blocks

**Stock price** — what someone is willing to pay for a share of a company right now.  
**Return** — how much a stock gained or lost over a period.
```
Daily return = (price today - price yesterday) / price yesterday
```

**Volatility** — how much a stock's returns vary (standard deviation of returns).  
High volatility = the stock swings a lot = riskier.

*"Standard deviation — Student knows this from stats. In finance, it IS risk. Low std dev = stable investment. High std dev = roller coaster."*

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

Renaissance is the extreme case, but they are not alone. Goldman Sachs has an entire quantitative strategies division — systematically applying this math to global markets. Two Sigma, founded in 2001, treats investing purely as a data science problem: they hire hundreds of PhDs in mathematics, computer science, and physics, and the firm barely resembles a traditional finance company. Citadel, run by Ken Griffin, manages around $63 billion and is widely considered the most profitable hedge fund ever built. These are the firms that recruit people who can combine statistical modelling with programming — exactly the combination of skills this course is building toward.

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
- The exponential and logarithm — Student knows these
- The normal distribution — covered in Session 5
- The partial derivatives — 12th-grade calculus

*"Every symbol in this formula is something you know. This equation is worth a Nobel Prize and runs a $10 trillion market. It's your maths, dressed up in finance."*

---

## ⚡ Wow Moment

Run the lab live. Download 5 years of real Man United stock data in 3 lines of Python. Plot it.  
Find the exact date the Glazers announced they were considering selling (November 2022) — watch the price spike on the chart.

*"You just downloaded and visualised 5 years of real financial data in under 60 seconds. A Bloomberg terminal costs $24,000 per year for the same thing."*

The data came from Yahoo Finance — the `yfinance` Python library pulls directly from it. Yahoo Finance is one of the few products that survived Yahoo's long decline from internet giant to acquisition target. Most of Yahoo's business faded, but the financial data product held on and became genuinely valuable. It is now one of the most-visited financial sites in the world, and for anyone learning quant finance without a Bloomberg subscription, it is the starting point.

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

## Teaching Notes for Teacher

- Connect everything to the math Student already knows. Don't introduce new math — reveal that familiar math has financial applications.
- The Man United example is personal and accessible. Use it as the thread.
- Don't go deep on derivatives pricing — Black-Scholes is a "here's what the math enables" moment, not a derivation.
- The Sharpe Ratio is the one formula worth memorising — it's used in every performance discussion.
- Best question at the end: *"If you were managing a £100m transfer budget like a portfolio, how would you apply what we learned today?"*

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** A stock is priced at £100 on Monday and £108 on Tuesday. What is the daily return?
- A) £8
- B) 0.08 or 8% ✓
- C) 1.08
- D) 8

**Q2.** The Sharpe Ratio formula is (Return − Risk-Free Rate) / Volatility. What does a higher Sharpe Ratio indicate?
- A) The investment is riskier
- B) The investment has lower returns
- C) The investment delivers more return per unit of risk taken ✓
- D) The investment is in a bear market

**Q3.** Why did Markowitz win the Nobel Prize? What was his key insight about diversification?
- A) He proved that holding more stocks always increases returns
- B) He showed that combining uncorrelated assets reduces total portfolio risk without reducing expected return ✓
- C) He invented the concept of a stock price
- D) He proved that diversification always leads to higher returns

**Q4.** Consider two strikers: Striker A scores 20, 21, 19, 22, 20 goals across five seasons. Striker B scores 38, 5, 29, 7, 31 goals. Which has higher volatility, and if you were a club with a tight budget, which would you prefer and why?

**Q5.** What is the correlation between two assets, and why does the Markowitz portfolio benefit most when you combine assets with a correlation close to −1?

**Q6.** Renaissance Technologies' Medallion Fund returned ~66% per year for 30 years. The S&P 500 index returns about 10% per year. What does this suggest about their approach to markets?
- A) They took enormous amounts of risk
- B) They found mathematical patterns in market data that others missed, giving them a persistent edge ✓
- C) They got lucky for three decades
- D) They only invested in technology stocks

**Q7.** Black-Scholes is used to price options. In plain terms, what is an option, and which two mathematical concepts from your 12th-grade studies appear in the formula?

**Q8 (explain in your own words).** The session described managing a football transfer budget "like a portfolio." Using the concepts of volatility, correlation, and diversification from today, explain what a data-driven sporting director might consider when allocating a £100m transfer budget across multiple player positions.

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — Return = (108 − 100) / 100 = 0.08 = 8%. The return is a percentage change, not an absolute number.

**Q2.** C — The Sharpe Ratio measures risk-adjusted return. Renaissance Medallion's ~2.0 versus the S&P 500's ~0.5 means Renaissance generated four times more return per unit of risk, which is extraordinary.

**Q3.** B — Markowitz proved that portfolio risk is not the weighted average of individual risks. Because assets do not move in perfect lockstep, combining them reduces overall volatility — the mathematical justification for "don't put all your eggs in one basket."

**Q4.** Striker B has far higher volatility (large swings between seasons). A club on a tight budget would likely prefer Striker A — more predictable output makes squad planning and wage structures more manageable, even if Striker B's peak seasons are spectacular.

**Q5.** Correlation ranges from −1 to +1 and measures how two assets move together. A correlation of −1 means they move in exactly opposite directions. Combining such assets means when one falls, the other rises, so losses in one are offset by gains in the other — the maximum risk reduction possible.

**Q6.** B — Renaissance employed mathematicians and physicists who found statistical patterns (signals) in price data that gave them a consistent edge. Their returns were too persistent and too large to be luck alone.

**Q7.** An option gives the buyer the right (but not the obligation) to buy or sell an asset at a fixed price on a future date. The Black-Scholes formula uses the normal distribution (from probability and statistics) and partial derivatives (from calculus) — both standard 12th-grade topics.

**Q8.** Model answer: A data-driven sporting director would treat each position as an "asset class" — spending on a mix of attackers, midfielders, and defenders. Volatility matters: a reliable 15-goal striker (low volatility) is more plannable than a boom-or-bust player. Correlation matters too — signing two players from the same injury-prone mould doubles risk. Diversification suggests spreading budget across age groups (a young player is a long-term asset, a proven veteran reduces near-term risk) rather than concentrating the entire £100m on one marquee signing.

---

## 📚 Research Materials

> 💡 **Start here:** Watch the "Quantitative Finance Full Course" by Coding Jesus on YouTube — it covers returns, volatility, and the Sharpe ratio with actual Python code, making it the perfect bridge from this session to hands-on practice.

### 🎬 Films & Documentaries

| Title | Year | What to watch for |
|---|---|---|
| [The Man Who Solved the Market](https://www.imdb.com/title/tt11528906/) | 2019 | Based on Gregory Zuckerman's biography of Jim Simons; no official documentary yet, but several documentary-style interviews on YouTube |
| [Betting on Zero](https://www.imdb.com/title/tt5818932/) | 2016 | Hedge fund short-selling in action; shows the adversarial side of quantitative trading |
| [Margin Call](https://www.imdb.com/title/tt1615147/) | 2011 | Fiction but forensically accurate about a Wall Street firm discovering a catastrophic risk model failure overnight |
| [The Big Short](https://www.imdb.com/title/tt1596363/) | 2015 | How a small group used quantitative analysis to short the 2008 housing market; excellent on CDOs and derivatives |

### 📺 YouTube

| Channel | Video | Link |
|---|---|---|
| Coding Jesus | Python for Finance — Sharpe Ratio, Volatility, Portfolio Theory | *search "Coding Jesus quantitative finance Python"* |
| Quantopian / QuantConnect | Introduction to Algorithmic Trading | *search "QuantConnect algorithmic trading tutorial"* |
| Patrick Boyle | Jim Simons and Renaissance Technologies Explained | [youtube.com/watch?v=dARzFl_U0cs](https://www.youtube.com/watch?v=dARzFl_U0cs) |
| Khan Academy | Finance & Capital Markets — Introduction to Stocks | [khanacademy.org/economics-finance-domain/core-finance](https://www.khanacademy.org/economics-finance-domain/core-finance) |
| 3Blue1Brown | The Black-Scholes Equation Explained | *search "3Blue1Brown Black-Scholes"* |
| Two Minute Papers | How AI is Used in Quantitative Finance | *search "Two Minute Papers AI hedge fund trading"* |

### 📖 Books

| Title | Author | Level | What it covers |
|---|---|---|---|
| *The Man Who Solved the Market* | Gregory Zuckerman | Easy | Narrative biography of Jim Simons and the founding of Renaissance Technologies; no maths required |
| *Beat the Dealer* | Edward O. Thorp | Easy | Thorp's original card-counting system and how it became the foundation of quantitative trading |
| *A Random Walk Down Wall Street* | Burton Malkiel | Easy | Classic argument that markets are efficient; great counterpoint to algorithmic trading approaches |
| *Options, Futures, and Other Derivatives* | John C. Hull | Hard | The standard university textbook for derivatives pricing including Black-Scholes; used in every finance programme |
| *Quantitative Finance for Dummies* | Steve Bell | Medium | Covers returns, volatility, portfolio theory, and options without requiring a maths degree |

### 🌐 Articles & Interactive Resources

| Resource | Link | What it covers |
|---|---|---|
| Investopedia — Sharpe Ratio | [investopedia.com/terms/s/sharperatio.asp](https://www.investopedia.com/terms/s/sharperatio.asp) | Clear definition and worked examples with interactive calculator |
| QuantLib | [quantlib.org](https://www.quantlib.org) | Open-source library for quantitative finance; used by banks and hedge funds |
| Quantopian Lectures (archived) | [quantopian.com/lectures](https://www.quantopian.com/lectures) | Free university-level course on algorithmic trading and portfolio theory in Python |
| Khan Academy — Stocks and Bonds | [khanacademy.org/economics-finance-domain/core-finance/stock-and-bonds](https://www.khanacademy.org/economics-finance-domain/core-finance/stock-and-bonds) | Free, beginner-friendly video series covering the fundamentals of financial markets |
| Black-Scholes Interactive Calculator | [optionspricingcalculator.net](https://www.optionspricingcalculator.net) | Plug in real numbers and see how each variable affects an option's price |

### 🔗 People to Look Up

- **Jim Simons** — Mathematician and founder of Renaissance Technologies; built the most successful quantitative hedge fund in history using pattern recognition in data
- **Ed Thorp** — Mathematician who invented card counting and then applied probability theory to beat financial markets; godfather of quant finance
- **Harry Markowitz** — Economist who invented Modern Portfolio Theory (MPT) in 1952; showed mathematically why diversification reduces risk; Nobel Prize winner
- **Fischer Black & Myron Scholes** — Developed the Black-Scholes options pricing model in 1973; Scholes won the Nobel Prize (Black had died); transformed derivatives markets
- **Warren Buffett** — The deliberate contrast to quant finance; fundamental value investor who relies on business analysis rather than statistical models — understanding both approaches sharpens thinking
- **Robert Shiller** — Yale economist known for the CAPE ratio and behavioural finance; argues markets are driven by narratives and psychology, not pure maths
