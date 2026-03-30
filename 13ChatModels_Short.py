from langchain_community.chat_models import ChatTongyi
from langchain_core.messages import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
chat = ChatTongyi(model="qwen3-max")

messages = [
    {"role": "system", "content": "you are a student"},
    {"role": "user", "content": "talk with me about sun"}
]

for chunk in chat.stream(messages):
    print(chunk.content, end="", flush=True)