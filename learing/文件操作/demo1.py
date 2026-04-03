import os

# 1. 统一管理路径
base_dir = os.path.dirname(__file__)
input_path = os.path.join(base_dir, "要使用的原始提供文件", "text1.txt")
output_dir = os.path.join(base_dir, "代码生成的新文件")


def test03_and_save():
    count = 0
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "result.txt")

    # 读取文件
    if not os.path.exists(input_path):
        print("错误：找不到原始文件！")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        for line in f:
            # 自动处理各种空格/换行符
            words = line.strip().split()
            count += words.count("pikaqiu")

    # 2. 将结果写入固定文件夹下的新文件
    with open(output_path, "w", encoding="utf-8") as f_out:
        f_out.write(f"统计日期: 2026-04-03\n")
        f_out.write(f"关键词 'pikaqiu' 出现的总次数是: {count}\n")

    print(f"统计完成！结果已存入: {output_path}")


if __name__ == '__main__':
    test03_and_save()