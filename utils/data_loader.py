import nltk
from nltk.corpus import words

nltk.download('words')

def load_dictionary():
    return set(words.words())