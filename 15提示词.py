from langchain_community.embeddings import DashScopeEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
from dotenv import load_dotenv
import time

load_dotenv()
embed = DashScopeEmbeddings()

prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}，刚生了{gender}，帮忙起名字，请简略回答。"
)

# 创建模型对象（提高温度增加多样性）
model = Tongyi(
    model="qwen-max",
    temperature=0.9  
)

# 循环100次，每次调用模型生成不同的名字
for i in range(100):
    prompt_text = prompt_template.format(lastname="张", gender="女儿")
    res = model.invoke(input=prompt_text)
    print(f"第{i+1}个建议: {res}")
    time.sleep(0.5)