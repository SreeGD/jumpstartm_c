# Lab — Inspect Instagram with DevTools
## Session 10: How Instagram Works

**Type:** Browser investigation  
**Time:** 20–30 minutes  
**Do with Sree:** Explore together, Advaith narrates what he sees

---

## Setup

1. Open Instagram in a **desktop browser** (instagram.com — not the app)
2. Log in to your account
3. Open DevTools: `Cmd+Option+I` (Mac) or `F12` (Windows)
4. Click the **Network** tab
5. Clear existing requests (the 🚫 button)

---

## Part 1 — Watch a Feed Load

1. Scroll down to load new posts in your feed
2. Watch the Network tab fill up with requests
3. Filter by **Fetch/XHR** (the API calls only — not images)

Look for requests to:
- `i.instagram.com/api/v1/feed/timeline/`  ← the main feed
- `graph.instagram.com/` ← profile and media data

**Questions:**
1. How many API requests did loading the feed make?
2. Click on the feed request. Under **Headers**, find the `Authorization` header. What type of token is it?
3. Under **Preview**, can you see the JSON response? What fields do you see on each post?

---

## Part 2 — Watch a Photo Load

1. Filter the Network tab by **Img** (images only)
2. Click on a photo in the feed
3. Find the image request in the Network tab

**Questions:**
1. What is the URL of the photo? Where does it come from? (Look at the domain — is it `instagram.com`?)
2. How large is the image file in KB?
3. How long did it take to download? (Check the **Timing** tab)
4. Is there a `cdninstagram.com` or `fbcdn.net` domain in the URL? That's the CDN.

---

## Part 3 — Watch a Story Load

1. Click on someone's Story
2. Watch the Network tab
3. Find the video or image requests

**Questions:**
1. Stories are video. Do you see `.mp4` requests?
2. Notice the URL parameters. Can you see any quality parameters (like `720p` or `480p`)?
3. Stories disappear after 24 hours. Can you see any `expires` field in the request headers?

---

## Part 4 — Find the Algorithm Response

When Instagram loads your Explore page, the API returns ranked posts.

1. Navigate to the Explore page (magnifying glass icon)
2. Filter Network by `XHR/Fetch`
3. Find a request to `/api/v1/discover/` or similar
4. Open the **Preview** tab of the response

**Questions:**
1. Can you see a `ranking_score` or similar field in the JSON?
2. How many posts does one API call return?
3. What other data comes back besides the post content?

---

## What You're Seeing

Every API call you've watched is:
- A real HTTP request your phone makes to Instagram's servers
- The response is JSON — the same Python dictionaries you've been working with
- The images come from CDN servers, not Instagram's main servers
- The ranking scores are computed by ML models on Instagram's servers

> "Every app on your phone is just making HTTP requests and parsing JSON. Instagram. YouTube. Spotify. WhatsApp. Now you know what's happening under the hood."
