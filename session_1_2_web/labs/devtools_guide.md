# Lab — Spy on the Internet with DevTools

**Time:** 20–30 minutes (do with Sree)  
**Requires:** Chrome or Firefox browser

---

## What You're Doing

Every time you visit a website, your browser sends dozens of invisible requests.  
DevTools lets you see all of them — in real time.

---

## Step-by-Step

### 1. Open DevTools
- Open Chrome
- Go to any website (try `youtube.com` or `espn.com`)
- Press `F12` (or right-click anywhere → **Inspect**)
- Click the **Network** tab at the top

### 2. Refresh the Page
- Press `Ctrl+R` (or `Cmd+R` on Mac)
- Watch requests appear in the list — they fire off in milliseconds

### 3. Explore the Requests

Look at the columns:
- **Name** — what file or URL was requested
- **Status** — the response code (200, 304, etc.)
- **Type** — what kind of resource (document, script, image, fetch/xhr)
- **Size** — how much data was transferred
- **Time** — how long the request took

### 4. Click on a Request

Click any row. A side panel opens. Explore:
- **Headers tab** — see the full request and response headers
  - Find the `Content-Type` header — what kind of data did the server return?
  - Find the `Status Code` — 200? 304? What does it mean?
- **Response tab** — see the actual data returned (HTML, JSON, or binary)
- **Timing tab** — see the breakdown: DNS lookup, connection, download

---

## The Interesting Part — Find the API Calls

1. In the filter bar, click **Fetch/XHR**
2. These are the API calls — not pages, just data
3. Click one and look at the **Response** tab
4. You should see **JSON** — structured data

*This is how every modern app works. The visual UI you see is built on top of dozens of these invisible JSON responses.*

---

## Questions to Answer

After exploring, write down:

1. How many total requests fired when you loaded the page?
2. What was the largest file downloaded (by size)?
3. Find one API (Fetch/XHR) request. What URL did it call? What data did it return?
4. Did any request fail (non-200 status code)? Which one?
5. How long did the full page take to load? (Look at the bottom status bar)

---

## Try It on Different Sites

| Site | What to look for |
|------|-----------------|
| instagram.com | API calls for your feed posts |
| espn.com | Live score data in XHR requests |
| google.com | How few requests a simple page makes |
| amazon.com | How MANY requests a complex page makes |

---

## The Key Insight

*"Every app is just a UI on top of API calls. When you know this, you stop seeing apps as magic boxes. They're just software making HTTP requests and rendering the JSON responses."*
