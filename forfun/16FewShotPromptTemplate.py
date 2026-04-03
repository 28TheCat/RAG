from openai import OpenAI

client = OpenAI(
    # 如果没有配置环境变量，请用阿里云百炼API Key替换：api_key="sk-xxx"
    api_key="sk-35381cc9163f40408674b8987efb1d88",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 示例数据
examples = [
    ("大", "小", "是"),
    ("高", "低", "是"),
    ("快", "慢", "是"),
    ("热", "冷", "是"),
    ("大", "高", "不是"),
    ("苹果", "香蕉", "不是"),
    ("快乐", "悲伤", "是"),
]

def check_antonym(w1, w2):
    messages = []

    messages.append({
        "role": "system",
        "content": "判断两个词语是否为反义词，只回答：是 或 不是"
    })

    # few-shot 示例
    for a, b, ans in examples:
        messages.append({"role": "user", "content": f"词语1：{a}\n词语2：{b}"})
        messages.append({"role": "assistant", "content": ans})

    # 当前问题
    messages.append({
        "role": "user",
        "content": f"词语1：{w1}\n词语2：{w2}"
    })

    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
    )

    return response.choices[0].message.content


# 测试
print(check_antonym("黑", "白"))
print(check_antonym("苹果", "电脑"))