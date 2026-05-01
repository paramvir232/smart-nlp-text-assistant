import streamlit as st

# Must be first Streamlit command
st.set_page_config(
    page_title="Smart NLP Assistant",
    layout="centered"
)

from modules.spell_checker import spell_check
from modules.autocomplete import train_ngram, predict_next
from modules.sentiment import predict_sentiment
from modules.pos_tagger import pos_tagging
from modules.ner import get_entities
from utils.highlighter import highlight_text
import string
import pandas as pd


# Cache model loading
@st.cache_resource
def load_models():
    train_ngram()
    return True


load_models()

# Title
st.title("🧠 Smart NLP Text Assistant")
st.write("Analyze your text using multiple NLP techniques.")

# Initialize session state
if "input_text" not in st.session_state:
    st.session_state.input_text = ""

# Buttons first
col1, col2 = st.columns(2)

with col1:
    analyze = st.button("Analyze")

with col2:
    example = st.button("Example")

# Set example text BEFORE text_area is created
if example:
    st.session_state.input_text = "I am go to Delhi tomorow to meet Rahul at Google"

# Input box
text = st.text_area(
    "Enter your sentence:",
    key="input_text"
)

# Process input
if analyze and text.strip():

    # Spell correction
    corrected = spell_check(text)

    # Named entities
    entities = get_entities(corrected)

    st.divider()

    # Highlighted output
    st.subheader("✨ Highlighted Output")
    highlighted = highlight_text(text, corrected, entities)
    st.markdown(highlighted, unsafe_allow_html=True)

    # Show corrected sentence separately
    st.subheader("🔧 Corrected Sentence")
    st.success(corrected)

    # Autocomplete suggestions
    st.subheader("🔮 Suggestions")

    last_word = text.split()[-1].lower().strip(string.punctuation)
    suggestions = predict_next(last_word)

    if suggestions:
        for i, word in enumerate(suggestions, start=1):
            st.write(f"{i}. {word}")
    else:
        st.write("No suggestions found")

    # POS tags
    st.subheader("🧠 POS Tags")

    pos_tags = pos_tagging(corrected)

    pos_df = pd.DataFrame(
        pos_tags,
        columns=["Word", "POS Tag", "Meaning"]
    )

    st.table(pos_df)

    # NER display
    st.subheader("🏷️ Named Entities")

    if entities:
        ner_df = pd.DataFrame(
            entities,
            columns=["Entity", "Entity Type"]
        )

        st.table(ner_df)
    else:
        st.write("No entities found")

    # Sentiment
    st.subheader("😊 Sentiment")

    sentiment = predict_sentiment(corrected)

    if "Positive" in sentiment:
        st.success(sentiment)
    else:
        st.error(sentiment)