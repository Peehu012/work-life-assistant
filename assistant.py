from calendar_events import create_event, get_upcoming_events
import datetime


def plan_and_schedule(goal, preferred_time, date, duration_minutes):
    print(f"🎯 Goal: {goal}")

    # Parse date and time
    full_start_str = f"{date} {preferred_time}"
    start_dt = datetime.datetime.strptime(full_start_str, "%Y-%m-%d %I:%M %p")

    # Calculate end time
    end_dt = start_dt + datetime.timedelta(minutes=duration_minutes)

    # Format to ISO 8601
    start_iso = start_dt.isoformat()
    end_iso = end_dt.isoformat()

    # Optional: Print planning summary
    print(f"🕒 Scheduled from {start_iso} to {end_iso}")

    # Optionally: show current calendar
    print("📅 Checking calendar availability...")
    get_upcoming_events()

    # Create the calendar event
    try:
        create_event(
            summary=goal,
            description="Auto-created by Work-Life Assistant",
            start_time=start_iso,
            end_time=end_iso
        )
    except Exception as e:
        print("❌ Failed to create event:", e)

