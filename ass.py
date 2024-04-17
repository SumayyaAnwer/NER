import streamlit as st
from newspaper import Article
import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

st.title("Named Entity Recognition")


input_url = st.text_area("Enter URL here:")
input_paragraph = st.text_area("Enter paragraph here:")

if st.button("Analyze"):
    if input_url:
        article = Article(input_url)
        article.download()
        article.parse()
        doc = nlp(article.text)
        html = displacy.render(doc, style='ent', jupyter=False)
        st.markdown(html, unsafe_allow_html=True)
    elif input_paragraph:
        doc = nlp(input_paragraph)
        html = displacy.render(doc, style='ent', jupyter=False)
        st.markdown(html, unsafe_allow_html=True)
    else:
        st.write("Please enter a URL or a paragraph.")

