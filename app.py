import streamlit as st
import google.generativeai as genai
st.title("Welcome to my chatbot")
genai.configure(api_key="AIzaSyBMp5P3axTqb6rHyq9DOAAWcoh0f6AKqmQ")
text=st.text_input("Enter your question")
model=genai.GenerativeModel('gemini-pro')
chat=model.start_chat(history=[])
if st.button("Click me to get Answer for your question"):
    response=chat.send_message(text)
    st.write(response.text)