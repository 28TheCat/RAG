def name_txt(name, age, gender='男'):
    print(f"姓名：{name} ，年龄：{age} ，性别：{gender}")

def print1(**abc):
    print(type(abc))
    print(abc)
if __name__ == '__main__':

    # name_txt(name='小明', age=18)
    # name_txt(name='小红', age=19, gender='女')
    print1(list_1=[32,435.56,234.3,435,23,543])
