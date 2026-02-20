'''
上下文管理器：
    确保with语句操作文件，主动关闭文件(即使代码出现问题 也会正常执行完成……)

1. 创建自定义类
2. 自己实现魔法方法
    2.1 __enter__ with语句之前执行 (打开文件，并返回文件对象)
    2.2 __exit__ with语句之后执行 (关闭文件)

'''
class MyFile:

    def __init__(self, file_path, file_model):
        # 文件的路径 / 文件名称
        self.file_path = file_path
        # 文件的操作模式：读 写
        self.file_model = file_model
        # 定义文件指针(文件对象) -> 初始化None
        self.fd = None

    def __enter__(self):

        # 打开文件，并返回文件对象
        self.fd = open(self.file_path, self.file_model, encoding='utf-8')
        return self.fd # 文件对象

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('文件关闭代码执行了')
        # 关闭文件
        self.fd.close()

if __name__ == '__main__':
    # 1. 不使用with语句 - 文件中写入内容 / 数据
    # src_f = open('123.txt', 'w', encoding='utf-8')
    # src_f.write('你好呀')
    # # # 传统方式遇到错误信息，程序直接报错，文件关闭受到影响 -> 内存泄露 / 占用内存
    # # print('测试代码', 10 + '10')
    # src_f.close()

    # 2. 使用 with 语句实现 - 精简代码
    # with open('123.txt', 'w', encoding='utf-8') as src_f:
    #     # 代码即使有问题，不影响文件的正常关闭
    #     print('测试代码', 10 + '10')
    #     src_f.write('我很好')

    # 3. 自定义类 - with 同样的能力
    with MyFile('123.txt', 'w') as src_f:
        # 无论以下代码是否出现问题，当代码执行结束之后，都会进入到__exit__内部中
        # 文件一定可以被关闭
        print('——————')
        src_f.write('我好 好好好~')
