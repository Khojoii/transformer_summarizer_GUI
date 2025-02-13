from transformers import pipeline
import streamlit as st
import pickle

summarizer = pipeline("summarization", model="./saved_model")

# Define summarization function
def summarization(article, max_length=130, min_length=30, do_sample=False):
    summary = summarizer(article, max_length=max_length, min_length=min_length, do_sample=do_sample)
    return summary[0]['summary_text']

# Streamlit UI
st.title("Text Summarizer")
input_text = st.text_area("Enter your text:", height=200)
max_length = st.slider("Maximum summary length", 50, 200, 130)
min_length = st.slider("Minimum summary length", 10, 50, 30)

if st.button("Summarize"):
    summary = summarization(input_text, max_length=max_length, min_length=min_length)
    st.write("**Summary:**", summary)