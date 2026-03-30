import os
from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import HumanMessage

from dotenv import load_dotenv

load_dotenv()

model = ChatTongyi(
    model="qwen-max",
)

messages = [HumanMessage(content="你好，请问你是谁？")]
response = model.stream(messages)

for chunk in response:
    print(chunk.content, end="", flush=True)
