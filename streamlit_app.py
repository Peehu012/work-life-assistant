import streamlit as st
from assistant import plan_and_schedule
from calendar_events import get_upcoming_events

st.set_page_config(page_title="🧠 Work-Life Assistant", layout="centered")

st.title("🤖 Proactive Work-Life Assistant")

st.sidebar.title("📌 Goal Input")
goal = st.sidebar.text_input("🎯 Goal", placeholder="e.g., Lunch with team near CP")
date = st.sidebar.date_input("📅 Date")
time = st.sidebar.time_input("🕒 Preferred Time")
duration = st.sidebar.number_input("⏱ Duration (minutes)", min_value=15, value=60)

if st.sidebar.button("📆 Schedule"):
    if goal and date and time:
        try:
            plan_and_schedule(
                goal=goal,
                preferred_time=time.strftime("%I:%M %p"),  # Convert time to 12hr format
                date=date.strftime("%Y-%m-%d"),
                duration_minutes=duration
            )
            st.success("✅ Event scheduled successfully!")
        except Exception as e:
            st.error(f"❌ Failed to schedule event: {e}")
    else:
        st.warning("⚠️ Please fill in all details.")

if st.button("🔍 Show Upcoming Calendar Events"):
    try:
        get_upcoming_events()
    except Exception as e:
        st.error(f"❌ Failed to fetch events: {e}")
