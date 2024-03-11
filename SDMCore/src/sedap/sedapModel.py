import sqlite3
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Download NLTK resources
nltk.download('vader_lexicon')


def summarize_sentiment(reviews):
    # Initialize sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # Initialize counters
    total_positive = 0
    total_neutral = 0
    total_negative = 0

    # Iterate through each review and analyze sentiment
    for review in reviews:
        print(review)
        scores = sia.polarity_scores(review)
        compound_score = scores['compound']

        # Classify sentiment
        if compound_score >= 0.05:
            total_positive += 1
        elif compound_score > -0.05 and compound_score < 0.05:
            total_neutral += 1
        else:
            total_negative += 1

    # Calculate percentages
    total_reviews = len(reviews)
    positive_percentage = (total_positive / total_reviews) * 100
    neutral_percentage = (total_neutral / total_reviews) * 100
    negative_percentage = (total_negative / total_reviews) * 100

    # Print summary
    print("Sentiment Summary:")
    print(f"Positive: {positive_percentage:.2f}%")
    print(f"Neutral: {neutral_percentage:.2f}%")
    print(f"Negative: {negative_percentage:.2f}%")


# Example usage
if __name__ == "__main__": \
        # Get data from DB
    conn = sqlite3.connect('../../data/restaurants.db')
    cursor = conn.cursor()

    # Get all reviews
    reviews_aggregate = cursor.execute('''SELECT * FROM reviews''')

    # Create a list of all Restaurants in the database
    restaurant_list = []
    for review in reviews_aggregate.fetchall():
        if review[0] not in restaurant_list:
            restaurant_list.append(review[0])

    review_list = []

    # For each restaurant ID, create a subarray of reviews
    for restaurant in restaurant_list:
        reviews = cursor.execute(
            '''SELECT review FROM reviews WHERE place_id=(?)''', (restaurant,)).fetchall()
        new_restaurant = []
        for review in reviews:
            new_restaurant.append(review[0])
        review_list.append(new_restaurant)

    for reviews in review_list:
        # Summarize sentiment
        summarize_sentiment(reviews)
