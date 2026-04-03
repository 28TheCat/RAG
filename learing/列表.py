def test01():
    """遍历普通列表（直接遍历元素）"""
    name_list = ['hello', 23, '34']
    # 直接遍历列表中的每个元素
    for i in name_list:
        print(i)


def test02():
    """遍历普通列表（通过索引遍历）"""
    name_list = ['hello', 23, '34']
    # 通过列表长度生成索引，再根据索引取值
    for i in range(len(name_list)):
        print(name_list[i])


def test03():
    """遍历二维列表（嵌套列表），格式化输出"""
    name_list = [
        ['hello', 23, '34'],
        ['dsfs', 3343, 'dsffdsf'],
        ['ewr', 324]
    ]

    # 外层循环遍历每一行
    for i in range(len(name_list)):
        # 内层循环遍历当前行的每一个元素
        for j in range(len(name_list[i])):
            # 制表符分隔，不换行
            print(f"{name_list[i][j]}\t", end='')
        # 一行遍历完成后换行
        print()

def test04():
    test_list = [
        'hello', 23, '34'
    ]
    print(test_list.index("hello"))
def test05():
    test_list = [
        'hello', 23, '34'
    ]
    test_list[0]='3ewr'
    print(len(test_list))
    test_list.insert(1,'ewr')
    test_list.append('ewrsdf')
    test_list1=['wrewr',534,324]
    test_list.extend(test_list1)
    test_list.remove('ewr')
    print(test_list)
    print(len(test_list))

def test06():
    test_list = [21, 25, 21, 23, 22, 20]
    print(test_list)
    test_list.append(31)
    print(test_list)
    test_list1=[29, 33, 30]
    test_list.extend(test_list1)
    print(test_list)
    test_list.remove(test_list[0])
    print(test_list)
    test_list.remove(test_list[len(test_list)-1])
    print(test_list)
    print(test_list.index(31))

def test07():
    test_list = [
        'hello', 23, '34'
    ]
    for i in range(len(test_list)):
        print(f"{test_list[i]}\t", end='')

def test08():
    test_list = [
        'hello', 23, '34'
    ]
    for i in range(-1, -len(test_list) - 1, -1):
        print(f"{test_list[i]}\t", end='')
if __name__ == '__main__':
    # 运行需要的函数
    test08()