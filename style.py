"""Shared Jeopardy-themed, mobile-friendly CSS with a muted, modern palette."""

JEOPARDY_CSS = """
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700;800&display=swap" rel="stylesheet">
<style>
:root {
    --bg: #1b2540;
    --panel: #25325a;
    --accent: #d8b46a;
    --accent-soft: #c9a86b;
    --text: #e8e9ee;
    --text-dim: #aab1c5;
    --d-color: #5b8aa8;
    --j-color: #b06a5b;
    --tie-color: #6b7280;
}

* {
    font-family: 'Inter', -apple-system, 'Segoe UI', sans-serif;
}

.stApp {
    background-color: var(--bg);
    color: var(--text);
}
.block-container {
    padding-top: 1.5rem;
    padding-left: 0.8rem;
    padding-right: 0.8rem;
    padding-bottom: 3rem;
    max-width: 700px;
}
h1, h2, h3 {
    color: var(--accent) !important;
    font-weight: 800;
    letter-spacing: 0.02em;
    text-align: center;
}
h1 {
    font-size: clamp(1.4rem, 6vw, 2.1rem) !important;
}
.team-name {
    font-size: clamp(1.1rem, 4.5vw, 1.6rem);
    font-weight: 700;
    color: var(--accent-soft);
    text-align: center;
    letter-spacing: 0.05em;
}
.score-box {
    background-color: var(--panel);
    border: 2px solid var(--accent-soft);
    border-radius: 14px;
    padding: clamp(10px, 4vw, 20px);
    text-align: center;
    font-size: clamp(2.2rem, 12vw, 3.5rem);
    font-weight: 800;
    color: var(--text);
    line-height: 1.1;
}
.stat-box {
    background-color: var(--panel);
    border: 2px solid var(--accent-soft);
    border-radius: 14px;
    padding: clamp(8px, 3vw, 15px);
    text-align: center;
    margin-bottom: 8px;
}
.stat-label {
    color: var(--text-dim);
    font-size: clamp(0.7rem, 2.8vw, 0.9rem);
    font-weight: 600;
    letter-spacing: 0.04em;
    text-transform: uppercase;
}
.stat-value {
    color: var(--accent);
    font-size: clamp(1.6rem, 8vw, 2.2rem);
    font-weight: 800;
}

/* Big, thumb-friendly buttons */
div.stButton > button {
    background-color: var(--accent);
    color: var(--bg);
    font-weight: 700;
    font-size: clamp(1rem, 4.5vw, 1.2rem);
    border-radius: 10px;
    border: none;
    width: 100%;
    min-height: 56px;
    touch-action: manipulation;
    transition: background-color 0.15s ease;
}
div.stButton > button:hover,
div.stButton > button:active {
    background-color: var(--accent-soft);
    color: var(--bg);
}

/* Date input */
div[data-testid="stDateInput"] input {
    font-weight: 600;
}

/* Calendar table */
table.cal {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
}
table.cal th {
    color: var(--accent);
    padding: 4px 2px;
    font-size: clamp(0.6rem, 2.5vw, 0.85rem);
    font-weight: 700;
}
table.cal td {
    border: 1px solid var(--panel);
    text-align: center;
    height: clamp(36px, 10vw, 60px);
    vertical-align: top;
    padding: 2px;
    font-size: clamp(0.65rem, 2.8vw, 0.95rem);
    word-break: break-word;
}
.day-num {
    color: var(--text-dim);
    font-size: clamp(0.55rem, 2.2vw, 0.75rem);
}
.win-d { background-color: var(--d-color); color: var(--text); font-weight: 700; }
.win-j { background-color: var(--j-color); color: var(--text); font-weight: 700; }
.win-tie { background-color: var(--tie-color); color: var(--text); }

/* Stack two-column rows on narrow phone screens so nothing gets squeezed */
@media (max-width: 480px) {
    div[data-testid="stHorizontalBlock"] {
        flex-direction: row;
        gap: 0.4rem;
    }
    div[data-testid="column"] {
        min-width: 0;
    }
    .block-container {
        padding-left: 0.5rem;
        padding-right: 0.5rem;
    }
}
</style>
"""
