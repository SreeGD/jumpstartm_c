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

Kevin Systrom had met Mark Zuckerberg through mutual contacts in the Bay Area startup scene. The acquisition was controversial at the time — Instagram had zero revenue. But Zuckerberg saw the threat clearly: mobile photo sharing was the thing Facebook had failed to crack, and Instagram was eating that space. It turned out to be one of the best investments in tech history. Thirteen years later, Instagram generates roughly **$32 billion per year in ad revenue** — more than YouTube. The $1 billion price tag looks absurd in hindsight, but only because the architecture decisions that followed were so good.

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

### The Ethical Dimension

The algorithm's stated goal is maximising **"time spent"** — the total minutes a user stays in the app. Meta tracks this obsessively as a core business metric, because more time spent means more ad impressions.

In 2021, **Frances Haugen** — a former Meta product manager turned whistleblower — leaked internal research documents to the Wall Street Journal. The documents revealed that Meta's own researchers had found the algorithm intentionally amplifies outrage and emotionally provocative content, because that content drives higher engagement than neutral or positive posts. Meta knew this, debated it internally, and largely chose not to fix it because the engagement numbers were too valuable.

This is the real ethical dimension of recommendation systems. The engineering is impressive. The goal it's optimising for is worth examining.

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

### Meta's Infrastructure — Built From Scratch

One thing that surprises most people: Instagram (Meta) does **not** run on AWS or Azure. Meta owns and operates its own data centres — enormous, custom-built facilities. In 2011, Meta launched the **Open Compute Project**, open-sourcing the hardware and data centre designs they'd developed, so the rest of the industry could benefit. They needed racks, cooling systems, and power management tailored to their exact workloads, and rather than keep it proprietary, they shared it.

Meta's engineering culture has also produced a striking number of tools the rest of the industry depends on. They wrote **Cassandra** (now Apache Cassandra) for their own inbox search. They open-sourced **React**, **GraphQL**, **PyTorch**, and **LLaMA**. This is worth pausing on: the company that built Instagram has become one of the most prolific open-source contributors in tech, releasing the infrastructure that other companies — including competitors — use to build their own products.

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

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** What is a CDN (Content Delivery Network) and why does Instagram use one?
- A) A type of database for storing user passwords
- B) A network of servers in cities worldwide that serves content from the location nearest to the user, reducing load times ✓
- C) A machine learning model that ranks posts in the feed
- D) Instagram's internal messaging system between microservices

**Q2.** What is the "fan-out problem" in the context of Instagram, and what technology does Instagram use to solve it?
- A) A problem where photos are too large to store; solved with image compression
- B) When a celebrity posts and 500M notifications must be created instantly; solved with message queues like Kafka ✓
- C) When the feed algorithm runs too slowly; solved with Redis caching
- D) When the CDN fails; solved with S3 replication

**Q3.** Instagram switched from chronological feed to algorithmic feed in 2016. What does the algorithm actually predict?
- A) Which posts were uploaded most recently
- B) Which posts have the most likes globally
- C) How likely a specific user is to engage with a specific post, based on their history ✓
- D) Which posts contain the most hashtags

**Q4.** Why does Instagram store Cristiano Ronaldo's profile data in Redis rather than querying PostgreSQL each time? What is the trade-off?

**Q5.** Stories disappear after 24 hours, but Posts are permanent. What is the technical mechanism that makes Stories expire, and why does this design make sense from a storage cost perspective?

**Q6.** A Reel uses "adaptive bitrate streaming." What does this mean for the viewer?
- A) The video always plays in the highest quality regardless of connection speed
- B) The video pauses every 30 seconds to check your connection
- C) The phone automatically switches video quality up or down based on available WiFi or 4G speed ✓
- D) Reels are pre-downloaded to your phone when connected to WiFi

**Q7.** Instagram is free to use. Explain the full business model: what is being sold, to whom, and how is it priced?

**Q8 (explain in your own words).** The session describes a "two-stage recommendation system" for the Explore page. Imagine you are designing the same system for a football highlights app — one that recommends clips to users. Describe what Stage 1 (candidate generation) and Stage 2 (ranking) would each do, and what signals you would use in each stage.

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — Without a CDN, all users worldwide would fetch photos from a single origin server (e.g., in California), adding hundreds of milliseconds of latency. CDN nodes in Mumbai, Frankfurt, and Singapore serve content locally, reducing photo load time from ~300ms to ~20ms.

**Q2.** B — When a user with 500 million followers posts, Instagram must create 500 million notification tasks near-simultaneously. Apache Kafka (or similar message queues) queues these tasks and distributes them across thousands of worker servers processing in parallel.

**Q3.** C — The algorithm is a machine learning model that predicts the probability a specific user will like, comment on, or save a specific post, based on that user's historical behaviour (likes, pauses, DMs, profile views).

**Q4.** Redis is an in-memory database — reads take under 1ms versus 5–50ms for PostgreSQL on disk. For data accessed by millions of users simultaneously (like Ronaldo's profile), caching in Redis prevents millions of identical database queries. The trade-off is memory cost and the need to keep the cache up to date when the underlying data changes.

**Q5.** Stories are stored with a TTL (Time-To-Live) field in the database. When 24 hours elapse, the database automatically marks them for deletion and the CDN purges the cached versions. This makes sense because temporary content does not need to be retained indefinitely — it reduces storage costs significantly for content most users watch once.

**Q6.** C — Adaptive bitrate streaming monitors connection speed in real time. On fast WiFi, the phone requests 1080p video chunks; on slow 4G, it switches to 360p chunks seamlessly. This prevents buffering while maintaining the best possible quality the connection allows.

**Q7.** Users' attention is the product. Meta sells advertisers the ability to show targeted ads to users based on detailed behavioural and demographic profiles. Advertisers bid in a real-time auction (completing in ~50ms per ad slot) and pay per 1,000 impressions (CPM) or per click (CPC). Instagram generated ~$32 billion in ad revenue in 2022 this way.

**Q8.** Model answer: Stage 1 (candidate generation) — from millions of clips available, quickly narrow to ~1,000 candidates relevant to this user. Signals: clips from teams and leagues the user has watched before, clips featuring players they follow, clips trending globally in the last 24 hours. Use a fast, simpler model (e.g., nearest-neighbour on user embeddings). Stage 2 (ranking) — score the 1,000 candidates precisely using a deep neural network. Signals: how long the user historically watches clips of similar type, whether they share or replay clips, their preferred clip length, time of day (short clips in the morning, longer ones at night). The top 20 are shown in the recommended feed.

---

## 📚 Research Materials

> 💡 **Start here:** Watch the "System Design Interview — Instagram" walkthrough by Gaurav Sen on YouTube — it takes the exact concepts from this session and shows how an engineer would sketch them in a real interview in under 20 minutes.

### 🎬 Films & Documentaries

| Title | Year | What to watch for |
|---|---|---|
| [The Social Network](https://www.imdb.com/title/tt1285016/) | 2010 | Fiction, but accurate on the early scaling challenges of a social platform — database overload, caching, and the move from dorm room to data centre |
| [The Social Dilemma](https://www.thesocialdilemma.com/) | 2020 | Former Instagram and Facebook engineers explain how the recommendation algorithm was designed to maximise engagement |
| [Break Point (Netflix series)](https://www.netflix.com/title/81482279/) | 2023 | Not a tech doc, but shows how sports media organisations use short-form video and engagement mechanics similar to Instagram's Reels |
| [Coded Bias](https://www.imdb.com/title/tt11394170/) | 2020 | Documentary on bias in algorithmic systems including ad targeting and recommendation engines |

### 📺 YouTube

| Channel | Video | Link |
|---|---|---|
| Gaurav Sen | System Design Interview — Design Instagram | [youtube.com/watch?v=QmX2NPkJTKg](https://www.youtube.com/watch?v=QmX2NPkJTKg) |
| ByteByteGo | How Instagram Scaled to 1 Billion Users | *search "ByteByteGo Instagram scale system design"* |
| Fireship | CDN Explained in 100 Seconds | *search "Fireship CDN 100 seconds"* |
| Gaurav Sen | Consistent Hashing — System Design | [youtube.com/watch?v=zaRkONvyGr8](https://www.youtube.com/watch?v=zaRkONvyGr8) |
| Hussain Nasser | Apache Kafka Explained — Message Queues for Beginners | *search "Hussain Nasser Kafka explained beginners"* |
| Google Developers | How Google Search Works (Crawling, Indexing, Ranking) | [youtube.com/watch?v=BNHR6IQJGZs](https://www.youtube.com/watch?v=BNHR6IQJGZs) |

### 📖 Books

| Title | Author | Level | What it covers |
|---|---|---|---|
| *Designing Data-Intensive Applications* | Martin Kleppmann | Hard | The definitive book on databases, replication, partitioning, and the systems that power apps like Instagram at scale |
| *System Design Interview — An Insider's Guide* | Alex Xu | Medium | Step-by-step walkthroughs of 15 real system design problems (including social media feeds and CDN design) |
| *The Art of Scalability* | Abbott & Fisher | Medium | Practical framework for scaling web applications; covers the database, caching, and microservices layers described in this session |
| *No Filter: The Inside Story of Instagram* | Sarah Frier | Easy | Narrative account of Instagram's founding, growth, and acquisition by Facebook — the human story behind the technical architecture |
| *Hooked* | Nir Eyal | Easy | How consumer products (including Instagram) are designed to build habits; explains the psychology behind the engagement loop the recommendation algorithm exploits |

### 🌐 Articles & Interactive Resources

| Resource | Link | What it covers |
|---|---|---|
| Instagram Engineering Blog | [engineering.fb.com/tag/instagram/](https://engineering.fb.com/tag/instagram/) | First-hand engineering posts from the Instagram team on scaling, machine learning, and infrastructure decisions |
| High Scalability — Instagram Architecture | [highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users.html](http://highscalability.com/blog/2011/12/6/instagram-architecture-14-million-users.html) | Classic breakdown of Instagram's early architecture decisions — CDN, PostgreSQL, Redis, Django |
| ByteByteGo System Design Newsletter | [blog.bytebytego.com](https://blog.bytebytego.com) | Weekly newsletter with clear visual explanations of how large-scale systems are built |
| Redis Documentation — Caching Patterns | [redis.io/docs/manual/patterns/](https://redis.io/docs/manual/patterns/) | Official guide to the caching patterns (cache-aside, write-through) described in this session |
| Cloudflare Learning Centre — What is a CDN? | [cloudflare.com/learning/cdn/what-is-a-cdn/](https://www.cloudflare.com/learning/cdn/what-is-a-cdn/) | Clear, visual explanation of how CDNs work with real latency diagrams |

### 🔗 People to Look Up

- **Kevin Systrom** — Co-founder and former CEO of Instagram; his technical and product decisions from 2010–2018 are the subject of this entire session
- **Mike Krieger** — Co-founder and former CTO of Instagram; a Brazilian-born engineer who built and scaled the original infrastructure from zero to one billion users
- **Adam Mosseri** — Current Head of Instagram; his public posts and interviews explain how the recommendation algorithm and ranking system work in plain language
- **Jeff Dean** — Google Senior Fellow who designed the infrastructure (Bigtable, MapReduce, Spanner) that influenced how every large-scale platform including Instagram thinks about distributed data
- **Werner Vogels** — CTO of Amazon/AWS; Instagram ran on AWS; his writing on distributed systems and the "eventually consistent" database model is fundamental to understanding how Instagram's data layer works
- **Andrej Karpathy** — His work on deep learning at Tesla and OpenAI is directly relevant to understanding how Instagram's recommendation neural networks are designed and trained
