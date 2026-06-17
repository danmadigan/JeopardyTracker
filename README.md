# JeopardyTracker

A free, Jeopardy!-themed Streamlit app for tracking how many correct answers Team D and Team J get each game.

## Features
- ➕ / ➖ buttons to tally correct answers for each team (no dollar amounts)
- 💾 Save button to record the day's final score
- 📊 Stats page: all-time daily wins, all-time correct answers, current win streak, best single-day score per team, and a win calendar

Scores are stored in a Google Sheet (so they persist across deploys and are
shared from any device, including your phone).

## Google Sheets setup
1. Create a Google Sheet with a worksheet named `games` (any sheet name, the
   worksheet must be named `games`).
2. In [Google Cloud Console](https://console.cloud.google.com/), create a
   project, enable the **Google Sheets API** and **Google Drive API**, then
   create a service account and download its JSON key.
3. Share the Google Sheet with the service account's email address
   (found in the JSON key as `client_email`) as an **Editor**.
4. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and
   fill in the values from the JSON key plus your sheet's URL. This file is
   gitignored — never commit real credentials.

## Run locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy to Streamlit Community Cloud
1. Push this repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io), sign in, and create
   a new app pointing at this repo/branch with main file `app.py`.
3. In the app's **Settings -> Secrets**, paste the contents of your filled-in
   `secrets.toml` (same format as `.streamlit/secrets.toml.example`).
4. Deploy, then open the app URL on your phone (add it to your home screen
   for an app-like experience).
