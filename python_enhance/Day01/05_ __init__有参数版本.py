'''
__init__魔力方法
执行时机：
    当创建一个对象时，会自动出发__init__() 魔力方法

'''


# 建议：类名的首个字母大写 -> 不成文的约束
class Car():

    def __init__(self, color='红色', brand='上汽'):
        self.color = color
        self.brand = brand

    def run(self):
        print(f'汽车会跑')

    def show_car_info(self):
        print(f'{self} 汽车信息：-汽车颜色：{self.color} 汽车品牌：{self.brand}')


# 需求：车这个对象创建时，给他添加一些通用的属性：颜色 / 轮子 / 品牌……

c1 = Car('白色', '保时捷')

c1.run()
c1.show_car_info()
print(f'c1 颜色：{c1.color} c1 品牌：{c1.brand}')

c2 = Car()
c2.run()
c2.show_car_info()
print(f'c2 颜色：{c2.color} c2 品牌：{c2.brand}')


