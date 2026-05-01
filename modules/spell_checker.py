from collections import Counter
from nltk.corpus import words, brown
from utils.edit_distance import edit_distance
import nltk

nltk.download('words')
nltk.download('brown')

dictionary = set(w.lower() for w in words.words())

# Word frequency from Brown corpus
word_freq = Counter(w.lower() for w in brown.words())


def correct_word(word):
    word_lower = word.lower()

    # Keep proper nouns
    if word[0].isupper():
        return word

    if word_lower in dictionary:
        return word

    candidates = []

    for dict_word in dictionary:
        dist = edit_distance(word_lower, dict_word)

        if dist <= 2:
            candidates.append((dict_word, word_freq[dict_word]))

    if candidates:
        # choose most frequent candidate
        best_word = max(candidates, key=lambda x: x[1])[0]
        return best_word

    return word


def spell_check(sentence):
    words_list = sentence.split()
    corrected = [correct_word(w) for w in words_list]
    return " ".join(corrected)