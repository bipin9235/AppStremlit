import streamlit as st
from agent import ask_agent

# Page setup
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.markdown("""
    <style>
    .fixed-text {
        position: fixed;
        top: 20px;
        left: 30px;
        font-size: 30px;
        font-weight: bold;
        color: white;
        z-index: 1000;
    }
    </style>
    <div class="fixed-text">🤖 Python Agent</div>
    """, unsafe_allow_html=True)

#st.markdown("Type something below and the bot will respond.")

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
    st.rerun()