"""
Session 10 — Instagram Simulator
Build a tiny version of the Instagram feed algorithm in Python.

Run: python3 instagram_simulator.py
No libraries needed beyond Python standard library.
"""

import random
import time

# ── 1. Simulate a user's Instagram data ─────────────────────────

# Advaith's interaction history (0–10 score)
user_profile = {
    "football_page":      {"past_likes": 9, "watch_time": 8, "dm_frequency": 2},
    "nba_highlights":     {"past_likes": 8, "watch_time": 9, "dm_frequency": 1},
    "cricket_india":      {"past_likes": 5, "watch_time": 4, "dm_frequency": 0},
    "meme_account":       {"past_likes": 7, "watch_time": 6, "dm_frequency": 0},
    "tech_news":          {"past_likes": 4, "watch_time": 3, "dm_frequency": 0},
    "close_friend_1":     {"past_likes": 6, "watch_time": 5, "dm_frequency": 9},
    "close_friend_2":     {"past_likes": 5, "watch_time": 4, "dm_frequency": 8},
    "celebrity_account":  {"past_likes": 3, "watch_time": 7, "dm_frequency": 0},
}

# Posts available in the feed (not yet ranked)
raw_posts = [
    {"id": 1,  "from": "football_page",    "age_minutes": 5,   "global_likes": 1200},
    {"id": 2,  "from": "nba_highlights",   "age_minutes": 30,  "global_likes": 800},
    {"id": 3,  "from": "cricket_india",    "age_minutes": 10,  "global_likes": 3000},
    {"id": 4,  "from": "meme_account",     "age_minutes": 120, "global_likes": 5000},
    {"id": 5,  "from": "tech_news",        "age_minutes": 15,  "global_likes": 400},
    {"id": 6,  "from": "close_friend_1",   "age_minutes": 2,   "global_likes": 45},
    {"id": 7,  "from": "close_friend_2",   "age_minutes": 8,   "global_likes": 12},
    {"id": 8,  "from": "celebrity_account","age_minutes": 60,  "global_likes": 980000},
]


# ── 2. The Ranking Algorithm ─────────────────────────────────────

def rank_post(post, user):
    """
    Score a post for this user. Higher = shown first.

    Real Instagram uses 100s of signals and a neural network.
    We use 4 signals + weighted average to keep it teachable.
    """
    account = post["from"]
    history = user.get(account, {"past_likes": 1, "watch_time": 1, "dm_frequency": 0})

    # Signal 1 — Interest (how much has Advaith liked this account before?)
    interest_score = history["past_likes"] / 10.0  # normalise to 0–1

    # Signal 2 — Relationship (DM frequency = close friend?)
    relationship_score = min(history["dm_frequency"] / 10.0, 1.0)

    # Signal 3 — Recency (fresher posts score higher, with decay)
    recency_score = max(0, 1 - (post["age_minutes"] / 200))

    # Signal 4 — Popularity (viral posts get a small boost, but not too much)
    popularity_score = min(post["global_likes"] / 100000, 0.5)

    # Weighted combination (these weights are what ML training adjusts)
    score = (
        interest_score    * 0.40 +   # Interest matters most
        relationship_score * 0.30 +  # Close friends second
        recency_score      * 0.20 +  # Freshness matters
        popularity_score   * 0.10    # Viral posts get small boost
    )

    return round(score, 3)


# ── 3. Build the Feed ────────────────────────────────────────────

def build_feed(posts, user):
    """Score every post, sort by score descending."""
    scored = []
    for post in posts:
        score = rank_post(post, user)
        scored.append({**post, "score": score})
    scored.sort(key=lambda p: p["score"], reverse=True)
    return scored


# ── 4. CDN Simulation ────────────────────────────────────────────

CDN_NODES = {
    "Mumbai":     10,   # ms latency
    "Singapore":  35,
    "Frankfurt":  120,
    "California": 180,
}

def fetch_from_cdn(post_id):
    """Simulate fetching a post from the nearest CDN node."""
    nearest = min(CDN_NODES, key=CDN_NODES.get)
    latency = CDN_NODES[nearest] + random.randint(0, 10)
    print(f"  📡  Post #{post_id} → CDN node: {nearest} ({latency}ms)")
    return latency


# ── 5. Run the Simulation ────────────────────────────────────────

def main():
    print("=" * 55)
    print("  INSTAGRAM FEED SIMULATOR")
    print("  Session 10 — How Instagram Works")
    print("=" * 55)
    print()

    # Step 1: Build the ranked feed
    print("⚙️   STEP 1: Ranking algorithm running...")
    print(f"    {len(raw_posts)} posts in candidate pool\n")

    feed = build_feed(raw_posts, user_profile)

    # Step 2: Show the ranked feed
    print("📱  YOUR FEED (ranked by algorithm):\n")
    print(f"  {'#':<3} {'Account':<22} {'Score':<8} {'Age':<12} {'Reason'}")
    print("  " + "-" * 65)

    for i, post in enumerate(feed):
        account = post["from"]
        history = user_profile.get(account, {})

        # Explain why this post ranks here
        if history.get("dm_frequency", 0) >= 5:
            reason = "close friend"
        elif history.get("past_likes", 0) >= 7:
            reason = "high interest"
        elif post["age_minutes"] <= 10:
            reason = "very fresh"
        elif post["global_likes"] > 100000:
            reason = "viral"
        else:
            reason = "moderate match"

        print(f"  {i+1:<3} {account:<22} {post['score']:<8} "
              f"{post['age_minutes']}min ago  ← {reason}")

    # Step 3: Simulate loading 3 posts from CDN
    print(f"\n📡  STEP 2: Loading top 3 posts from CDN...\n")
    total_latency = 0
    for post in feed[:3]:
        latency = fetch_from_cdn(post["id"])
        total_latency += latency
    print(f"\n  Total load time for 3 posts: {total_latency}ms")

    # Step 4: Simulate an action (like) and explain what happens
    print("\n❤️   STEP 3: Advaith double-taps post #1...")
    top_post = feed[0]
    print(f"\n  What Instagram does in background:")
    print(f"  → Write 'LIKE' to PostgreSQL database")
    print(f"  → Increment like counter in Redis cache (fast!)")
    print(f"  → Send notification to '{top_post['from']}'")
    print(f"  → Update Advaith's interest model: '{top_post['from']}' ↑")
    print(f"  → Log event for ML training pipeline")
    print(f"  All of this happens in < 50ms")

    # Step 5: Show what changes if Advaith posts
    print("\n📤  STEP 4: Advaith posts a photo...")
    print(f"\n  Journey of your photo:")
    steps = [
        ("Phone → API Gateway",      "HTTP POST with JPEG + caption"),
        ("API Gateway → Media Service", "Validates file, checks file type"),
        ("Media Service → Image Processor", "Creates 4 versions (thumbnail, 640, 1080, story)"),
        ("Image Processor → S3",     "Stores all 4 versions permanently"),
        ("S3 → CDN",                 "Distributes to 200+ edge nodes worldwide"),
        ("Media Service → Database", "Writes post metadata to PostgreSQL"),
        ("Notification Service",     f"Queues notifications for all followers"),
    ]
    for step, detail in steps:
        print(f"  → {step}")
        print(f"       {detail}")
    print(f"\n  Total: < 2 seconds from tap to friends seeing it")

    print("\n" + "=" * 55)
    print("  🎓  KEY TAKEAWAYS")
    print("=" * 55)
    print("""
  1. Your feed is ranked — not chronological. Every post
     gets a score from a machine learning model.

  2. Photos live in S3 (permanent storage) but are served
     from CDNs close to you (fast delivery).

  3. Instagram is not one program — it's dozens of services
     talking to each other via APIs.

  4. Every action you take is training data for the ML model
     that decides what you see next.

  5. Redis caching is why Instagram feels instant — hot data
     lives in memory, not on disk.
""")
    print("Try it: Change the 'past_likes' for 'close_friend_1'")
    print("to 1. Does the feed change? Why?\n")


if __name__ == "__main__":
    main()
