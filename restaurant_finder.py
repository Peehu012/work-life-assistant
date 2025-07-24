# restaurant_finder.py
import streamlit as st

api_key = st.secrets["GOOGLE_MAPS_API_KEY"]

if not api_key:
    raise ValueError("GOOGLE_MAPS_API_KEY not found. Check your .env file or environment.")


import googlemaps
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_MAPS_API_KEY")

# Connect to Google Maps
gmaps = googlemaps.Client(key=api_key)

def find_restaurants(area, cuisine, radius=3000):
    # Optional: Predefined coordinates for Gachibowli
    if area.lower() == "gachibowli":
        location = (17.4401, 78.3489)
    else:
        # Convert area name to lat/lng using Geocoding API
        geocode_result = gmaps.geocode(area)
        if geocode_result:
            location = geocode_result[0]['geometry']['location'].values()
        else:
            print("Could not geocode area.")
            return []

    # Perform nearby search
    places_result = gmaps.places_nearby(
        location=tuple(location),
        radius=radius,
        keyword=cuisine,
        type='restaurant'
    )

    top_places = sorted(
        places_result.get('results', []),
        key=lambda x: x.get('rating', 0),
        reverse=True
    )[:3]

    results = []
    for place in top_places:
        results.append({
            'name': place.get('name'),
            'rating': place.get('rating'),
            'address': place.get('vicinity'),
            'map_url': f"https://www.google.com/maps/place/?q=place_id:{place.get('place_id')}"
        })

    return results
