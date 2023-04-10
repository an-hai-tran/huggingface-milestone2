import streamlit as st
from transformers import pipeline

#title
st.title("Sentiment analysis of text")

#substitle
st.markdown("## We will analyze the sentence `I hate you` using a pretrained model from Hugging Face")

if st.button("Submit"):
    sentiment_pipeline = pipeline("sentiment-analysis")
    data = "I hate you"
    result = sentiment_pipeline(data)
    st.write(result)