import json

data=[
    {"name":"111","age":22},
    {"name":"222","age":33},
    {"name":"333","age":44}
]
json_data=json.dumps(data)
print(type(data))
print(type(json_data))

json_data_trans=json.loads(json_data)
print(type(json_data_trans))