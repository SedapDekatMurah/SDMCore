import requests
import googlemaps
import sqlite3
from generate_scripts import save_data


from geopy.geocoders import GoogleV3


# DATA BOOTSTRAP: Script to generate initial training data


def get_api_key(file_path):
    # Path to the text file containing the API key
    api_key_file = file_path

    # Read API key from the text file
    with open(api_key_file, 'r') as file:
        api_key = file.read().strip()
        print(api_key)
    return api_key


def get_current_location():
    # DOTO get current location
    # PLACEHOLDER return tutorial location (I think its in sacramento..)
    return (40.7128, -74.0060)


# Retrieve your api key
API_KEY = get_api_key('api_key.txt')

# Build google maps client
gmaps_client = googlemaps.Client(key=API_KEY)

# Places SearchNearby API url
URL = "https://places.googleapis.com/v1/places:searchNearby"

latitude, longitude = get_current_location  # Example New York City

# Set Header info
headers = {
    'Content-Type': "application/json",
    'X-Goog-API-Key': API_KEY,

    # FieldMask fields are available at: https://developers.google.com/maps/documentation/places/web-service/nearby-search
    'X-Goog-FieldMask': "places.id,places.displayName,places.rating,places.formattedAddress,places.reviews",
}

# Set data info. Syntax for Google Places API(New) available at: https://developers.google.com/maps/documentation/places/web-service/nearby-search
data = {
    "includedTypes": ["restaurant"],
    "maxResultCount": 5,
    "locationRestriction": {
        "circle": {
            "center": {
                "latitude": latitude,
                "longitude": longitude,
            },
            "radius": 500.0
        }
    }
}

# Get data from Google Maps
response = requests.post(URL, headers=headers, json=data)
# Check the response
if response.status_code == 200:
    print("Request successful!")
    # If the response is JSON, you can access it like this
    # print(response.json())
else:
    print("Request failed!")
    print("Status code:", response.status_code)
    # print("Response content:", response.text)

# Connect to SQLite database
conn = sqlite3.connect('./data/restaurants.db')
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.executescript('''DROP TABLE IF EXISTS restaurants;
                     DROP TABLE IF EXISTS reviews;
                     CREATE TABLE IF NOT EXISTS restaurants
                  (name TEXT, place_id TEXT PRIMARY KEY, address TEXT, loc_latitude TEXT, loc_longitude TEXT , range TEXT, maps_url TEXT, menu_1_name TEXT, menu_1_price TEXT, menu_2_name TEXT, menu_2_price TEXT, menu_3_name TEXT, menu_3_price TEXT,keyword_1 TEXT, keyword_2 TEXT, keyword_3 TEXT, keyword_4 TEXT, keyword_5 TEXT);
                     CREATE TABLE IF NOT EXISTS reviews (place_id TEXT, uri TEXT PRIMARY KEY, rating NUMERIC, review TEXT);
                     ''')

data = response.json()

# Save data to db
save_data(cursor, data)


# Commit changes and close connection
conn.commit()
conn.close()


# TODO Separate function to generate review data
