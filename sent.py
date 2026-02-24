import streamlit as st
from model import predict_sentiment

st.set_page_config(page_title="AI Sentiment Analyzer")



st.title("🤖AI Sentiment Analyzer")
st.write("Enter text and AI will detect emotion.")

user_input = st.text_area("Enter your sentence: ")

if st.button("Analyze"):
    if user_input:
        result = predict_sentiment(user_input)
        st.success(f"Sentiment: {result}")
    else:
        st.warning("Please enter some text!")