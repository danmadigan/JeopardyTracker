import streamlit as st
from datetime import date

from db import init_db, save_game, get_game, TEAMS

st.set_page_config(page_title="Jeopardy! Tracker", page_icon="🔷", layout="centered")
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
.team-name {
    font-family: 'Georgia', serif;
    font-size: 2rem;
    color: #FFCC00;
    text-align: center;
    text-shadow: 2px 2px 3px #000;
}
.score-box {
    background-color: #000099;
    border: 3px solid #FFCC00;
    border-radius: 10px;
    padding: 20px;
    text-align: center;
    font-size: 3.5rem;
    font-weight: bold;
    color: #FFFFFF;
    font-family: 'Georgia', serif;
}
div.stButton > button {
    background-color: #FFCC00;
    color: #060CE9;
    font-weight: bold;
    font-size: 1.3rem;
    border-radius: 8px;
    border: 2px solid #FFFFFF;
    width: 100%;
}
div.stButton > button:hover {
    background-color: #FFFFFF;
    color: #060CE9;
}
</style>
"""
st.markdown(JEOPARDY_CSS, unsafe_allow_html=True)

st.title("🔷 JEOPARDY! TRACKER 🔷")
st.markdown(
    "<p style='text-align:center; color:#FFFFFF;'>Tally today's correct answers for Team D and Team J</p>",
    unsafe_allow_html=True,
)

today = date.today()

if "game_date" not in st.session_state or st.session_state.game_date != today:
    existing = get_game(today)
    st.session_state.game_date = today
    st.session_state.d_score = existing[0] if existing else 0
    st.session_state.j_score = existing[1] if existing else 0

st.markdown(f"<p style='text-align:center;'>Today: {today.strftime('%B %d, %Y')}</p>", unsafe_allow_html=True)

col_d, col_j = st.columns(2)

with col_d:
    st.markdown("<div class='team-name'>TEAM D</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-box'>{st.session_state.d_score}</div>", unsafe_allow_html=True)
    plus_d, minus_d = st.columns(2)
    with plus_d:
        if st.button("➕", key="d_plus"):
            st.session_state.d_score += 1
    with minus_d:
        if st.button("➖", key="d_minus"):
            st.session_state.d_score = max(0, st.session_state.d_score - 1)

with col_j:
    st.markdown("<div class='team-name'>TEAM J</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-box'>{st.session_state.j_score}</div>", unsafe_allow_html=True)
    plus_j, minus_j = st.columns(2)
    with plus_j:
        if st.button("➕", key="j_plus"):
            st.session_state.j_score += 1
    with minus_j:
        if st.button("➖", key="j_minus"):
            st.session_state.j_score = max(0, st.session_state.j_score - 1)

st.markdown("---")

if st.button("💾 SAVE TODAY'S SCORE", key="save"):
    save_game(today, st.session_state.d_score, st.session_state.j_score)
    st.success(f"Saved! D: {st.session_state.d_score} — J: {st.session_state.j_score}")

st.markdown(
    "<p style='text-align:center; color:#FFCC00;'>See the Stats page in the sidebar for all-time records and the win calendar.</p>",
    unsafe_allow_html=True,
)
