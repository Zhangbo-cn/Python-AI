class Master:
    # 属性
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    # 方法
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')


class Prentice(Master):
    pass

if __name__ == '__main__':
    xiaoming = Prentice()

    print(xiaoming.kongfu)
    xiaoming.make_cake()