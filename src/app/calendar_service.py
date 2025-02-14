import os
import json
import googleapiclient.discovery
import google.oauth2.credentials
from flask import jsonify

def book_calendar_event(data):
    try:
        if os.path.exists("token.json"):
            with open("token.json", "r") as token_file:
                creds_data = json.load(token_file)
            creds = google.oauth2.credentials.Credentials.from_authorized_user_info(creds_data)
        else:
            return jsonify({'error': 'User not authenticated'}), 401

        service = googleapiclient.discovery.build('calendar', 'v3', credentials=creds)

        event = {
            'summary': data['summary'],
            'description': data['description'],
            'start': {'dateTime': data['start_time'], 'timeZone': 'Asia/Kolkata'},
            'end': {'dateTime': data['end_time'], 'timeZone': 'Asia/Kolkata'}
        }
        
        event_result = service.events().insert(calendarId='primary', body=event).execute()
        return jsonify({'success': True, 'event_link': event_result.get('htmlLink')})
    except Exception as e:
        return jsonify({'error': str(e)}), 500