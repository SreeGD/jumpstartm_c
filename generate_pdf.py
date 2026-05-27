"""
Generate a printable HTML curriculum document.

Usage:
    python3 generate_pdf.py

Output:
    curriculum_advaith.html  ← open in Chrome, then Cmd+P → Save as PDF

To get the best PDF:
    1. Open curriculum_advaith.html in Chrome
    2. Press Cmd+P (Mac) or Ctrl+P (Windows)
    3. Destination → Save as PDF
    4. More settings → Paper size: A4, Margins: Default
    5. ✓ Background graphics  ← check this for coloured headers
    6. Save
"""

import os
import markdown
from pathlib import Path

BASE = Path(__file__).parent

# ─────────────────────────────────────────
# CURRICULUM STRUCTURE
# ─────────────────────────────────────────

SESSIONS = [
    {
        "id": "session_1_history",
        "title": "Session 1 — History of Computing",
        "subtitle": "The Greatest Heist in History",
        "color": "#e94560",
        "emoji": "🕰️",
    },
    {
        "id": "session_1_1_building_blocks",
        "title": "Session 1.1 — Building Blocks",
        "subtitle": "What's Actually Inside the Box",
        "color": "#e94560",
        "emoji": "⚡",
    },
    {
        "id": "session_1_2_web",
        "title": "Session 1.2 — How the Web Works",
        "subtitle": "Every Time You Open Instagram, 50 Things Happen",
        "color": "#e94560",
        "emoji": "🌐",
    },
    {
        "id": "session_2_maths",
        "title": "Session 2 — Maths for Computing",
        "subtitle": "Math Is the Operating System of Reality",
        "color": "#7c3aed",
        "emoji": "🔢",
    },
    {
        "id": "session_3_languages",
        "title": "Session 3 — Programming Languages",
        "subtitle": "The Family Tree of Code",
        "color": "#7c3aed",
        "emoji": "🌍",
    },
    {
        "id": "session_4_python",
        "title": "Session 4 — Python",
        "subtitle": "Math with Superpowers",
        "color": "#0891b2",
        "emoji": "🐍",
    },
    {
        "id": "session_5_math_stats_ai",
        "title": "Session 5 — Math & Stats for AI",
        "subtitle": "The Engine Behind Every AI",
        "color": "#0891b2",
        "emoji": "🧠",
    },
    {
        "id": "session_6_agentic_ai",
        "title": "Session 6 — Agentic AI",
        "subtitle": "The Thing That Changes Everything",
        "color": "#059669",
        "emoji": "🤖",
    },
    {
        "id": "session_7_quant_finance",
        "title": "Session 7 — Quant Finance",
        "subtitle": "Hedge Funds Are Just Applied Math",
        "color": "#059669",
        "emoji": "📈",
    },
    {
        "id": "session_8_capstone",
        "title": "Session 8 — Capstone Project",
        "subtitle": "Build Something Real",
        "color": "#d97706",
        "emoji": "🏆",
    },
    {
        "id": "session_9_software_engineering",
        "title": "Session 9 — Software Engineering Landscape",
        "subtitle": "How the Profession Evolved: 2010 → 2026",
        "color": "#6b7280",
        "emoji": "🏗️",
    },
    {
        "id": "session_10_instagram",
        "title": "Session 10 — How Instagram Works",
        "subtitle": "The Billion-Dollar Engineering Inside the App You Use Every Day",
        "color": "#e1306c",
        "emoji": "📸",
    },
]


# ─────────────────────────────────────────
# READ MARKDOWN FILES
# ─────────────────────────────────────────

def read_md(path: Path) -> str:
    """Read a markdown file and convert to HTML"""
    if not path.exists():
        return f'<p class="missing">File not found: {path}</p>'
    text = path.read_text(encoding="utf-8")
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "codehilite", "toc"]
    )

def collect_labs(session_id: str) -> list[tuple[str, str]]:
    """Collect all lab files for a session"""
    labs_dir = BASE / session_id / "labs"
    if not labs_dir.exists():
        return []
    labs = []
    for f in sorted(labs_dir.iterdir()):
        if f.suffix in (".py", ".md", ".html"):
            name = f.name
            content = f.read_text(encoding="utf-8")
            if f.suffix == ".py":
                html = f'<pre class="code-block"><code>{escape_html(content)}</code></pre>'
            elif f.suffix == ".html":
                html = f'<pre class="code-block"><code>{escape_html(content)}</code></pre>'
            else:
                html = markdown.markdown(content, extensions=["tables", "fenced_code"])
            labs.append((name, html))
    return labs

def escape_html(text: str) -> str:
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


# ─────────────────────────────────────────
# HTML TEMPLATE
# ─────────────────────────────────────────

CSS = """
/* ── Reset & Base ── */
* { box-sizing: border-box; margin: 0; padding: 0; }

body {
    font-family: 'Georgia', serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a2e;
    background: #ffffff;
}

/* ── Cover Page ── */
.cover {
    page-break-after: always;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    min-height: 100vh;
    background: linear-gradient(135deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    color: white;
    text-align: center;
    padding: 60px 40px;
}
.cover-badge {
    background: #e94560;
    color: white;
    padding: 6px 20px;
    border-radius: 20px;
    font-size: 10pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 30px;
    font-family: 'Arial', sans-serif;
}
.cover h1 {
    font-size: 36pt;
    font-weight: bold;
    margin-bottom: 10px;
    color: white;
}
.cover .cover-sub {
    font-size: 16pt;
    color: #00d4aa;
    margin-bottom: 40px;
}
.cover-divider {
    width: 80px;
    height: 3px;
    background: #e94560;
    margin: 30px auto;
}
.cover-meta {
    font-family: 'Arial', sans-serif;
    font-size: 11pt;
    color: #ccc;
    line-height: 2;
}
.cover-meta strong { color: white; }
.cover-sessions {
    margin-top: 50px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    max-width: 500px;
    text-align: left;
}
.cover-session-item {
    font-family: 'Arial', sans-serif;
    font-size: 9pt;
    color: #aaa;
    padding: 4px 10px;
    border-left: 2px solid #e94560;
}
.cover-session-item span { color: white; }

/* ── Table of Contents ── */
.toc-page {
    page-break-after: always;
    padding: 60px 60px;
}
.toc-page h2 {
    font-size: 22pt;
    color: #1a1a2e;
    border-bottom: 3px solid #e94560;
    padding-bottom: 12px;
    margin-bottom: 30px;
}
.toc-entry {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    padding: 8px 0;
    border-bottom: 1px dotted #ddd;
    font-family: 'Arial', sans-serif;
}
.toc-entry:hover { background: #f9f9f9; }
.toc-num { color: #e94560; font-weight: bold; min-width: 80px; font-size: 10pt; }
.toc-title { flex: 1; font-size: 11pt; }
.toc-subtitle { color: #888; font-size: 9pt; font-style: italic; margin-left: 10px; }

/* ── Session Chapters ── */
.session-chapter {
    page-break-before: always;
}
.session-header {
    padding: 40px 60px 30px;
    color: white;
    margin-bottom: 0;
}
.session-header .session-label {
    font-family: 'Arial', sans-serif;
    font-size: 9pt;
    letter-spacing: 3px;
    text-transform: uppercase;
    opacity: 0.8;
    margin-bottom: 8px;
}
.session-header h1 {
    font-size: 24pt;
    margin-bottom: 8px;
    color: white;
}
.session-header .session-subtitle {
    font-size: 13pt;
    opacity: 0.85;
    font-style: italic;
}

/* ── Content Areas ── */
.content-body {
    padding: 30px 60px;
}

/* Section blocks */
.section-block {
    margin-bottom: 30px;
    border-left: 4px solid #e0e0e0;
    padding-left: 20px;
}
.section-block.lesson { border-left-color: #3b82f6; }
.section-block.lab    { border-left-color: #10b981; }
.section-block.assign { border-left-color: #f59e0b; }

.section-label {
    font-family: 'Arial', sans-serif;
    font-size: 8pt;
    letter-spacing: 2px;
    text-transform: uppercase;
    font-weight: bold;
    margin-bottom: 12px;
    padding: 3px 10px;
    display: inline-block;
    border-radius: 3px;
    color: white;
}
.lesson .section-label { background: #3b82f6; }
.lab    .section-label { background: #10b981; }
.assign .section-label { background: #f59e0b; }

/* ── Markdown content styles ── */
.content-body h1, .content-body h2 {
    font-size: 15pt;
    color: #1a1a2e;
    margin: 20px 0 10px;
    padding-bottom: 5px;
    border-bottom: 1px solid #eee;
}
.content-body h3 {
    font-size: 12pt;
    color: #374151;
    margin: 15px 0 8px;
}
.content-body h4 {
    font-size: 11pt;
    color: #4b5563;
    margin: 12px 0 6px;
}
.content-body p {
    margin-bottom: 10px;
}
.content-body ul, .content-body ol {
    margin: 8px 0 12px 24px;
}
.content-body li { margin-bottom: 4px; }
.content-body blockquote {
    border-left: 4px solid #e94560;
    padding: 10px 20px;
    background: #fef7f7;
    margin: 15px 0;
    color: #374151;
    font-style: italic;
}
.content-body table {
    width: 100%;
    border-collapse: collapse;
    margin: 15px 0;
    font-family: 'Arial', sans-serif;
    font-size: 9.5pt;
}
.content-body th {
    background: #1a1a2e;
    color: white;
    padding: 8px 12px;
    text-align: left;
}
.content-body td {
    padding: 7px 12px;
    border-bottom: 1px solid #e5e7eb;
}
.content-body tr:nth-child(even) td { background: #f9fafb; }

/* Code blocks */
.content-body pre, .code-block {
    background: #1e1e2e;
    color: #cdd6f4;
    padding: 16px 20px;
    border-radius: 6px;
    font-family: 'Courier New', monospace;
    font-size: 8.5pt;
    overflow-x: auto;
    margin: 12px 0;
    white-space: pre-wrap;
    word-wrap: break-word;
    line-height: 1.5;
}
.content-body code {
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    background: #f1f5f9;
    padding: 1px 5px;
    border-radius: 3px;
    color: #e94560;
}
.content-body pre code {
    background: none;
    color: #cdd6f4;
    padding: 0;
}

/* Checkboxes */
.content-body input[type="checkbox"] { margin-right: 8px; }

/* ── Dividers ── */
.section-divider {
    border: none;
    border-top: 2px dashed #e5e7eb;
    margin: 30px 0;
}

/* ── Footer ── */
.page-footer {
    text-align: center;
    font-family: 'Arial', sans-serif;
    font-size: 8pt;
    color: #9ca3af;
    padding: 20px 60px;
    border-top: 1px solid #e5e7eb;
    margin-top: 40px;
}

/* ── Quick Reference Card ── */
.quick-ref {
    page-break-before: always;
    padding: 40px 60px;
}
.quick-ref h2 {
    font-size: 20pt;
    color: #1a1a2e;
    border-bottom: 3px solid #e94560;
    padding-bottom: 10px;
    margin-bottom: 25px;
}
.era-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-top: 20px;
}
.era-card {
    border: 1px solid #e5e7eb;
    border-radius: 8px;
    padding: 12px 15px;
    border-top: 4px solid #e94560;
}
.era-card .era-year {
    font-family: 'Arial', sans-serif;
    font-size: 9pt;
    color: #6b7280;
    margin-bottom: 3px;
}
.era-card .era-title {
    font-weight: bold;
    font-size: 10pt;
    color: #1a1a2e;
    margin-bottom: 4px;
}
.era-card .era-tech {
    font-size: 8.5pt;
    color: #6b7280;
    font-style: italic;
}

/* ── Print Overrides ── */
@media print {
    body { font-size: 10pt; }
    .cover { background: #1a1a2e !important; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .session-header { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .content-body pre, .code-block { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .content-body th { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    .section-label { -webkit-print-color-adjust: exact; print-color-adjust: exact; }
    a { text-decoration: none; color: inherit; }
    pre { page-break-inside: avoid; }
    h1, h2, h3 { page-break-after: avoid; }
    .session-chapter { page-break-before: always; }
}
"""

def build_toc(sessions):
    rows = ""
    for i, s in enumerate(sessions):
        num = s["title"].split("—")[0].strip()
        title = s["title"].split("—")[1].strip() if "—" in s["title"] else s["title"]
        rows += f"""
        <div class="toc-entry">
            <span class="toc-num">{s['emoji']} {num}</span>
            <span class="toc-title">{title}</span>
            <span class="toc-subtitle">— {s['subtitle']}</span>
        </div>"""
    return rows

def build_session_html(session):
    sid   = session["id"]
    color = session["color"]
    emoji = session["emoji"]
    title = session["title"]
    sub   = session["subtitle"]

    # Lesson
    lesson_html = read_md(BASE / sid / "lesson.md")

    # Labs
    labs = collect_labs(sid)
    labs_html = ""
    for lab_name, lab_content in labs:
        labs_html += f'<h3>📄 {lab_name}</h3>\n{lab_content}\n<hr class="section-divider">\n'
    if not labs_html:
        labs_html = "<p><em>No lab files for this session.</em></p>"

    # Assignment
    assign_html = read_md(BASE / sid / "assignments" / "assignment.md")
    if not assign_html:
        assign_html = "<p><em>No assignment for this session.</em></p>"

    return f"""
    <div class="session-chapter" id="{sid}">
        <div class="session-header" style="background: linear-gradient(135deg, {color}dd, {color}99);">
            <div class="session-label">{emoji} Curriculum</div>
            <h1>{title}</h1>
            <div class="session-subtitle">{sub}</div>
        </div>

        <div class="content-body">

            <div class="section-block lesson">
                <span class="section-label">📖 Lesson — the teacher's Teaching Guide</span>
                {lesson_html}
            </div>

            <hr class="section-divider">

            <div class="section-block lab">
                <span class="section-label">🔧 Labs — Hands-On Activities</span>
                {labs_html}
            </div>

            <hr class="section-divider">

            <div class="section-block assign">
                <span class="section-label">📝 Assignment — the student's Independent Work</span>
                {assign_html}
            </div>

        </div>

        <div class="page-footer">
            NITW M&C Prep · Student · {title} · Taught by Teacher
        </div>
    </div>
    """

def build_quick_ref():
    eras = [
        ("2010", "Java, OOP & Web Fundamentals", "Java · HTML/CSS/JS · server-side basics"),
        ("2012", "Python & JavaScript",           "Python scripting · Node.js · frontend"),
        ("2014", "SPA & TypeScript",              "React/Angular · single-page apps · TypeScript"),
        ("2015", "Spring Boot & REST APIs",       "Backend frameworks · REST · enterprise patterns"),
        ("2016", "Microservices & DevOps",        "Docker · CI/CD · service decomposition"),
        ("2017", "Cloud Engineering",             "AWS/Azure/GCP · managed services · IaC"),
        ("2020", "Kubernetes & Observability",    "Container orchestration · logs · metrics · tracing"),
        ("2023", "Platform Engineering",          "Golden paths · shift-left security · IDPs"),
        ("2026", "AI-Assisted Engineering",       "Code copilots · agents · LLM-native apps"),
    ]
    cards = ""
    for year, title, tech in eras:
        cards += f"""
        <div class="era-card">
            <div class="era-year">{year}</div>
            <div class="era-title">{title}</div>
            <div class="era-tech">{tech}</div>
        </div>"""
    return f"""
    <div class="quick-ref">
        <h2>⚡ Quick Reference — Software Engineering Eras (Session 9)</h2>
        <div class="era-grid">{cards}</div>

        <h2 style="margin-top:40px">🗺️ Two-Month Roadmap</h2>
        <table>
            <tr><th>Week</th><th>Sessions</th><th>Key Output</th></tr>
            <tr><td>Week 1</td><td>1 + 1.1 + 1.2</td><td>Computing timeline · Logic gates · First webpage</td></tr>
            <tr><td>Week 2</td><td>2 + 3</td><td>Caesar cipher · Passing network · Fibonacci</td></tr>
            <tr><td>Week 3–4</td><td>4</td><td>4 Python projects: waves · guessing game · charts · dice</td></tr>
            <tr><td>Week 5</td><td>5</td><td>xG model · dot products · correlation analysis</td></tr>
            <tr><td>Week 6</td><td>6</td><td>Sports analyst AI agent (Claude API)</td></tr>
            <tr><td>Week 7</td><td>7 + 9</td><td>Stock analysis · Man United · SE landscape</td></tr>
            <tr><td>Week 8</td><td>8</td><td>Capstone project · Demo day</td></tr>
        </table>

        <h2 style="margin-top:40px">🛠️ Setup Checklist</h2>
        <table>
            <tr><th>Tool</th><th>When Needed</th><th>How to Install</th></tr>
            <tr><td>Python 3.11+</td><td>Session 4</td><td>python.org/downloads</td></tr>
            <tr><td>VS Code</td><td>Session 4</td><td>code.visualstudio.com</td></tr>
            <tr><td>Python extension</td><td>Session 4</td><td>VS Code Extensions tab → "Python"</td></tr>
            <tr><td>matplotlib, numpy, pandas</td><td>Session 4</td><td><code>pip install matplotlib numpy pandas</code></td></tr>
            <tr><td>networkx</td><td>Session 2</td><td><code>pip install networkx</code></td></tr>
            <tr><td>yfinance</td><td>Session 7</td><td><code>pip install yfinance</code></td></tr>
            <tr><td>anthropic</td><td>Session 6</td><td><code>pip install anthropic</code></td></tr>
            <tr><td>Anthropic API key</td><td>Session 6</td><td>console.anthropic.com</td></tr>
        </table>
    </div>
    """


# ─────────────────────────────────────────
# ASSEMBLE FINAL HTML
# ─────────────────────────────────────────

def generate():
    # Cover page
    session_list_html = ""
    for s in SESSIONS:
        session_list_html += f'<div class="cover-session-item">{s["emoji"]} <span>{s["title"]}</span></div>'

    cover = f"""
    <div class="cover">
        <div class="cover-badge">NITW M&amp;C Preparation · 2026</div>
        <h1>the student's Curriculum</h1>
        <div class="cover-sub">Computing · Math · AI · Quant Finance · Software Engineering</div>
        <div class="cover-divider"></div>
        <div class="cover-meta">
            <strong>Student:</strong> Student &nbsp;·&nbsp; <strong>Teacher:</strong> Teacher<br>
            <strong>Duration:</strong> 2 months &nbsp;·&nbsp; <strong>Sessions:</strong> 11<br>
            <strong>Starting Point:</strong> 12th PCM done, zero coding experience<br>
            <strong>Goal:</strong> NITW M&amp;C ready — computing, AI, and quant finance
        </div>
        <div class="cover-sessions">{session_list_html}</div>
    </div>
    """

    # TOC
    toc = f"""
    <div class="toc-page">
        <h2>📚 Table of Contents</h2>
        {build_toc(SESSIONS)}
    </div>
    """

    # All sessions
    sessions_html = ""
    for session in SESSIONS:
        print(f"  Building: {session['title']} ...")
        sessions_html += build_session_html(session)

    # Quick reference
    quick_ref = build_quick_ref()

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>the student's NITW M&C Curriculum — Teacher</title>
    <style>{CSS}</style>
</head>
<body>
    {cover}
    {toc}
    {sessions_html}
    {quick_ref}
</body>
</html>"""

    out_path = BASE / "curriculum_advaith.html"
    out_path.write_text(html, encoding="utf-8")
    print(f"\n✅ Generated: {out_path}")
    print(f"   Size: {out_path.stat().st_size / 1024:.0f} KB")
    print()
    print("📄 To save as PDF:")
    print("   1. Open the file in Chrome")
    print("   2. Press Cmd+P (Mac) or Ctrl+P (Windows)")
    print("   3. Destination → Save as PDF")
    print("   4. More settings:")
    print("      • Paper size: A4")
    print("      • Margins: Default")
    print("      • ✓ Background graphics  ← important for coloured headers")
    print("   5. Save")

if __name__ == "__main__":
    print("🏗️  Building curriculum HTML...\n")
    generate()
