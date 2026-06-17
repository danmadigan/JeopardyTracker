"""Google Sheets persistence for the Jeopardy tracker.

Requires a `[connections.gsheets]` section in `.streamlit/secrets.toml`
(see `.streamlit/secrets.toml.example`) pointing at a Google Sheet shared
with a service account. The sheet just needs a worksheet named "games";
the header row is written automatically on the first save.
"""
from datetime import date

import pandas as pd
import streamlit as st
from streamlit_gsheets import GSheetsConnection

WORKSHEET = "games"
COLUMNS = ["game_date", "d_score", "j_score", "winner"]
TEAMS = ("D", "J")


def _get_conn():
    return st.connection("gsheets", type=GSheetsConnection)


def _read_df() -> pd.DataFrame:
    conn = _get_conn()
    try:
        df = conn.read(worksheet=WORKSHEET, ttl=0)
    except Exception:
        df = None

    if df is None or df.empty:
        return pd.DataFrame(columns=COLUMNS)

    df = df.dropna(how="all")
    df["game_date"] = df["game_date"].astype(str)
    df["d_score"] = pd.to_numeric(df["d_score"], errors="coerce").fillna(0).astype(int)
    df["j_score"] = pd.to_numeric(df["j_score"], errors="coerce").fillna(0).astype(int)
    df["winner"] = df["winner"].astype(str)
    return df[COLUMNS]


def init_db():
    """No-op: the worksheet header is created on first save_game call."""
    pass


def save_game(game_date: date, d_score: int, j_score: int):
    if d_score > j_score:
        winner = "D"
    elif j_score > d_score:
        winner = "J"
    else:
        winner = "TIE"

    date_str = game_date.isoformat()
    df = _read_df()
    df = df[df["game_date"] != date_str]
    new_row = pd.DataFrame(
        [{"game_date": date_str, "d_score": d_score, "j_score": j_score, "winner": winner}]
    )
    df = pd.concat([df, new_row], ignore_index=True).sort_values("game_date")

    conn = _get_conn()
    conn.update(worksheet=WORKSHEET, data=df)
    st.cache_data.clear()


def get_game(game_date: date):
    df = _read_df()
    row = df[df["game_date"] == game_date.isoformat()]
    if row.empty:
        return None
    r = row.iloc[0]
    return (int(r.d_score), int(r.j_score))


def get_all_games():
    df = _read_df().sort_values("game_date")
    return list(df[COLUMNS].itertuples(index=False, name=None))
