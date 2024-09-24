# streamlit_app.py (Streamlit app)
import streamlit as st
import requests

# URL of the Flask app
FLASK_API_URL = "http://localhost:5000/query"

# Streamlit UI
st.title("AI Model Selection")

# Dropdown for model selection
model_option = st.selectbox(
    "Choose an AI model:",
    ["text-to-text", "text-to-speech", "text-to-image"]
)

# Input for user prompt
user_prompt = st.text_input("Enter your prompt:")

if st.button("Submit"):
    if user_prompt and model_option:
        # Prepare the request payload
        payload = {
            "prompt": user_prompt,
            "model": model_option
        }

        # Send POST request to Flask app
        try:
            response = requests.post(FLASK_API_URL, json=payload)
            result = response.json()
            
            # Display the response from the API
            st.write("Response from the AI:")
            st.write(result)
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please select a model and enter a prompt.")
