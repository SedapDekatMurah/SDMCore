from SDMCore.generate.models import Restaurant, Review

# Save data retrieved from Places API


def save_places(data):
    try:
        for place in data['places']:
            # Test: print data
            # print(place)

            # Name
            name = place['displayName']['text']

            # ID (Primary Key)
            place_id = place['id']

            # Address
            address = place['formattedAddress']

            # Latitude
            loc_latitude = place['location']['latitude']

            # Longitude
            loc_longitude = place['location']['longitude']

            # Rating
            rating = place['rating']

            # Maps URL
            maps_url = place['googleMapsUri']

            # Insert restaurant into table
            Restaurant.objects.get_or_create(name=name, place_id=place_id, address=address,
                                             loc_latitude=loc_latitude, loc_longitude=loc_longitude, rating=rating, maps_url=maps_url)

            # Insert reviews into table
            for review in place['reviews']:
                review_url = review['authorAttribution']['uri']
                review_text = review['text']['text']

                Review.objects.get_or_create(
                    place_id=place_id,
                    url=review_url, review=review_text)

        # Returns true if successful
        print("Successfully saved data to database")
        return True
    except Exception as exc:
        # Returns false if failed
        print("Error saving data to database", exc)
        return False
