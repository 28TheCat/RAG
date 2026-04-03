import json
from openai import OpenAI

# 获取client对象（阿里云通义千问）
client = OpenAI(
    api_key="sk-35381cc9163f40408674b8987efb1d88",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 示例数据（少样本学习）
examples_data = [
    {
        "content": "句子一: 公司ABC发布了季度财报，显示盈利增长。\n句子二: 财报披露，公司ABC利润上升",
        "answer": "是"
    },
    {
        "content": "句子一: 黄金价格下跌，投资者抛售。\n句子二: 外汇市场交易额创下新高",
        "answer": "不是"
    },
    {
        "content": "句子一: 苹果公司发布新款手机。\n句子二: iPhone新品正式亮相",
        "answer": "是"
    },
    {
        "content": "句子一: 天气晴朗适合出游。\n句子二: 公司股价大幅上涨",
        "answer": "不是"
    }
]

# 待判断的问题列表
questions = [
    {"text": "句子一: 公司利润大幅增长。\n句子二: 企业盈利显著提升"},
    {"text": "句子一: 苹果发布新款手机。\n句子二: iPhone新品正式亮相"},
    {"text": "句子一: 天气晴朗适合出游。\n句子二: 今天阳光明媚适合外出"},
    {"text": "句子一: 股票市场出现大幅下跌。\n句子二: 投资者情绪高涨纷纷买入"},
    {"text": "句子一: 公司宣布裁员以降低成本。\n句子二: 企业减少员工数量以节约开支"},
    {"text": "句子一: 黄金价格持续上涨。\n句子二: 油价出现明显下降"},
    {"text": "句子一: 该地区经济逐步复苏。\n句子二: 当地经济正在恢复增长"},
    {"text": "句子一: 新能源汽车销量创新高。\n句子二: 电动车市场表现强劲"},
    {"text": "句子一: 他今天去上学了。\n句子二: 公司发布了年度财报"},
    {"text": "句子一: 人工智能技术发展迅速。\n句子二: AI领域正在快速进步"}
]

# 循环判断每一组句子
for q in questions:
    messages = []

    # 系统提示词
    messages.append({
        "role": "system",
        "content": "你是一个文本相似度判断助手。判断句子一和句子二语义是否相似，只回答：是 或 不是。"
    })

    # 加入示例（少样本）
    for ex in examples_data:
        messages.append({"role": "user", "content": ex["content"]})
        messages.append({"role": "assistant", "content": ex["answer"]})

    # 加入当前问题
    messages.append({
        "role": "user",
        "content": q["text"]
    })

    # 调用 API
    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages,
        temperature=0.1  # 加这个让输出更稳定
    )

    # 输出结果
    print("文本：", q["text"])
    print("结果：", response.choices[0].message.content.strip())
    print("-" * 50)