from __future__ import print_function

import os.path
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']


def construct_payload(summary='Google I/O 2015', location='Vladivostok',
                      description='Meetup', start='2021-02-23T09:00:00-07:00',
                      end='2021-02-23T17:00:00-07:00',
                      attendees=[{'email': 'dostoyewski@yandex.ru'}, {'email': 'nik.tesla637@gmail.com'}]):
    data = {
        'summary': summary,
        'location': location,
        'description': description,
        'start': {
            'dateTime': start,
            'timeZone': 'Europe/Moscow',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Europe/Moscow',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': attendees,
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    return data


def create_event(summary, location, description, start, end, attendee):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('diagnostic/credentials.json', SCOPES)
            creds = flow.run_local_server(port=8880)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    payload = construct_payload(summary, location, description, start, end, attendee)
    # Call the Calendar API
    event = service.events().insert(calendarId='primary',
                                    sendUpdates='all', body=payload).execute()
    print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    create_event("test", 'spb', 'test event', '2021-02-27T09:00:00-07:00',
                 '2021-02-27T17:00:00-07:00', [{'email': 'fdrkondor@gmail.com'},
                                               {'email': 'dostoyewski@yandex.ru'}])
