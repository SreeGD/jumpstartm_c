# Session 1.2 — Every Time You Open Instagram, 50 Things Happen in Half a Second
## How the Web Works

**Duration:** 2 hours  
**the teacher's prep:** Have Chrome DevTools open. Know how to open Network tab. Have the HTML template ready.

---

## 🎯 Goal

By the end of this session, Student understands:
- What happens step-by-step when you type a URL and hit Enter
- What DNS, HTTP, requests, responses, and status codes are
- The difference between HTML, CSS, and JavaScript
- What an API is
- How to build and view a basic HTML page (first webpage!)

---

## 📖 the teacher's Narrative

### Hook

*"Quick question — when you type youtube.com and press Enter, what actually happens?"*

Let Student guess. He'll probably say something like "it loads the website." That's true — but there are 8 distinct technical steps that happen in under a second. Today we learn all 8.

---

### Step 1 — DNS: The Internet's Phone Book

Every device on the internet has a numeric address — an **IP address**.  
`142.250.80.46` is one of Google's servers.

But nobody types IP addresses. We type `youtube.com`.

**DNS (Domain Name System)** translates the name into the number.

*"DNS is like your phone's contacts list. You search 'Mum' — the phone looks up her number. You type 'youtube.com' — DNS looks up its IP address."*

The lookup happens automatically, in milliseconds, through a chain of servers.

---

### Step 2 — TCP Connection: Establishing the Call

Your computer connects to the server using **TCP** (Transmission Control Protocol).  
Think of it as the phone call being picked up — both sides agree: *"I'm ready, let's talk."*

If it's **HTTPS** (the padlock in your browser), there's also an **SSL handshake** — a cryptographic agreement to encrypt all communication. Nobody can eavesdrop.

*"When you see the padlock, your browser and the server agreed on a secret code. Everything between them is scrambled for anyone else watching."*

---

### Step 3 — HTTP Request: Asking for Something

Now your browser sends a **request**. It looks like this:

```
GET /home HTTP/1.1
Host: youtube.com
User-Agent: Chrome/120
Accept: text/html
```

- **Method** — GET (I want something), POST (I'm sending data), DELETE, PUT...
- **Path** — Which page you want (`/home`, `/watch?v=abc`)
- **Headers** — Extra info: who you are, what format you want, your cookies

*"Every tap, every scroll, every search — your browser is sending a message to a server. This is the format of that message."*

---

### Step 4 — Server Processes and Responds

The server receives the request, figures out what to send back, and returns a **response**:

```
HTTP/1.1 200 OK
Content-Type: text/html

<!DOCTYPE html>
<html>...the actual page...</html>
```

**Status codes** — the server's one-number summary:
| Code | Meaning |
|------|---------|
| 200 | OK — here's what you asked for |
| 301 | Moved permanently — go here instead |
| 404 | Not Found — that page doesn't exist |
| 403 | Forbidden — you don't have permission |
| 500 | Server Error — something broke on our end |

*"404 you've definitely seen. Now you know what it means — the server is saying 'I can't find that path.'"*

---

### Step 5 — The Browser Builds the Page

The response body contains **HTML**. The browser reads it and builds the page.

Three languages work together:

| Language | Job | Analogy |
|----------|-----|---------|
| **HTML** | Structure and content | The skeleton |
| **CSS** | Visual design | The clothes and makeup |
| **JavaScript** | Behaviour and interactivity | The muscles |

The browser turns HTML tags into visual elements, applies CSS styles, and runs JavaScript for interactivity.

---

### Step 6 — APIs: Apps Talking to Apps

Not every server sends HTML. Some send pure data — usually **JSON** format.

```json
{
  "player": "Vinícius Jr",
  "goals": 24,
  "assists": 11,
  "club": "Real Madrid"
}
```

That's an **API** (Application Programming Interface) — a server that speaks data, not pages.

When Instagram loads your feed, it's making dozens of API calls: one for posts, one for stories, one for suggested accounts, one for ads. Each returns JSON. JavaScript assembles them into what you see.

*"Every app you've ever used is just a pretty face on top of API calls. The intelligence lives in the data, not the design."*

---

## ⚡ Wow Moment — Spy on the Internet

**Do this live with Student:**

1. Open Chrome. Go to any website — Instagram, YouTube, ESPN
2. Right-click → Inspect → Network tab
3. Refresh the page
4. Watch 50–100 requests light up in real time

Show Student:
- The status codes (green 200s, occasional 304s)
- The different types: Doc, Script, Image, XHR (API calls)
- Click on an XHR request — show the request headers and the JSON response
- The timing waterfall — how long each piece took

*"This is the internet. Every single time you use any app, this is what's happening invisibly. Now you can see it."*

Then find an API call returning JSON. Show the raw data.  
*"That JSON is what React or your app's JavaScript turns into the UI. The screen is just a rendering of this data."*

---

## 🔑 Key Concepts Checklist

- [ ] IP address — the actual numeric address of a server
- [ ] DNS — translates domain names to IP addresses
- [ ] HTTP — the protocol browsers and servers use to communicate
- [ ] HTTPS — encrypted HTTP (the padlock)
- [ ] Request — browser asking for something (method + path + headers)
- [ ] Response — server's reply (status code + body)
- [ ] Status codes — 200 OK, 404 Not Found, 500 Server Error
- [ ] HTML — structure, CSS — style, JavaScript — behaviour
- [ ] API — a server that returns data (JSON), not pages
- [ ] JSON — the data format apps use to communicate

---

## Teaching Notes for Teacher

- The DevTools demo is the session highlight. Spend time here.
- Don't go deep on TCP/IP internals — just "they agree to connect."
- JSON is important. Student will use it constantly from Session 4 onwards.
- The HTML lab is light — it's just to make the web feel tangible and owned.
- Great question to ask: *"When you POST a login form, where does your password go?"* (It goes in the request body, encrypted by HTTPS.) Leads naturally to a security conversation.

---

## 🧪 Quiz

*Complete after the session. Bring answers to the next class.*

**Q1.** You type `espn.com` into your browser. Before your computer can connect to ESPN's server, it needs to find the server's numeric address. What system handles this lookup, and what is the numeric address format called?
- A) TCP performs the lookup; the format is called a port number
- B) DNS (Domain Name System) performs the lookup; the numeric format is an IP address ✓
- C) HTTP performs the lookup; the numeric format is a MAC address
- D) SSL performs the lookup; the numeric format is a subnet mask

**Q2.** You receive a server response with status code 404. What does this tell you, and who is "at fault" — the client (your browser) or the server?

**Q3.** What is the difference between HTTP and HTTPS? What does the padlock icon in your browser actually mean technically?
- A) HTTPS is faster than HTTP because it uses compressed headers
- B) HTTPS adds SSL/TLS encryption — the browser and server perform a cryptographic handshake so all data is scrambled and unreadable to anyone intercepting the connection ✓
- C) HTTPS uses a different port that is reserved for premium websites
- D) HTTPS means the website has been verified as legitimate by Google

**Q4.** Explain in your own words the roles of HTML, CSS, and JavaScript. If a football club's website suddenly had no CSS applied, what would you see?

**Q5.** When Instagram loads your feed, it doesn't make a single request for the whole page. What technology does it use to fetch posts, stories, and ads separately, and in what data format does the server return that information?
- A) It uses FTP to request files; data arrives as XML
- B) It uses API calls (typically over HTTP); data arrives as JSON ✓
- C) It uses direct database queries from the browser; data arrives as CSV
- D) It uses WebSockets for everything; data arrives as binary streams

**Q6.** What is the difference between a GET request and a POST request? Give one real example of each from a website you use regularly.

**Q7.** You open Chrome DevTools on the Network tab and refresh YouTube. You see requests with types labelled "Doc", "Script", "Img", and "XHR". What does "XHR" represent, and why is it interesting compared to the other types?
- A) XHR is the main HTML document — the skeleton of the page
- B) XHR (XMLHttpRequest) represents API calls — requests that return raw data (JSON) rather than rendered files, showing the app fetching dynamic content like video recommendations ✓
- C) XHR is the browser's internal error log
- D) XHR stands for "external HTML resource" — it's CSS loaded from a CDN

**Q8.** A status code of 500 appears on ESPN's website during a big match. Is this your problem to fix? What does it tell you about where in the system something went wrong?

---

*Answers are at the bottom of this file.*

## Quiz Answers

**Q1.** B — DNS translates human-readable domain names (like espn.com) into IP addresses (like 142.250.80.46) that routers can use to direct traffic. Without DNS, you'd have to memorise numeric addresses for every site.

**Q2.** A 404 means "Not Found" — the server received the request and understood it, but couldn't find the resource at that path. The client (browser) is technically at fault in the sense that it requested a path that doesn't exist, though it's often caused by a broken link on the server side.

**Q3.** B — HTTPS uses TLS (Transport Layer Security) to encrypt all data between browser and server. During the SSL/TLS handshake, both parties agree on encryption keys. Anyone intercepting packets sees scrambled data, not your passwords or personal information.

**Q4.** HTML provides the structure and content (headings, paragraphs, images, links). CSS controls visual appearance (colours, fonts, layout). JavaScript adds interactivity (button clicks, animations, live updates). Without CSS, you'd see raw unstyled HTML — plain black text on a white background, no layout, no colours, no branding.

**Q5.** B — Modern apps like Instagram separate the data layer (API calls returning JSON) from the presentation layer (JavaScript that renders that data). This is why Instagram can update your feed without reloading the whole page.

**Q6.** GET retrieves data without changing anything on the server — e.g. searching Google or loading a YouTube video page. POST sends data to the server to create or change something — e.g. submitting a login form, posting a comment, or placing an order. GET parameters appear in the URL; POST data travels in the request body.

**Q7.** B — XHR/Fetch requests are the API calls your app makes to fetch dynamic data. Unlike Doc (HTML), Script (JavaScript), or Img (images), XHR returns JSON — raw data the JavaScript code then uses to populate what you see. Watching XHR requests shows you what data the app is actually working with behind the rendered interface.

**Q8.** A 500 error is a Server Error — something broke on ESPN's servers, not in your browser. It's not your problem to fix. It tells you the server received the request but failed while trying to process it, likely due to a bug, overload, or database failure on their end.

---

## 📚 Research Materials

> 💡 **Start here:** Watch "How the Internet Works in 5 Minutes" by Aaron (https://www.youtube.com/watch?v=7_LPdttKXPc) — it covers DNS, TCP, and HTTP with clear animations and is the fastest way to cement the 8-step journey from URL to page load.

### 🎬 Films & Documentaries

| Title | Year | What to Watch For |
|-------|------|-------------------|
| *Lo and Behold: Reveries of the Connected World* | 2016 | Werner Herzog documentary tracing the internet from ARPANET to today; features Vint Cerf and early pioneers discussing the web's design decisions |
| *The Internship* | 2013 | Lighthearted but shows real Google infrastructure; pay attention to the servers scene — those are the machines answering your HTTP requests |
| *We Are Legion: The Story of the Hacktivists* | 2012 | Shows how HTTP, DNS, and server vulnerabilities work in practice — a real-world lens on what happens when the web's protocols are exploited |

### 📺 YouTube

| Video / Channel | Link | Why Watch |
|-----------------|------|-----------|
| "How the Internet Works in 5 Minutes" — Aaron | https://www.youtube.com/watch?v=7_LPdttKXPc | Clear animated overview of DNS, TCP/IP, and HTTP; best 5-minute introduction |
| "DNS Explained" — Computerphile | https://www.youtube.com/watch?v=72snZctFFtA | Professor explains DNS hierarchy step by step; exactly what happens when you type a URL |
| "HTTP Crash Course" — Traversy Media | https://www.youtube.com/watch?v=iYM2zFP3Zn0 | Covers request methods, headers, status codes — everything from the lesson in 30 minutes |
| "How HTTPS Works" — ByteByteGo | https://www.youtube.com/watch?v=j9QmMEWmcfo | Animated walkthrough of the TLS handshake and why HTTPS protects your data |
| "What is a REST API?" — Fireship | https://www.youtube.com/watch?v=-MTSQjw5DrM | Fast, visual explanation of REST, HTTP methods, and JSON — 5 minutes |
| "How Browsers Work" — Google Chrome Developers | https://www.youtube.com/watch?v=0IsQqJ7pwhw | Inside Chrome's rendering pipeline: HTML parsing, CSS layout, JavaScript execution |

### 📖 Books

| Title | Author | Level | Covers |
|-------|--------|-------|--------|
| *How the Internet Works* | Preston Gralla | Easy | Illustrated guide to DNS, TCP/IP, HTTP, and web infrastructure — visual and accessible |
| *HTTP: The Definitive Guide* | Gourley & Totty | Medium | Deep reference on HTTP protocol, headers, methods, and caching — essential for web developers |
| *Web Scalability for Startup Engineers* | Artur Ejsmont | Medium–Hard | How large companies (Instagram, YouTube) architect their web systems — extends the API discussion from this session |
| *Weaving the Web* | Tim Berners-Lee | Easy | First-person account of inventing the World Wide Web; describes the design decisions behind URLs, HTTP, and HTML |

### 🌐 Articles & Interactive Resources

| Resource | URL | What It Covers |
|----------|-----|----------------|
| "How DNS Works" — comic | https://howdns.works | A comic-strip walkthrough of DNS resolution — free, visual, and memorable |
| MDN Web Docs: HTTP Overview | https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview | The authoritative reference on HTTP methods, headers, and status codes |
| "What happens when you type google.com?" — GitHub | https://github.com/alex/what-happens-when | Exhaustive technical breakdown of every step from keystroke to rendered page |
| HTTP Status Cats | https://http.cat | Status codes illustrated with cats — ridiculous but you will never forget what 404 means |
| Chrome DevTools Documentation | https://developer.chrome.com/docs/devtools/network | Official guide to the Network tab used in the session's live demo |

### 🔗 People to Look Up

- **Tim Berners-Lee** — Invented the World Wide Web in 1989 at CERN; designed the original HTTP protocol, HTML, and the URL format used in this session.
- **Vint Cerf** — Co-designed TCP/IP with Bob Kahn in the 1970s; the protocols that underpin every internet connection are largely his work.
- **Marc Andreessen** — Co-wrote Mosaic (1993), the first graphical web browser; later co-founded Netscape, which popularised the web for ordinary users.
- **Brendan Eich** — Created JavaScript in 10 days in 1995 at Netscape; the language that makes every interactive web page work is entirely his invention.
- **Roy Fielding** — Defined REST (Representational State Transfer) in his 2000 doctoral dissertation; the architectural style behind every modern API.
