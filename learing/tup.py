
def test01():
    test_tum=(
        1,24,"3rwer"
    )
    print(test_tum)
    print(len(test_tum))
    print(test_tum[0])


def test02():
    # 定义元组：名字、年龄、爱好列表
    test_tup = ('马冬梅', 18, ['football', 'music'])

    print(test_tup.index(18))
    print(test_tup[0])

    test_tup[2].remove('football')
    print(test_tup)

    test_tup[2].append('coding')
    print(test_tup)


if __name__ == '__main__':
    test02()



