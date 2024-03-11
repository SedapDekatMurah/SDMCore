def save_data(cursor, data):

    # Insert data into the database
    for place in data['places']:
        # Test: print data
        print(place)

        # Name
        name = place['displayName']['text']

        # ID (Primary Key)
        place_id = place['id']

        # Address
        address = place['formattedAddress']

        # TODO the rest

        # Insert the restaurant into the table
        cursor.execute('INSERT OR IGNORE INTO restaurants VALUES (?, ?, ?)',
                       (name, place_id, address))

        for review in place['reviews']:
            review_url = review['authorAttribution']['uri']
            review_rating = review['rating']
            review_text = review['text']['text']

            cursor.execute('INSERT OR IGNORE INTO reviews VALUES(?, ?, ?, ?)',
                           (place_id, review_url, review_rating, review_text))
    print("Data saved successfully to restaurants.db.")
