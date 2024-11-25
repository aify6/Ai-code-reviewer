import streamlit as st
import google.generativeai as genai 

# Set up the Google Generative AI API
with open('apikey.txt', 'r') as key_file:
    key = key_file.read().strip()
genai.configure(api_key=key)

# Streamlit UI setup
st.title("🤖 AI Code Reviewer")
st.caption("Enhancing your code, one review at a time!")  

# Add a visual divider
st.divider()

# Text area for user to input Python code
st.subheader("Enter Your Code Below:")
user_code = st.text_area("", height=250, placeholder="Paste your Python code here...")


# Button to submit the code
if st.button("Review Code"):
    if user_code.strip():
        with st.spinner("Analyzing your code... 🚀"):
            try:
                # Prepare the prompt
                prompt = (
                    """You are an experienced code reviewer specializing in clean, efficient, and error-free code. 
                    Analyze the following code and provide a detailed review, including:
                    Identification of the language, identification of any bugs, logical errors, or syntax issues.
                    Suggestions for performance improvements or best practices.
                    Corrected code snippets with clear explanations for each suggested fix.
                    Please ensure your feedback is concise, actionable, and easy to understand.\n\n"""
                    f"Code:\n{user_code}"
                )

                # Use the correct model
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(prompt)

                # Extract the response text
                feedback = response.text

                # Display the results
                st.subheader("Code Review Results")

                # Use expander to neatly organize the bug report
                with st.expander("Bug Report and Suggestions"):
                    st.markdown("### Bug Report:")
                    st.write(feedback)

                # Display the fixed code in a highlighted code block
                st.markdown("### Suggested Fixed Code:")
                st.code(user_code)  # Replace with corrected code when available

            except Exception as e:
                st.error(f"❗ An error occurred: {str(e)}")
    else:
        st.warning("Please enter your code for review.")

# Footer for attribution
st.caption("🚀 Developed during my internship with Innomatics Research Labs.")
