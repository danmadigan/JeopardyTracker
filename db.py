"""SQLite persistence for the Jeopardy tracker."""
import sqlite3
from contextlib import contextmanager
from datetime import date

DB_PATH = "jeopardy.db"

TEAMS = ("D", "J")


@contextmanager
def get_conn():
    conn = sqlite3.connect(DB_PATH)
    try:
        yield conn
    finally:
        conn.close()


def init_db():
    with get_conn() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS games (
                game_date TEXT PRIMARY KEY,
                d_score INTEGER NOT NULL DEFAULT 0,
                j_score INTEGER NOT NULL DEFAULT 0,
                winner TEXT
            )
            """
        )
        conn.commit()


def save_game(game_date: date, d_score: int, j_score: int):
    if d_score > j_score:
        winner = "D"
    elif j_score > d_score:
        winner = "J"
    else:
        winner = "TIE"

    with get_conn() as conn:
        conn.execute(
            """
            INSERT INTO games (game_date, d_score, j_score, winner)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(game_date) DO UPDATE SET
                d_score=excluded.d_score,
                j_score=excluded.j_score,
                winner=excluded.winner
            """,
            (game_date.isoformat(), d_score, j_score, winner),
        )
        conn.commit()


def get_game(game_date: date):
    with get_conn() as conn:
        row = conn.execute(
            "SELECT d_score, j_score FROM games WHERE game_date = ?",
            (game_date.isoformat(),),
        ).fetchone()
    return row


def get_all_games():
    with get_conn() as conn:
        rows = conn.execute(
            "SELECT game_date, d_score, j_score, winner FROM games ORDER BY game_date"
        ).fetchall()
    return rows
