# 🚀 Car Service Booking AI Assistant

## 📖 Introduction
This project is a **Flask-based AI-powered Car Service Booking Assistant** that allows users to:
- Make AI-driven voice calls using OpenAI Realtime API.
- Book car service appointments via **Google Calendar API**.
- Receive email confirmations via **SMTP email service**.

This guide will walk you through **setting up the project, configuring Google Calendar & SMTP, and running the application.**

---

## 📂 **Project Structure**
```plaintext
📦 car-service-booking
├── 📂 src
│   ├── 📂 app
│   │   ├── __init__.py          # Initializes Flask app
│   │   ├── routes.py            # API routes
│   │   ├── openai_service.py    # OpenAI realtime API integration
│   │   ├── email_service.py     # SMTP email configuration
│   │   ├── config.py            # Loads configuration from `.env`
│   ├── 📂 static
│   │   ├── 📂 assets             # Audio & media files
│   │   ├── 📂 js                 # JavaScript files
│   │   ├── 📂 css                # CSS stylesheets
│   ├── 📂 templates
│   │   ├── call.html            # Frontend UI
│   ├── configuration.json       # Stores application settings (excluded from Git)
│   ├── main.py                  # Flask entry point
├── .env                          # Environment variables (excluded from Git)
├── docker-compose.yml            # Docker configuration (Optional)
├── pyproject.toml                # Poetry dependencies
├── poetry.lock                   # Poetry lock file
├── .gitignore                     # Excludes sensitive files from Git
└── README.md                     # This guide
```
---

## 🏗️ **Setup Guide**

### 1️⃣ **Clone the Repository**
```sh
git clone https://github.com/your-username/car-service-booking.git
cd car-service-booking
```

### 2️⃣ **Install Dependencies** (Using Poetry)
```sh
poetry install
```

### 3️⃣ **Create `.env` File in the Project Root**
Create a `.env` file in the main project folder and add the following:
```env
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key

# Google Calendar API Credentials
GOOGLE_CREDENTIALS_FILE=src/credentials.json

# SMTP Email Configuration
SMTP_HOST=smtp.gmail.com
SMTP_PORT=465
SMTP_USERNAME=your_email@gmail.com
SMTP_PASSWORD=your_email_password
RECEIVING_EMAIL=recipient@example.com
```
📌 **Note:** Never hardcode credentials in the code! Use `.env`.

---

## 📅 **Google Calendar API Setup**
### 4️⃣ **Enable Google Calendar API**
1. Go to **[Google Cloud Console](https://console.cloud.google.com/)**.
2. Click **New Project** → Name it **Car Service Booking**.
3. Go to **APIs & Services** → **Library**.
4. Search for **Google Calendar API** → Enable it.
5. Go to **Credentials** → **Create Credentials** → Select **OAuth 2.0 Client ID**.
6. Choose **Desktop App** → Click **Create**.
7. Download the **JSON credentials file** and rename it to `credentials.json`.
8. Move `credentials.json` to `src/credentials.json`.

### 5️⃣ **Authorize Google Calendar API**
Run the following command **to authorize the application**:
```sh
poetry run python src/main.py
```
Then open the following URL in your browser:
```plaintext
http://127.0.0.1:5000/authorize
```
Sign in with your Google account and grant **Calendar access**.
After authorization, a `token.json` file will be created.

---

## 📧 **SMTP Email Setup**
### 6️⃣ **Get SMTP Credentials (for Gmail)**
1. **Enable Less Secure Apps (Gmail users only)**
   - Go to [Google Less Secure Apps](https://myaccount.google.com/lesssecureapps) → Enable.
   - (If you have **2FA enabled**, use an **App Password** instead.)

2. **Find Your SMTP Details**
   | Email Provider | SMTP Host       | Port |
   |--------------|----------------|------|
   | Gmail       | smtp.gmail.com  | 465  |
   | Outlook     | smtp.office365.com | 587  |
   | Yahoo       | smtp.mail.yahoo.com | 465  |
   
3. **Add Credentials to `.env`** (See Step 3 above).

---

## 🚀 **Run the Application**

### 7️⃣ **Start Flask Application**
```sh
poetry run python src/main.py
```

### 8️⃣ **Access the Web Interface**
Open a browser and go to:
```plaintext
http://127.0.0.1:5000
```

---

## 🛠 **Troubleshooting**
**Error: `.env` file not found**
- Ensure the `.env` file is in the root directory.

**Error: `configuration.json` missing**
- Ensure `configuration.json` is inside `src/`.

**Google Calendar API not working?**
- Run `/authorize` to re-authenticate.

---

## 📜 **License**
This project is open-source under the MIT License.

---

✅ **Now your application is fully documented for anyone to use!** 🚀

