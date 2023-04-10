import streamlit as st
from transformers import pipeline

#title
st.title("Sentiment analysis of text")

#substitle
st.markdown("## We will analyze a sentence using a pretrained model from Hugging Face")

input = st.text_input("Input sentence:","I hate you")

if st.button("Submit"):
    sentiment_pipeline = pipeline("sentiment-analysis")
    data = [input]
    result = sentiment_pipeline(data)
    st.write(result)