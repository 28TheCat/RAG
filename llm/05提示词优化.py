# 获取client对象

from openai import OpenAI
import os

from pyexpat.errors import messages

client=OpenAI(
    api_key="sk-35381cc9163f40408674b8987efb1d88",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)
examples_data = {
    '新闻报道': '近日，某科技公司发布新一代人工智能产品，引发行业广泛关注。专家表示，该技术有望推动产业升级，并带动相关市场增长。',

    '财务报告': '公司2025年第一季度实现营业收入12.5亿元，同比增长15%；净利润为2.3亿元，同比增长8%。经营活动现金流保持稳定。',

    '公司公告': '本公司董事会宣布，将于2025年4月15日召开年度股东大会，审议利润分配及董事会换届等事项。',

    '分析师公告': '某证券分析师发布研报称，该公司未来三年盈利能力有望持续提升，维持“买入”评级，目标价上调至45元。'
}
examples_types = [
    '新闻报道',
    '财务报告',
    '公司公告',
    '分析师公告'
]
questions = [
    {'text': '据报道，该地区经济复苏明显，消费市场逐步回暖。'},
    {'text': '公司2025年第一季度实现营业收入12.5亿元，同比增长15%；净利润为2.3亿元。'},
    {'text': '董事会同意聘任张某为公司首席财务官，任期三年。'},
    {'text': '研报指出，公司估值具备吸引力，目标价上调至50元。'},
    {'text': '喵喵喵'}
]


# 逐个分类
for q in questions:
    messages = []

    # 系统提示
    messages.append({
        "role": "system",
        "content": "你是一个文本分类助手，只输出类别名称：新闻报道、财务报告、公司公告、分析师公告、无法分类。"
    })

    # 示例（few-shot）
    for key, value in examples_data.items():
        messages.append({"role": "user", "content": value})
        messages.append({"role": "assistant", "content": key})

    # 当前问题
    messages.append({
        "role": "user",
        "content": q["text"]
    })

    response = client.chat.completions.create(
        model="qwen3-max",
        messages=messages
    )

    print("文本：", q["text"])
    print("分类：", response.choices[0].message.content)
    print("------")