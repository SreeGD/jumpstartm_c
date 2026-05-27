# Session 10 — How Instagram Actually Works
## The app you use every day hides a billion-dollar engineering story

**Teacher:** *(your name)*  
**Student:** *(your student's name)*  
**Prerequisite:** Session 1.2 (How the Web Works), Session 4 (Python), Session 6 (Agentic AI)  
**Duration:** 90–120 minutes

---

## HOOK — The 30-Second Test

> "Open Instagram right now. Scroll for 30 seconds. Close it."

Ask Student: **How many servers just worked for you?**

The answer: **hundreds**.

In 30 seconds of scrolling, Instagram:
- Authenticated you (checked your login)
- Ranked *thousands* of posts to pick the 20 you saw
- Fetched images from servers that might be in Singapore, Frankfurt, or Mumbai
- Predicted which posts you'd double-tap (to show you more like them)
- Measured exactly how long you paused on each post
- Updated an advertising profile in real time

And it did all of this in under **200 milliseconds** per action.

Student uses Instagram for hours every day. Today he finds out it's one of the most sophisticated engineering systems ever built.

---

## Part 1 — The Instagram Origin Story

### 2010: Two guys, 13 days, 1 million users

Kevin Systrom and Mike Krieger built the first version of Instagram in **13 days**. Their technical choices were:
- Python backend (Flask framework)
- PostgreSQL database
- Amazon Web Services (S3 for photos, EC2 for servers)
- No desktop app — mobile only

**The Wow:** In 2012, Facebook acquired Instagram for **$1 billion**. Instagram had 13 employees. That's $77 million per person.

Why was it worth that? Not the app. The **architecture decisions** — they'd built something that could scale.

---

## Part 2 — What Happens When You Post a Photo

This is the journey of a single Instagram post.

### Step 1 — You tap "Post"
Your phone sends an HTTP POST request to `graph.instagram.com/v1/media` with:
- The image file (compressed JPEG or HEIF)
- Caption text
- Location tag (if set)
- Your authentication token (so Instagram knows it's you)

### Step 2 — The API Gateway receives it
Not every request goes to the same server. A **load balancer** at the front door distributes millions of simultaneous requests across thousands of backend servers. Your request lands on one server among thousands.

### Step 3 — Image Processing Pipeline
Instagram doesn't just save your photo. It creates **multiple versions**:

| Version | Resolution | Used for |
|---------|-----------|---------|
| Thumbnail | 150×150 | Grid view on your profile |
| Feed size | 640×640 | Main feed |
| Full size | 1080×1080 | When someone zooms in |
| Story | 1080×1920 | Stories format |

Each version is stored in **Amazon S3** — a file storage service that holds billions of objects. Instagram stores **100+ billion photos**. At ~50KB average, that's 5 petabytes of storage.

### Step 4 — CDN Distribution
Once saved to S3, the image URL is distributed to a **Content Delivery Network (CDN)** — Fastly or Akamai. CDNs have servers in 200+ cities worldwide. When your friend in Chennai loads your photo, it comes from the nearest CDN node — not from a server in California.

**The Wow:** Without CDN, loading one photo from the US would take 300ms. With CDN, it takes 20ms from a Mumbai node.

### Step 5 — Database Write
Instagram writes metadata to its databases:
- **PostgreSQL** — post ID, user ID, timestamp, caption, location
- **Cassandra** — activity feed (who liked, commented)
- **Redis** — in-memory cache (for instant access to recent data)

### Step 6 — Notification Fan-out
If you have 5,000 followers, Instagram creates 5,000 notifications saying "X posted". This is called **fan-out**. At Instagram scale, a celebrity with 500M followers posting creates 500 million tasks in milliseconds.

Instagram uses **message queues** (like Apache Kafka) to handle this — tasks are queued and processed in parallel by thousands of worker servers.

---

## Part 3 — The Feed Algorithm (The Magic Black Box)

The Instagram feed algorithm is the most important piece of code at Meta. It determines what you see and what gets ignored.

### Pre-2016: Chronological Feed
Posts appeared in the order posted. Simple. Fair. No algorithm.

### 2016: The Algorithm Switch
Instagram switched to **ranked feed**. Now posts are sorted by a score — not time.

### How the Score is Calculated

Instagram considers **hundreds of signals**, but the main ones:

**Interest signals (what you care about):**
- Have you liked photos from this person before?
- Do you watch their Stories?
- Did you DM them this week?
- How long do you pause on their posts?

**Relationship signals (how close are you?):**
- Tagged in the same photos
- Mutual followers
- Looked at their profile

**Recency signals:**
- When was this posted? (Fresher = higher score, but not always)

**This is a machine learning model.** Every action you take — like, skip, pause, zoom — is training data. Instagram predicts: **"Given what Student has done before, how likely is he to like this post?"**

### The Recommendation System

Explore page is different from the feed. It uses a **two-stage recommendation system**:

**Stage 1 — Candidate Generation:**
From 100 million possible posts, find 1,000 that might be relevant.
(Fast but rough — uses simpler ML models)

**Stage 2 — Ranking:**
From 1,000 candidates, rank them precisely using a deep neural network.
(Slow but accurate — runs on every user's Explore page)

**Stage 3 — Diversity filter:**
Don't show 10 posts from the same person in a row.

---

## Part 4 — Stories vs Reels vs Posts (Different Data Models)

Instagram has three content types that work completely differently:

### Posts (permanent)
- Stored permanently in S3
- Indexed in PostgreSQL
- Shown in feed + profile grid
- Can get likes/comments for years

### Stories (24-hour expiry)
- Stored with TTL (Time-To-Live) in the database
- After 24 hours, automatically deleted from CDN and database
- Uses a separate **ring buffer** data structure — oldest stories fall off automatically
- Speed matters more than persistence

### Reels (video + recommendation)
- Video encoded in multiple resolutions (360p, 720p, 1080p)
- Uses **adaptive bitrate streaming** — your phone switches quality based on WiFi/4G speed
- Recommendation engine is separate from feed — similar to TikTok's algorithm
- A Reel from someone you don't follow can go viral if engagement rate is high

**The Wow:** A Reel you post can reach 1 million people who've never heard of you. A post from 2012 could not.

---

## Part 5 — How Instagram Handles 500 Million Daily Users

### The Scale Problem

Instagram has ~500 million daily active users. Peak usage is evenings — especially weekends.

At peak:
- 1 million photo uploads per minute
- 4.2 billion likes per day
- 100 million Stories posted per day

A single server can handle ~1,000 requests/second. Instagram needs **millions** of servers.

### Horizontal Scaling

Instead of buying one very powerful server, Instagram runs **thousands of cheaper servers** in parallel. When traffic spikes, they add more servers automatically (**auto-scaling**).

This is why cloud computing (AWS, GCP, Azure) exists — you pay for what you use. At 3 AM, Instagram uses fewer servers. At 8 PM Friday, it spins up thousands more.

### Microservices Architecture

Instagram isn't one program. It's dozens of independent services:

| Service | Does what |
|---------|-----------|
| `auth-service` | Checks your login token |
| `media-service` | Stores and serves photos/videos |
| `feed-service` | Builds your personalised feed |
| `notification-service` | Sends push notifications |
| `search-service` | Powers hashtag and account search |
| `ads-service` | Decides which ads to show |
| `ml-ranking-service` | Scores posts for the algorithm |

Each service is deployed independently. If `search-service` crashes, the feed still works.

### Caching with Redis

Reading from a database is slow (5–50ms). For popular data (celebrity profiles, viral posts), Instagram caches results in **Redis** — an in-memory database.

When 10 million people load Cristiano Ronaldo's profile simultaneously, Instagram doesn't query the database 10 million times. It caches his profile data in Redis and serves all 10 million from memory.

---

## Part 6 — The Privacy and Ad Machine

### Every Action is Data

Instagram tracks:
- Every post you see (even if you don't like it)
- How long you pause on each post
- When you zoom into a photo
- When you close the app
- What you search for

This data trains the recommendation model and the **ad targeting model**.

### How Ads Work

Instagram shows you ads based on:
- Your interests (inferred from posts you like)
- Your demographics (age, location)
- **Lookalike audiences** — "Find users similar to this customer list"
- Retargeting — "This person visited our website, show them our ad"

A company pays Meta per 1,000 impressions (CPM) or per click (CPC). Instagram uses a **real-time auction** — multiple advertisers bid on each ad slot. The winning ad is shown in ~50ms.

**The Business Model:** Instagram generated ~$32 billion in ad revenue in 2022. It's free to use because you are the product — your attention is what's being sold.

---

## WOW Moment — The Illusion of Simplicity

Instagram's interface is simple. 5 icons at the bottom. Post, like, comment.

But behind that simple interface:
- **Thousands of servers** running 24/7
- **Petabytes of storage** replicated across multiple data centres
- **ML models** running 500 million times a day
- **Real-time auctions** happening in milliseconds
- **Distributed databases** keeping everything consistent across 20+ data centres

And all of it was built by humans who learned the same things Student is learning now.

Kevin Systrom, Instagram's co-founder, studied symbolic systems at Stanford. His co-founder Mike Krieger built the first backend in Python. The first engineer they hired was a 22-year-old.

> "The best engineers aren't the ones who know everything. They're the ones who can look at a complicated system and understand how the pieces fit."

---

## Teaching Notes for Teacher

**Key connections to previous sessions:**
- HTTP requests (Session 1.2) → Instagram's API calls
- Databases (mentioned in Session 9) → PostgreSQL, Cassandra, Redis
- Machine learning concepts (Session 5) → The ranking algorithm
- APIs and microservices (Session 9) → Instagram's service architecture

**Good questions to ask Student:**
1. "Why does Instagram not show posts chronologically anymore?"
2. "If you have 1 million followers and you post, what has to happen technically?"
3. "Why does the same Reel load faster on WiFi than 4G — what's adapting?"
4. "If Instagram is free, how does Meta make $32 billion a year from it?"

**The connect to his future:**
> "If you learn Python, backend web development, and ML — you could build something like the early Instagram. Not the scale (you'd need thousands of engineers for that) but the ideas? Completely learnable."

**Optional deep dive (if time allows):**
- Show Student how to inspect Instagram's API calls using browser DevTools
- Look at the `graph.instagram.com` requests in the Network tab
- Discuss GraphQL vs REST (Instagram uses GraphQL internally)
