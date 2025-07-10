from autogen import ConversableAgent

import streamlit as st
model = "openai/gpt-4.1-Nano"
llm_config = {
    "model": model,
    'base_url':'https://openrouter.ai/api/v1',
    'api_key':st.secrets["OPENAI_API_KEY"],
    #'api_key':OPENAI_API_KEY,
    
}
def ask_agent(msg):
    agent=ConversableAgent(
        name='Chatbot',
        llm_config=llm_config,
        human_input_mode='NEVER',
        system_message='You are a Software Engineer, reply each ask in engineering context.',
    )
    response=agent.generate_reply(
            messages=[{'role':'user','content':{msg}},{'role':'system','content':'You are a Software Engineer, reply each ask in engineering context.'}]
            )
    return response
    
