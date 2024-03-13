from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from collections import Counter
import sqlite3
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

# PoC Bootstrap Keyword generation from Google Reviews


def get_top_keywords(texts, n=10):
    # Combine all texts into one string
    combined_text = ' '.join(texts)

    # Tokenize the text
    tokens = word_tokenize(combined_text)

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [
        word for word in tokens if word.lower() not in stop_words]

    # Join filtered tokens back into text
    filtered_text = ' '.join(filtered_tokens)

    # Use CountVectorizer to count word frequencies
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([filtered_text])
    word_freq = dict(zip(vectorizer.get_feature_names_out(), X.toarray()[0]))

    # Sort the word frequencies
    sorted_word_freq = dict(
        sorted(word_freq.items(), key=lambda item: item[1], reverse=True))

    # Get top n keywords
    top_keywords = dict(Counter(sorted_word_freq).most_common(n))

    return top_keywords


# Example usage
def generate_keywords():

    # TODO
    return True

    # Get data from DB
    conn = sqlite3.connect('../data/restaurants.db')
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
        # Get top 10 keywords
        print(get_top_keywords(reviews, 10))

        # IDEAS: FURTHER FILTERING OF KEYWORDS (e.g. only adjectives to assess 'sedap', nouns for menu items)
