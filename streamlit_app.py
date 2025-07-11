import streamlit as st
from agent import ask_agent

# Page setup
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chat with AI")
st.markdown("Type something below and the bot will respond.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display messages top-down
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Bottom input using chat_input
user_input = st.chat_input("You:")

if user_input:
    # Add user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Show bot is "thinking"
    with st.chat_message("assistant"):
        with st.spinner("🤖 Generating response..."):
            response = ask_agent(user_input)
            st.markdown(response)

    # Add bot message
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Refresh to show updated messages
    st.experimental_rerun()