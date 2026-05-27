# Capstone Lab — Sports Oracle Starter (Track D)
# Session 8: Capstone
#
# This is a SKELETON — not a finished project.
# Student fills in the functions using what he learned in Sessions 4, 5, 6.
#
# Prerequisites: pip install matplotlib numpy pandas anthropic
# Run: python sports_dashboard_starter.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import anthropic

# ─────────────────────────────────────────
# THE DATA — Teacher provides this
# Student can also find his own data online:
# https://fbref.com (football)
# https://www.basketball-reference.com
# ─────────────────────────────────────────

SOCCER_DATA = {
    'player':   ['Haaland',  'Mbappe',  'Vini Jr', 'Kane',   'Salah',  'Bellingham', 'Saka',   'Olmo'],
    'team':     ['Man City', 'PSG',     'Real Mad','Bayern', 'Liverpool','Real Mad', 'Arsenal','Barcelona'],
    'goals':    [27,          24,         22,        21,       19,        19,          16,        14],
    'assists':  [5,           8,          11,        14,       12,        12,          14,         7],
    'xg':       [24.3,        20.1,       18.3,      20.8,     16.2,      14.5,        12.8,      11.3],
    'minutes':  [2850,        2700,       2650,      2900,     2800,      2750,        2600,      2100],
}

BASKETBALL_DATA = {
    'player':   ['Luka',     'SGA',     'Embiid',  'Giannis', 'LeBron', 'Jokic',    'Booker',  'KD'],
    'team':     ['Mavs',     'OKC',     '76ers',   'Bucks',   'Lakers', 'Nuggets',  'Suns',    'Suns'],
    'ppg':      [33.9,        30.1,      34.7,      30.4,      25.7,     26.4,       27.1,      26.6],
    'apg':      [9.8,         6.2,       5.6,       5.6,       8.3,     13.0,        4.5,       3.9],
    'rpg':      [9.2,         5.5,       11.8,      12.0,      7.3,     12.4,         4.5,      6.4],
}


# ─────────────────────────────────────────
# FUNCTION 1: Load the data
# Student: turn the dictionaries above into DataFrames
# ─────────────────────────────────────────

def load_data(sport: str) -> pd.DataFrame:
    """
    Load player data for 'soccer' or 'basketball'
    Returns a pandas DataFrame

    TODO: Student fills this in
    Hint: pd.DataFrame(SOCCER_DATA) or pd.DataFrame(BASKETBALL_DATA)
    """
    if sport == 'soccer':
        pass  # Replace with your code
    elif sport == 'basketball':
        pass  # Replace with your code
    else:
        raise ValueError(f"Unknown sport: {sport}")


# ─────────────────────────────────────────
# FUNCTION 2: Compute interesting stats
# Student: add computed columns to the DataFrame
# ─────────────────────────────────────────

def compute_stats(df: pd.DataFrame, sport: str) -> pd.DataFrame:
    """
    Add computed columns to the DataFrame.

    For soccer: add 'goal_contributions' (goals + assists),
                'goals_per_90' (goals / minutes * 90),
                'xg_diff' (goals - xg)  ← over/under-performing

    For basketball: add 'efficiency' (ppg + rpg + apg)

    TODO: Student fills this in
    """
    if sport == 'soccer':
        pass  # Replace with your code
    elif sport == 'basketball':
        pass  # Replace with your code
    return df


# ─────────────────────────────────────────
# FUNCTION 3: Plot the dashboard
# Student: create 2 charts per sport (4 total)
# Use code from Session 4 labs as reference
# ─────────────────────────────────────────

def plot_soccer_dashboard(df: pd.DataFrame):
    """
    Create 2 soccer charts:
    Chart 1: Goals vs Assists bar chart (like lab3_top_scorers.py)
    Chart 2: Scatter plot of Goals vs xG (who is over/under-performing?)

    TODO: Student fills this in
    Hint: copy from lab3_top_scorers.py and modify
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#0f0f1a')

    # Chart 1: Bar chart — your code here

    # Chart 2: Scatter — your code here

    plt.suptitle('⚽ Soccer Dashboard', color='white', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('soccer_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
    plt.show()


def plot_basketball_dashboard(df: pd.DataFrame):
    """
    Create 2 basketball charts:
    Chart 1: PPG bar chart sorted by score
    Chart 2: PPG vs APG scatter (scorer vs playmaker)

    TODO: Student fills this in
    """
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))
    fig.patch.set_facecolor('#0f0f1a')

    # Your code here

    plt.suptitle('🏀 Basketball Dashboard', color='white', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig('basketball_dashboard.png', dpi=150, bbox_inches='tight', facecolor='#0f0f1a')
    plt.show()


# ─────────────────────────────────────────
# FUNCTION 4: AI Commentary
# Student: use skills from Session 6
# ─────────────────────────────────────────

def ai_commentary(df: pd.DataFrame, sport: str) -> str:
    """
    Feed the stats to Claude and ask for 3 insights.
    Use the system prompt and API call from Session 6.

    TODO: Student fills this in
    Hint: Convert df to a string with df.to_string()
         Then pass it to the Claude API like in sports_analyst.py
    """
    client = anthropic.Anthropic()

    # Convert data to text
    stats_text = df.to_string()

    # Your API call here
    pass


# ─────────────────────────────────────────
# MAIN — runs everything
# ─────────────────────────────────────────

def main():
    print("🏆 Sports Oracle — Capstone Project\n")

    for sport in ['soccer', 'basketball']:
        print(f"\n{'='*40}")
        print(f"  {sport.upper()} ANALYSIS")
        print(f"{'='*40}")

        # Load and compute
        df = load_data(sport)
        if df is None:
            print(f"  ⚠️  load_data('{sport}') not implemented yet")
            continue

        df = compute_stats(df, sport)
        print(df.to_string(index=False))

        # Plot
        if sport == 'soccer':
            plot_soccer_dashboard(df)
        else:
            plot_basketball_dashboard(df)

        # AI commentary
        commentary = ai_commentary(df, sport)
        if commentary:
            print(f"\n🤖 AI Analyst says:\n{commentary}")
        else:
            print("\n  ⚠️  ai_commentary() not implemented yet")


if __name__ == "__main__":
    main()


# ─────────────────────────────────────────
# HINTS IF STUCK
# ─────────────────────────────────────────
# load_data:     pd.DataFrame(SOCCER_DATA)
# goal_contributions: df['goals'] + df['assists']
# goals_per_90:  df['goals'] / df['minutes'] * 90
# xg_diff:       df['goals'] - df['xg']
# Charts:        copy from session_4_python/labs/lab3_top_scorers.py
# AI call:       copy from session_6_agentic_ai/labs/sports_analyst.py
