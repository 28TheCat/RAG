import sys

class Redirection:
    def __init__(self, in_obj, out_obj):
        self.in_obj = in_obj
        self.out_obj = out_obj

    def readline(self):
        res = self.in_obj.readline()
        if res:
            self.out_obj.write(f"[自动回显]: {res}")
            self.out_obj.flush()
        return res

if __name__ == '__main__':
    if not sys.stdin.isatty():
        sys.stdin = Redirection(in_obj=sys.stdin, out_obj=sys.stdout)

    try:
        a = input("输入第一个字符串: ")
        b = input("输入第二个字符串: ")
        print(f"\n程序接收到的结果是: {repr(a)} 和 {repr(b)}")
    except EOFError:
        print("\n[错误]: 输入流已提前结束")