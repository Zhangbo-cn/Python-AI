# 1. 创建一个学生花名册字典 students，涵盖：姓名、学号
students = {
    'S001':'张三',
    'S002':'李四',
    'S003':'王五'
}

# 2.按照学号查姓名
name = students.get('S001')
print(name)

# 3. 查看所有学号
print(list(students.keys()))

# 4. 查看所有姓名
print(list(students.values()))

# 5. 查看完整对应关系
print(students.items())

# 6. 增加一个S004学员，名字田六
students['S004'] = '田六'
print(list(students.items()))

# 7. 修改 学号S002学员，改成 李小龙
print(students.get('S002'))
students['S002'] = '李小龙'
print(students.get('S002'))

# 8. 学号S004 转学了，需要从花名册中删除
students.pop('S004')
print(students)