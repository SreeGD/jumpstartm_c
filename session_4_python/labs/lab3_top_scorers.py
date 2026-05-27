# Lab 3 — Top Scorers Chart
# Session 4: Lists, Sorting, Bar Charts
#
# Concepts: lists, dicts, sorted(), zip(), matplotlib bar charts
# Run: python lab3_top_scorers.py
#
# ADVAITH: Change the data to YOUR favourite players before running!

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ─────────────────────────────────────────
# PART 1: Your Data — Edit This!
# ─────────────────────────────────────────

# ⚽ SOCCER — Top scorers (change these to your picks!)
soccer_players = ['Haaland',  'Mbappe',   'Vini Jr',  'Kane',    'Salah']
soccer_goals   = [27,          24,          22,          21,        19]
soccer_assists = [5,           8,           11,          14,         12]

# 🏀 BASKETBALL — Top scorers (change these to your picks!)
bball_players  = ['Luka',      'SGA',       'Embiid',   'Giannis',  'LeBron']
bball_ppg      = [33.9,        30.1,        34.7,        30.4,       25.7]
bball_apg      = [9.8,         6.2,         5.6,         5.6,        8.3]


# ─────────────────────────────────────────
# PART 2: Soccer — Goals and Assists
# ─────────────────────────────────────────

fig, axes = plt.subplots(1, 2, figsize=(14, 6))
fig.patch.set_facecolor('#0f0f1a')

# Sort by goals (descending)
soccer_data = sorted(zip(soccer_goals, soccer_assists, soccer_players), reverse=True)
goals_sorted, assists_sorted, players_sorted = zip(*soccer_data)

ax1 = axes[0]
ax1.set_facecolor('#0f0f1a')

x = range(len(players_sorted))
width = 0.35

bars1 = ax1.bar([i - width/2 for i in x], goals_sorted,   width, label='Goals',   color='#e94560')
bars2 = ax1.bar([i + width/2 for i in x], assists_sorted, width, label='Assists', color='#00d4aa')

# Add value labels on bars
for bar in bars1:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(int(bar.get_height())), ha='center', va='bottom',
             color='white', fontsize=9, fontweight='bold')
for bar in bars2:
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
             str(int(bar.get_height())), ha='center', va='bottom',
             color='white', fontsize=9, fontweight='bold')

ax1.set_xticks(list(x))
ax1.set_xticklabels(players_sorted, color='white', fontsize=10)
ax1.set_ylabel('Count', color='white')
ax1.set_title('⚽ Top Scorers 2023-24', color='white', fontsize=13, fontweight='bold')
ax1.legend(facecolor='#1a1a2e', labelcolor='white')
ax1.tick_params(colors='white')
ax1.spines[:].set_color('#333')
ax1.set_facecolor('#1a1a2e')

# Highlight the top scorer
bars1[0].set_edgecolor('gold')
bars1[0].set_linewidth(2)


# ─────────────────────────────────────────
# PART 3: Basketball — PPG vs APG
# ─────────────────────────────────────────

ax2 = axes[1]
ax2.set_facecolor('#1a1a2e')

# Sort by PPG
bball_data = sorted(zip(bball_ppg, bball_apg, bball_players), reverse=True)
ppg_sorted, apg_sorted, bball_sorted = zip(*bball_data)

scatter = ax2.scatter(ppg_sorted, apg_sorted,
                      s=200, c=ppg_sorted,
                      cmap='RdYlGn', edgecolors='white', linewidth=1.5, zorder=5)

# Label each point
for ppg, apg, name in zip(ppg_sorted, apg_sorted, bball_sorted):
    ax2.annotate(name, (ppg, apg),
                 textcoords="offset points", xytext=(8, 4),
                 color='white', fontsize=9)

ax2.set_xlabel('Points Per Game (PPG)', color='white')
ax2.set_ylabel('Assists Per Game (APG)', color='white')
ax2.set_title('🏀 Scorer vs Playmaker Balance', color='white', fontsize=13, fontweight='bold')
ax2.tick_params(colors='white')
ax2.spines[:].set_color('#333')
ax2.set_facecolor('#1a1a2e')

plt.colorbar(scatter, ax=ax2, label='PPG').ax.yaxis.label.set_color('white')

plt.tight_layout()
plt.savefig('top_scorers.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
plt.show()

print("Chart saved as top_scorers.png — send it to your friends!")


# ─────────────────────────────────────────
# PART 4: Quick Stats Analysis
# ─────────────────────────────────────────

print("\n=== Soccer Analysis ===")
print(f"Top scorer:       {soccer_players[soccer_goals.index(max(soccer_goals))]} ({max(soccer_goals)} goals)")
print(f"Top assister:     {soccer_players[soccer_assists.index(max(soccer_assists))]} ({max(soccer_assists)} assists)")
combined = [g + a for g, a in zip(soccer_goals, soccer_assists)]
print(f"Best combined:    {soccer_players[combined.index(max(combined))]} ({max(combined)} G+A)")
print(f"Average goals:    {sum(soccer_goals)/len(soccer_goals):.1f}")

print("\n=== Basketball Analysis ===")
print(f"Top scorer:       {bball_players[bball_ppg.index(max(bball_ppg))]} ({max(bball_ppg)} PPG)")
print(f"Best playmaker:   {bball_players[bball_apg.index(max(bball_apg))]} ({max(bball_apg)} APG)")
