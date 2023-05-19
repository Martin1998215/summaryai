import streamlit as st
import re

import tensorflow as tf

from transformers import pipeline



st.title("MySummary App")
st.write("---")
st.write("### Fatest way to summarize long articles.")
st.write(
    """
    - Summarize news articles, school or work Notes, Bible or Book chapters for easy and faster reading.
    
    """)

st.warning("**Simply paste whatever you want to summarize in our text bar below. And wait a while for the AI model to process the article. thats it!**")
    

article= st.text_area("Paste Article Here", height=200)



words = len(re.findall(r'\w+', article))
st.write("**Number of words in article is :**", words)

st.write("---")

if st.button("Summarize"):

    if words == 0:

        st.write("### Hello, Paste the article you want to be summarized in the above text bar.")


    elif words < 100:

        st.write("## Sorry! The Article is too short...")
        st.write("### Look for a longer article")


    elif words > 751:

        st.write("## Sorry! The maximum Number of words should not exceed 750.")
        st.write("### Reduce the number of words in your article to around 730-750.")

    else:
        st.write("### Summarize....")

        if words < 200:

            summarizer = pipeline('summarization', model="facebook/bart-large-cnn", framework="tf")
            result = summarizer(article, max_length=70, min_length=30, do_sample=False)[0]["summary_text"]
            st.success(result)
            out = len(re.findall(r'\w+', result))
            st.write("### Number of Summarized Words :", out)


        elif words < 400:
            summarizer = pipeline('summarization', model="facebook/bart-large-cnn", framework="tf")
            result = summarizer(article, max_length=150, min_length=100, do_sample=False)[0]["summary_text"]
            st.success(result)
            out = len(re.findall(r'\w+', result))
            st.write("### Number of Summarized Words :", out) 

        elif words < 600:
            summarizer = pipeline('summarization', model="facebook/bart-large-cnn", framework="tf")
            result = summarizer(article, max_length=180, min_length=130, do_sample=False)[0]["summary_text"]
            st.success(result)
            out = len(re.findall(r'\w+', result))
            st.write("### Number of Summarized Words :", out)    

        elif words < 751:      

            summarizer = pipeline('summarization', model="facebook/bart-large-cnn", framework="tf")
            result = summarizer(article, max_length=250, min_length=200, do_sample=False)[0]["summary_text"]
            st.success(result)
            out = len(re.findall(r'\w+', result))
            st.write("### Number of Summarized Words :", out)

   