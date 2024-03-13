from SDMCore.generate.scripts import save, places, keywords, menu

# Master script for triggering generation process


def generate_data(latitude, longitude):
    # Get data from Google Places API
    restaurant_data = places.get_restaurants(latitude, longitude)

    if 'ErrorStatus' in restaurant_data:
        return False

    # Populate db with initial data
    if not save.save_places(restaurant_data):
        return False

    # Create keywords
    if not keywords.generate_keywords():
        return False

    # Create menu
    if not menu.generate_menu():
        return False

    # Return successful only if all operations pass
    return True
