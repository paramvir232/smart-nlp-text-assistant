import nltk

# Dictionary for tag meanings
POS_TAG_MEANINGS = {
    "CC": "Coordinating Conjunction",
    "CD": "Cardinal Digit",
    "DT": "Determiner",
    "EX": "Existential There",
    "FW": "Foreign Word",
    "IN": "Preposition/Subordinating Conjunction",
    "JJ": "Adjective",
    "JJR": "Adjective, Comparative",
    "JJS": "Adjective, Superlative",
    "LS": "List Marker",
    "MD": "Modal",
    "NN": "Noun, Singular",
    "NNS": "Noun, Plural",
    "NNP": "Proper Noun, Singular",
    "NNPS": "Proper Noun, Plural",
    "PDT": "Predeterminer",
    "POS": "Possessive Ending",
    "PRP": "Personal Pronoun",
    "PRP$": "Possessive Pronoun",
    "RB": "Adverb",
    "RBR": "Adverb, Comparative",
    "RBS": "Adverb, Superlative",
    "RP": "Particle",
    "SYM": "Symbol",
    "TO": "to",
    "UH": "Interjection",
    "VB": "Verb, Base Form",
    "VBD": "Verb, Past Tense",
    "VBG": "Verb, Gerund/Present Participle",
    "VBN": "Verb, Past Participle",
    "VBP": "Verb, Non-3rd Person Singular Present",
    "VBZ": "Verb, 3rd Person Singular Present",
    "WDT": "Wh-determiner",
    "WP": "Wh-pronoun",
    "WP$": "Possessive Wh-pronoun",
    "WRB": "Wh-adverb"
}


def pos_tagging(text):
    tokens = nltk.word_tokenize(text)
    tags = nltk.pos_tag(tokens, lang='eng')

    result = []

    for word, tag in tags:
        full_form = POS_TAG_MEANINGS.get(tag, "Unknown")
        result.append((word, tag, full_form))

    return result