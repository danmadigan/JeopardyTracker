"""Google Sheets persistence via an Apps Script Web App.

No Google Cloud Console project, API enabling, or service account is
needed. Deploy `apps_script/Code.gs` as a Web App from inside the Google
Sheet itself, then put the resulting URL and shared token in
`.streamlit/secrets.toml` (see `.streamlit/secrets.toml.example`).
"""
from datetime import date

import requests
import streamlit as st

TEAMS = ("D", "J")
TIMEOUT = 10


def _config():
    cfg = st.secrets["gsheets_webapp"]
    return cfg["url"], cfg["token"]


def init_db():
    """No-op: the Apps Script creates the sheet/header on first save."""
    pass


def _fetch_all():
    url, token = _config()
    resp = requests.get(url, params={"token": token}, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if "error" in data:
        raise RuntimeError(f"Apps Script error: {data['error']}")

    games = []
    for row in data.get("games", []):
        try:
            games.append(
                (
                    str(row["game_date"]),
                    int(row["d_score"] or 0),
                    int(row["j_score"] or 0),
                    str(row["winner"]),
                )
            )
        except (KeyError, TypeError, ValueError):
            continue
    games.sort(key=lambda g: g[0])
    return games


def save_game(game_date: date, d_score: int, j_score: int):
    if d_score > j_score:
        winner = "D"
    elif j_score > d_score:
        winner = "J"
    else:
        winner = "TIE"

    url, token = _config()
    payload = {
        "token": token,
        "game_date": game_date.isoformat(),
        "d_score": d_score,
        "j_score": j_score,
        "winner": winner,
    }
    resp = requests.post(url, json=payload, timeout=TIMEOUT)
    resp.raise_for_status()
    data = resp.json()
    if data.get("status") != "ok":
        raise RuntimeError(f"Apps Script error: {data.get('error', 'unknown')}")


def get_game(game_date: date):
    date_str = game_date.isoformat()
    for d, d_score, j_score, _winner in _fetch_all():
        if d == date_str:
            return (d_score, j_score)
    return None


def get_all_games():
    return _fetch_all()
