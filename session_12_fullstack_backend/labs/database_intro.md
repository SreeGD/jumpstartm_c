# Databases: SQL vs NoSQL
## A conceptual guide using sports examples

---

## What is a database, really?

A database is a program whose entire purpose is to store data reliably and let you retrieve it quickly.

"Reliably" means: even if the server crashes, the power goes out, or 10,000 people write data at the same moment, nothing is lost or corrupted.

"Quickly" means: even with 100 million rows, a good query returns in milliseconds.

Without a database, every app would lose all its data when the server restarts — exactly like the in-memory list in `sports_api.py`. Databases solve this.

---

## Part 1 — SQL Databases (Relational)

### The core idea: tables with relationships

A relational database organizes data into **tables** (like spreadsheets). Each table represents one type of thing. The tables relate to each other through keys.

### Example: A sports stats database

**players table**

| id | name | team_id | position | jersey_number |
|----|------|---------|----------|---------------|
| 1 | LeBron James | 3 | Forward | 23 |
| 2 | Stephen Curry | 7 | Guard | 30 |
| 3 | Lionel Messi | 12 | Forward | 10 |
| 4 | Kylian Mbappe | 15 | Forward | 7 |

**teams table**

| id | name | city | sport | founded |
|----|------|------|-------|---------|
| 3 | Lakers | Los Angeles | basketball | 1947 |
| 7 | Warriors | San Francisco | basketball | 1946 |
| 12 | Inter Miami | Miami | soccer | 2018 |
| 15 | Real Madrid | Madrid | soccer | 1902 |

**seasons table**

| id | player_id | year | games | points | assists | goals |
|----|-----------|------|-------|--------|---------|-------|
| 1 | 1 | 2024 | 71 | 25.7 | 7.3 | null |
| 2 | 2 | 2024 | 74 | 29.4 | 6.1 | null |
| 3 | 3 | 2024 | 19 | null | null | 11 |
| 4 | 4 | 2024 | 35 | null | null | 32 |

Notice:
- `players.team_id` references `teams.id` — this is a **foreign key**
- `seasons.player_id` references `players.id` — another foreign key
- basketball rows have `null` for `goals`; soccer rows have `null` for `points`

### SQL queries on this database

**"Find all basketball players":**
```sql
SELECT players.name, teams.name AS team_name
FROM players
JOIN teams ON players.team_id = teams.id
WHERE teams.sport = 'basketball';
```
Result:
```
name            | team_name
----------------|----------
LeBron James    | Lakers
Stephen Curry   | Warriors
```

**"Find Messi's goal stats for 2024":**
```sql
SELECT players.name, seasons.year, seasons.goals
FROM players
JOIN seasons ON players.id = seasons.player_id
WHERE players.name = 'Lionel Messi'
  AND seasons.year = 2024;
```
Result:
```
name          | year | goals
--------------|------|------
Lionel Messi  | 2024 | 11
```

**"Top 3 scorers in basketball, 2024":**
```sql
SELECT players.name, teams.name AS team, seasons.points
FROM players
JOIN teams   ON players.team_id    = teams.id
JOIN seasons ON players.id         = seasons.player_id
WHERE teams.sport = 'basketball'
  AND seasons.year = 2024
ORDER BY seasons.points DESC
LIMIT 3;
```

**"Which team has the highest combined points per game?":**
```sql
SELECT teams.name, SUM(seasons.points) AS total_points
FROM teams
JOIN players ON teams.id         = players.team_id
JOIN seasons ON players.id       = seasons.player_id
WHERE teams.sport = 'basketball'
  AND seasons.year = 2024
GROUP BY teams.name
ORDER BY total_points DESC;
```

This kind of query — aggregating across multiple tables — is where SQL shines. It would take 20+ lines of Python to do what SQL does in 8 lines.

### Popular SQL databases

| Database | Where it's used | Key strength |
|----------|----------------|--------------|
| PostgreSQL | Instagram, Reddit, Dropbox | Most feature-rich; great for complex queries |
| MySQL | WordPress, Twitter (early), Facebook (early) | Fast reads; massive adoption |
| SQLite | Mobile apps, browser storage | Zero setup; the entire database is a file |

---

## Part 2 — NoSQL Databases

### Why SQL sometimes isn't enough

SQL databases are built around the **ACID** guarantee:
- **Atomic:** a transaction either fully completes or fully fails (no partial writes)
- **Consistent:** data always follows the rules you defined
- **Isolated:** two transactions don't interfere with each other
- **Durable:** once committed, data survives crashes

These guarantees are powerful — but they require coordination. When you write to a SQL database, it locks the relevant rows, writes to disk, confirms. This takes time.

At Twitter's scale — 500 million tweets per day, 330 million users — a single SQL database would become a bottleneck. The coordination required for ACID guarantees across billions of rows and thousands of simultaneous writes is too slow.

NoSQL databases make different trade-offs: they relax some ACID guarantees in exchange for speed, scale, or schema flexibility.

---

### Type 1 — Document Databases (MongoDB)

Instead of tables and rows, MongoDB stores **documents** — objects that look like JSON.

**A player document in MongoDB:**
```json
{
  "_id": "player_lebron_001",
  "name": "LeBron James",
  "team": "Lakers",
  "position": "Forward",
  "stats": {
    "2024": {"games": 71, "points": 25.7, "assists": 7.3, "rebounds": 7.5},
    "2023": {"games": 55, "points": 28.9, "assists": 6.8, "rebounds": 8.3},
    "2022": {"games": 56, "points": 30.3, "assists": 6.2, "rebounds": 8.2}
  },
  "awards": ["2016 NBA Finals MVP", "4× NBA Champion", "4× NBA MVP"],
  "social": {
    "instagram_followers": 159000000,
    "twitter_followers": 52800000
  }
}
```

Notice what's different from SQL:
- **Nested data:** `stats` is a nested object, not a separate table
- **Arrays:** `awards` is a list — no join table needed
- **Variable structure:** one player could have 10 awards, another could have 2 — MongoDB handles both without schema changes

**MongoDB query to find the top scorer:**
```javascript
db.players.find(
  { "sport": "basketball" },
  { name: 1, "stats.2024.points": 1 }
).sort({ "stats.2024.points": -1 }).limit(1)
```

**When to use MongoDB:**
- Content management (articles, blog posts with varying fields)
- User profiles with optional attributes
- Product catalogs (a shoe has different attributes than a laptop)
- Any data where the structure varies between records

**When MongoDB is the wrong choice:**
- When you need complex joins across many entities
- When data integrity constraints are critical (banking, medical records)
- When you need strong ACID guarantees

---

### Type 2 — Key-Value Stores (Redis)

Redis is a database in RAM. It's not a replacement for PostgreSQL — it's a cache layer in front of it.

**The concept:** store the most frequently accessed data in memory so you never have to hit the database for it.

Think of it this way: your PostgreSQL database is like a library — incredibly comprehensive, but it takes time to find a book. Redis is like the books currently on your desk — you grabbed them already, they're right there, access is instant.

**Sports app examples:**

```
# Cache a player's stats (expires after 1 hour)
SET player:1:stats '{"points": 25.7, "assists": 7.3}'
EXPIRE player:1:stats 3600

# Read it back (microseconds)
GET player:1:stats

# Cache today's top scorer (update every 5 minutes)
SET leaderboard:top_scorer "Stephen Curry"
EXPIRE leaderboard:top_scorer 300

# Store a live game score (update in real time)
SET game:lakers_vs_warriors:score "108-104"
```

**Real performance numbers:**
- PostgreSQL query (with index): ~1–5 milliseconds
- Redis GET: ~0.1 milliseconds (10–50× faster)

For a page that loads 20 pieces of data, Redis can cut load time from 100ms to 2ms.

**Instagram's use of Redis:**
- Cached follower counts (updated when someone follows/unfollows)
- Recent activity feed items (top 20 notifications)
- Session tokens (fast lookup, auto-expire when you log out)

**When Redis is the right tool:**
- Caching frequently read, rarely changed data
- Session storage (user login state)
- Rate limiting (counting API requests per user per minute)
- Real-time leaderboards (Redis has a sorted set data structure perfect for this)
- Pub/sub messaging (notify all clients when a score changes)

---

### Type 3 — Wide-Column Databases (Cassandra)

Cassandra was designed by Facebook to solve one specific problem: storing and querying enormous amounts of write-heavy data that is distributed across many servers worldwide.

**The sports analogy:**

Imagine logging every single action every user takes in your sports app:
- User 4821 viewed player 7's profile at 14:32:01
- User 4821 clicked "stats" at 14:32:03
- User 4821 added player 7 to their watchlist at 14:32:05
- User 9023 opened the leaderboard at 14:32:01
- ...millions of these per second

In PostgreSQL, this volume of writes would overwhelm a single server. Cassandra distributes data across many servers automatically. If three data centers go offline, Cassandra keeps serving data from the remaining ones — it's designed for this.

**Cassandra schema for user activity:**
```
user_id   | event_time          | event_type    | player_id
----------|---------------------|---------------|----------
4821      | 2024-01-15 14:32:01 | view_profile  | 7
4821      | 2024-01-15 14:32:03 | click_stats   | 7
4821      | 2024-01-15 14:32:05 | add_watchlist | 7
9023      | 2024-01-15 14:32:01 | view_board    | null
```

**Who uses Cassandra:**
- Netflix: viewing history for 230 million users
- Discord: trillions of stored messages
- Instagram: activity feed ("X liked your photo" notifications)

**When Cassandra is the right tool:**
- Massive write volume (millions of writes per second)
- Time-series data (activity logs, sensor readings, financial ticks)
- When you need multi-region replication with no single point of failure
- When queries are simple (no complex joins needed)

---

## Part 3 — Choosing the Right Database

The question is never "which database is best?" It's "which database is best for this specific problem?"

| Scenario | Best choice | Why |
|----------|-------------|-----|
| Player profiles with stats history | PostgreSQL | Complex queries, joins, strong consistency |
| Real-time leaderboard updates | Redis | Sub-millisecond reads, sorted sets built-in |
| Live game event log (1M events/hour) | Cassandra | Built for massive write throughput |
| Player profile with variable attributes | MongoDB | Flexible schema, no migration needed |
| User session (login token) | Redis | Fast lookup, auto-expiry |
| Financial transactions (ticket sales) | PostgreSQL | ACID guarantees are essential |
| Search (find players by name) | Elasticsearch | Optimized for full-text search |

### The Instagram architecture, explained

Instagram doesn't use one database. It uses all of them:

```
User taps "Like" on a post
        │
        ├─→ PostgreSQL: update like count for the post
        │   (source of truth; ACID-compliant)
        │
        ├─→ Redis: increment cached like count by 1
        │   (what you actually see on screen; fast)
        │
        ├─→ Cassandra: append activity event
        │   ("@user liked your photo" notification)
        │   (append-only; massive write volume)
        │
        └─→ Elasticsearch: index the activity
            (so users can search their notification history)
```

Each database does what it's best at. The app orchestrates them.

---

## Summary

| | SQL (PostgreSQL) | Document (MongoDB) | Cache (Redis) | Wide-column (Cassandra) |
|--|------------------|--------------------|---------------|-------------------------|
| **Data model** | Tables + rows | JSON documents | Key-value pairs | Rows + column families |
| **Schema** | Fixed, defined upfront | Flexible, per document | None | Semi-flexible |
| **Strengths** | Complex queries, joins, ACID | Flexible structure, nesting | Speed (RAM), expiry | Write scale, availability |
| **Weaknesses** | Harder to scale writes | Weak for complex joins | Data lost on restart (without persistence) | Limited query patterns |
| **Sports use case** | Player stats, team records | Player profiles, news articles | Live scores, leaderboards | Activity feeds, event logs |
| **Companies** | Instagram, Reddit | EA Games, eBay | Instagram, Twitter | Netflix, Discord |

**The rule:** Start with PostgreSQL. Add Redis when reads are too slow. Add Cassandra when writes are too slow. Add MongoDB when your schema changes too often.

Most apps that aren't at massive scale only ever need PostgreSQL + Redis. That's enough to run a multi-million user app.
