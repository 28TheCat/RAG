def test01():
    name={"鸣人", "卡莉熙", "志田未来"}
    print(name)
    name.add("dfs")
    print(name)
    name.add("鸣人")
    # print(name)
    # name.remove("dfs")
    print(name)
    name1={"鸣人", "卡莉熙", "志田未来"}
    print(name.difference(name1))
    # name.clear()
    # print(name)

def test02():
    list1= list1 = ["三藏", "Harry Potter", "柿子", "远坂凛", "赤井秀一", "远坂凛", "加藤惠", "Harry Potter", "Tony Stark", "Harry Potter", "Sheldon Cooper"]
    print(list1)
    set1=set(list1)
    print(set1)


if __name__ == '__main__':
    test02()
