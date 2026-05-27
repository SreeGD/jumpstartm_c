# Sports Stats API
# ─────────────────────────────────────────────────────────────
# A complete REST API built with Flask.
# This is the same pattern used by real apps — just at a
# smaller scale and with an in-memory list instead of a database.
#
# Run:  python3 sports_api.py
# Test: open http://localhost:5000/players in your browser
#
# Requires: pip install flask
# ─────────────────────────────────────────────────────────────

from flask import Flask, jsonify, request

app = Flask(__name__)

# ── In-memory "database" ──────────────────────────────────────
# In a real app this would be PostgreSQL or MySQL.
# We use a Python list so you can focus on the API structure,
# not on database setup. All data resets when the server restarts.

PLAYERS = [
    {"id": 1, "name": "LeBron James",   "team": "Lakers",    "points": 25.7, "assists": 7.3, "sport": "basketball"},
    {"id": 2, "name": "Stephen Curry",  "team": "Warriors",  "points": 29.4, "assists": 6.1, "sport": "basketball"},
    {"id": 3, "name": "Giannis Antetokounmpo", "team": "Bucks", "points": 30.4, "assists": 5.7, "sport": "basketball"},
    {"id": 4, "name": "Lionel Messi",   "team": "Inter Miami", "points": 0.0, "assists": 0.9, "sport": "soccer"},
    {"id": 5, "name": "Kylian Mbappe",  "team": "Real Madrid", "points": 0.0, "assists": 0.7, "sport": "soccer"},
    {"id": 6, "name": "Erling Haaland", "team": "Man City",  "points": 0.0, "assists": 0.3, "sport": "soccer"},
]

# We use this to assign IDs to newly added players.
_next_id = 7


# ── Endpoint 1: GET /players ──────────────────────────────────
# Returns all players. Supports optional filters:
#   ?sport=basketball    → only basketball players
#   ?min_points=25       → only players averaging 25+ points
#
# Examples:
#   GET /players
#   GET /players?sport=soccer
#   GET /players?sport=basketball&min_points=28

@app.route('/players', methods=['GET'])
def get_players():
    results = PLAYERS  # start with all players

    # Filter by sport if the ?sport= query param is present
    sport = request.args.get('sport')
    if sport:
        results = [p for p in results if p['sport'].lower() == sport.lower()]

    # Filter by minimum points if ?min_points= is present
    min_points = request.args.get('min_points')
    if min_points:
        try:
            threshold = float(min_points)
            results = [p for p in results if p['points'] >= threshold]
        except ValueError:
            # If ?min_points=abc (not a number), return a helpful error
            return jsonify({"error": "min_points must be a number"}), 400

    return jsonify(results), 200


# ── Endpoint 2: GET /players/<player_id> ─────────────────────
# Returns a single player by their numeric ID.
# Returns 404 if no player with that ID exists.
#
# Examples:
#   GET /players/1    → LeBron James
#   GET /players/99   → 404 Not Found

@app.route('/players/<int:player_id>', methods=['GET'])
def get_player(player_id):
    # Search the list for a matching ID
    player = next((p for p in PLAYERS if p['id'] == player_id), None)

    if player is None:
        return jsonify({"error": f"Player with id {player_id} not found"}), 404

    return jsonify(player), 200


# ── Endpoint 3: POST /players ─────────────────────────────────
# Adds a new player. Expects a JSON body with at minimum:
#   name, team, points, sport
# assists is optional (defaults to 0.0).
#
# Returns 201 Created with the new player (including its assigned ID).
#
# Example request body:
#   {"name": "Kevin Durant", "team": "Suns", "points": 27.1,
#    "assists": 4.5, "sport": "basketball"}

@app.route('/players', methods=['POST'])
def add_player():
    global _next_id

    data = request.get_json()

    # Validate: request body must be JSON
    if data is None:
        return jsonify({"error": "Request body must be JSON"}), 400

    # Validate: required fields
    required = ['name', 'team', 'points', 'sport']
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": f"Missing required fields: {missing}"}), 400

    # Build the new player record
    new_player = {
        "id":      _next_id,
        "name":    data['name'],
        "team":    data['team'],
        "points":  float(data['points']),
        "assists": float(data.get('assists', 0.0)),  # optional field
        "sport":   data['sport'],
    }

    PLAYERS.append(new_player)
    _next_id += 1

    # 201 Created is the correct status code for a successful resource creation
    return jsonify(new_player), 201


# ── Endpoint 4: GET /stats/top ────────────────────────────────
# Returns the top 3 scorers across all sports, sorted by points.
# Useful for a leaderboard or "Players to Watch" widget.
#
# Example:
#   GET /stats/top

@app.route('/stats/top', methods=['GET'])
def get_top_scorers():
    # Sort all players by points descending, take the first 3
    top_three = sorted(PLAYERS, key=lambda p: p['points'], reverse=True)[:3]
    return jsonify(top_three), 200


# ── Run the server ────────────────────────────────────────────
if __name__ == '__main__':
    print("Sports Stats API is running!")
    print("Try these URLs in your browser:")
    print("  http://localhost:5000/players")
    print("  http://localhost:5000/players?sport=basketball")
    print("  http://localhost:5000/players?sport=basketball&min_points=28")
    print("  http://localhost:5000/players/1")
    print("  http://localhost:5000/stats/top")
    print("\nPress Ctrl+C to stop the server.\n")

    # debug=True means:
    #   - the server restarts automatically when you save changes
    #   - detailed error messages appear in the browser
    # Never use debug=True in production.
    app.run(debug=True)
