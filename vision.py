from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro-vision")

def get_gemini_response(image, input):
    if input != "" :
        response = model.generate_content([image, input])
    else:
        response = model.generate_content(image)
    return response.text

## Initialize page

st.set_page_config("GEMINI LLM APP")
st.header("GEMNI VISION MODEL")

input = st.text_input("Input Prompt: ", key="input")

uploaded_file = st.file_uploader("Choose an image....", type=["jpg", "jpeg", "png"])
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)

submit = st.button("Tell me about the image")

if submit:
    response = get_gemini_response(image, input)
    st.write(response)