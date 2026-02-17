'''


'''


# 建议：类名的首个字母大写 -> 不成文的约束
class Car():

    def run(self):
        print(f'汽车会跑')

    def show_car_info(self):
        print(f'{self} 汽车信息：-汽车颜色：{self.color} 汽车轮子数：{self.num}')


# 对象：由类创建 / 构造出来的实例对象
# 创建了一个实物 汽车类
c1 = Car()
c1.run()

# 需求：添加 属性：汽车 轮子 颜色 座椅……
# 1. 类的外面添加 -> 弊端，一次调用 一次结束，不利于复用
c1.color = '黑色'
c1.num = 4
# print(f'c1 的轮子数：{c1.num}, c1 的颜色：{c1.color}')

c2 = Car()
c2.run()
c2.color = '黑色'
c2.num = 4
# print(f'c2 的轮子数：{c2.num}, c2 的颜色：{c2.color}')

# 2. 类的内部添加
c1.show_car_info()
c2.show_car_info()
