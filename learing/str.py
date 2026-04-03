def test01():
    name="sdfaafdgdsfs"
    print(name)
    print(name[0])
    name=name.replace("sd", "9")
    print(name)
    name1=name.split("dg")
    print(type(name1))
    print(name1)
    print(name.count("9"))

def test02():
    name="itheima itcast boxuegu"
    print(name.count("it"))
    name= name.replace(" ","|")
    print(name)
    name1=name.split("|")
    print(type(name1))
    print(name1)
if __name__ == '__main__':
    test02()