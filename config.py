import streamlit as st
model = "openai/gpt-4.1-Nano"
try:
    from api_key import OPEN_API_KEY
    api_key=OPEN_API_KEY
except Exception as e:
     api_key=st.secrets["OPENAI_API_KEY"]

llm_config = {
    "model": model,
    'base_url':'https://openrouter.ai/api/v1',
    'api_key':api_key,
}