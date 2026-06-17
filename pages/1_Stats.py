import calendar
from datetime import date

import streamlit as st

from db import init_db, get_all_games

st.set_page_config(page_title="Jeopardy! Stats", page_icon="📊", layout="centered")
init_db()

JEOPARDY_CSS = """
<style>
.stApp {
    background-color: #060CE9;
    color: #FFFFFF;
}
h1, h2, h3 {
    font-family: 'Georgia', serif;
    color: #FFCC00 !important;
    text-shadow: 2px 2px 4px #000000;
    text-align: center;
}
.stat-box {
    background-color: #000099;
    border: 3px solid #FFCC00;
    border-radius: 10px;
    padding: 15px;
    text-align: center;
    font-family: 'Georgia', serif;
}
.stat-label {
    color: #FFFFFF;
    font-size: 1rem;
}
.stat-value {
    color: #FFCC00;
    font-size: 2.2rem;
    font-weight: bold;
}
table.cal {
    width: 100%;
    border-collapse: collapse;
}
table.cal th {
    color: #FFCC00;
    font-family: 'Georgia', serif;
    padding: 6px;
}
table.cal td {
    border: 1px solid #FFCC00;
    text-align: center;
    height: 60px;
    vertical-align: top;
    padding: 4px;
    font-family: 'Georgia', serif;
}
.day-num {
    color: #FFFFFF;
    font-size: 0.8rem;
}
.win-d { background-color: #1a4fd6; color: #FFCC00; font-weight: bold; }
.win-j { background-color: #d62828; color: #FFCC00; font-weight: bold; }
.win-tie { background-color: #444444; color: #FFFFFF; }
</style>
"""
st.markdown(JEOPARDY_CSS, unsafe_allow_html=True)

st.title("📊 ALL-TIME STATS")

games = get_all_games()  # (date_str, d_score, j_score, winner)

if not games:
    st.info("No games saved yet. Go play some Jeopardy!")
    st.stop()

total_d_wins = sum(1 for g in games if g[3] == "D")
total_j_wins = sum(1 for g in games if g[3] == "J")
total_d_correct = sum(g[1] for g in games)
total_j_correct = sum(g[2] for g in games)
best_d_day = max(g[1] for g in games)
best_j_day = max(g[2] for g in games)


def current_streak(team):
    streak = 0
    for g in reversed(games):
        if g[3] == team:
            streak += 1
        else:
            break
    return streak


streak_d = current_streak("D")
streak_j = current_streak("J")

st.subheader("Daily Wins")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM D WINS</div>"
        f"<div class='stat-value'>{total_d_wins}</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM J WINS</div>"
        f"<div class='stat-value'>{total_j_wins}</div></div>",
        unsafe_allow_html=True,
    )

st.subheader("All-Time Correct Answers")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM D CORRECT</div>"
        f"<div class='stat-value'>{total_d_correct}</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM J CORRECT</div>"
        f"<div class='stat-value'>{total_j_correct}</div></div>",
        unsafe_allow_html=True,
    )

st.subheader("Current Win Streak")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM D STREAK</div>"
        f"<div class='stat-value'>{streak_d}</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM J STREAK</div>"
        f"<div class='stat-value'>{streak_j}</div></div>",
        unsafe_allow_html=True,
    )

st.subheader("Most Correct Answers in a Single Day")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM D BEST DAY</div>"
        f"<div class='stat-value'>{best_d_day}</div></div>",
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        f"<div class='stat-box'><div class='stat-label'>TEAM J BEST DAY</div>"
        f"<div class='stat-value'>{best_j_day}</div></div>",
        unsafe_allow_html=True,
    )

st.markdown("---")
st.subheader("🗓️ Win Calendar")

results_by_date = {g[0]: g[3] for g in games}
years_months = sorted({(int(d[:4]), int(d[5:7])) for d in results_by_date})
labels = [f"{calendar.month_name[m]} {y}" for y, m in years_months]
default_idx = len(labels) - 1
choice = st.selectbox("Month", labels, index=default_idx)
sel_year, sel_month = years_months[labels.index(choice)]

cal = calendar.Calendar(firstweekday=6)  # Sunday start
weeks = cal.monthdayscalendar(sel_year, sel_month)

html = "<table class='cal'><tr>"
for wd in ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]:
    html += f"<th>{wd}</th>"
html += "</tr>"

for week in weeks:
    html += "<tr>"
    for day in week:
        if day == 0:
            html += "<td></td>"
            continue
        day_str = date(sel_year, sel_month, day).isoformat()
        winner = results_by_date.get(day_str)
        if winner == "D":
            cls = "win-d"
            label = "D"
        elif winner == "J":
            cls = "win-j"
            label = "J"
        elif winner == "TIE":
            cls = "win-tie"
            label = "TIE"
        else:
            cls = ""
            label = ""
        html += f"<td class='{cls}'><div class='day-num'>{day}</div>{label}</td>"
    html += "</tr>"
html += "</table>"

st.markdown(html, unsafe_allow_html=True)
st.markdown(
    "<p style='text-align:center; margin-top:10px;'>"
    "<span style='background-color:#1a4fd6; color:#FFCC00; padding:2px 8px; border-radius:4px;'>D win</span> "
    "<span style='background-color:#d62828; color:#FFCC00; padding:2px 8px; border-radius:4px;'>J win</span> "
    "<span style='background-color:#444444; color:#FFFFFF; padding:2px 8px; border-radius:4px;'>Tie</span>"
    "</p>",
    unsafe_allow_html=True,
)
