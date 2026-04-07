import os


def check_dir(os_dir):
    if not os.path.exists(dir):
        print(os_dir,"不存在")
        exit(0)

def ask_for_confirm():
    ans=input("继续？yes/no\n")
    global con_exit
    if ans=="yes":
        con_exit=0
        return con_exit
    elif ans=="no":
        con_exit=1
        return con_exit
    else:
        print("错误输入，请重新输入")
        ask_for_confirm()


def delete_files(backup_dir, ending):
    for root, dirs, files in os.walk(backup_dir):
        for file in files:
            if file.endswith(ending):
                file_path = os.path.join(root, file)
                print("删除:", file_path)
                os.remove(file_path)