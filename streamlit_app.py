# Import libraries -
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
 
# Load dotenv -
load_dotenv()
 
# API retrive -
api_key = os.getenv("GENAI_API_KEY")
genai.configure(api_key = api_key)
 
# Model Initialize -
llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])
 
# Streamlit -
st.title("Code Reviewer")
st.chat_message("AI").write("Hello! What can i help you!")
 
user_code = st.text_area("Type Input Here...")
 
# Flow -
if user_code:
    st.chat_message("user").write("Review this code, please.")
    review_prompt = f"Please review the following code: \n\n{user_code}\n\n"
    review_prompt += "Check for the best practices, optimizations, and potential issues/errors."
    response = chatbot.send_message(review_prompt)
 
    # Display Output -
    st.chat_message("AI").write(response.text)
 