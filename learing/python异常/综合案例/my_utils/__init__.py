import file_util
import str_util
from learing.python异常.综合案例.my_utils.file_util import append_to_file, print_file_info
from learing.python异常.综合案例.my_utils.str_util import str_reverse, substr

filepath = r"C:\Users\26076\Desktop\bailiang\learing\python异常\综合案例\my_utils\bili.txt"


if __name__ == '__main__':
    str1="dfsfdsgsdag11"
    print(str_reverse(str1))
    print(substr(str1,1,4))
    print(print_file_info(filepath))
    print(append_to_file(filepath, str1))
