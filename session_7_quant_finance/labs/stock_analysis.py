# Lab — Stock Analysis with Real Data
# Session 7: Quantitative Finance
#
# Prerequisites: pip install yfinance matplotlib numpy pandas
# Run: python stock_analysis.py

import yfinance as yf
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# ─────────────────────────────────────────
# PART 1: Download Real Data
# Man United is publicly listed — perfect for this session
# ─────────────────────────────────────────

print("Downloading stock data...")

tickers = {
    "MANU":  "Manchester United",
    "AAPL":  "Apple",
    "NVDA":  "NVIDIA",
}

# Download 3 years of data
data = {}
for ticker, name in tickers.items():
    stock = yf.Ticker(ticker)
    hist = stock.history(period="3y")
    data[ticker] = hist['Close']
    print(f"  ✓ {name}: {len(hist)} trading days")

prices = pd.DataFrame(data)


# ─────────────────────────────────────────
# PART 2: Plot Price History
# ─────────────────────────────────────────

fig, axes = plt.subplots(3, 1, figsize=(12, 10))
fig.patch.set_facecolor('#0f0f1a')

colours = {'MANU': '#e94560', 'AAPL': '#00d4aa', 'NVDA': '#ffd700'}

for idx, (ticker, name) in enumerate(tickers.items()):
    ax = axes[idx]
    ax.set_facecolor('#1a1a2e')

    ax.plot(prices.index, prices[ticker],
            color=colours[ticker], linewidth=1.5, label=name)

    # Highlight max and min
    max_price = prices[ticker].max()
    min_price = prices[ticker].min()
    max_date  = prices[ticker].idxmax()
    min_date  = prices[ticker].idxmin()

    ax.scatter([max_date], [max_price], color='gold', s=100, zorder=5)
    ax.scatter([min_date], [min_price], color='white', s=60, zorder=5)

    ax.set_title(f'{name} ({ticker})', color='white', fontsize=11, fontweight='bold')
    ax.set_ylabel('Price (USD)', color='white')
    ax.tick_params(colors='white')
    ax.spines[:].set_color('#333')
    ax.grid(alpha=0.2)

    # Add annotation for MANU (Man United sale news Nov 2022)
    if ticker == 'MANU':
        ax.axvline(pd.Timestamp('2022-11-22'), color='yellow',
                   linewidth=1, linestyle='--', alpha=0.7)
        ax.text(pd.Timestamp('2022-11-25'), max_price * 0.8,
                'Glazers\nfor sale', color='yellow', fontsize=7)

axes[-1].set_xlabel('Date', color='white')
plt.suptitle('3-Year Stock Price Comparison', color='white',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('price_history.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
plt.show()


# ─────────────────────────────────────────
# PART 3: Calculate Returns and Risk
# ─────────────────────────────────────────

print("\n=== Risk & Return Analysis ===")
print(f"{'Company':<20} {'Annual Return':>14} {'Volatility (Risk)':>18} {'Sharpe Ratio':>14}")
print("─" * 70)

risk_free_rate = 0.05  # 5% — approximate US treasury yield

for ticker, name in tickers.items():
    daily_returns = prices[ticker].pct_change().dropna()

    # Annualise (252 trading days per year)
    annual_return = daily_returns.mean() * 252
    annual_vol    = daily_returns.std() * np.sqrt(252)
    sharpe        = (annual_return - risk_free_rate) / annual_vol

    print(f"{name:<20} {annual_return:>13.1%} {annual_vol:>17.1%} {sharpe:>14.2f}")

print()
print("Sharpe Ratio > 1.0 = good  |  > 2.0 = excellent  |  Renaissance: ~2.0")


# ─────────────────────────────────────────
# PART 4: Correlation Between Assets
# ─────────────────────────────────────────

daily_returns = prices.pct_change().dropna()
correlation_matrix = daily_returns.corr()

print("\n=== Correlation Matrix ===")
print("(1 = move together perfectly, 0 = no relationship, -1 = opposite)")
print()
print(correlation_matrix.round(3).to_string())

# Find the lowest correlation pair (best diversification)
pairs = []
for i, t1 in enumerate(tickers):
    for j, t2 in enumerate(tickers):
        if i < j:
            corr = correlation_matrix.loc[t1, t2]
            pairs.append((t1, t2, corr))

best_pair = min(pairs, key=lambda x: abs(x[2]))
print(f"\nBest diversification pair: {tickers[best_pair[0]]} + {tickers[best_pair[1]]} (corr = {best_pair[2]:.3f})")


# ─────────────────────────────────────────
# PART 5: Key Stats Summary
# ─────────────────────────────────────────

print("\n=== Man United Deep Dive ===")
manu = prices['MANU'].dropna()
print(f"Current price:    ${manu.iloc[-1]:.2f}")
print(f"3-year high:      ${manu.max():.2f}")
print(f"3-year low:       ${manu.min():.2f}")
print(f"Price range:      ${manu.max() - manu.min():.2f}")

start_price = manu.iloc[0]
end_price   = manu.iloc[-1]
total_return = (end_price - start_price) / start_price * 100
print(f"3-year return:    {total_return:+.1f}%")
print()
print(f"Compare: NVIDIA 3-year return = {((prices['NVDA'].iloc[-1] - prices['NVDA'].iloc[0]) / prices['NVDA'].iloc[0] * 100):+.1f}%")
print("Discussion: Was buying Man United stock a good investment?")


# ─────────────────────────────────────────
# DISCUSSION QUESTIONS
# ─────────────────────────────────────────
# 1. MANU vs NVDA — if you invested £1000 in each 3 years ago, what would each be worth now?
#
# 2. Which has higher volatility — Man United or NVIDIA? What does that mean for an investor?
#
# 3. The Glazers bought Man United at ~£790M. The club is worth ~£2.5B.
#    But the Sharpe Ratio of MANU stock is probably negative.
#    How can a club be worth more but be a bad stock investment?
#
# 4. What would you add to a portfolio containing MANU to reduce risk?
#    (Hint: look at the correlation matrix — what's LEAST correlated with MANU?)
