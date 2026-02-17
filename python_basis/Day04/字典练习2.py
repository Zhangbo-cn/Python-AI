students = {
    'S01':'罗翔',
    'S02':'芒格',
    'S03':'王阳明',
    'S04':'孔子',
}

# 2. 按照学号查姓名
print(students['S01'])

# 3. 查看所有学号
print(students.keys())
print(list[students.keys()])

# 4. 查看所有姓名
print(students.values())
print(list[students.values()])

# 5. 查看完整的学号-姓名对应关系
print(students.items())

# 6. 增加一个学员S05，名字小七
students['S05'] = '小七'
print(students)

# 7. 把学号S02学员， 改成张麻子
students['S02'] = '张麻子'
print(students)

# 8. 学号S04孔子 转学，需要从花名册中删除
students.pop('S04')
print(students)