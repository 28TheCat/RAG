import os

import json
from pyecharts.charts import Line
import pyecharts.options as opts

file_path = "./data/消费账单数据.txt"
def test01():
    line = Line()
    line.add_xaxis(["1", "2", "3", "4"])
    line.add_yaxis("商家A", [24, 25, 26, 27])
    line.add_yaxis("商家B", [29, 20, 28, 244])
    line.set_global_opts(title_opts=opts.TitleOpts(title="折线图示例"))

    line.render()
    print("图表已生成")


def test02():
    if not os.path.exists(file_path):
        print(f"错误：找不到文件 {file_path}")
        return

    # 读取 JSON 数据
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # 提取数据
    dates = []
    amounts = []

    for item in data["data"]:
        dates.append(item["date"])
        amounts.append(item["amount"])

    # 生成折线图
    line = Line()
    line.add_xaxis(dates)
    line.add_yaxis("每日消费", amounts)

    line.set_global_opts(
        title_opts=opts.TitleOpts(title=data["chart_name"])
    )

    line.render("expense_chart.html")
    print("图表已生成：expense_chart.html")


if __name__ == '__main__':
    test02()