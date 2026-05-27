# Lab — The xG (Expected Goals) Model
# Session 5: Math & Stats for AI
#
# Concepts: scatter plots, intuitive logistic regression,
#           probability, data patterns
# Run: python xg_model.py

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# ─────────────────────────────────────────
# PART 1: The Shot Data
# Each row: [distance_from_goal_m, angle_degrees, is_goal]
# ─────────────────────────────────────────

# Real-ish shot data from a Premier League season
shots = np.array([
    # Very close, central → high xG
    [3.5,  12, 1], [4.0,  20, 1], [4.5,  15, 1], [5.0,  18, 1],
    [5.5,  25, 1], [4.2,  30, 0], [6.0,  10, 1], [5.8,  22, 0],
    # Medium range, decent angle
    [8.0,  20, 1], [9.0,  25, 1], [10.0, 22, 0], [11.0, 18, 1],
    [10.5, 30, 0], [9.5,  15, 1], [8.5,  35, 0], [12.0, 20, 0],
    # Medium range, tight angle
    [10.0,  8, 0], [12.0,  5, 0], [8.0,   7, 1], [15.0,  6, 0],
    # Long range
    [20.0, 15, 0], [22.0, 18, 0], [25.0, 20, 0], [18.0, 12, 1],
    [20.0, 25, 0], [23.0, 22, 0], [19.0, 10, 0], [21.0, 15, 0],
    # Long range, headers from corners
    [7.0,  40, 0], [8.0,  45, 1], [6.0,  50, 0], [9.0,  42, 0],
    # Penalties
    [11.0, 90, 1], [11.0, 90, 1], [11.0, 90, 1], [11.0, 90, 0],
])

distances = shots[:, 0]
angles    = shots[:, 1]
goals     = shots[:, 2]


# ─────────────────────────────────────────
# PART 2: Visualise the Data
# ─────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('#0f0f1a')

# Plot 1: Distance vs outcome
ax1 = axes[0]
ax1.set_facecolor('#1a1a2e')

goals_mask   = goals == 1
no_goal_mask = goals == 0

ax1.scatter(distances[goals_mask],   np.random.uniform(0.9, 1.1, goals_mask.sum()),
            color='#00d4aa', s=80, alpha=0.7, label='Goal ⚽', zorder=5)
ax1.scatter(distances[no_goal_mask], np.random.uniform(-0.1, 0.1, no_goal_mask.sum()),
            color='#e94560', s=60, alpha=0.5, label='No Goal', zorder=5)

ax1.set_xlabel('Distance from goal (metres)', color='white')
ax1.set_ylabel('Outcome (1=Goal, 0=No Goal)', color='white')
ax1.set_title('Closer = More Likely to Score', color='white', fontsize=12, fontweight='bold')
ax1.legend(facecolor='#0f0f1a', labelcolor='white')
ax1.tick_params(colors='white')
ax1.spines[:].set_color('#333')
ax1.set_yticks([0, 1])
ax1.set_yticklabels(['No Goal', 'Goal'], color='white')


# Plot 2: Distance vs Angle — coloured by outcome
ax2 = axes[1]
ax2.set_facecolor('#1a1a2e')

ax2.scatter(distances[no_goal_mask], angles[no_goal_mask],
            color='#e94560', s=60, alpha=0.6, label='No Goal', zorder=5)
ax2.scatter(distances[goals_mask], angles[goals_mask],
            color='#00d4aa', s=100, alpha=0.9, label='Goal ⚽', zorder=6,
            marker='*')

ax2.set_xlabel('Distance from goal (metres)', color='white')
ax2.set_ylabel('Shot angle (degrees from centre)', color='white')
ax2.set_title('Distance + Angle = xG Pattern', color='white', fontsize=12, fontweight='bold')
ax2.legend(facecolor='#0f0f1a', labelcolor='white')
ax2.tick_params(colors='white')
ax2.spines[:].set_color('#333')

plt.tight_layout()
plt.savefig('xg_scatter.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
plt.show()


# ─────────────────────────────────────────
# PART 3: Simple xG Rule (Intuitive Model)
# Build a MANUAL xG estimator — no ML library
# ─────────────────────────────────────────

def estimate_xg(distance, angle):
    """
    A simple hand-crafted xG model.
    Real xG models use logistic regression on thousands of shots.
    This gives the right intuition.
    """
    # Base probability — decreases with distance
    base_prob = max(0, 1 - distance / 35)

    # Angle bonus — wider angle = harder shot
    angle_factor = angle / 90   # normalise to 0-1

    # Combine: closer AND better angle = higher xG
    xg = base_prob * (0.4 + 0.6 * angle_factor)

    # Penalty is special (11m, straight on = 76% historically)
    if distance == 11 and angle >= 85:
        xg = 0.76

    return min(xg, 0.99)


# Test our model on famous shots
print("=== xG Estimates ===")
famous_shots = [
    ("Penalty (11m, central)",         11, 88),
    ("Close range tap-in (4m)",         4, 20),
    ("Mbappe vs Argentina 2018 (22m)",  22, 15),
    ("Gerrard long shot (30m)",         30, 20),
    ("Salah one-on-one (8m)",           8, 25),
    ("Header from corner (7m)",         7, 42),
    ("Haaland header (6m)",             6, 15),
]

for name, dist, ang in famous_shots:
    xg = estimate_xg(dist, ang)
    difficulty = "Easy" if xg > 0.5 else "Difficult" if xg < 0.15 else "Moderate"
    print(f"{name:<35} xG = {xg:.2f}  ({difficulty})")


# ─────────────────────────────────────────
# PART 4: Team xG Analysis
# ─────────────────────────────────────────

print("\n=== Team Shot Analysis ===")
total_xg = sum(estimate_xg(d, a) for d, a in zip(distances, angles))
actual_goals = int(sum(goals))

print(f"Total shots analysed:  {len(shots)}")
print(f"Actual goals scored:   {actual_goals}")
print(f"Total xG:              {total_xg:.1f}")
print(f"Goals vs xG:           {actual_goals - total_xg:+.1f}")

if actual_goals > total_xg:
    print("→ Team is over-performing xG (lucky or clinical finishers)")
else:
    print("→ Team is under-performing xG (wasteful or unlucky)")


# ─────────────────────────────────────────
# DISCUSSION QUESTIONS
# ─────────────────────────────────────────
# 1. What would the xG model say about Mbappe's goal vs Argentina?
#    Why was it so impressive?
#
# 2. If a team's xG for the season is 50 but they've scored 65 goals,
#    what does that tell you? Is it sustainable?
#
# 3. What other features would improve the xG model?
#    (Hint: game state, foot vs head, assisted vs solo, keeper position)
