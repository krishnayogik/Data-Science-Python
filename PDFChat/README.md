## PDF CHAT APPLICATION

 - In the provided code, we utilize PyPDF2, a Python library, to extract text from uploaded PDF files. PyPDF2 enables the application to process PDF content effectively. 

- Additionally, we integrate Hugging Face's Transformers library, a widely-used NLP toolkit, leveraging its pre-trained question-answering model (specifically, 'distilbert-base-cased-distilled-squad'). 

- This model empowers the application to generate meaningful answers based on the content of the PDF and the questions posed by the user. 

- To build the user interface and create an interactive web application, we employ Streamlit.

## INSTRUCTIONS TO RUN IN COLAB

``` !pip install streamlit -q ```

``` !wget -q -O - ipv4.icanhazip.com ```

``` !streamlit run app.py & npx localtunnel --port 8501 ```

## OUTPUT SCREENSHOT

![image](https://github.com/krishnayogik/Data-Science-Python/assets/7524417/9c3bf1ad-64c9-4e05-bca3-0ae037a9facb)
