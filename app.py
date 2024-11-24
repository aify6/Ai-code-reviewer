import streamlit as st
import google.generativeai as genai  # Correct import

# Set up the Google Generative AI API
with open('apikey.txt', 'r') as key_file:
        key = key_file.read().strip()
genai.configure(api_key=key)

# Streamlit UI setup
st.title("🤖 An AI Code Reviewer")
st.subheader("Enter your Python code below:")

# Text area for user to input Python code
user_code = st.text_area("", height=200, placeholder="Enter your Python code here...")

# Button to submit the code
if st.button("Generate"):
    if user_code.strip():
        with st.spinner("Analyzing your code..."):
            try:
                # Prepare the prompt
                prompt = (
                    """You are an experienced code reviewer specializing in clean, efficient, and error-free code. 
                    Analyze the following code and provide a detailed review, including:
                    Identification of any bugs, logical errors, or syntax issues.
                    Suggestions for performance improvements or best practices.
                    Corrected code snippets with clear explanations for each suggested fix.
                    Please ensure your feedback is concise, actionable, and easy to understand.\n\n"""
                    f"Code:\n{user_code}"
                )

                # Use the correct model
                model = genai.GenerativeModel('gemini-pro')  # 'gemini-pro' or relevant model
                response = model.generate_content(prompt)

                # Extract the response text
                feedback = response.text

                # Display the results
                st.subheader("Code Review")
                st.markdown("### Bug Report:")
                st.write(feedback)

                st.markdown("### Fixed Code:")
                st.code(user_code, language="python")  # Replace with corrected code when available

            except Exception as e:
                st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter your code for review.")
