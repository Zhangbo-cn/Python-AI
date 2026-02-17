'''
需求：学生对象 -> 字典
    __dict__ python内置的属性，作用：将对象 转成字典

'''
from student import Student

if __name__ == '__main__':

    # 单个学生对象 -> 字典
    s1 = Student('小王', 18, '男', '12345678901', '无')
    print(s1)
    print(type(s1))

    s1_dict = s1.__dict__
    print(s1_dict)
    print(type(s1_dict))
    print()

    # 多个学生对象 -> 字典
    students = [
        Student('小王', 18, '男', '12345678901', '无'),
        Student('小张', 28, '男', '12345678901', '无'),
        Student('小明', 25, '男', '12345678901', '无')
    ]

    # students_dict = []
    # for stu in students:
    #     students_dict.append(stu.__dict__)
    # 列表推导式 遍历 一行代码 + if 判断
    stu_dict = [stu.__dict__ for stu in students]
    print(stu_dict)
    print()

    # 字典 -> 学生对象（主逻辑是按照对象来处理数据的）
    # 更新学生的功能 -> 代码 -> 学生列表 ==》 [学生对象1，学生对象2，xxx]
    # 修改方式：学生对象.属性名 = 新值
    # 字典.属性名 = 值 error
    my_dict = {
        'name': '小王',
        'age': 18,
        'gender': '男',
        'phone': '12345678901',
        'desc': '无'
    }

    # s2 = Student(my_dict['name'], my_dict['age'], my_dict['gender'], my_dict['phone'], my_dict['desc'])
    # print(s2)
    # print(s2.name)
    # print(type(s2))
    # 语法糖
    s3 = Student(**my_dict) # '*'一个星号放到元组里面，'**'两个星号放到字典里面 -> key=value
    print(s3)
    print(s3.name)
    print(type(s3))
