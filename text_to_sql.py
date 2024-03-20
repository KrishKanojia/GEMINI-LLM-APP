import streamlit as st
import os
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()

## Configure our API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load Google Gemini Model and provide sql query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

## Retrieve query from Sql Database
def read_sql_query(sql_query, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql_query)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    # for row in rows:
    #     print(row)
    return rows

## Define your prompt
prompt = [
    """
    You are expert in converting English question to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT;\n
    Example 2 - Tell me all the students studying in Data Science class?,
    the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS = "Data Science";
    also the sql code should not have ''' in the beginning or end and sql word in the output
"""
]

## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve SQL Data")

question = st.text_input("Input: ", key="input")

submit = st.button("Ask me question")

## if submit is clicked 
if submit:
    response = get_gemini_response(question, prompt)
    print(response)
    data = read_sql_query(response, "student.db")
    st.subheader("The Response is:")
    for row in data:
        print(row)
        st.header(row)