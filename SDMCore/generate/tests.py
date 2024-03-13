from django.test import TestCase

# generate-scripts/

# generate.py
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
