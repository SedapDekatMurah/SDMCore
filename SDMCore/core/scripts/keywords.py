from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from collections import Counter
from SDMCore.core.models import Restaurant, Review
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('stopwords')

# PoC Bootstrap Keyword generation from Google Reviews


def get_top_keywords(reviews, n=10):
    # Combine all review text into one string
    combined_text = ""
    for review in reviews:
        combined_text += review.review + " "

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

    # Fetch all entries in review table
    reviews_all = Review.objects.all()

    # List all Restaurants by place id
    restaurants_by_place_id = []
    for review in reviews_all:
        if review.place_id not in restaurants_by_place_id:
            restaurants_by_place_id.append(review.place_id)

    # Create a sorted review list, by restaurant id
    for restaurant in restaurants_by_place_id:
        reviews_filter = reviews_all.filter(place_id=restaurant)

        # Adding top keywords to restaurant profile

        # Generate keywords using NLP
        top_keywords = get_top_keywords(reviews_filter)

        # Get list of keyword keys
        keyword_list = list(top_keywords)

        # TODO additional processing

        # Insert top 5 into restaurant profile
        restaurant = Restaurant.objects.get(place_id=restaurant)
        restaurant.keyword_1 = keyword_list[0]
        restaurant.keyword_2 = keyword_list[1]
        restaurant.keyword_3 = keyword_list[2]
        restaurant.keyword_4 = keyword_list[3]
        restaurant.keyword_5 = keyword_list[4]

        restaurant.save()

    return True
