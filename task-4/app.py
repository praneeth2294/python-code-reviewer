import streamlit as st
import google.generativeai as ai

ai.configure(api_key="AIzaSyBvcEU2QNjDcvh3w-hFv7RDN4YbMzB3I1g")

sys_prompt = """You are an AI Code Reviewer specializing in Python programming. Your task is to analyze Python code, detect potential bugs, syntax errors, logical mistakes, inefficiencies, and best practice violations, and provide clear and actionable fixes with explanations."""

gemini_model = ai.GenerativeModel(model_name="models/gemini-1.5-pro", system_instruction=sys_prompt)

st.title("Python Code Reviewer")

user_input = st.text_area(label="Enter your query/issue", placeholder="Ask me about the datascience ")

btn_click = st.button("Click Me!")

if btn_click == True:
    response = gemini_model.generate_content(user_input)
    print("OUTPUT ON TERMINAL: ", len(response.text))
    st.write(response.text)