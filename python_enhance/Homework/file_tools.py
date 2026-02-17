'''
新建自定义模块 file_tools.py，在模块中定义以下两个函数：
read_file(file_path)：接收文件路径，读取文件所有内容并返回（若文件不存在，返回 “文件不存在”）
write_file(file_path, content)：接收文件路径和内容，将内容写入文件（若文件已存在，在末尾追加内容）

再新建文件 test_file_tools.py，导入file_tools模块，调用write_file("test.txt", "国庆复习\n")，
再调用write_file("test.txt", "Python文件操作\n")，最后调用read_file("test.txt")并打印返回结果。
'''
import os


def read_file(file_path):

    # 检查文件是否存在
    if not os.path.exists(file_path):
        return '文件不存在'

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    return content

def write_file(file_path, content):

    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(content)

    return '写入成功'

if __name__ == '__main__':
    print(read_file("./data/test.txt"))
    print(write_file("./data/test.txt", "Python文件操作\n"))


