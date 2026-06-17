import streamlit as st
from datetime import date

from sheets_db import init_db, save_game, get_game
from style import JEOPARDY_CSS

st.set_page_config(page_title="Jeopardy! Tracker", page_icon="🔷", layout="centered")
init_db()
st.markdown(JEOPARDY_CSS, unsafe_allow_html=True)

st.title("🔷 JEOPARDY! TRACKER 🔷")
st.markdown(
    "<p style='text-align:center; color:#aab1c5;'>Tally correct answers for Team D and Team J</p>",
    unsafe_allow_html=True,
)

today = date.today()

selected_date = st.date_input(
    "Game date",
    value=st.session_state.get("selected_date", today),
    max_value=today,
)

if "game_date" not in st.session_state or st.session_state.game_date != selected_date:
    existing = get_game(selected_date)
    st.session_state.game_date = selected_date
    st.session_state.selected_date = selected_date
    st.session_state.d_score = existing[0] if existing else 0
    st.session_state.j_score = existing[1] if existing else 0

if "busy" not in st.session_state:
    st.session_state.busy = False
if "pending_save" not in st.session_state:
    st.session_state.pending_save = False

busy = st.session_state.busy

col_d, col_j = st.columns(2)

with col_d:
    st.markdown("<div class='team-name'>TEAM D</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-box'>{st.session_state.d_score}</div>", unsafe_allow_html=True)
    plus_d, minus_d = st.columns(2)
    with plus_d:
        if st.button("➕", key="d_plus", disabled=busy):
            st.session_state.d_score += 1
    with minus_d:
        if st.button("➖", key="d_minus", disabled=busy):
            st.session_state.d_score = max(0, st.session_state.d_score - 1)

with col_j:
    st.markdown("<div class='team-name'>TEAM J</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='score-box'>{st.session_state.j_score}</div>", unsafe_allow_html=True)
    plus_j, minus_j = st.columns(2)
    with plus_j:
        if st.button("➕", key="j_plus", disabled=busy):
            st.session_state.j_score += 1
    with minus_j:
        if st.button("➖", key="j_minus", disabled=busy):
            st.session_state.j_score = max(0, st.session_state.j_score - 1)

st.markdown("---")

save_col, stats_col = st.columns(2)
with save_col:
    if st.button("💾 SAVE SCORE", key="save", disabled=busy):
        st.session_state.busy = True
        st.session_state.pending_save = True
        st.session_state.save_payload = (selected_date, st.session_state.d_score, st.session_state.j_score)
        st.rerun()
with stats_col:
    if st.button("📊 STATS", key="go_stats", disabled=busy):
        st.switch_page("pages/1_Stats.py")

if st.session_state.pending_save:
    save_date, save_d, save_j = st.session_state.save_payload
    with st.spinner("Saving..."):
        save_game(save_date, save_d, save_j)
    st.session_state.pending_save = False
    st.session_state.busy = False
    st.toast(f"Saved {save_date.strftime('%b %d, %Y')}! D: {save_d} — J: {save_j}", icon="✅")
