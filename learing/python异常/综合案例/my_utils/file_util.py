def print_file_info(file_name):
    try:
        file = open(file_name,"r", encoding="utf-8")
        file_content = file.read()
        print("文件的全部内容如下：")
        print(file_content)
    except Exception as e:
        print(f"写入异常: {e}")
    finally:
        file.close()

def append_to_file(file_name, data):
    f = open(file_name, "a", encoding="UTF-8")
    f.write(data)
    f.write("\n")
    f.close()