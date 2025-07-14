from autogen import ConversableAgent,initiate_chats
from config import llm_config
from pprint import pprint

"""The first agent is our **Onboarding Personal Information Agent**.
 Its main goal is to get the name and location of the customer. """
onboarding_personal_information_agent = ConversableAgent(
    name="Onboarding_Personal_Information_Agent",
    system_message='''You are a helpful customer onboarding agent,
    you work for a phone provider called ACME.
    Your job is to gather the customer's name and location.
    Do not ask for any other information, only ask about the customer's name and location.
    After the customer gives you their name and location, repeat them 
    and thank the user, and ask the user to answer with TERMINATE to move on to describing their issue.
    ''',
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower()
)

"""The second agent is our **Onboarding Issue Agent**. 
Its main goal is to determine the issue the customer is facing with ACME's products."""
onboarding_issue_agent = ConversableAgent(
    name="Onboarding_Issue_Agent",
    system_message='''You are a helpful customer onboarding agent,
    you work for a phone provider called ACME,
    you are here to help new customers get started with our product.
    Your job is to gather the product the customer use and the issue they currently 
    have with the product,
    Do not ask for other information.
    After the customer describes their issue, repeat it and add
    "Please answer with 'TERMINATE' if I have correctly understood your issue." ''',
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower()
)

"""The third agent is our **Customer Engagement Agent**. 
Its main goal is to interact with the customer based on the 
previously gathered information until a human agent can start intertacting 
with the customer to solve their issue."""
customer_engagement_agent = ConversableAgent(
    name="Customer_Engagement_Agent",
    system_message='''You are a helpful customer service agent.
    Your job is to gather customer's preferences on news topics.
    You are here to provide fun and useful information to the customer based on the user's
    personal information and topic preferences.
    This could include fun facts, jokes, or interesting stories.
    Make sure to make it engaging and fun!
    Return 'TERMINATE' when you are done.''',
    llm_config=llm_config,
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "terminate" in msg.get("content").lower(),
)

"""Finally, this time, we will also have to define a **customer proxy agent**. 
The customer proxy agent is a Conversable Agent that is not an LLM (`llm_config=False`),
it will however have the `human_input_mode="ALWAYS"` which means that you, the human, 
will play the role of this agent. You will be the customer through this agent."""
customer_proxy_agent = ConversableAgent(
    name="customer_proxy_agent",
    llm_config=False,
    code_execution_config=False,
    human_input_mode="ALWAYS",
)

"""## Chat orchestration

We are now going to define how the chat will happen. This means that we will define in which order agents will interact and who'll interact with who when. To define this, we will use a list, that will contain several elements, each one corresponding to a chat. The chats will then happen in that specific order.

Let's define a `chat` object and then the first chat:"""

chats = [] # This is going to be our list of chats
chats.append(
    {
        "sender": onboarding_personal_information_agent,
        "recipient": customer_proxy_agent,
        "message": 
            "Hello, I'm here to help you solve any issue you have with our products. "
            "Could you tell me your name?",
        "summary_method": "reflection_with_llm",
        "summary_args": {
        "summary_prompt" : "Return the customer information "
                             "into a JSON object only: "
                             "{'name': '', 'location': ''}",
        },
        "clear_history" : True
    })
chats.append(
    {
        "sender": onboarding_issue_agent,
        "recipient": customer_proxy_agent,
        "message": 
                "Great! Could you tell me what issue you're "
                "currently having and with which product?",
        "summary_method": "reflection_with_llm",
        "clear_history" : False
    }
)
chats.append(
        {
        "sender": customer_proxy_agent,
        "recipient": customer_engagement_agent,
        "message": "While we're waiting for a human agent to take over and help you solve "
        "your issue, can you tell me more about how you use our products or some "
        "topics interesting for you?",
        "max_turns": 2,
        "summary_method": "reflection_with_llm",
    }
)

chat_results = initiate_chats(chats)
for chat_result in chat_results:
    pprint(chat_result.summary)