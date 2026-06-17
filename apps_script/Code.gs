/**
 * Jeopardy Tracker backend.
 *
 * Setup:
 * 1. Open your Google Sheet -> Extensions -> Apps Script.
 * 2. Replace the default code with this file's contents.
 * 3. Change TOKEN below to your own random secret string.
 * 4. Click Deploy -> New deployment -> select type "Web app".
 *    - Execute as: Me
 *    - Who has access: Anyone with the link
 * 5. Click Deploy, authorize the script when prompted, and copy the
 *    web app URL it gives you.
 * 6. Put that URL and your TOKEN into .streamlit/secrets.toml
 *    (see .streamlit/secrets.toml.example).
 *
 * No Google Cloud Console project, API enabling, or service account
 * needed - everything runs under your own Google account for free.
 */

var SHEET_NAME = "games";
var TOKEN = "CHANGE_ME_TO_A_RANDOM_SECRET";
var HEADER = ["game_date", "d_score", "j_score", "winner"];

function getSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheetByName(SHEET_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(SHEET_NAME);
  }
  if (sheet.getRange(1, 1).getValue() === "") {
    sheet.getRange(1, 1, 1, HEADER.length).setValues([HEADER]);
  }
  return sheet;
}

function jsonOutput_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

function doGet(e) {
  if (!e || e.parameter.token !== TOKEN) {
    return jsonOutput_({ error: "unauthorized" });
  }
  var sheet = getSheet_();
  var rows = sheet.getDataRange().getValues();
  var header = rows.shift();
  var games = rows
    .filter(function (r) { return r[0] !== ""; })
    .map(function (r) {
      var obj = {};
      header.forEach(function (h, i) { obj[h] = r[i]; });
      return obj;
    });
  return jsonOutput_({ games: games });
}

function doPost(e) {
  var body;
  try {
    body = JSON.parse(e.postData.contents);
  } catch (err) {
    return jsonOutput_({ error: "invalid json" });
  }
  if (body.token !== TOKEN) {
    return jsonOutput_({ error: "unauthorized" });
  }

  var sheet = getSheet_();
  var rows = sheet.getDataRange().getValues();
  var targetRow = -1;
  for (var i = 1; i < rows.length; i++) {
    if (rows[i][0] === body.game_date) {
      targetRow = i + 1; // 1-indexed sheet row
      break;
    }
  }

  var newRow = [body.game_date, body.d_score, body.j_score, body.winner];
  if (targetRow > 0) {
    sheet.getRange(targetRow, 1, 1, newRow.length).setValues([newRow]);
  } else {
    sheet.appendRow(newRow);
  }

  return jsonOutput_({ status: "ok" });
}
