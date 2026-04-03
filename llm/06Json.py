import json

d = [
    {
        "name": "Alice",
        "age": 20,
        "gender": "female",
        "city": "Tokyo",
        "email": "alice@example.com"
    },
    {
        "name": "Bob",
        "age": 22,
        "gender": "male",
        "city": "Shanghai",
        "email": "bob@example.com"
    },
    {
        "name": "Charlie",
        "age": 19,
        "gender": "male",
        "city": "Beijing",
        "email": "charlie@example.com"
    },
    {
        "name": "Daisy",
        "age": 21,
        "gender": "female",
        "city": "Guangzhou",
        "email": "daisy@example.com"
    },
    {
        "name": "Ethan",
        "age": 23,
        "gender": "male",
        "city": "Shenzhen",
        "email": "ethan@example.com"
    }
]

# 1. 直接打印 Python 列表（原生格式）
print("===== 原生 Python 对象 str(d) =====")
print(str(d))

# 2. 转换为 JSON 字符串并打印（标准JSON格式）
print("\n===== json.dumps 生成的 JSON 字符串 =====")
json_dumps = json.dumps(d, ensure_ascii=False)
print(json_dumps)

# 3. JSON 字符串 转回 Python 字典/列表
py_data = json.loads(json_dumps)  # 把 json_str 改成 json_dumps
print("\n===== 转回 Python 对象 =====")
print(py_data)
print("类型：", type(py_data))  # 列表
print("取第一个名字：", py_data[0]["name"])
