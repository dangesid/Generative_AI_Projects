from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os 
import sqlite3
import google.generativeai as genai

## Configure API key 
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model and provide SQL query as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content([prompt[0], question])
    sql_query = response.text
    
    # Remove any markdown code block delimiters and whitespace
    sql_query = sql_query.replace("```sql", "").replace("```SQL", "").replace("```", "").strip()
    
    return sql_query

# Function to retrieve query from SQL database

def read_sql_query(sql, db):
    conn = sqlite3.connect(db)  # Establish the connection
    cur = conn.cursor()         # Create a cursor object
    cur.execute(sql)            # Execute the SQL query
    rows = cur.fetchall()       # Fetch all rows from the result
    conn.close()                # Close the connection
    return rows                 # Return the fetched rows

## Define your Prompt 
prompt = [
    """
    You are an expert in converting English question to SQL query!
    The SQL database is named STUDENT and has the following columns - NAME, CLASS, SECTION, and MARKS.
    
    Example 1 - How many entries of records are present? The SQL command will be something like this:
    SELECT COUNT(*) FROM STUDENT;
    
    Example 2 - Tell me all the students studying in DevOps class? The SQL Command will be something like this:
    SELECT * FROM STUDENT WHERE CLASS="DEVOPS";
    
    Make sure the SQL code is wrapped with ''' at the beginning and end, and contains the word SQL.
    """
]

## Streamlit app
st.set_page_config(page_title="SQL query Generator")
st.header("Gemini app to retrieve SQL Data")

question = st.text_input('Input:', key="input")

submit = st.button("Ask the Question")

## If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    print(f"Generated SQL query: {response}")
    
    try:
        data = read_sql_query(response, "student.db")
        st.subheader("The Response is:")
        for row in data:
            st.write(row)
    except sqlite3.Error as e:
        st.error(f"SQL Error: {e}")
