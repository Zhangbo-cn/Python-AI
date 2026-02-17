'''
__init__魔力方法
执行时机：
    当创建一个对象时，会自动出发__init__() 魔力方法

'''


# 建议：类名的首个字母大写 -> 不成文的约束
class Car():

    def __init__(self):
        # 创建对象 -> 自动执行
        # 给所有的对象都添加可访问的属性，谁调用就是谁的属性
        self.color = '白色'
        self.num = 4

    def run(self):
        print(f'汽车会跑')

    def show_car_info(self):
        print(f'{self} 汽车信息：-汽车颜色：{self.color} 汽车轮子数：{self.num}')

# 需求：车这个对象创建时，给他添加一些通用的属性：颜色 / 轮子 / 品牌……

# 推荐写法 ↓
c1 = Car()
c1.color = '黑色'
c1.num = 8
print(f'c1 车的颜色：{c1.color} 车的轮子数：{c1.num}')
# 不推荐该写法 -> 只关注c1 这一辆车而已
# c1.color = 'white'
# c1.num = 4


c2 = Car()
print(f'c2 车的颜色：{c2.color} 车的轮子数：{c2.num}')
