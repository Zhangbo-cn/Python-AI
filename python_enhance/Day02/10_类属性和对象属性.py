'''
属性：特征 / 变量值
对象属性
类属性

'''
class Students:

    '''
        类属性
        类，对象也可以获取
        推荐：类

        对象可以获取，但是不建议，没必要
    '''
    holiday_time = 14

    '''
    self 实例对象 -> 谁调用 就指向谁
    name age ---> 属于实例对象本身的，互不影响
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'姓名：{self.name}，年龄：{self.age}'

stu1 = Students('七七', 24)
stu1.age = 25
print(stu1)

stu2 = Students('小七', 23)
print(stu2)

# 如果当前直接通过类.属性名 进行类属性的修改 -> 会修改类属性，影响类属性和对象属性的输出结果
Students.holiday_time += 3

# 对象获取类的属性
print(stu1.holiday_time)

# 类获取属性
print(f'类获取属性：{Students.holiday_time}')
