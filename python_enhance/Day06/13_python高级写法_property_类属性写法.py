'''
定义学生类：
    私有属性 age，通过property实现简化

'''


class Student:
    def __init__(self):
        self.__age = 18

    # 暴漏公共方法

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    # 将方法封装成 类属性
    stu_age = property(get_age, set_age)


s = Student()

# s.set_age(25)
# print(s.get_age())


s.stu_age = 27
print(s.stu_age)
