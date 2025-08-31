import streamlit as st
import google.generativeai as genai
import os
import time

# --- Page Configuration ---
# Set the page title and icon
st.set_page_config(page_title="Health Assistant", page_icon="⚕️")

# --- Introduction & Instructions ---
# Display the title and a short introductory message for the chatbot
st.title("⚕️ Your Health Assistant")
st.write(
    "Hello! I am here to provide general information on health and wellness. "
    "I can give advice on nutrition, exercise, and lifestyle, and can suggest common "
    "over-the-counter medicines. "
    "**Disclaimer: I am not a medical professional. Always consult a doctor "
    "for professional medical advice.**"
)

# --- API Key Setup ---
# The API key is stored securely in Streamlit's secrets management.
# You need to create a file named `.streamlit/secrets.toml` with the following content:
# GOOGLE_API_KEY="your_api_key_here"
# Replace "your_api_key_here" with your actual Gemini API key.
api_key = st.secrets["GOOGLE_API_KEY"]

# Configure the Gemini API client with the retrieved key
genai.configure(api_key=api_key)

# --- Model Initialization ---
# Initialize the Gemini Flash model for the conversation
# This model is a newer, more efficient version than gemini-pro.
model = genai.GenerativeModel('gemini-1.5-flash')

# --- Session State Management ---
# Initialize chat history in Streamlit's session state if it doesn't exist.
# This ensures the conversation is remembered across interactions.
if "messages" not in st.session_state:
    st.session_state.messages = []

# --- Display Chat Messages ---
# Loop through the messages in the session state and display them
# with the appropriate icon (user or bot).
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- User Input Handling ---
# Get user input from the chat input box.
if prompt := st.chat_input("Ask a health-related question..."):
    # Add user message to the session state
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display the user's message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # --- Generate Model Response ---
    with st.chat_message("assistant"):
        # Create a container for the response to be streamed into
        stream = st.empty()
        full_response = ""

        # Use a try-except block to handle potential API errors.
        try:
            # Generate the response from the Gemini model.
            # We use a custom system instruction to guide the model's persona.
            # The streaming=True parameter allows for real-time text generation.
            response = model.generate_content(
                f"""
                You are a helpful healthcare assistant chatbot. You are designed to provide general information on health,
                wellness, nutrition, exercise, and lifestyle. You can also suggest common, non-prescriptive, over-the-counter
                (OTC) medicines for minor ailments like headaches or colds.

                **IMPORTANT RULE:** You must include a prominent disclaimer in your response stating that you are not a medical
                professional and that the user should always consult a doctor for a proper diagnosis or professional advice.
                Place this disclaimer at the beginning or end of your response.

                User query: {prompt}
                """,
                stream=True
            )

            # Stream the response word by word
            for chunk in response:
                if chunk.parts and chunk.parts[0].text:
                    full_response += chunk.parts[0].text
                    stream.markdown(full_response + "▌")  # Add a blinking cursor effect

            # Remove the blinking cursor
            stream.markdown(full_response)
            # Add the assistant's full response to the session state
            st.session_state.messages.append({"role": "assistant", "content": full_response})

        except Exception as e:
            # If an error occurs (e.g., API key is invalid), display an error message.
            error_message = f"An error occurred: {e}. Please check your API key and try again."
            st.error(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})