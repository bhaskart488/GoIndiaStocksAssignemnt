import os.path
import csv
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
# SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SCOPES = ["https://www.googleapis.com/auth/spreadsheets",
          "https://www.googleapis.com/auth/drive"]

# The ID of the target spreadsheet.
SPREADSHEET_ID = "1bAuXtPfp6BVluhVyEa7BMEfqIuHkTobS2sfbMKTpiCk"

def read_csv(file_path):
    """
    Read data from a CSV file and return it as a list of lists.
    """
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def main():
    """Updates the Google Sheet with CSV data."""
    # Read CSV data
    csv_data = read_csv("results.csv")

    # Authenticate with Google Sheets API
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=3000)
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        # Build the service for Google Sheets API
        service = build("sheets", "v4", credentials=creds)

        # Update the target spreadsheet with CSV data
        body = {"values": csv_data}
        result = service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range="Sheet1",  # Specify the range where you want to update the data
            valueInputOption="RAW",
            body=body
        ).execute()

        print("CSV data successfully uploaded to Google Sheets!")

    except HttpError as err:
        print("An error occurred:", err)

if __name__ == "__main__":
    main()
