money = 500  # 全局变量


def show_balance():
    print(f"当前余额为: {money}")
    return money


def save_money(new_money):
    global money
    money = money + new_money
    print(f"存入成功！现在余额: {money}")


def spend_money(amount):
    global money
    if amount > money:
        print("余额不足，无法取款")
        return
    else:
        money = money - amount
        print(f"取款成功！剩余余额: {money}")


if __name__ == '__main__':
    while True:
        print("\n--- 银行系统 ---")
        print("1. 查询余额 | 2. 存款 | 3. 取款 | 4. 退出")
        choice = input("请输入选项: ")

        if choice == "1":
            show_balance()
        elif choice == "2":
            num = int(input("请输入存款金额: "))
            save_money(num)
        elif choice == "3":
            num = int(input("请输入取款金额: "))
            spend_money(num)
        elif choice == "4":
            break