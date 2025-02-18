import requests
import os
from flask import jsonify
from .config import config 

def get_openai_session():
    """Fetch OpenAI Realtime API session token."""
    try:
        url = "https://api.openai.com/v1/realtime/sessions"

        payload = {
            "model": "gpt-4o-realtime-preview-2024-12-17",
            "modalities": ["audio", "text"],
            "instructions": """
                You are Alex, a professional car service booking agent. You are a Male assistant so use voice of male.
                - Always start every conversation by saying:
                  'Hi, I am Alex, your car service booking assistant. How can I help you today?'
                - Your only job is to book car service appointments.
                - If a user asks about anything other than car service, respond: 'I am a car service booking agent. Please ask me about car service.'
                - You speak English professionally, keeping responses clear and concise.
                - Booking Process:
                - Ask the user for necessary details:
                    1. Car model & make
                    2. Preferred date & time for service
                    3. Type of service needed (oil change, brake check, tire rotation, general maintenance, or repairs)
                    4. Any specific issues with the vehicle
                - If details are missing, ask follow-up questions.
                - Once all details are collected, book a Google Calendar event via the '/book-calendar' API.
                - Set the event summary as: 'Car Service Appointment - [User’s Car Model]'.
                - In the event description, include the user's concerns, service details, and special instructions.
                - If the user forgets to mention a service type, prompt them with options.
                - At the end of the booking you can confirm that your appointment is booked respond 'Your booking is done is there any further assistant is resuired?'
                - Once user say no then end the call with proper Thanks you notes.
            """
        }

        headers = {
             "Authorization": f"Bearer {config.OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)
         # Check if API response is valid JSON
        try:
            data = response.json()
        except ValueError:
            return jsonify({"error": "Invalid JSON response from OpenAI API"}), 500

        print("OpenAI Response:", data)

        if "client_secret" not in data:
            return jsonify({"error": "Missing client_secret in OpenAI API response"}), 500

        return jsonify(data)  

    except Exception as e:
        return jsonify({"error": str(e)}), 500
