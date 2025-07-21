import os.path
import datetime
from datetime import datetime as dt
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# Full calendar access
SCOPES = ['https://www.googleapis.com/auth/calendar']

# ✅ 1. Reusable credentials loader
def get_credentials():
    creds = None
    credential_path = 'credentials/client_secret.json'

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential_path, SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

# ✅ 2. Function to fetch upcoming calendar events
def get_upcoming_events():
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'  # Current time in UTC
    print('Getting the upcoming 10 events...')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=10, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])

# ✅ 3. Function to create new event dynamically
def create_event(summary, description, start_time, end_time):
    creds = get_credentials()
    service = build('calendar', 'v3', credentials=creds)

    event = {
        'summary': summary,
        'description': description,
        'start': {
            'dateTime': start_time,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end_time,
            'timeZone': 'Asia/Kolkata',
        },
        'reminders': {
            'useDefault': True,
        },
    }

    created_event = service.events().insert(calendarId='primary', body=event).execute()
    print(f"✅ Event created: {created_event.get('htmlLink')}")

# Optional: run to test from terminal
if __name__ == '__main__':
    get_upcoming_events()
