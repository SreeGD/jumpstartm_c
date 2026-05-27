# Session 12 — Full Stack Development: The Backend Layer
## What happens on the server

**Duration:** 2–3 hours  
**Teacher's prep:** `pip install flask`. Have `sports_api.py` ready to run. Test it before the session: `python3 sports_api.py`, then open `http://localhost:5000/players` in a browser — you should see JSON.

---

## 🎯 Goal

By the end of this session, the student can:
- Explain what a server does and why APIs exist
- Read and modify a working Flask REST API
- Understand the difference between SQL and NoSQL databases
- Explain JWT authentication at a conceptual level
- Describe the full request journey from browser to database and back

---

## 📖 Teacher's Narrative

### Hook

> "When you search 'Messi career goals' on Google, in 50 milliseconds, a server somewhere retrieved that number from a database of billions of facts and sent it back. Let's build that."

Ask the student: **What do you think is happening between when you press Enter and when you see the result?**

Let them guess. They'll probably say "it searches the web." Dig deeper:
- Where does the number actually live? (A database, not a webpage)
- Who runs the computer that stores it? (Google's data centers)
- How does it arrive on your screen? (HTTP, JSON, rendering)

Then make it real: "In the next two hours, you're going to build a server that answers questions about sports stats. Same idea, one ten-thousandth of the scale."

---

### Part 1: What is a Server?

**The plain English version:** A server is just a program that sits and waits. When a request arrives, it wakes up, does some work, and sends a response. Then it goes back to waiting.

That's it. There's no magic.

**The request-response cycle — step by step:**

```
Your browser (or app)
    │
    │  HTTP Request: GET /players?team=Lakers
    ▼
Server (our Flask app)
    │
    │  Looks up data
    ▼
Database (or in-memory list)
    │
    │  Returns rows
    ▼
Server formats it as JSON
    │
    ▼
HTTP Response: 200 OK + JSON body
    │
    ▼
Your browser renders it
```

**Key insight:** The same Python you already know runs on servers. Flask, Django, and FastAPI are all Python frameworks that make it easier to build servers. Instagram's first backend was Python + Flask. So was Pinterest's.

**A server vs. a client:**
- **Client:** makes requests (your browser, a mobile app, a Python script using `requests`)
- **Server:** receives requests and responds (Flask app, Django app, Node.js app)
- The same machine can be both. When your Flask app calls an external API, it's acting as a client.

**Ask the student:** "When you open Spotify on your phone, is your phone a client or a server?" (Client — it requests songs from Spotify's servers.)

**Follow-up:** "What about when you share a playlist and your friend opens it?" (Still client — both phones are clients, Spotify's servers handle everything.)

---

### Part 2: Building an API with Python Flask

**What is an API?**

API stands for Application Programming Interface. It's a contract: "Send me a request in this format, and I'll send back a response in this format."

When ESPN's website shows live scores, it's calling an API. When your phone's weather app shows rain tomorrow, it called an API. APIs are how different software systems talk to each other.

**REST APIs** follow conventions:
- Use HTTP methods to express intent: GET (read), POST (create), PUT (update), DELETE (remove)
- Use URLs to identify resources: `/players`, `/players/23`, `/teams/lakers`
- Send and receive data as JSON

**The minimal Flask app — 5 lines:**

```python
from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, world!"

app.run()
```

That's a server. Run it, visit `http://localhost:5000/hello`, and you get a response.

**Explain each line:**
- `Flask(__name__)` — creates the app; `__name__` tells Flask where it lives
- `@app.route('/hello')` — this is a **decorator**; it registers the function as a handler for `/hello`
- `return "Hello, world!"` — whatever the function returns becomes the HTTP response
- `app.run()` — starts the server and begins listening for requests

**Returning JSON:**

Real APIs return JSON, not plain text. Flask has a built-in helper:

```python
from flask import Flask, jsonify

@app.route('/players')
def get_players():
    players = [{"name": "LeBron James", "points": 25.7}]
    return jsonify(players)
```

`jsonify()` converts a Python list or dict into a JSON response with the correct Content-Type header.

**Path parameters** — putting variables in the URL:

```python
@app.route('/players/<int:player_id>')
def get_player(player_id):
    # player_id is automatically an integer because of <int:...>
    return jsonify({"id": player_id, "name": "LeBron James"})
```

Visit `/players/1` → gets player with ID 1. Visit `/players/23` → gets player 23.

**Query parameters** — optional filters at the end of a URL:

```python
from flask import request

@app.route('/players')
def get_players():
    team = request.args.get('team')   # Gets ?team=lakers from URL
    if team:
        # filter players by team
        pass
```

Visit `/players` → all players. Visit `/players?team=Lakers` → only Lakers players.

**Now open `sports_api.py`** and walk through it together. Point out:
- The in-memory "database" (a Python list of dicts)
- Each of the four route handlers
- How filters are applied with list comprehensions
- The 404 response when a player isn't found
- The POST handler that reads JSON from the request body

**Run it together:**
```bash
python3 sports_api.py
```
Then test in the browser:
- `http://localhost:5000/players`
- `http://localhost:5000/players?sport=basketball`
- `http://localhost:5000/players/1`
- `http://localhost:5000/stats/top`

**Bonus if time permits:** Show how to test the POST endpoint using `curl`:
```bash
curl -X POST http://localhost:5000/players \
  -H "Content-Type: application/json" \
  -d '{"name": "Giannis Antetokounmpo", "team": "Bucks", "points": 29.9, "assists": 5.8, "sport": "basketball"}'
```

---

### Part 3: Databases — Where Data Lives

**Every app has a database.** The Flask lab uses a Python list in memory — that's fine for learning, but when the server restarts, all data is gone. Real apps use databases that persist to disk.

**Some databases you've already heard of:**
- **Instagram:** PostgreSQL (main data) + Cassandra (activity feeds) + Redis (cache)
- **Netflix:** Cassandra (viewing history for 230M users)
- **Google:** Bigtable (Google literally invented distributed databases — their 2006 paper changed the industry)
- **Twitter/X:** MySQL + Manhattan (their own distributed key-value store)

**The relational model — it's just a spreadsheet with superpowers:**

Imagine a spreadsheet for players:

| id | name | team | points | sport |
|----|------|------|--------|-------|
| 1 | LeBron James | Lakers | 25.7 | basketball |
| 2 | Stephen Curry | Warriors | 29.4 | basketball |
| 3 | Lionel Messi | Inter Miami | 0.8 | soccer |

Each row is a **record**. Each column is a **field**. The whole sheet is a **table**.

**Primary key:** `id` — a unique identifier for each row. No two players share the same ID. This is how you find exactly one record.

**Foreign key:** Imagine a separate `teams` table. A player's `team_id` column would be a foreign key — it references the `id` in the `teams` table. This is how tables relate to each other (hence "relational database").

```
players table          teams table
──────────────         ────────────
id  name     team_id   id  name      city
1   LeBron   3    ──►  3   Lakers    Los Angeles
2   Curry    7    ──►  7   Warriors  San Francisco
```

**Why not just store everything in one table?** Because data gets duplicated. If the Lakers move cities, you'd have to update every single player row. With foreign keys, you update one row in `teams` and every player row automatically reflects it.

---

### Part 4: SQL — The Language of Data

SQL (Structured Query Language) is 50 years old and still the most important query language in the world. Every major tech company uses it somewhere. It reads almost like English.

**SELECT — read data:**
```sql
SELECT name, points
FROM players
WHERE sport = 'basketball';
```
"Give me the name and points of all basketball players."

**ORDER BY — sort results:**
```sql
SELECT name, points
FROM players
WHERE sport = 'basketball'
ORDER BY points DESC;
```
"...sorted by points, highest first."

**LIMIT — cap results:**
```sql
SELECT name, points
FROM players
ORDER BY points DESC
LIMIT 3;
```
"...just the top 3 scorers."

**WHERE with conditions:**
```sql
SELECT name, team, points
FROM players
WHERE sport = 'basketball'
  AND points > 25;
```
"Basketball players who average more than 25 points per game."

**INSERT — add a record:**
```sql
INSERT INTO players (name, team, points, sport)
VALUES ('Kevin Durant', 'Suns', 27.1, 'basketball');
```

**UPDATE — change a record:**
```sql
UPDATE players
SET points = 26.3
WHERE name = 'LeBron James';
```

**DELETE — remove a record:**
```sql
DELETE FROM players
WHERE id = 5;
```

**JOIN — connect two tables:**
```sql
SELECT players.name, teams.city
FROM players
JOIN teams ON players.team_id = teams.id
WHERE teams.city = 'Los Angeles';
```
"Give me the names of players whose team is in Los Angeles."

**Ask the student:** "Write a SQL query to find all soccer players with more than 15 goals, sorted by goals." Let them attempt it before showing the answer:
```sql
SELECT name, goals
FROM players
WHERE sport = 'soccer'
  AND goals > 15
ORDER BY goals DESC;
```

**Key insight:** SQL lets you ask complex questions about millions of rows in milliseconds. A well-indexed database query that would take hours to write in Python takes one line of SQL.

---

### Part 5: NoSQL — When SQL Isn't Enough

SQL works brilliantly for structured data with clear relationships. But some problems are different:

- **Twitter:** 500 million tweets per day. Every tweet needs to appear in the feeds of all followers — simultaneously. A single SQL database would collapse.
- **Instagram:** 100 billion photos. The metadata (who liked what, when) updates constantly for 2 billion users.
- **Online games:** Player positions update 60 times per second. There's no time for disk writes.

These problems need a different approach.

**NoSQL** doesn't mean "no SQL ever." It means "not only SQL" — a family of databases optimized for different use cases.

**MongoDB — Document databases:**
Instead of rows in tables, MongoDB stores **documents** (like JSON objects):
```json
{
  "_id": "player_001",
  "name": "LeBron James",
  "stats": {
    "points": 25.7,
    "assists": 7.3,
    "rebounds": 7.5
  },
  "career_highlights": ["2016 NBA Finals MVP", "4× NBA Champion"],
  "teams": ["Cavaliers", "Heat", "Cavaliers", "Lakers"]
}
```
Notice: no fixed columns. One player can have 3 career highlights, another can have 10. The schema is flexible. Great for content that varies in structure.

**Redis — Key-value cache:**
Redis is like a dictionary in RAM. Extremely fast (microseconds), but limited:
```
SET player:1:name "LeBron James"    → OK
GET player:1:name                   → "LeBron James"
SET player:1:points 25.7            → OK
EXPIRE player:1:points 3600         → expires in 1 hour
```
Instagram uses Redis to cache the follower counts you see on profiles. The real number lives in PostgreSQL, but reading it from PostgreSQL for every page load would be too slow. Redis serves it in microseconds.

**Cassandra — Wide-column database:**
Designed to handle massive write volume across many servers. Netflix uses Cassandra for viewing history. Even if three data centers go down simultaneously, Cassandra keeps serving data (it's designed for this). Instagram uses it for activity feeds — "X liked your photo" — because the write volume is enormous and the reads are simple.

**The rule of thumb:**
> Use SQL (PostgreSQL, MySQL) for structured data you need to query in complex ways.  
> Use NoSQL when you need massive scale, flexible structure, or millisecond read/write performance.

Most real applications use both. That's why Instagram runs PostgreSQL + Cassandra + Redis simultaneously — each database does what it's best at.

---

### Part 6: Authentication

**The problem:** How does the server know who you are?

HTTP has no memory. Every request is a blank slate — the server doesn't know if you've been using the app for years or if this is your first visit. Something needs to carry your identity with each request.

**Passwords + hashing:**

When you create an account, the server never stores your actual password. It stores a **hash** — the output of a one-way function:

```
"mypassword123" → bcrypt → "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW"
```

A hash is irreversible — you can't go from the hash back to the password. When you log in, the server hashes what you typed and compares the hashes. If they match, you're in.

**Why not just store passwords?** Because databases get hacked. If Instagram's database leaked and passwords were stored in plain text, every user's password — and every other site they reuse it on — would be exposed. Hashing means the attacker gets useless strings.

**JWT — JSON Web Tokens:**

After you log in, the server issues a **token** — a small signed string you carry with every subsequent request. Think of it like a wristband at a concert: you prove your identity once (at the door), get a wristband, and then the staff just checks the wristband.

A JWT looks like this (split into 3 parts by dots):
```
eyJhbGciOiJIUzI1NiJ9.eyJ1c2VySWQiOjQyLCJleHAiOjE3MDAwMDAwMDB9.xK3GjR8k9PlMnLv4JXrG_Pg0LDv4B_eFd3Kz8nVl
```

The three parts are Base64-encoded:
1. **Header:** algorithm used (`{"alg": "HS256"}`)
2. **Payload:** the data (`{"userId": 42, "exp": 1700000000}`)
3. **Signature:** cryptographic proof it hasn't been tampered with

The server signs the token with a secret key. Anyone can read the payload, but only the server can create a valid signature. If an attacker modifies the payload (to change `userId` to someone else's), the signature breaks and the server rejects it.

**The login flow:**
```
1. POST /login  { email: "...", password: "..." }
2. Server: hash(entered_password) == stored_hash? → YES
3. Server: issue JWT containing { userId: 42, exp: tomorrow }
4. Client: stores JWT (in browser localStorage or phone storage)
5. All future requests: include JWT in header:
   Authorization: Bearer eyJhbGciO...
6. Server: verify signature → extract userId → serve their data
```

**OAuth — "Login with Google":**

OAuth solves a different problem: what if you don't want to build your own login system? Instead, you trust Google (or Apple, or GitHub) to verify identity.

The flow: "I want to log in to SportsApp → SportsApp redirects me to Google → I prove to Google who I am → Google tells SportsApp 'yes, this is sreenivas@gmail.com' → SportsApp creates a session."

You never give SportsApp your Google password. Google handles authentication; SportsApp handles authorization (what you can do once authenticated).

---

### Part 7: The Full Stack — Connecting Front to Back

This is the session where everything from Sessions 1–11 connects.

**The complete request journey:**

```
User types URL or taps a button
        │
        ▼
  DNS Lookup
  (domain → IP address)
        │
        ▼
    CDN Edge Server
  (static files served here:
   HTML, CSS, JS, images)
        │
        ▼
  Load Balancer
  (distributes traffic across
   many API server instances)
        │
        ▼
    API Server
  (Flask / Django / FastAPI —
   Python running your code)
        │
        ├─────────────────────────┐
        ▼                         ▼
  Primary Database           Cache (Redis)
  (PostgreSQL / MySQL)       (check here first —
  (source of truth)           100× faster reads)
        │                         │
        └──────────┬──────────────┘
                   ▼
         Build JSON response
                   │
                   ▼
         Send back through
         load balancer → CDN
                   │
                   ▼
         Browser receives JSON
                   │
                   ▼
         JavaScript renders HTML
         (React, vanilla JS, etc.)
```

**This is Instagram.** Every time you open it:
- Your phone hits a CDN for the app shell
- An API call hits a load balancer
- Dozens of microservices activate: feed ranking, ad targeting, story loading
- PostgreSQL serves your follow graph
- Cassandra serves your activity feed
- Redis serves cached follower counts
- S3 serves photos via CDN nodes near you

**This is Google.** Same pattern, 10,000× the scale.

**The "full stack" developer** understands every layer in this diagram — not necessarily expert in all of them, but comfortable working anywhere in it.

**Session 11** covered the left side of this picture: HTML, CSS, JavaScript, fetch(). **This session** covered the right side: Flask, databases, authentication. Put them together and you have an app.

---

## ⚡ Wow Moment

Run `sports_api.py`. Then, in a separate file (or in the browser console), run this JavaScript:

```javascript
fetch('http://localhost:5000/players')
  .then(r => r.json())
  .then(players => {
    players.forEach(p => console.log(p.name, '-', p.points, 'pts'));
  });
```

Watch data that lives in a Python file on your computer appear in JavaScript. That's a full-stack application in 5 lines. The Session 11 HTML lab was one half. The Session 12 Flask API is the other half. Together: a working app.

---

## 🔑 Key Concepts Checklist

- [ ] **HTTP methods:** GET, POST, PUT, DELETE — and when to use each
- [ ] **REST API:** URL identifies a resource; method expresses the action
- [ ] **Flask route decorator:** `@app.route('/path', methods=['GET'])`
- [ ] **Path parameter:** `/players/<int:player_id>` — part of the URL
- [ ] **Query parameter:** `/players?team=lakers` — after the `?`
- [ ] **jsonify():** converts Python dict/list to JSON response
- [ ] **Status codes:** 200 (OK), 201 (Created), 400 (Bad Request), 404 (Not Found), 500 (Server Error)
- [ ] **Database:** persistent storage for structured data
- [ ] **Primary key:** unique identifier for each row
- [ ] **Foreign key:** reference to a row in another table
- [ ] **SQL SELECT / WHERE / ORDER BY / JOIN** — what each does
- [ ] **SQL vs NoSQL:** SQL for structured+relational, NoSQL for scale/flexibility
- [ ] **Redis:** in-memory key-value cache; extremely fast; data can expire
- [ ] **MongoDB:** document database; flexible schema; JSON-like storage
- [ ] **Cassandra:** wide-column; built for massive write volume; never goes down
- [ ] **Password hashing:** server never stores plaintext passwords
- [ ] **JWT:** signed token that proves identity; payload is readable, signature prevents tampering
- [ ] **OAuth:** delegate authentication to a trusted provider (Google, Apple)
- [ ] **Full stack request journey:** browser → DNS → CDN → load balancer → API → database/cache → response

---

## Teaching Notes for Teacher

**Pace guidance:**
- Parts 1–2 (server + Flask): 40–50 min. This is hands-on — get the code running early.
- Parts 3–4 (databases + SQL): 25–30 min. Use the whiteboard for the table diagram.
- Parts 5–6 (NoSQL + auth): 20–25 min. These are conceptual — no code needed.
- Part 7 (full stack): 10–15 min. Draw the diagram slowly. Let it sink in.

**Common student confusions:**
- "What's the difference between a path parameter and a query parameter?" — Path parameter is part of the resource identity (`/players/23` means player 23). Query parameter is a filter on a collection (`/players?team=lakers`).
- "Why does the server return 404?" — 404 means "I understood your request, but the thing you asked for doesn't exist." 400 means "your request doesn't make sense." 500 means "I understood and tried, but I broke."
- "Why can't I just put the database password in the code?" — Show them: if this code ever goes on GitHub, everyone in the world can see it. Environment variables are the standard solution.

**If the student finishes early:**
- Have them open Postman (free download) and test all four endpoints
- Ask them to add a 5th endpoint: `GET /stats/sport/<sport>` returning average points per sport
- Show them how to add `flask-cors` and why it's needed when the HTML lab calls the Flask API

**Real-world grounding:**
- Flask is what Instagram started with. FastAPI (which we use in production Python) is the modern version.
- Every endpoint in the lab corresponds to a real REST API pattern used by companies worldwide.
- The in-memory list is a teaching simplification. In production, replace it with `psycopg2` calls to PostgreSQL — the rest of the code barely changes.

---

## 🧪 Quiz

**1.** What does a server do when it's not handling a request?

a) It shuts down to save power  
b) It waits (listens) for incoming connections  
c) It queries the database to stay warm  
d) It sends requests to other servers  

**Answer:** b

---

**2.** In Flask, what does the `@app.route('/players')` decorator do?

a) Creates a new database table called "players"  
b) Registers the function below it as the handler for `GET /players`  
c) Imports the players data from a JSON file  
d) Sets the URL of the server to `/players`  

**Answer:** b

---

**3.** A request comes in as `GET /players/7`. Which Flask route would handle it?

a) `@app.route('/players')`  
b) `@app.route('/players/<string:name>')`  
c) `@app.route('/players/<int:player_id>')`  
d) `@app.route('/players/7')`  

**Answer:** c

---

**4.** What HTTP status code should a server return when it successfully creates a new resource (like adding a new player)?

a) 200  
b) 201  
c) 204  
d) 404  

**Answer:** b — 201 Created is the standard response for successful POST requests

---

**5.** Which SQL query finds all basketball players with more than 20 points per game, sorted highest first?

a) `SELECT * FROM players WHERE sport = 'basketball' AND points > 20 ORDER BY points ASC`  
b) `SELECT * FROM players WHERE points > 20 AND sport = 'basketball' ORDER BY points DESC`  
c) `FIND players WHERE sport = 'basketball' SORT BY points`  
d) `GET players WHERE sport = 'basketball' AND points > 20`  

**Answer:** b

---

**6.** Instagram stores 100 billion photos. Why does Instagram use a CDN (Content Delivery Network) to serve them?

a) CDNs are cheaper than storing photos directly  
b) CDNs compress photos to save storage space  
c) CDNs serve files from servers near the user, reducing load time from 300ms to 20ms  
d) CDNs encrypt photos to protect user privacy  

**Answer:** c

---

**7.** You're building a sports app. A player's profile page shows their follower count. This count changes every few seconds. What's the best database strategy?

a) Query PostgreSQL every time the page loads  
b) Store the count in Redis with a 60-second expiry; fall back to PostgreSQL on cache miss  
c) Use Cassandra for the follower count because it's a NoSQL database  
d) Hard-code the count and update it manually every day  

**Answer:** b — Redis cache dramatically reduces database load for frequently-read, slightly-stale-tolerant data

---

**8.** A JWT token is sent with every API request. What makes it secure — why can't an attacker just change the `userId` field inside it?

a) The token is encrypted so no one can read it  
b) The token is stored on the server and the client only has a reference  
c) The token contains a cryptographic signature; modifying the payload invalidates the signature  
d) The token expires after 5 seconds so there's no time to modify it  

**Answer:** c

---

## 📚 Research Materials

**Flask:**
- Flask official quickstart: https://flask.palletsprojects.com/en/latest/quickstart/
- "What is a REST API?" — Red Hat explainer: https://www.redhat.com/en/topics/api/what-is-a-rest-api
- HTTP status codes reference: https://developer.mozilla.org/en-US/docs/Web/HTTP/Status

**Databases:**
- "PostgreSQL vs MySQL vs SQLite — what's the difference?" — search this phrase for good blog comparisons
- The original Google Bigtable paper (2006) — search "Bigtable: A Distributed Storage System for Structured Data"
- "How Instagram stores data" — Instagram Engineering blog: https://instagram-engineering.com/

**SQL:**
- SQLZoo interactive SQL tutorial: https://sqlzoo.net — students can practice SQL queries in the browser
- "Learn SQL in 10 minutes" — search YouTube for this; there are excellent short tutorials

**NoSQL:**
- MongoDB University free courses: https://university.mongodb.com
- "NoSQL Databases Explained" — MongoDB: https://www.mongodb.com/nosql-explained
- Redis documentation (start with the "Introduction to Redis" page): https://redis.io/docs/

**Authentication:**
- "JWT.io" — paste any JWT token here to decode and inspect it: https://jwt.io
- "How does OAuth 2.0 work?" — search for Okta's explainer (clear diagrams)
- "How to store passwords safely in 2024" — any recent blog post on bcrypt/Argon2

**Going deeper:**
- "The Architecture of Instagram" — High Scalability blog: http://highscalability.com/blog/2022/1/11/designing-instagram.html
- "System Design Interview" by Alex Xu — a book used by engineers preparing for Google/Meta interviews; Chapter 1 is accessible and relevant
- FastAPI documentation (the production-grade Python API framework): https://fastapi.tiangolo.com/
