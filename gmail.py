from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from datetime import datetime, timedelta
import os

# Define the scopes for Gmail API
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def authenticate():
    # Authenticate with Gmail API using OAuth2 credentials
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json')
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    return creds

def main():
    # Authenticate with Gmail API
    creds = authenticate()
    service = build('gmail', 'v1', credentials=creds)

    # Calculate date range for the last week
    end_date = datetime.now()
    start_date = end_date - timedelta(days=7)

    # Format dates as RFC3339 strings for Gmail API
    start_date_str = start_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    end_date_str = end_date.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Fetch emails from the last week
    results = service.users().messages().list(userId='me', q=f'after:{start_date_str}').execute()
    messages = results.get('messages', [])

    # Process fetched emails
    for message in messages:
        msg = service.users().messages().get(userId='me', id=message['id']).execute()
        # Extract relevant information from the email message
        print('From:', next(h['value'] for h in msg['payload']['headers'] if h['name'] == 'From'))
        print('Subject:', next(h['value'] for h in msg['payload']['headers'] if h['name'] == 'Subject'))
        print('Snippet:', msg['snippet'])
        print('---')

if __name__ == '__main__':
    main()
