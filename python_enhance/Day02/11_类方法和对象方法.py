'''
对象方法
定义：
    def 方法名(self): # self -> 实例对象
        方法体
使用：实例对象.方法名() / self.方法名()

类方法
定义：
    @classmethod
    def 方法名(cls): # cls -> 类
        方法体
使用: 类名.方法名() / cls.方法名() / 实例对象.类方法()

静态方法
定义：
    @staticmethod
    def 方法名():
        方法体

'''

class Students:
    holiday_time = 14

    # 类方法
    @classmethod
    def fn1(cls): # cls -> 类
        print(cls)
        print(cls.holiday_time) # 获取类的属性

    # 静态方法
    @staticmethod
    def fn2():
        print(Students)
        print(f'类 静态方法{Students.holiday_time}')

Students.fn1()
Students.fn2()
