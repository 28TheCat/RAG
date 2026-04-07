from configparser import ConfigParser
import os
if not os.path.exists('read_simple.ini'):
    print("错误：未找到 read_simple.ini 文件！")
else:
    p = ConfigParser()
    p.read('read_simple.ini', encoding='utf-8') # 建议指定编码，防止中文乱码

    print(p.get('bug_tracker','url'))