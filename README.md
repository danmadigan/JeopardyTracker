# JeopardyTracker

A free, Jeopardy!-themed Streamlit app for tracking how many correct answers Team D and Team J get each game.

## Features
- ➕ / ➖ buttons to tally correct answers for each team (no dollar amounts)
- 💾 Save button to record the day's final score
- 📊 Stats page: all-time daily wins, all-time correct answers, current win streak, best single-day score per team, and a win calendar

Scores are stored in a Google Sheet (so they persist across deploys and are
shared from any device, including your phone).

## Google Sheets setup (no Cloud Console needed)
Scores are stored via a small Apps Script "Web App" bound to your own
Google Sheet — no Google Cloud Console project, API enabling, or service
account required, and it's entirely free.

1. Create a Google Sheet (any name).
2. In the Sheet, go to **Extensions -> Apps Script**, delete the default
   code, and paste in the contents of [`apps_script/Code.gs`](apps_script/Code.gs).
3. In the script, change the `TOKEN` constant to your own random secret
   string (this keeps strangers from writing to your sheet).
4. Click **Deploy -> New deployment**, choose type **Web app**, set
   "Execute as" to **Me** and "Who has access" to **Anyone with the link**,
   then click **Deploy** and authorize the script when prompted.
5. Copy the web app URL it gives you.
6. Copy `.streamlit/secrets.toml.example` to `.streamlit/secrets.toml` and
   fill in that URL and your `TOKEN`. This file is gitignored — never
   commit real secrets.

The script automatically creates a `games` worksheet with the right header
the first time you save a score.

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
