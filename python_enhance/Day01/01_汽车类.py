'''
# 定义汽车类 使用类中提供的方法（跑）
面相对象核心概念：
    类：抽象的概念，看不见、摸不着，是属性（名词）和方法（动词/行为）的集合
    对象：类的具体体现 -> 类创造出来的
    属性：外在特征，比如姓名、年龄、家乡、性别……
    行为：描述当前对象或实物的功能，能干什么；比如：汽车会跑

    # 定义类
    class 类名：
        # 属性
        # 方法

    # 创建对象
    对象名 = 类（）

    # 访问对象中的属性和方法
    对象名.属性
    对象名.方法（）

self 内置关键字
指向的是创建的示例对象本身，返回地址(引用)
翻译成白话：谁调用函数，指向的是谁
'''
# 建议：当前类名的首个字母大写
class Car():

    def run(self):
        print(f'{self} 汽车会跑')
        # print(f'汽车会跑')
    def start(self):
        # 创建实例对象时，调用的时候 -> 谁调用，self 就是谁
        print(f'{self} 汽车启动')
        # 实现：汽车在启动时 -> 自动执行 点火 + 运行
        self.fire()
        self.work()
    def fire(self):
        print(f'{self} 汽车点火')
    def work(self):
        print(f'{self} 汽车运行')
# 创建对象
car1 = Car()

car1.start() # 函数嵌套，等价于下面三行
car1.start()
car1.fire()
car1.work()

# car1.run()

class Dog():
    def shout(self):
        print(f'叫喊')

dog1 = Dog()
dog1.shout()
