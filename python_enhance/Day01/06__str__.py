'''


'''

# 建议：类名的首个字母大写 -> 不成文的约束
class Car():

    def __init__(self, color='红色', brand='上汽'):
        self.color = color
        self.brand = brand

    def run(self):
        print(f'汽车会跑')

    def __str__(self):
        # 执行时机：print打印对象的时候，自动调用__str__方法
        return f'汽车信息：-汽车颜色：{self.color} -汽车品牌：{self.brand}'



# 需求：车这个对象创建时，给他添加一些通用的属性：颜色 / 轮子 / 品牌……
c1 = Car('白色', '保时捷')

print(c1) # 返回值：0x000001B4D6C0BA40 -> 对用户来说没有意义

c2 = Car()
print(c2)

