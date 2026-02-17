
# 老师傅
class Master:
    # 属性
    def __init__(self):
        self.kongfu = '[古法 煎饼果子配方]'
    # 方法
    def make_cake(self):
        print(f'使用{self.kongfu}制作煎饼果子')

# 学校
class School:
    # 属性
    def __init__(self):
        self.kongfu = '[学校 煎饼果子]'
    # 方法
    def make_cake(self):
        print(f'使用{self.kongfu}智能制作煎饼果子')


# 需求：既希望保留徒弟自己的配方，又希望使用学校和师傅的配方
# 实现思路：不更改老师傅和学校配方方法的前提下，在字类中调用父类的方法
# 方式1：父类名.父类方法名（） -> 精准调用父类身上的方法
# 方式2.

class Prentice(Master, School):
    def __init__(self):
        self.kongfu = '[徒弟 独创煎饼果子配方]'
    def make_cake(self):
        self.__init__()
        print(f'使用{self.kongfu}智能制作煎饼果子')

    # 获取老师傅的配方技术
    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    # 获取学校的配方技术
    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)

if __name__ == '__main__':

    xiaoming = Prentice()

    print(xiaoming.kongfu)
    xiaoming.make_cake()
    xiaoming.make_master_cake()
    xiaoming.make_school_cake()
    xiaoming.make_cake()

