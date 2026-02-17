'''

self 内置关键字：指向的是创建的实例对象本身，返回地址（引用）
谁调用函数，ta指向谁

'''

# 建议：当前类名的首个字母大写
class Car():

    def run(self):
        print(f'汽车会跑')

    def start(self):
        # self 定义类中函数的时候 -> 不知道self最终是谁
        # 创建实例对象，谁调用，self是谁
        print(f'{self}汽车启动')
        self.fire()
        self.work()

    def fire(self):
        print(f'{self}汽车打火')

    def work(self):
            print(f'{self}汽车开始工作')
# 创建对象
car1 = Car()
car1.start()

