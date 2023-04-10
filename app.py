import streamlit as st
from transformers import pipeline

#title
st.title("Sentiment analysis of text")

sentiment_pipeline = pipeline("sentiment-analysis")
data = "I hate you"
st.write(sentiment_pipeline(data))