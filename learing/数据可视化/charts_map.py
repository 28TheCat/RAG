from pyecharts.charts import Map

map=Map()

data = [
    ("北京市", 99),
    ("上海市", 199),
    ("湖南省", 299),
    ("台湾省", 399),
    ("安徽省", 499)
]

map.add("测试地图",data,"china")
map.render()
