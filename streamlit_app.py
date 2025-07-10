import streamlit as st

# Set up the page
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chat with AI")
st.markdown("Type something below and the bot will respond.")

# Initialize session state to store the conversation
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input box
user_input = st.text_input("You:", "")

# Simulate a response function (placeholder)
def get_bot_response(user_message):
    # Add logic here to connect to an AI model
    return f"You said: '{user_message}'. I'm still learning—try again!"

# Handle new input
if user_input and st.session_state.get("last_input") != user_input:
    st.session_state.messages.append(("User", user_input))
    bot_reply = get_bot_response(user_input)
    st.session_state.messages.append(("Bot", bot_reply))
    st.session_state.last_input = user_input

# Display conversation history
for sender, message in st.session_state.messages:
    if sender == "User":
        st.markdown(f"👤 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")