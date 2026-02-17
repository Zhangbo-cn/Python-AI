'''
需求：

小明同学体重 100kg
每次跑步一次, 减少 0.5kg
每当大吃大喝一次, 增加 2kg

'''

class Student():

    def __init__(self, name, weight):
        # 属性：姓名 和 体重
        self.name = name
        self.weight = weight

    # 方法：跑步 和 吃喝
    def run(self):
        self.weight -= 0.5

    def eat_drink(self):
        self.weight += 2

    def __str__(self):
        return f'{self.name} 的体重为{self.weight}'

    def __del__(self):
        print(f'对象{self.name} 被删除了')

# 规范写法
if __name__ == '__main__':
    xiao_ming = Student('小明', 100)
    xiao_ming.run() # weight 减掉0.5kg
    xiao_ming.eat_drink() # wight 增加 2kg
    print(xiao_ming)