# Session 12 — Assignment
## Full Stack Development: The Backend Layer

**Before starting:** Make sure `sports_api.py` runs without errors and you can reach `http://localhost:5000/players` in your browser.

---

## Task 1 — Add a DELETE Endpoint

Extend `sports_api.py` with a new endpoint:

```
DELETE /players/<player_id>
```

**Requirements:**
- If the player exists, remove them from `PLAYERS` and return `200 OK` with a confirmation message:  
  `{"message": "Player 3 deleted"}`
- If no player with that ID exists, return `404 Not Found` with:  
  `{"error": "Player with id 3 not found"}`

**Test your endpoint** with curl (run in a terminal):
```bash
# Delete player 6
curl -X DELETE http://localhost:5000/players/6

# Try to delete them again (should get 404)
curl -X DELETE http://localhost:5000/players/6

# Verify they're gone from the list
curl http://localhost:5000/players
```

Write 2–3 sentences explaining: why does `DELETE /players/6` make more sense as a URL design than `POST /delete-player?id=6`?

---

## Task 2 — Add Input Validation to POST /players

The current `POST /players` already checks for missing required fields. Make it more robust:

1. **Type validation:** If `points` is provided but is not a number (e.g., `"points": "twenty-five"`), return `400 Bad Request` with `{"error": "points must be a number"}`.

2. **Range validation:** If `points` is negative, return `400 Bad Request` with `{"error": "points cannot be negative"}`.

3. **Name validation:** If `name` is an empty string `""`, return `400 Bad Request` with `{"error": "name cannot be empty"}`.

**Test your validation:**
```bash
# Missing required field
curl -X POST http://localhost:5000/players \
  -H "Content-Type: application/json" \
  -d '{"name": "Test Player", "team": "Test Team", "sport": "basketball"}'
# Expected: 400 + missing fields error

# Points not a number
curl -X POST http://localhost:5000/players \
  -H "Content-Type: application/json" \
  -d '{"name": "Test", "team": "Test", "points": "lots", "sport": "basketball"}'
# Expected: 400 + type error

# Valid player (should succeed)
curl -X POST http://localhost:5000/players \
  -H "Content-Type: application/json" \
  -d '{"name": "Kevin Durant", "team": "Suns", "points": 27.1, "assists": 4.5, "sport": "basketball"}'
# Expected: 201 + new player with id 7
```

---

## Task 3 — Add a Team Stats Endpoint

Add the following endpoint:

```
GET /stats/team/<team_name>
```

**Requirements:**
- Return all players who play for the specified team (case-insensitive matching — `"lakers"` and `"Lakers"` both work)
- Include a `count` field and an `average_points` field in the response
- If no players are found for that team, return `404 Not Found` with `{"error": "No players found for team 'Unknown FC'"}`

**Expected response format:**
```json
{
  "team": "Lakers",
  "count": 1,
  "average_points": 25.7,
  "players": [
    {"id": 1, "name": "LeBron James", "team": "Lakers", "points": 25.7, "...": "..."}
  ]
}
```

**Test:**
```bash
curl http://localhost:5000/stats/team/Lakers
curl http://localhost:5000/stats/team/warriors    # lowercase -- should still work
curl http://localhost:5000/stats/team/FakeTeam    # should return 404
```

---

## Task 4 — Connect Session 11 to This API

This is where the full stack comes together.

**Setup:** Make sure `sports_api.py` is running in one terminal window. Open a separate window for your HTML work.

Create a new file called `sports_dashboard.html`. It should:

1. **On page load**, call `fetch('http://localhost:5000/players')` and display all players in a table or card layout — no hardcoded data.

2. **Include a sport filter.** Two buttons: "Basketball" and "Soccer". Clicking either calls `fetch('http://localhost:5000/players?sport=basketball')` (or soccer) and updates the display — without reloading the page.

3. **Include a leaderboard section** that calls `fetch('http://localhost:5000/stats/top')` and displays the top 3 scorers with their names, teams, and points.

4. **Add a form** with fields for Name, Team, Points, and Sport. Submitting the form should call `fetch` with `method: 'POST'` to add the new player, then refresh the player list.

**Starter pattern for the fetch call — build each player card using DOM methods:**
```javascript
fetch('http://localhost:5000/players')
  .then(response => response.json())
  .then(players => {
    const container = document.getElementById('player-list');
    container.textContent = '';  // clear existing content
    players.forEach(player => {
      const card = document.createElement('div');
      card.className = 'player-card';

      const name = document.createElement('strong');
      name.textContent = player.name;

      const info = document.createElement('span');
      info.textContent = ' — ' + player.team + ' — ' + player.points + ' pts';

      card.appendChild(name);
      card.appendChild(info);
      container.appendChild(card);
    });
  })
  .catch(error => console.error('API error:', error));
```

**Note:** If your browser shows a CORS error (something about "Access-Control-Allow-Origin"), install flask-cors and add two lines to `sports_api.py`:
```python
# At the top of the file
from flask_cors import CORS

# Right after: app = Flask(__name__)
CORS(app)
```
Install it with: `pip install flask-cors`

**Deliverable:** A working HTML page that shows live data from your Flask API. Take a screenshot or screen recording showing the page loading data and the filter buttons working.

---

## Task 5 — The Scale Design Question

This is the kind of question asked in engineering interviews at Google, Meta, and Stripe.

> **Scenario:** Your sports stats API gets featured on a major sports news site. Suddenly 1,000,000 users are hitting `GET /players` every minute — simultaneously.

Answer these questions in your own words. Each answer should be 3–5 sentences.

**5a. What breaks first in the current `sports_api.py` setup?**  
Think about: a single Python process, no caching, the in-memory list being read by millions of concurrent requests. What is the bottleneck?

**5b. What is the first fix you'd make?**  
Hint: most of those 1 million requests are reading the same data. Do they all need to hit the server?

**5c. What is a load balancer and how would it help here?**  
If you ran 10 copies of `sports_api.py` on 10 different servers, how would a user's request reach the right one?

**5d. If you replaced the in-memory list with a real database (PostgreSQL), what new bottleneck might appear?**  
Consider: the database is now handling 1 million queries per minute. What strategy reduces the number of queries that hit the database?

**5e. Design sketch:** Draw (on paper or digitally) the architecture of a `sports_api` that could handle 1 million users. Include: user, CDN, load balancer, multiple API servers, Redis cache, PostgreSQL database. Label the arrows with what flows between each layer.

---

## Bring to Next Session

- `sports_api.py` with all four tasks implemented (DELETE endpoint, validation, team stats)
- `sports_dashboard.html` with live API data
- Written answers to Task 5 (scale design question)
- Architecture sketch from Task 5e
- One question you have about anything from this session

---

## Stretch Goal (Optional)

If you finish early and want to go further:

Add **pagination** to `GET /players`. Large APIs never return all records at once — they return pages.

Design the endpoint so it supports:
```
GET /players?page=1&per_page=2    -- players 1-2
GET /players?page=2&per_page=2    -- players 3-4
GET /players?page=3&per_page=2    -- players 5-6
```

The response should include:
```json
{
  "players": ["..."],
  "total": 6,
  "page": 1,
  "per_page": 2,
  "total_pages": 3
}
```

Pagination is used by every real API. GitHub's API, Spotify's API, Twitter's API — all of them paginate results. You've now built the same pattern.
