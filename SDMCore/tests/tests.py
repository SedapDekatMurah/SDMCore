from django.test import TestCase
from unittest.mock import patch

import requests
from SDMCore.core.scripts import generate, places, save

# generate-scripts/

# generate.py

# generate_data function


class TestGenerateData(TestCase):
    def test_func_generate_data(self):
        # Assert that generate_data returns true on a valid query
        self.assertEqual(generate.generate_data(
            "3.139003", "101.686852"), True)

        # Assert that generate_data returns False on an invalid query
        self.assertEqual(generate.generate_data("100", "10"), False)


class TestSave(TestCase):
    testData = {"places": [{'displayName': {
        'text': "testvalue"}, 'id': "testId", 'formattedAddress': "112233 Malibu Point", 'location': {'latitude': "10", 'longitude': '10'}, 'rating': "4", 'googleMapsUri': "http://test", 'reviews': [{'authorAttribution': {'uri': "testUrl"}, 'text': {'text': "testreview"}}]}]}

    def test_func_save_places(self):
        # Assert that save_places returns True on a valid operatiosn
        self.assertEqual(save.save_places(self.testData), True)


class TestPlaces(TestCase):
    def test_unit_get_restaurants(self):
        # Assert that get_restaurant returns true on a valid query
        data = places.get_restaurants(
            "3.139003", "101.686852")
        assert 'places' in data

        # Assert that get_restaurants returns False on an invalid query
        data = places.get_restaurants("100", "10")
        assert 'places' not in data

    def test_unit_get_api_key(self):
        # Returns a string value when given a valid file path
        data = places.get_api_key("api_key.txt")
        assert data != ""

        # Returns a blank string when given an invalid file path
        data = places.get_api_key("invalidpath")
        assert data == ""


class TestKeywords(TestCase):
    def test_func_generate_keywords(self):
        return

    def test_unit_get_top_keywords(self):
        return
        # get_top_keywords returns a list of keywords given a list of strings
        # get_top_keywords returns a blank array if given a blank string


class TestPlacesAPI(TestCase):
    def test_int_places_api(self):
        # Places API should return expected values. Test does not include a valid API key so it should give 'no key' error

        URL = "https://places.googleapis.com/v1/places:searchNearby"

        API_KEY = ""

        headers = {
            'Content-Type': "application/json",
            'X-Goog-API-Key': API_KEY,
            'X-Goog-FieldMask': "places.id,places.displayName,places.rating,places.googleMapsUri,places.formattedAddress,places.location,places.reviews",
        }

        data = {
            "includedTypes": ["restaurant"],
            "maxResultCount": 2,
            "locationRestriction": {
                "circle": {
                    "center": {
                        "latitude": 10,
                        "longitude": 10,
                    },
                    "radius": 500.0
                }
            }
        }

        response = requests.post(URL, headers=headers, json=data)

        # Error code 403 (no API key)
        assert response.status_code == 403


class TestViews(TestCase):
    def test_func_generate(self):
        return


class TestMenu(TestCase):
    def test_get_menu(self):
        return

# # generate_initial_data function
# # # Should take two number parameters
# # # returns False when any of the 4 tasks fail
# # # returns True when all 4 tasks succeed

# save.py
# # save_places function
# # # takes an object variable
# # # returns False when task fails
# # # return True when task succeeds

# keywords.py
# # generate_keywords function
# # # Should take no parameters
# # # Return False if task fails
# # # Return True if task succeeds
# # get_top_keywords function
# # # Should take one Array<string> parameter
# # # Return False if task fails
# # # Return True if task succeeds

# menu.py
# # generate_menu function
# # # Should take no parameters
# # # Return False if task fails
# # # Return True if task succeeds

# model.py
# # generate_data function
# # # should take 2 variables: latitude, longitude
# # # should return error message on a failure
# # # should return success message on a pass

# views.py
# # post_generate function
# # # should take 1 variable: packet
# # # should return error reply packet if packet does not contain data (latitude, longitude)
# # # should return reply packet from generate_data function
