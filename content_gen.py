from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

st.set_page_config("GEMINI LLM APP")
st.header('GEMINI LLM APPLICATION')

input = st.text_input("Input: ", key="input")

submit = st.button("SUBMIT")

if submit and input:
    response = get_gemini_response(input)
    st.write(response)