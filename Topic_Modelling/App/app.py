import streamlit as st
import pandas as pd
import nltk
from src.preprocessing import clean_text
from src.lda_model import build_lda_model

# Ensure necessary NLTK resources are available
try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')

# Set page configuration
st.set_page_config(page_title="Indian Express News Topic Modeling", layout="wide")

# Styling for dark mode and branding
st.markdown("""
    <style>
        .main {
            background-color: #1E1E1E;
            color: #F1C40F;
        }
        .stButton>button {
            color: white;
            background-color: #F39C12;
            border-radius: 10px;
        }
        .stSlider>div>div>div>div {
            background-color: #F39C12;
        }
    </style>
""", unsafe_allow_html=True)

st.title(":newspaper: Indian Express News - Topic Modeling")
st.markdown("""
Welcome to the Indian Express Topic Modeling App!  
Upload your dataset (CSV format), select the number of topics, and discover insights.
""")

uploaded_file = st.file_uploader("📁 Upload Indian Express CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    # Check and fix column
    if 'text' not in df.columns:
        if 'content' in df.columns:
            df.rename(columns={'content': 'text'}, inplace=True)
            st.info("ℹ️ 'content' column renamed to 'text'.")
        else:
            st.error("❌ The CSV must have a 'text' column or at least a 'content' column.")
            st.stop()

    st.success("✅ File uploaded and processed successfully!")
    df['cleaned_text'] = df['text'].astype(str).apply(clean_text)

    st.markdown("### :gear: Topic Modeling Settings")
    num_topics = st.slider("Select Number of Topics", min_value=2, max_value=10, value=5)

    if st.button("✨ Discover Topics"):
        with st.spinner("Running LDA Topic Modeling..."):
            lda_model, corpus, dictionary = build_lda_model(df['cleaned_text'], num_topics)

        st.markdown("### :bulb: Extracted Topics")
        for idx, topic in lda_model.print_topics():
            st.markdown(f"**Topic {idx + 1}:** {topic}")

        st.balloons()
