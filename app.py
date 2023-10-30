# Main logic for autogen ai agent

import os
import autogen

# load .env file
from dotenv import load_dotenv

load_dotenv()

print("Loading Autogen AI agent...")
print("Loading OpenAI API key...", os.environ["OPENAI_API_KEY"][:5] + "..." + os.environ["OPENAI_API_KEY"][-5:])

config_list = [
    {
        'model': "gpt-3.5-turbo-16k",
        'api_key': os.environ["OPENAI_API_KEY"],
    }
]

llm_config = [
    {
        "request_timeout": 600,
        "seed": 42,
        "config_list": config_list,
        "temperature": 0.9,
    }
]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
    system_message="Hello, I am Autogen. I am an AI assistant that can help you write code. What would you like to do?",
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={"work_dir": "web"},
    llm_config=llm_config,
    system_message="""Reply TERMINATE if the task has been solved at full satisfaction.
Otherwise, reply CONTINUE, or the reason why the task is not solved yet.""",
)

task = '''
Give me a summary of this article: https://www.eurogamer.net/xbox-announces-long-term-partnership-with-glaad
'''

user_proxy.initiate_chat(
    assistant,
    message=task
)