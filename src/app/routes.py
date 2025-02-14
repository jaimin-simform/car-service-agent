from flask import Blueprint, render_template, request, jsonify
from .email_service import send_email
from .calendar_service import book_calendar_event
from .openai_service import get_openai_session
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
from .config import config

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('call.html')

@main_bp.route('/session', methods=['GET'])
def session():
    try:
        response = get_openai_session()  # ✅ This now returns a Flask response
        return response  # ✅ Return the Flask response directly
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@main_bp.route('/send-email', methods=['POST'])
def email():
    data = request.json
    return send_email(data['message'])


# ✅ Add Google OAuth Routes Here
@main_bp.route('/authorize')
def authorize():
    try:
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            config.GOOGLE_CREDENTIALS_FILE, ["https://www.googleapis.com/auth/calendar.events"]
        )
        flow.redirect_uri = "http://localhost:5000/oauth2callback"

        # Run local server to complete OAuth flow
        creds = flow.run_local_server(port=8000, prompt='consent')

        # Save credentials to token.json
        with open("token.json", "w") as token_file:
            token_file.write(creds.to_json())

        return jsonify({'message': 'Authorization successful! You can now book calendar events.'}), 200  # ✅ Return JSON response

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@main_bp.route('/oauth2callback')
def oauth2callback():
    try:
        flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
            config.GOOGLE_CREDENTIALS_FILE, ["https://www.googleapis.com/auth/calendar.events"]
        )
        flow.redirect_uri = "http://localhost:5000/oauth2callback"

        authorization_response = request.url
        flow.fetch_token(authorization_response=authorization_response)

        credentials = flow.credentials
        with open("token.json", "w") as token_file:
            token_file.write(credentials.to_json())

        return jsonify({'message': 'Authorization successful! You can now book calendar events.'})

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/book-calendar', methods=['POST'])
def calendar():
    data = request.json
    return book_calendar_event(data)