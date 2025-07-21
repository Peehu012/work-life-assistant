from restaurant_finder import find_restaurants

parsed_input = {
    "Location": "Hyderabad",
    "Cuisine": "Hyderabadi Biryani",
    "Area": "Gachibowli",
    "Date/Time": "Next week",
    "Team size": 6
}

# Step 2 – Get restaurant suggestions
restaurants = find_restaurants(parsed_input["Area"], parsed_input["Cuisine"])

for i, r in enumerate(restaurants, 1):
    print(f"\nOption {i}: {r['name']} ({r['rating']}⭐)")
    print(f"Address: {r['address']}")
    print(f"Map: {r['map_url']}")

from assistant import plan_and_schedule

goal_details = {
    "goal": "Lunch with team near Connaught Place",
    "preferred_time": "1:00 PM",
    "date": "2025-07-23",
    "duration_minutes": 90
}

plan_and_schedule(**goal_details)

from auto_reserve import auto_fill_reservation

auto_fill_reservation(
    name="Peehu",
    date="2025-07-23",
    time_str="1:00 PM",
    people_count=6,
    url="https://your-restaurant-form-url.com"
)


