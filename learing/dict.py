def test01():
    dic1={1:"dsf",5:"dd"}
    print(dic1)

def test02():
    name = {
        "韦冬梅": {"部门": "科技部", "工资": 3000, "级别": 1},
        "米老鼠": {"部门": "市场部", "工资": 5000, "级别": 2},
        "皮卡丘": {"部门": "市场部", "工资": 7000, "级别": 3},
        "皮可熊": {"部门": "科技部", "工资": 4000, "级别": 1},
        "波赛冬": {"部门": "市场部", "工资": 6000, "级别": 2},
    }
    for k in name:

        if name[k]["级别"]==1:
            name[k]["级别"]=2
            name[k]["工资"]=name[k]["工资"]+1000;
    print(name)

def test03():
    name = {
        "sdfs":423,"dfsf":34,"dsf":45,"dfsfsdf":345
    }
    print(name)
    name.pop("dsf")
    print(name)

if __name__ == '__main__':
    test03()