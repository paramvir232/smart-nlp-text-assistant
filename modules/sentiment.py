import nltk
from nltk.corpus import movie_reviews
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

nltk.download('movie_reviews')

documents = []

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        review = " ".join(movie_reviews.words(fileid))
        documents.append((review, category))

# Shuffle data
random.shuffle(documents)

# More training samples
texts = [doc[0] for doc in documents[:1800]]
labels = [1 if doc[1] == "pos" else 0 for doc in documents[:1800]]

# Better vectorization
vectorizer = TfidfVectorizer(
    stop_words='english',
    max_features=5000
)

X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)


def predict_sentiment(text):
    X_test = vectorizer.transform([text])

    prediction = model.predict(X_test)[0]
    probability = model.predict_proba(X_test)[0]

    confidence = round(max(probability) * 100, 2)

    if prediction == 1:
        return f"Positive 😊 ({confidence}% confidence)"
    else:
        return f"Negative 😡 ({confidence}% confidence)"