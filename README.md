# JeopardyTracker

A free, Jeopardy!-themed Streamlit app for tracking how many correct answers Team D and Team J get each game.

## Features
- ➕ / ➖ buttons to tally correct answers for each team (no dollar amounts)
- 💾 Save button to record the day's final score
- 📊 Stats page: all-time daily wins, all-time correct answers, current win streak, best single-day score per team, and a win calendar

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Scores are stored in a local SQLite file (`jeopardy.db`).
