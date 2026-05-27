# Session 10 — Assignment
## How Instagram Works

---

## Task 1 — Trace a Post's Journey

Draw a diagram (boxes and arrows, on paper or digital) tracing the full journey of a photo from:

**Tap "Post" → Friends see it in their feed**

Your diagram must include at minimum:
- Your phone
- The API Gateway
- The Media Service
- Amazon S3
- The CDN
- The database
- The notification system

Label each arrow with what data is flowing (e.g., "JPEG file + caption" or "post ID + metadata").

---

## Task 2 — Algorithm Experiment

Open `instagram_simulator.py`. Run it and understand the output.

Then:

1. Change `close_friend_2`'s `past_likes` from `5` to `9`. Run again. What changed in the feed ranking?
2. Change `football_page`'s `age_minutes` from `5` to `300` (5 hours old). Run again. Did it move down the feed? Why?
3. Add a new account called `"your_favourite_footballer"` to both `user_profile` and `raw_posts`. Give it a `past_likes` of `10` and `age_minutes` of `3`. What position does it appear in?

Write 3–4 sentences explaining what the experiment showed you about how the algorithm works.

---

## Task 3 — The $1 Billion Architecture Question

Instagram sold for $1 billion in 2012 with 13 employees. Today Meta earns $32 billion per year from Instagram.

Answer these questions in your own words (3–5 sentences each):

1. **What did Facebook actually buy when they bought Instagram?** (It wasn't just the app)
2. **If you were going to build a competitor to Instagram from scratch today, what is the hardest technical problem you'd face?** (Not the business problem — the engineering problem)
3. **Instagram started as a Python + PostgreSQL app. Does that surprise you, given the scale it operates at today?**

---

## Task 4 — DevTools Investigation

Open Instagram in a desktop browser. Use DevTools (Network tab) to investigate:

1. How many HTTP requests does loading your feed make? (Count the XHR/Fetch requests)
2. What CDN domain do Instagram's images come from? Write the full domain name.
3. Pick one API request. Write down:
   - The URL endpoint
   - The HTTP method (GET or POST)
   - The status code
   - One interesting field from the response JSON

Write a short paragraph about what surprised you most from the investigation.

---

## Task 5 — Design Your Own App

You now understand how Instagram works under the hood. Design a simple version of a **sports highlights app** (like Instagram, but only for goals, dunks, and match highlights).

Describe your design:
1. What would users be able to post? (What data types?)
2. What would the feed algorithm rank on? (What signals matter for sports content?)
3. What three microservices would be the most important ones to build first?
4. Would you use CDN for video? Why?

This is exactly the kind of thinking that happens in engineering interviews at tech companies.

---

## Bring to Next Session

- Post journey diagram (Task 1)
- Algorithm experiment results + explanation (Task 2)
- The three written answers (Task 3)
- DevTools findings (Task 4)
- Sports highlights app design (Task 5)
