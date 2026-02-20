'''
定义学生类：
    私有属性 age，通过property实现简化

'''
# s = Student()
# print(s.__age)
# s.set_age(27)
# print(s.get_age())

class Student:
    def __init__(self):
        self.__age = 18

    # 暴漏公共方法
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age):
        self.__age = age


s = Student()
# .get_age 实际是方法 -> 当做属性使用
# s.set_age = 28
# print(s.get_age)

# s.age 表面看起来是操作属性 -> 可能内部是用函数进行封装的
s.age = 35
print(s.age)
