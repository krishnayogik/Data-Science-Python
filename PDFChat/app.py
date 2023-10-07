import streamlit as st
import PyPDF2
from transformers import pipeline
import tensorflow as tf

# Load the PDF and extract text
# Load the PDF and extract text
def extract_text_from_pdf(pdf_file):
    pdf_text = ""
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        pdf_text += page.extract_text()
    return pdf_text

# Load the question-answering model
qa_model = pipeline("question-answering", model="distilbert-base-cased-distilled-squad")

# Streamlit app
st.title("PDF Question Answering App")

uploaded_file = st.file_uploader("Choose a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Display the PDF content
    pdf_text = extract_text_from_pdf(uploaded_file)

    # User input for question
    question = st.text_input("Ask a question about the PDF:")

    if question:
        # Ask question and get the answer
        answer = qa_model(context=pdf_text, question=question)
        st.write("Answer:", answer['answer'])
