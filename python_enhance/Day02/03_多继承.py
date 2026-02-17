
# 老师傅
class Master:
    # 属性
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'
    # 方法
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 学校
class School:
    # 属性
    def __init__(self):
        self.kongfu = '[智能煎饼果子]'
    # 方法
    def make_cake(self):
        print(f'使用{self.kongfu}智能制作煎饼果子')


# 徒弟
# class Prentice(Master): -> 继承自Master -> 单继承
# class Prentice(Master, School): -> 继承自Master和School -> 多继承
# 继承顺序 -> 就近原则 -> 先找自己（看自己是否有这个属性和方法，如果没有 -> 找父级（优先级：从左 向右）

class Prentice(Master, School):
    pass

if __name__ == '__main__':
    xiaoming = Prentice()

    print(xiaoming.kongfu)
    xiaoming.make_cake()

    # 继承是类和类之间的关系
    # 获取继承顺序
    # 1. 类名.__mro__
    # 2. 类名.mro() 方法
    # mro机制 可以查看某个对象，在调用函数时，寻找方法的路径
    print(Prentice.__mro__) # 查找顺序 (Prentice, School, Master, object)
    print(Prentice.mro())