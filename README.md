# 🤖 Proactive Work-Life Assistant

A smart AI-powered personal assistant that helps schedule tasks, plan events, and automate reservations — using Google Calendar API, LLMs (like GPT), and Selenium.

---

## 🔥 Features

- 🧠 **Goal Interpretation** from natural language using GPT-4.
- 📅 **Smart Calendar Scheduling** (Google Calendar integration).
- 🏙️ **Nearby Restaurant Suggestions** (Google Places API).
- 📝 **Event Creation** with reminder support.
- 🤖 **Web Automation** for restaurant form filling (Selenium).
- 🌐 **Streamlit UI** for user-friendly interaction.

---

## 🏁 Getting Started

### 1. **Clone the Repo**

```bash
git clone https://github.com/your-username/proactive-worklife-assistant.git
cd proactive-worklife-assistant
2. Install Requirements
bash
Copy
Edit
pip install -r requirements.txt
3. Google Calendar Setup
Go to Google Cloud Console.

Enable Google Calendar API and Places API.

Create OAuth Client ID.

Download the client_secret.json and place it in credentials/ folder.
🎯 How It Works
bash
Copy
Edit
streamlit run streamlit_app.py
Fill in your goal, date, time, and duration.

The app:

Interprets input using GPT (if enabled).

Fetches your Google Calendar availability.

Schedules the event.

(Optional) Triggers auto-reservation via Selenium.

🗂️ Project Structure
markdown
Copy
Edit
📁 nebula9.ai/
├── assistant.py
├── calendar_events.py
├── create_events.py
├── auto_reserve.py
├── restaurant_finder.py
├── streamlit_app.py
├── requirements.txt
📁 credentials/
    └── client_secret.json  (ignored in .gitignore)

