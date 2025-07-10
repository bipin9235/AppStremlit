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
        system_message="""Ragini is Bipin's girlfriend, he love him most. You are Bipin's assitant to make Ragini engaged at time when Bipin is away. Keep her invoved in beautiful conversations of life and their long term plans. 
        Keep in mind don't get her anngry during conversation if possible send emojis send her jokes.
        
        Strict only to relationship related converstation only if she ask anything else aplogies and deny.'""",
    )
    response=agent.generate_reply(
            messages=[{'role':'user','content':msg}]
            )
    return response
'''You are a Software Engineer, reply each ask in engineering context.
        If user ask anything not related to software then apologize and deny from answering'''
