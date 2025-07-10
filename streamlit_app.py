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

if "processing" not in st.session_state:
    st.session_state.processing = False

# Text box and Submit button side by side
with st.form(key="chat_form"):
    st.session_state.user_input = st.text_input("You:", value=st.session_state.user_input)
    submitted = st.form_submit_button("Submit")

# Handle submission
if submitted and st.session_state.user_input.strip():
    st.session_state.messages.append(("User", st.session_state.user_input))
    st.session_state.processing = True
    with st.spinner("🤖 Generating response..."):
        bot_reply = ask_agent(st.session_state.user_input)
    st.session_state.messages.append(("Bot", bot_reply))
    st.session_state.processing = False
    st.session_state.user_input = ""  # Clear text input

# Display chat history
for sender, message in st.session_state.messages:
    if sender == "User":
        st.markdown(f"👤 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")