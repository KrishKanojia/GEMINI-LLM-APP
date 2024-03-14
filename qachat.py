from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))


## Function to load GEMINI pro model and get response
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## Set up page
st.set_page_config("GEMINI LLM APP")
st.header("Conversational QA Chatbot")


## Initialize Stream session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []


input = st.text_input("Enter Text")
submit = st.button("Submit")

if input and submit:
    response = get_gemini_response(input)
    # Add input in chat history
    st.session_state['chat_history'].append(('You', input))
    st.subheader("The Response is")
    # Add model response in chat history
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(('Bot', chunk.text))

st.subheader('The chatbot history')

for role, text in st.session_state['chat_history']:
    st.write(f'{role}:{text}')