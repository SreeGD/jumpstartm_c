# Session 11 — Full Stack Development: The Frontend Layer
## What the user sees, touches, and feels

**Duration:** 2–3 hours
**The teacher's prep:** Open a browser and a plain text editor side by side. Have sports_frontend.html ready to open and live-edit during the lesson. Know how to open DevTools (F12 or Cmd+Opt+I). Pull up a live sports app like ESPN or NBA.com on your phone and desktop to show the responsive difference. Optional: have a simple CodePen or JSFiddle tab open for quick experiments.

---

## 🎯 Goal

- Understand the three layers of a webpage (HTML, CSS, JavaScript) and what each one actually does
- Understand how a browser turns text files into a visual, interactive page
- Write JavaScript that responds to user actions and changes what is on screen
- Understand *why* frameworks like React exist — the real problem they solve
- See the complete modern frontend toolchain so nothing feels mysterious later

---

## 📖 The Teacher's Narrative

### Hook — The Invisible Work Behind a Scoreboard

Open the NBA or ESPN live scoreboard on your phone. Hold it up.

> "This is just a webpage. There is nothing magic about it. It is HTML, CSS, and JavaScript — the same three things a beginner can learn in a week."

Now ask:

> "If I told you that you could build *this* today — a live scoreboard that updates in real time, works on any phone, and talks to a server — would you believe me?"

Because by the end of this session, you will understand every single piece that makes it work. Not just the theory. You will *build* one.

The reason people think frontend development is mysterious is that they see the polished result and assume it must require special magic. It doesn't. It requires understanding three ingredients.

---

### Part 1: The Three Ingredients

Every single webpage on the internet — from Google's homepage to Netflix to the NBA scoreboard — is built from exactly three things.

#### HTML — The Skeleton

HTML is structure. It says: *what exists* on the page.

```html
<h1>NBA Live Scores</h1>
<table>
  <tr><td>Lakers</td><td>108</td></tr>
  <tr><td>Celtics</td><td>104</td></tr>
</table>
<button>Refresh</button>
```

This is like the *skeleton* of a basketball player. It defines what body parts exist: a head, two arms, two legs. But without muscles or skin, it just sits there — it can't move, it doesn't look like anything useful.

**Sports analogy:** HTML is the *team roster sheet*. It lists who is on the team, in what order. But paper can't play basketball.

#### CSS — The Skin (and Uniform)

CSS is appearance. It says: *how things look*.

```css
body {
  background-color: #1a1a2e;  /* dark navy */
  color: white;
  font-family: Arial, sans-serif;
}

h1 {
  color: #e94560;  /* red accent */
  font-size: 2rem;
}

button {
  background: #e94560;
  border-radius: 8px;
  padding: 10px 20px;
}
```

CSS puts the skin on the skeleton. It colours it, sizes it, positions it on the page, and makes it look the way you actually see it in a browser.

**Sports analogy:** CSS is the *Lakers purple and gold jersey*, the court floor design, the scoreboard font. All visual. None of it changes the game — it just changes what you see.

#### JavaScript — The Muscles

JavaScript is behaviour. It says: *what happens* when things occur.

```javascript
document.querySelector('button').addEventListener('click', function() {
  document.querySelector('h1').textContent = 'Score Updated!';
});
```

JavaScript gives the page life. Clicks, typing, timers, fetching data from a server — all JavaScript.

**Sports analogy:** JavaScript is the *muscles and reflexes* of the player. When the ball comes (an event happens), the player's arm goes up to catch it (the function runs). Without muscles, the skeleton and skin just stand there doing nothing.

**The Key Insight:** These three are completely separate concerns. An HTML file with no CSS and no JavaScript still works — it just looks ugly and does nothing. Separating them is one of the best design decisions in computing history.

---

### Part 2: How a Page Actually Renders

When you type a URL and press Enter, here is exactly what happens before you see anything:

**Step 1 — The browser downloads the HTML file**
Your browser sends an HTTP GET request (Session 1.2) and gets back a text file full of HTML tags.

**Step 2 — Parse HTML → Build the DOM**
The browser reads the HTML top to bottom and builds a *tree structure* in memory called the **DOM** (Document Object Model). Every tag becomes a node in the tree.

```
document
  └── html
        ├── head
        │     └── title: "NBA Scores"
        └── body
              ├── h1: "Live Scores"
              └── table
                    ├── tr → td: "Lakers" | td: "108"
                    └── tr → td: "Celtics" | td: "104"
```

This tree is what JavaScript manipulates later. When you say `document.querySelector('h1')`, you're asking: "Give me the h1 node in this tree."

**Step 3 — Fetch CSS → Apply styles → Build the CSSOM**
The browser downloads all CSS files, builds a CSS Object Model, and figures out the final computed style of every element.

**Step 4 — Combine DOM + CSSOM → Render Tree**
Now the browser knows *what* exists (DOM) and *how it looks* (CSSOM). It combines them into a render tree — only elements that are actually visible.

**Step 5 — Layout**
The browser calculates the exact pixel position of every element on screen. This is called *layout* or *reflow*. "The h1 is 40px tall, starts at x=20, y=80. The table starts at y=140..."

**Step 6 — Paint**
The browser draws the pixels. Literally fills in colours, text, borders on the screen.

**Step 7 — Execute JavaScript**
The browser runs any JavaScript. If the JS changes the DOM (e.g., adds a row to the table), the browser loops back through layout and paint for the changed parts.

**The Basketball Scoreboard Example:**

Imagine a live scoreboard. The initial HTML is downloaded and painted — it shows `LAL 0 — BOS 0`.

Then JavaScript runs a timer. Every second, it *updates the DOM* — changes the number in the score cell. The browser repaints just that cell. The rest of the page stays exactly the same.

That is how "live" scoreboards work. Not magic. A timer + DOM update.

**Why this matters:** Every time JavaScript changes the DOM, the browser has to redo layout and paint. If you're not careful — updating 1,000 elements every second — the page becomes slow. This performance concern is exactly why React was invented. But we'll get there.

---

### Part 3: Making It Interactive — JavaScript

JavaScript has three core tools for interactivity: **events**, **DOM manipulation**, and **fetch()**.

#### Events — "When This Happens"

The browser fires *events* constantly: clicks, key presses, mouse moves, the page loading, a timer firing.

```javascript
// "When the button is clicked, run this function"
document.querySelector('#sort-btn').addEventListener('click', function() {
  console.log('Button was clicked!');
});

// "When the user types in the search box, run this function"
document.querySelector('#search').addEventListener('input', function(event) {
  const searchText = event.target.value;
  filterTable(searchText);
});
```

**Sports analogy:** Events are like referee signals. The referee blows the whistle (event fires), and the players respond (function runs).

#### DOM Manipulation — "Change What's on Screen"

```javascript
// Change text
document.querySelector('#score').textContent = '108';

// Change style
document.querySelector('#score').style.color = 'red';

// Add a new row to a table (safely, using DOM methods)
const tbody = document.querySelector('#stats-table tbody');
const newRow = document.createElement('tr');
const nameCell = document.createElement('td');
const goalsCell = document.createElement('td');
nameCell.textContent = 'LeBron James';
goalsCell.textContent = '28';
newRow.appendChild(nameCell);
newRow.appendChild(goalsCell);
tbody.appendChild(newRow);

// Show/hide an element
document.querySelector('#panel').style.display = 'none';  // hide
document.querySelector('#panel').style.display = 'block'; // show
```

#### fetch() — "Get Data from a Server"

This is how a real live scoreboard would work. Instead of hardcoded data, it calls an API.

```javascript
// Fetch live scores from an API every 30 seconds
async function updateScores() {
  const response = await fetch('https://api.sportsdata.io/v3/nba/scores/json/GamesByDate/2026-05-27');
  const games = await response.json();

  games.forEach(function(game) {
    document.querySelector('#home-score').textContent = game.HomeTeamScore;
    document.querySelector('#away-score').textContent = game.AwayTeamScore;
  });
}

// Call it immediately, then every 30 seconds
updateScores();
setInterval(updateScores, 30000);
```

**The Basketball Scoreboard — All Together:**

```javascript
let quarter = 1;
let seconds = 0;

setInterval(function() {
  seconds++;
  if (seconds >= 720) {  // 12 minutes per quarter
    seconds = 0;
    quarter++;
  }

  const mins = Math.floor(seconds / 60);
  const secs = seconds % 60;
  const display = 'Q' + quarter + ': ' + mins + ':' + secs.toString().padStart(2, '0');
  document.querySelector('#game-clock').textContent = display;
}, 1000);
```

No page reload. No server needed. Just JavaScript updating the DOM every second. This is exactly what you'll build in the lab.

---

### Part 4: Why We Need Frameworks

Here's a real problem.

You're building a sports app. When a goal is scored, these five things need to update simultaneously:

1. The scoreline at the top of the page
2. A goal-events timeline on the left
3. The goalscorer's stats card on the right
4. A notification badge on the "Highlights" tab
5. The match report text in the centre panel

With plain JavaScript, you'd write five separate DOM manipulation calls. Every time the score changes, you update five places. Fine.

But now: what happens when the score changes, *and* a player gets substituted, *and* there's a VAR review happening, *and* the game clock is running?

With plain JavaScript you now have dozens of interdependencies. Changing the score might accidentally break the timeline. You need to track which elements depend on which data. Your code becomes a nest of manual updates. Every piece knows about every other piece.

This is called the **state management problem**.

**The React Solution — One Source of Truth**

React says: instead of updating the DOM directly, just update *data*. React will figure out what changed and update only the affected parts of the screen automatically.

```javascript
// OLD WAY — manual DOM updates in five separate places
function goalScored(player, minute) {
  document.querySelector('#score').textContent = getNewScore();
  addGoalToTimeline(player, minute);
  incrementPlayerGoalCount(player.id);
  incrementHighlightsBadge();
  regenerateMatchReport();
}

// REACT WAY — update state, React handles the DOM
function goalScored(player, minute) {
  setState({
    score: state.score + 1,
    goals: state.goals.concat({ player: player, minute: minute })
  });
  // React automatically re-renders every component that uses score or goals
}
```

React introduces the concept of **components** — self-contained pieces of UI that know their own data and know how to render themselves.

```
App
  ScoreBoard  (reads: score)
  GoalTimeline  (reads: goals)
  PlayerCard  (reads: playerStats)
  TabBar  (reads: highlightCount)
  MatchReport  (reads: allEvents)
```

Each component is like a specialist player. The ScoreBoard component only cares about the score. The GoalTimeline only cares about goals. React figures out which components need to re-render when state changes.

**The Football (Soccer) Goal — Explained as State:**

- Before goal: `{ score: { home: 0, away: 0 }, goals: [] }`
- After goal: `{ score: { home: 1, away: 0 }, goals: [{ player: 'Mbappe', minute: 23 }] }`

React detects this state change and re-renders everything that depends on `score` or `goals`. The developer never touches the DOM.

**The four main frameworks:**

| Framework | Creator | When to choose |
|-----------|---------|---------------|
| **React** | Meta (Facebook) | Most popular, huge ecosystem, most jobs |
| **Vue** | Evan You (community) | Easier learning curve, gentle ramp |
| **Angular** | Google | Enterprise apps, strong opinions |
| **Svelte** | Rich Harris | No virtual DOM, very fast, newer |

For a first job in 2026, React is still the most valuable one to know. But they all solve the same fundamental problem: managing state so your UI stays consistent.

---

### Part 5: Responsive Design

**The number that changes everything:**

> 63% of all web traffic in 2026 is on mobile devices.

If your sports app doesn't work on a phone, you've failed more than half your users before they even start.

**Mobile-First Design:** Write CSS for the smallest screen first, then add styles for larger screens. This is the industry standard.

```css
/* DEFAULT (mobile) — single column, stacked layout */
.dashboard {
  display: flex;
  flex-direction: column;   /* stack items vertically */
  padding: 10px;
}

/* TABLET — switch to two columns at 768px */
@media (min-width: 768px) {
  .dashboard {
    flex-direction: row;    /* side by side */
    flex-wrap: wrap;
  }
}

/* DESKTOP — three columns at 1200px */
@media (min-width: 1200px) {
  .stats-card {
    width: 33%;
  }
}
```

**The Basketball Scoreboard on Phone vs Desktop:**

On a phone (375px wide):
- Score at the top, full width
- Player stats table scrolls horizontally
- Sidebar hidden, shown via a "Menu" button

On desktop (1400px wide):
- Score in the top bar
- Player stats table in the main panel
- Live game clock sidebar always visible

Same HTML. Same CSS file. The `@media` queries do all the switching automatically.

**Flexbox and Grid:** Two CSS layout systems that replaced decades of float hacks.

- **Flexbox**: for one-dimensional layouts (a row of buttons, a vertical stack of cards)
- **Grid**: for two-dimensional layouts (a 3×4 grid of player cards)

```css
/* Flexbox — align buttons in a row with space between */
.button-row {
  display: flex;
  gap: 12px;
  justify-content: space-between;
  align-items: center;
}

/* Grid — 3 cards per row */
.player-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}
```

---

### Part 6: The Full Frontend Stack (2026)

A complete picture of what professional frontend developers actually use:

```
FOUNDATION
  HTML5 ─── structure, semantics
  CSS3  ─── layout (Flexbox/Grid), animations, media queries
  JavaScript (ES2024) ─── logic, events, fetch, DOM

TYPED JAVASCRIPT
  TypeScript ─── JavaScript + types. Catches bugs before they happen.
                 Used in over 70% of professional projects in 2026.

UI FRAMEWORK (pick one)
  React 19  ─── components, state, hooks
  Vue 3     ─── similar concept, slightly easier start
  Angular 17 ─── opinionated, enterprise-focused

STYLING (pick one)
  Tailwind CSS ─── utility-first, write classes directly in HTML
  CSS Modules  ─── scoped CSS per component
  Styled Components ─── CSS written alongside JavaScript

BUILD TOOLS
  Vite ─── development server + production bundler (replaced Webpack for most projects)
  esbuild ─── extremely fast JavaScript bundler
  The bundler takes your 50+ JS files and combines them into 1-2 optimised files

TESTING
  Vitest / Jest ─── unit tests for JavaScript functions
  Playwright / Cypress ─── end-to-end browser tests ("click this button, check result")

DEPLOYMENT
  Vercel / Netlify ─── push to GitHub → automatic deploy in 30 seconds
```

**The journey from beginner to professional:**

1. Plain HTML/CSS/JS (what you're learning today)
2. Add TypeScript (learn types, same concepts)
3. Learn React (components replace DOM manipulation)
4. Learn Tailwind (replace hand-written CSS)
5. Add Vite (learn the build pipeline)
6. Add testing (automated confidence)

Every professional React developer started at step 1. The session you're doing today is not baby stuff — it is the foundation that everything else stands on.

---

## ⚡ Wow Moment

Open the browser DevTools (F12). Click the Elements tab. Find the live score element on any live sports website and double-click its text. You can change the score in the DOM right there in front of you.

The score on the screen will update instantly. You have just manipulated the DOM — the exact same thing JavaScript does thousands of times per second on a live scoreboard.

Then: right-click any element, click "Inspect". Watch the highlighted DOM node in the Elements panel. Go to the Console tab and type:

```javascript
document.querySelector('h1').style.color = 'red';
```

Press Enter. The h1 on the page turns red. You just ran JavaScript against a live production website. This is exactly what browser extensions do — they run JavaScript on pages after they load.

**One more:** In DevTools, go to Network tab, reload the page, and watch hundreds of requests fire in milliseconds. That's the entire rendering pipeline — DNS, HTML, CSS, JS, images, API calls — all visible.

---

## 🔑 Key Concepts Checklist

- [ ] HTML is structure (what exists), CSS is appearance (how it looks), JavaScript is behaviour (what it does)
- [ ] The DOM is a tree representation of the HTML that JavaScript can read and modify
- [ ] The browser rendering pipeline: parse HTML → build DOM → apply CSS → layout → paint → execute JS
- [ ] An event listener waits for something to happen (click, key press, timer) and runs a function
- [ ] `document.querySelector()` finds an element in the DOM; `.textContent` changes its text
- [ ] `fetch()` makes HTTP requests from JavaScript without reloading the page
- [ ] `setInterval(fn, ms)` runs a function repeatedly — the foundation of live scoreboards
- [ ] The state management problem: when many parts of the screen depend on the same data, manual DOM updates become unmaintainable
- [ ] React solves state management with components and a single source of truth
- [ ] CSS media queries switch layouts at different screen widths (responsive design)
- [ ] Flexbox is for one-dimensional layouts; Grid is for two-dimensional layouts
- [ ] The modern frontend stack: HTML/CSS/JS → TypeScript → React → Tailwind → Vite → Testing → Deploy

---

## Teaching Notes for Teacher

**Pacing:** Parts 1–3 should take about 45–60 minutes total. Parts 4–6 can go faster — they're conceptual. The lab is where most time goes.

**Live coding works best here.** Start with a blank HTML file and build the scoreboard incrementally during the lesson. Let the student type. Don't demo-and-watch.

**The "Inspect Element" wow moment** almost always lands. Do it early if energy dips.

**Common confusion points:**
- Students confuse HTML attributes (`class="box"`) with CSS properties (`color: red`). Be explicit: the HTML *references* the CSS. They're separate files that reference each other.
- Students think JavaScript has to reload the page. Show `textContent` change happening instantly with no reload to make the point viscerally.
- "What's the difference between a framework and a library?" — React is technically a library (just the UI layer), not a full framework. Don't get too deep here; the point is components and state management.

**For the React section:** You do not need to write actual React code. The conceptual explanation is enough. The goal is that when they encounter React later, it doesn't feel alien — they already understand the problem it solves.

**If you have extra time:** Open a real sports API (like balldontlie.io — it's free, no auth needed for basic endpoints) and do a live `fetch()` call in the browser console to show real data coming back.

---

## 🧪 Quiz

**1.** (Multiple choice) What does HTML stand for, and what is its job in a webpage?

   a) HyperText Markup Language — controls how the page looks  
   b) HyperText Markup Language — defines the structure and content of the page ✓  
   c) High Transfer Markup Language — sends data between browser and server  
   d) HyperText Method Language — handles button click events  

---

**2.** (Multiple choice) A basketball scoreboard shows `LAL 0 — BOS 0` when the page loads. The score changes to `LAL 2 — BOS 0` without the page reloading. Which technology made that change happen?

   a) HTML — it re-downloaded a new HTML file  
   b) CSS — it applied a new stylesheet  
   c) JavaScript — it updated the DOM ✓  
   d) The server sent a new webpage automatically  

---

**3.** (Multiple choice) What is the DOM?

   a) A database of user preferences stored in the browser  
   b) A tree-shaped representation of the HTML page that JavaScript can read and modify ✓  
   c) A CSS tool for responsive layouts  
   d) A type of HTTP request used by JavaScript  

---

**4.** (Short answer) Put the browser rendering pipeline steps in the correct order:

   *(Paint, Execute JS, Parse HTML, Apply CSS, Build DOM, Layout)*

   **Answer:** Parse HTML → Build DOM → Apply CSS → Layout → Paint → Execute JS

---

**5.** (Short answer) Explain what `setInterval` does and why it is useful for a live sports ticker.

   **Answer:** `setInterval(function, milliseconds)` runs a function repeatedly on a timer. For a live ticker, it lets you update the clock, score, or stats display every second (or however often you choose) without requiring any user interaction or page reload.

---

**6.** (Explain in your own words) A sports app has five sections: scoreline, goal timeline, scorer stats card, notification badge, and match report. All five need to update when a goal is scored. Explain the *state management problem* — why this gets complicated — and how React's approach is different from plain JavaScript.

   **Sample answer:** In plain JavaScript, you'd write five separate DOM update calls inside the `goalScored()` function. As the app grows, every function that changes data has to know which parts of the screen depend on that data. If a bug hides in one of those update calls, one panel goes out of sync with the others. React solves this by separating data (state) from the display. You update the data once — `setState({ score: 1 })` — and React automatically re-renders every component that reads `score`. The developer never touches the DOM directly.

---

**7.** (Multiple choice) What does a CSS media query do?

   a) Fetches images from a media server  
   b) Applies different CSS styles depending on the screen width (or other conditions) ✓  
   c) Blocks videos from autoplay on mobile  
   d) Tells JavaScript which device type is being used  

---

**8.** (Explain in your own words — sports connection) A React component has been compared to a player on a sports team. Based on what you learned today, write 3–5 sentences explaining this analogy. What is the component's "job"? What is the team's "shared game state"? What happens when the game state changes?

   **Sample answer:** Each React component, like a player on a team, has a specific role and only needs to know about the part of the game that affects them. A goalkeeper component only cares about shots on goal; a striker component only cares about goal opportunities. The shared game state — the score, the time, who has the ball — is like the game situation everyone on the team responds to. When the game state changes (a goal is scored), each player (component) automatically updates their behaviour based on the new situation. No player has to manually tell every other player what changed — they all react to the shared state.

---

**Answers summary:** 1-b, 2-c, 3-b, 4-see above, 5-see above, 6-see above, 7-b, 8-see above

---

## 📚 Research Materials

### Films and Documentaries
- **"The Social Dilemma"** (Netflix, 2020) — engineers who built these frontend products explain the psychology they deliberately designed in
- **"General Magic"** (2018) — the forgotten 1990s startup that imagined the smartphone and internet browser 20 years early

### YouTube
- **Fireship** — "HTML, CSS, JS in 100 seconds" (start here — exactly this lesson in a tight package)
- **Fireship** — "React in 100 seconds" (after understanding the problem)
- **Kevin Powell** — any video on CSS Flexbox or Grid (the clearest CSS teacher on YouTube)
- **The Coding Train** — JavaScript basics with visual, creative examples
- **Traversy Media** — "Vanilla JS Crash Course" — builds a project without frameworks

### Books
- **"JavaScript: The Good Parts"** by Douglas Crockford — short and essential; explains which parts of JS are actually good design
- **"CSS: The Definitive Guide"** by Eric Meyer — the reference; don't read cover to cover, use it when stuck
- **"Don't Make Me Think"** by Steve Krug — not a coding book; a book about how users actually use websites; every frontend developer should read it

### Articles
- **"The Anatomy of a Frame"** — Paul Lewis, developers.google.com — explains the rendering pipeline in depth with real performance data
- **"A Brief History of CSS"** — CSS-Tricks — understanding how CSS evolved explains why some things feel weird
- **"JavaScript Rising Stars"** (2025 edition) — Bestofjs.org — annual snapshot of what the JS ecosystem actually looks like

### People to Look Up
- **Brendan Eich** — created JavaScript in 10 days in 1995. It was supposed to be a simple scripting language. It became the most-used programming language in the world.
- **Jordan Walke** — created React at Facebook in 2011. He was inspired by a PHP framework called XHP.
- **Evan You** — created Vue.js while working at Google. He wanted something simpler than Angular.
- **Rich Harris** — created Svelte. A journalist who taught himself programming. His talk "Rethinking Reactivity" is worth watching.

### Start Here Tip

If you only have 30 minutes before this session, watch Fireship's "HTML CSS JavaScript Explained" and "React in 100 seconds" back to back. That's 5 minutes of video that previews everything in this lesson. Then open the sports_frontend.html lab file and read through the comments before opening it in a browser.
