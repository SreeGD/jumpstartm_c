# Lab 4 — Dice Simulator & The Law of Large Numbers
# Session 4: Randomness, Histograms, List Comprehensions
#
# Concepts: random, list comprehensions, matplotlib histograms,
#           Law of Large Numbers
# Run: python lab4_dice_simulator.py

import random
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

# ─────────────────────────────────────────
# PART 1: Roll a dice once
# ─────────────────────────────────────────

single_roll = random.randint(1, 6)
print(f"Single roll: {single_roll}")


# ─────────────────────────────────────────
# PART 2: Roll many times — list comprehension
# [expression for item in range(n)]
# ─────────────────────────────────────────

rolls_10    = [random.randint(1, 6) for _ in range(10)]
rolls_100   = [random.randint(1, 6) for _ in range(100)]
rolls_1000  = [random.randint(1, 6) for _ in range(1000)]
rolls_10000 = [random.randint(1, 6) for _ in range(10000)]

print(f"\n10 rolls:    {rolls_10}")
print(f"Average of 10:     {sum(rolls_10)/len(rolls_10):.2f}  (expected: 3.5)")
print(f"Average of 100:    {sum(rolls_100)/len(rolls_100):.2f}  (expected: 3.5)")
print(f"Average of 1000:   {sum(rolls_1000)/len(rolls_1000):.2f}  (expected: 3.5)")
print(f"Average of 10000:  {sum(rolls_10000)/len(rolls_10000):.2f}  (expected: 3.5)")


# ─────────────────────────────────────────
# PART 3: Visualise the Law of Large Numbers
# ─────────────────────────────────────────

fig = plt.figure(figsize=(14, 8))
fig.patch.set_facecolor('#0f0f1a')
gs = gridspec.GridSpec(2, 2, figure=fig)

datasets = [
    (rolls_10,    "10 rolls"),
    (rolls_100,   "100 rolls"),
    (rolls_1000,  "1,000 rolls"),
    (rolls_10000, "10,000 rolls"),
]

for idx, (data, title) in enumerate(datasets):
    ax = fig.add_subplot(gs[idx // 2, idx % 2])
    ax.set_facecolor('#1a1a2e')

    ax.hist(data, bins=range(1, 8), align='left',
            color='#e94560', edgecolor='#0f0f1a', rwidth=0.8)

    avg = sum(data) / len(data)
    ax.axvline(avg, color='#00d4aa', linewidth=2, linestyle='--',
               label=f'Mean = {avg:.2f}')

    ax.set_title(title, color='white', fontsize=12, fontweight='bold')
    ax.set_xlabel('Dice value', color='white')
    ax.set_ylabel('Count', color='white')
    ax.set_xticks([1, 2, 3, 4, 5, 6])
    ax.tick_params(colors='white')
    ax.legend(facecolor='#0f0f1a', labelcolor='white', fontsize=9)
    ax.spines[:].set_color('#333')

fig.suptitle('Law of Large Numbers — More Rolls → Flatter Distribution',
             color='white', fontsize=14, fontweight='bold', y=1.02)

plt.tight_layout()
plt.savefig('dice_simulator.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
plt.show()


# ─────────────────────────────────────────
# PART 4: Sports Connection — Free Throw %
# ─────────────────────────────────────────
# Simulate a player with 75% free throw percentage
# How many shots to get a reliable estimate?

def simulate_free_throws(true_pct, num_shots):
    """Simulate free throws with a given true success rate"""
    makes = sum(1 for _ in range(num_shots) if random.random() < true_pct)
    observed_pct = makes / num_shots * 100
    return observed_pct

print("\n=== Free Throw Simulation ===")
print(f"Player's true free throw %: 75%")
print(f"How many shots to get an accurate read?\n")

true_pct = 0.75
for n in [5, 10, 25, 50, 100, 500]:
    observed = simulate_free_throws(true_pct, n)
    error = abs(observed - 75)
    print(f"{n:4d} shots → observed {observed:.1f}% (error: {error:.1f}%)")

print("\nMore shots → better estimate → Law of Large Numbers in sports!")

print("\n" + "="*50)
print("This is why:")
print("- 5-game shooting slump means nothing statistically")
print("- 82-game NBA season sample size tells you everything")
print("- xG models need thousands of shots to be reliable")


# ─────────────────────────────────────────
# CHALLENGE
# ─────────────────────────────────────────
# 1. Simulate rolling TWO dice and plotting their SUM
#    What shape does the distribution take? Why?
#    (Hint: there's only 1 way to roll a 2, but 6 ways to roll a 7)
#
# 2. Simulate a basketball player taking 100 three-point shots
#    with a 37% success rate. Run the simulation 1000 times.
#    What's the range of makes they could get?
#    Plot the distribution of outcomes.
