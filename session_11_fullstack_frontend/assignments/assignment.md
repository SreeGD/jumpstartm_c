# Session 11 — Assignment
## Full Stack Development: The Frontend Layer

**Start from:** `labs/sports_frontend.html` — make a copy called `sports_dashboard_v2.html` and do all tasks in the copy.

**Rule:** No frameworks. No npm. No build tools. Open the file directly in a browser. Every task is achievable with the HTML, CSS, and JavaScript you learned today.

---

## Task 1 — Sort by Assists

The lab dashboard has a "Sort by Points" button. Add a second button: **"Sort by Assists"**.

When clicked, it should reorder the player stats table so that the player with the most assists appears at the top (descending order).

**What to do:**
1. Add a `<button id="sort-ast-btn">Sort by Assists</button>` in the `.controls` div
2. Add a JavaScript `addEventListener` for this button (below the existing sort-by-points listener)
3. Sort the players array by the `ast` property (descending), then call `renderTable()`

**You know you've done it correctly when:** clicking "Sort by Assists" shows D'Angelo Russell at the top (9 assists), and clicking "Sort by Points" re-orders back to Anthony Davis at the top (31 points).

**Hint:** The sort logic is identical to the existing button — just swap `b.pts - a.pts` for `b.ast - a.ast`.

---

## Task 2 — Live Player Search

Add a text input above the table that filters the rows in real time as you type.

When the user types "le", only "LeBron James" should appear. When they clear the input, all players return.

**What to do:**
1. Add `<input type="text" id="player-search" placeholder="Search players...">` in the `.controls` div
2. Add a `style` for the input — match the dark theme (background: `var(--bg-card)`, color: white, border, border-radius, padding)
3. Add a JavaScript `addEventListener('input', ...)` on the search input
4. Inside the listener, filter the `players` array using `.filter()` to keep only players whose name includes the typed text (case-insensitive)
5. Call `renderTable()` with the filtered array

**You know you've done it correctly when:** typing a single letter narrows the table in real time without any button click or page reload.

**Hint for the filter:**
```javascript
var query = event.target.value.toLowerCase();
var filtered = players.filter(function(p) {
  return p.name.toLowerCase().includes(query);
});
renderTable(filtered);
```

**Stretch:** Make the search also match by position (so typing "PG" shows only point guards).

---

## Task 3 — Soccer Colour Scheme

Change the entire colour theme from the current dark navy / red to a **soccer / football green field palette**.

**What to do:**
1. Update the CSS custom properties at the top of the `<style>` block:
   - `--bg-deep`: a very dark green (e.g., `#0d1f0d`)
   - `--bg-card`: a slightly lighter dark green (e.g., `#122912`)
   - `--bg-row`: a mid-tone green (e.g., `#1a3d1a`)
   - `--accent`: a bright grass green (e.g., `#4caf50`) or a golden yellow (e.g., `#f9a825`)
   - `--accent-dim`: a slightly darker version of your accent
   - `--green`: keep as-is or change to a bright white for contrast
2. Update the `<h1>` text to read "Soccer Live Dashboard"
3. Update the team names in the scoreboard to two football clubs of your choice

**You know you've done it correctly when:** the page feels like it belongs on a football pitch, not a basketball court.

**Challenge:** Look up "FIFA green hex code" and try to match the exact shade of a real grass football pitch.

---

## Task 4 — Add a Soccer Team Stats Panel

Below the existing basketball stats table, add a second stats panel for a soccer team.

**What to do:**
1. Add a new heading: `<h2>Starting XI — [your club name]</h2>` between the two tables
2. Create a second array `var soccerPlayers` with 6–11 players. Soccer stats use different columns: **Goals**, **Assists**, **Passes**, **Tackles**, **Minutes**
3. Add a second table with id `soccer-table` and a `<tbody id="soccer-body">`
4. Write a `renderSoccerTable()` function (copy `renderTable()` as a starting point, adjust column names and properties)
5. Call it on page load
6. Add a "Sort by Goals" button that sorts the soccer table

**Example soccer players array:**
```javascript
var soccerPlayers = [
  { name: 'Bukayo Saka',     pos: 'RW', goals: 18, assists: 11, passes: 42, tackles: 3, mins: 2814 },
  { name: 'Martin Odegaard', pos: 'CM', goals: 10, assists: 14, passes: 71, tackles: 5, mins: 2520 },
  { name: 'Leandro Trossard',pos: 'LW', goals: 12, assists: 6,  passes: 38, tackles: 2, mins: 2100 },
  { name: 'Kai Havertz',     pos: 'CF', goals: 14, assists: 5,  passes: 29, tackles: 4, mins: 2430 },
  { name: 'Declan Rice',     pos: 'DM', goals: 3,  assists: 8,  passes: 85, tackles: 9, mins: 2790 },
  { name: 'Ben White',       pos: 'RB', goals: 2,  assists: 5,  passes: 63, tackles: 7, mins: 2650 }
];
```

**You know you've done it correctly when:** both tables are visible on the page, independently sortable, and styled consistently.

---

## Task 5 — Essay: The React Component Analogy

Write 4–6 paragraphs (roughly 250–350 words) answering this prompt:

> **"A React component is like a player on a team. Explain this analogy, using what you learned about state management in this session."**

Your answer must cover:

1. **The role of a component** — What does a single component do? What does it *not* do? How is that like a specialist player's position?

2. **Shared state as the game situation** — What is "state" in React terms? How is it like the live match situation that all players respond to? What is the "single source of truth" equivalent in football?

3. **What happens when state changes** — When a goal is scored, the whole team adjusts. When React state changes, components re-render. Explain the parallel. Why is this better than each component/player acting independently?

4. **The coach and the DOM** — In the analogy, who is the "coach" giving instructions? How does React being the one who updates the DOM (not the developer) compare to a coach directing players rather than players improvising individually?

5. **A limitation of the analogy** — No analogy is perfect. Where does the "component = player" comparison break down? What does a React component do that a player *cannot* do?

**Grading note:** This is not a quiz — there is no single right answer. The goal is to show that you understand the *problem* React solves, not just the syntax. A strong answer uses specific examples from football and from code concepts.

---

## Bring to Next Session

- `sports_dashboard_v2.html` with Tasks 1–4 complete (open it in a browser, show it works)
- Task 5 essay — written out in full (can be handwritten or typed)
- Be ready to explain your code for any one of the four tasks without looking at notes
