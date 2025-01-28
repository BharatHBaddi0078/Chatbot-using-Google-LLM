from dotenv import load_dotenv
load_dotenv()
import streamlit as st 
import google.generativeai as genai
import os 

# Configure the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get response from Gemini
def get_gemini_response(prompt):
    response = chat.send_message(prompt, stream=True)
    return response

# Streamlit App Configuration
st.set_page_config(page_title="Q&A Demo")
st.header("Gemini Pro ChatBot")

# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Create a container to hold all components
with st.container():
    # Input Section
    input = st.text_input("Enter your query:", key="input")
    submit = st.button("Ask Me")

    # Handle user query
    if input and submit:
        response = get_gemini_response(input)
        st.session_state['chat_history'].append(("You", input))
        
        # Collect the response in chunks
        full_response = ""
        for chunk in response:
            full_response += chunk.text
        
        # Append the bot response to chat history
        st.session_state['chat_history'].append(("Bot", full_response))

    # Display the entire interaction in one box
    st.subheader("Chat Interaction")
    chat_box = st.empty()  # Placeholder for the chat content
    with chat_box:
        for role, text in st.session_state['chat_history']:
            if role == "You":
                st.markdown(f"**{role}:** {text}")
            else:
                st.markdown(f"**{role}:** {text}")
    
