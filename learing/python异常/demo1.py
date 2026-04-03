

def test01():
    try:
        f = open("C:\Users\26076\Desktop\bailiang\learing\python异常\ckckck.txt", "r")
    except NameError as e:
        print("出现了变量未定义的情况！")
        print(e)

def test02():
    try:
        f = open("F:/kkkk.txt", "r", encoding="UTF-8")
    except Exception as e:
        print("出现异常,改成写权限进行创建文件")
        f = open("F:/kkkk.txt", "w", encoding="UTF-8")
    else:
        print("未出现异常")
    finally:
        print("代码已完成，关闭文件")
        f.close()

def func01():
    print("这是func01的开始")
    num = 1 / 0
    print("这是func01的结束")
def func02():
    print("这是func02的开始")
    func01()
    print("这是func02的开始")


if __name__ == '__main__':
    test02()
    # try:
    #     func02()
    # except Exception as e:
    #     print(e)