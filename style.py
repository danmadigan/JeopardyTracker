"""Shared Jeopardy-themed, mobile-friendly CSS."""

JEOPARDY_CSS = """
<style>
.stApp {
    background-color: #060CE9;
    color: #FFFFFF;
}
.block-container {
    padding-top: 1.5rem;
    padding-left: 0.8rem;
    padding-right: 0.8rem;
    padding-bottom: 3rem;
    max-width: 700px;
}
h1, h2, h3 {
    font-family: 'Georgia', serif;
    color: #FFCC00 !important;
    text-shadow: 2px 2px 4px #000000;
    text-align: center;
}
h1 {
    font-size: clamp(1.4rem, 6vw, 2.2rem) !important;
}
.team-name {
    font-family: 'Georgia', serif;
    font-size: clamp(1.2rem, 5vw, 2rem);
    color: #FFCC00;
    text-align: center;
    text-shadow: 2px 2px 3px #000;
}
.score-box {
    background-color: #000099;
    border: 3px solid #FFCC00;
    border-radius: 10px;
    padding: clamp(10px, 4vw, 20px);
    text-align: center;
    font-size: clamp(2.2rem, 12vw, 3.5rem);
    font-weight: bold;
    color: #FFFFFF;
    font-family: 'Georgia', serif;
    line-height: 1.1;
}
.stat-box {
    background-color: #000099;
    border: 3px solid #FFCC00;
    border-radius: 10px;
    padding: clamp(8px, 3vw, 15px);
    text-align: center;
    font-family: 'Georgia', serif;
    margin-bottom: 8px;
}
.stat-label {
    color: #FFFFFF;
    font-size: clamp(0.75rem, 3vw, 1rem);
}
.stat-value {
    color: #FFCC00;
    font-size: clamp(1.6rem, 8vw, 2.2rem);
    font-weight: bold;
}

/* Big, thumb-friendly buttons */
div.stButton > button {
    background-color: #FFCC00;
    color: #060CE9;
    font-weight: bold;
    font-size: clamp(1.1rem, 5vw, 1.3rem);
    border-radius: 8px;
    border: 2px solid #FFFFFF;
    width: 100%;
    min-height: 56px;
    touch-action: manipulation;
}
div.stButton > button:hover,
div.stButton > button:active {
    background-color: #FFFFFF;
    color: #060CE9;
}

/* Calendar table */
table.cal {
    width: 100%;
    border-collapse: collapse;
    table-layout: fixed;
}
table.cal th {
    color: #FFCC00;
    font-family: 'Georgia', serif;
    padding: 4px 2px;
    font-size: clamp(0.6rem, 2.5vw, 0.9rem);
}
table.cal td {
    border: 1px solid #FFCC00;
    text-align: center;
    height: clamp(36px, 10vw, 60px);
    vertical-align: top;
    padding: 2px;
    font-family: 'Georgia', serif;
    font-size: clamp(0.65rem, 2.8vw, 1rem);
    word-break: break-word;
}
.day-num {
    color: #FFFFFF;
    font-size: clamp(0.55rem, 2.2vw, 0.8rem);
}
.win-d { background-color: #1a4fd6; color: #FFCC00; font-weight: bold; }
.win-j { background-color: #d62828; color: #FFCC00; font-weight: bold; }
.win-tie { background-color: #444444; color: #FFFFFF; }

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
