# Session 1.2 — Every Time You Open Instagram, 50 Things Happen in Half a Second
## How the Web Works

**Duration:** 2 hours  
**Sree's prep:** Have Chrome DevTools open. Know how to open Network tab. Have the HTML template ready.

---

## 🎯 Goal

By the end of this session, Advaith understands:
- What happens step-by-step when you type a URL and hit Enter
- What DNS, HTTP, requests, responses, and status codes are
- The difference between HTML, CSS, and JavaScript
- What an API is
- How to build and view a basic HTML page (first webpage!)

---

## 📖 Sree's Narrative

### Hook

*"Quick question — when you type youtube.com and press Enter, what actually happens?"*

Let Advaith guess. He'll probably say something like "it loads the website." That's true — but there are 8 distinct technical steps that happen in under a second. Today we learn all 8.

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

**Do this live with Advaith:**

1. Open Chrome. Go to any website — Instagram, YouTube, ESPN
2. Right-click → Inspect → Network tab
3. Refresh the page
4. Watch 50–100 requests light up in real time

Show Advaith:
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

## Teaching Notes for Sree

- The DevTools demo is the session highlight. Spend time here.
- Don't go deep on TCP/IP internals — just "they agree to connect."
- JSON is important. Advaith will use it constantly from Session 4 onwards.
- The HTML lab is light — it's just to make the web feel tangible and owned.
- Great question to ask: *"When you POST a login form, where does your password go?"* (It goes in the request body, encrypted by HTTPS.) Leads naturally to a security conversation.
