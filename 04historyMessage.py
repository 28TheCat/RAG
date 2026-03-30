# 获取client对象
from openai import OpenAI
import os

client=OpenAI(
    api_key="sk-35381cc9163f40408674b8987efb1d88",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
# 调用模型
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role":"system","content":"你是一只小猫,性格比较软萌"},
        {"role": "user", "content": "你的名字是什么"},
        {"role": "assistant", "content": "我是可爱猫娘"},
        {"role": "user", "content": "我有三只小猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "我的小猫生了小小猫4只"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "我一共有几只猫"},
    ],
    stream=True
)
# 处理结果
for chunk in response:
    if chunk.choices and chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="", flush=True)
