from django.test import TestCase
from unittest.mock import patch
from SDMCore.core.scripts import save, places, keywords, menu, generate
from SDMCore.core.scripts import generate

# generate-scripts/

# generate.py

# generate_data function


class GenerateDataTestCase(TestCase):
    # get_restaurant returns 'ErrorStatus'
    @patch('places.get_restaurant')
    def get_restaurants_error_returns_false(self, mock_get_restaurant):

        # Mock return value of places.get_restaurants
        mock_get_restaurant.return_value = {'ErrorStatus': 'test'}

        # Assert that getting 'ErrorStatus' from places.get_restaurants will cause generate_data to return False
        self.assertEqual(generate.generate_data("10", "10"), False)

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
