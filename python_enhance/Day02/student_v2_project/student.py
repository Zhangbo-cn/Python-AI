'''
该模块包含学生属性信息：姓名 / 年龄 / 性别 / 电话 / 描述

'''
class Student():
    def __init__(self, name, age, gender, phone, desc):
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone
        self.desc = desc

    def __str__(self):
        return (f'姓名：{self.name}，年龄：{self.age}，性别：{self.gender}，电话：{self.phone}，描述：{self.desc}')


if __name__ == '__main__':
    s1 = Student('小王', 18, '男', '12345678901', '无')
    print(s1)
    s2 = Student(name='小张', age=28, gender='男', phone='12345678901', desc='无')
    print(s2)
