import streamlit as st
from agent import ask_agent

# Page setup
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chat with AI")
st.markdown("Type something below and the bot will respond.")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

# Text input
user_input = st.text_input("You:", value=st.session_state.user_input)

# Handle new input
if user_input and st.session_state.get("last_input") != user_input:
    st.session_state.messages.append(("User", user_input))
    with st.spinner("🤖 Generating response..."):
        bot_reply = ask_agent(user_input)
    st.session_state.messages.append(("Bot", bot_reply))
    st.session_state.last_input = user_input
    st.session_state.user_input = ""  # Clear input box

# Scrollable conversation history
st.markdown("""
<div style="height: 300px; overflow-y: auto; padding: 10px; border: 1px solid #ccc; background-color: #f9f9f9;">
""", unsafe_allow_html=True)

for sender, message in st.session_state.messages:
    if sender == "User":
        st.markdown(f"👤 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")

st.markdown("</div>", unsafe_allow_html=True)