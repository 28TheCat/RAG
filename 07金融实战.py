# 获取client对象
import json
from openai import OpenAI

client = OpenAI(
    api_key="sk-35381cc9163f40408674b8987efb1d88",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
schema = ['日期', '股票名称', '开盘价', '收盘价', '成交量']
examples_data = [
    {
        "content": "2023年1月10日，古哥-D（美股）开盘价为100美元，当日成交量为520000股。",
        "answer": {
            "日期": "2023-01-10",
            "股票名称": "古哥-D",
            "开盘价": "100美元",
            "收盘价": "未提及",
            "成交量": "520000"
        }
    }
]

questions = [
    {"text": "2024年3月5日，苹果公司开盘价为150美元，收盘价为155美元，成交量为300万股。"},

    {"text": "腾讯控股于2024年4月10日开盘价为320港元，当日成交量为120万股。"},

    {"text": "2023年12月1日，特斯拉开盘价为250美元，收盘价为260美元。"},

    {"text": "阿里巴巴今日成交量为500万股，开盘价为85美元。"},

    {"text": "今天阳光很好，适合晒猫。"}  # 干扰数据
]

for q in questions:
    messages = []

    messages.append({
        "role": "system",
        "content": "你是一个信息抽取助手，只输出JSON，字段包括：日期、股票名称、开盘价、收盘价、成交量。没有就写未提及。"
    })

    for ex in examples_data:
        messages.append({"role": "user", "content": ex["content"]})
        messages.append({
            "role": "assistant",
            "content": json.dumps(ex["answer"], ensure_ascii=False)
        })

    messages.append({
        "role": "user",
        "content": q["text"]
    })

    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
    )

    print("文本：", q["text"])
    print("结果：", response.choices[0].message.content)
    print("------")