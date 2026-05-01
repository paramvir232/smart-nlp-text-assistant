from collections import defaultdict
from nltk.corpus import brown
import nltk

nltk.download('brown')

ngram_model = defaultdict(list)


def train_ngram():
    sentences = brown.sents()

    for sent in sentences:
        words = [w.lower() for w in sent]

        for i in range(len(words)-1):
            ngram_model[words[i]].append(words[i+1])


def predict_next(word):
    word = word.lower()

    if word in ngram_model:
        suggestions = ngram_model[word]

        # remove duplicates
        unique = list(dict.fromkeys(suggestions))

        return unique[:5]

    return []