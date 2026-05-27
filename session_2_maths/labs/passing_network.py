# Lab — Football Passing Network
# Session 2: Graph Theory in Action
#
# Concepts: graphs, nodes, edges, centrality
# Library needed: pip install networkx matplotlib
#
# Instructions for Teacher:
#   This lab requires networkx. Install it beforehand.
#   Run Part 1 first to show the concept, then Part 2 for the visual.

import networkx as nx
import matplotlib.pyplot as plt

# ─────────────────────────────────────────
# PART 1: Build the Graph
# ─────────────────────────────────────────
# Each tuple: (passer, receiver, number_of_passes)
# Based loosely on a classic Barcelona passing game

passes = [
    ('Ter Stegen', 'Pique',      8),
    ('Pique',      'Busquets',   12),
    ('Busquets',   'Xavi',       18),
    ('Xavi',       'Iniesta',    15),
    ('Iniesta',    'Messi',      14),
    ('Messi',      'Suarez',     10),
    ('Suarez',     'Messi',       8),
    ('Xavi',       'Messi',      12),
    ('Iniesta',    'Xavi',       11),
    ('Busquets',   'Pique',       9),
    ('Pique',      'Xavi',        7),
    ('Messi',      'Iniesta',     9),
    ('Xavi',       'Busquets',   10),
    ('Alba',       'Xavi',        6),
    ('Alba',       'Iniesta',     5),
]

# Create a directed graph (passes have direction)
G = nx.DiGraph()
for passer, receiver, count in passes:
    G.add_edge(passer, receiver, weight=count)

print("=== Barcelona Passing Network ===")
print(f"Players (nodes): {G.number_of_nodes()}")
print(f"Pass connections (edges): {G.number_of_edges()}")


# ─────────────────────────────────────────
# PART 2: Who Is the Most Important Player?
# Use betweenness centrality
# ─────────────────────────────────────────
# Betweenness centrality: how many shortest paths
# between other players pass THROUGH this player?
# High centrality = team plays through you

centrality = nx.betweenness_centrality(G)

print("\n=== Player Centrality (Importance) ===")
ranked = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
for player, score in ranked:
    bar = "█" * int(score * 50)
    print(f"{player:<15} {bar} ({score:.3f})")

print(f"\n🎯 Most central player: {ranked[0][0]}")
print(f"   This player controls the flow of play.")


# ─────────────────────────────────────────
# PART 3: Visualise the Network
# ─────────────────────────────────────────

fig, ax = plt.subplots(1, 1, figsize=(12, 8))
fig.patch.set_facecolor('#0f0f1a')
ax.set_facecolor('#0f0f1a')

# Layout — spring layout spaces nodes naturally
pos = nx.spring_layout(G, seed=42, k=2)

# Edge thickness = number of passes
edge_weights = [G[u][v]['weight'] / 4 for u, v in G.edges()]
# Node size = centrality score
node_sizes = [3000 * centrality[node] + 500 for node in G.nodes()]
# Node colour — highlight the most central player
node_colours = ['#e94560' if node == ranked[0][0] else '#00d4aa'
                for node in G.nodes()]

# Draw the network
nx.draw_networkx_edges(G, pos, width=edge_weights,
                       edge_color='#ffffff', alpha=0.4,
                       arrows=True, arrowsize=15, ax=ax)

nx.draw_networkx_nodes(G, pos, node_size=node_sizes,
                       node_color=node_colours, ax=ax)

nx.draw_networkx_labels(G, pos, font_color='white',
                        font_size=9, font_weight='bold', ax=ax)

ax.set_title("Barcelona Passing Network\nRed = Most Central Player",
             color='white', fontsize=14, pad=20)
ax.axis('off')

plt.tight_layout()
plt.savefig('barcelona_passing_network.png', dpi=150,
            bbox_inches='tight', facecolor='#0f0f1a')
plt.show()

print("\nChart saved as 'barcelona_passing_network.png'")


# ─────────────────────────────────────────
# DISCUSSION QUESTIONS
# ─────────────────────────────────────────
# 1. Who came out as most central? Does that match your intuition?
# 2. What would happen to Barcelona's game if Xavi was injured?
#    (Remove him from the graph and re-run centrality)
# 3. How is this graph similar to Google's PageRank algorithm?
#    (PageRank is betweenness centrality on the web's link graph)
