import requests
import json

# Gets data from Google Places API


# # # IMPORTANT: PLACE YOUR GOOGLE API KEY INTO A TEXT FILE NAMED 'api_key.txt' IN THE SAME DIRECTORY # # #


def get_api_key(file_path):
    # Path to the text file containing the API key
    api_key_file = file_path

    # Read API key from the text file
    try:
        with open(api_key_file, 'r') as file:
            api_key = file.read().strip()
        return api_key
    except FileNotFoundError:
        print("File not found.")
        return ""
    except IOError as e:
        print("Error reading the file:", e)
        return ""
    except Exception as e:
        print("An unexpected error occurred:", e)
        return ""


def get_restaurants(latitude, longitude):
    # Places SearchNearby API url
    URL = "https://places.googleapis.com/v1/places:searchNearby"

    # Retrieve your api key
    API_KEY = get_api_key('api_key.txt')

    # Set Header info
    headers = {
        'Content-Type': "application/json",
        'X-Goog-API-Key': API_KEY,

        # FieldMask fields are available at: https://developers.google.com/maps/documentation/places/web-service/nearby-search
        'X-Goog-FieldMask': "places.id,places.displayName,places.rating,places.googleMapsUri,places.formattedAddress,places.location,places.reviews",
    }

    # Set data info. Syntax for Google Places API(New) available at: https://developers.google.com/maps/documentation/places/web-service/nearby-search
    data = {
        "includedTypes": ["restaurant"],
        "maxResultCount": 2,
        "locationRestriction": {
            "circle": {
                "center": {
                    "latitude": float(latitude),
                    "longitude": float(longitude),
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
        return response.json()
    else:
        print("Request failed!")
        print("Status code:", response.json())
        return json.dumps({'ErrorStatus': "true"})
