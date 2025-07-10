import streamlit as st
from agent import ask_agent

# Page setup
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 Chat with AI")
st.markdown("Type something below and the bot will respond.")

# Initialize session states
if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_input" not in st.session_state:
    st.session_state.user_input = ""

if "submit_clicked" not in st.session_state:
    st.session_state.submit_clicked = False

# Layout for input and button
col1, col2 = st.columns([5, 1])

with col1:
    st.session_state.user_input = st.text_input("You:", value=st.session_state.user_input, label_visibility="collapsed")

with col2:
    if st.button("Submit"):
        st.session_state.submit_clicked = True

# Handle submission
if st.session_state.submit_clicked and st.session_state.user_input.strip():
    st.session_state.messages.append(("User", st.session_state.user_input))
    with st.spinner("🤖 Generating response..."):
        bot_reply = ask_agent(st.session_state.user_input)
    st.session_state.messages.append(("Bot", bot_reply))
    st.session_state.user_input = ""  # Clear input field
    st.session_state.submit_clicked = False  # Reset button state

# Display chat history
for sender, message in st.session_state.messages:
    if sender == "User":
        st.markdown(f"👤 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")