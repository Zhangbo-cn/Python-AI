'''
- 添加学生信息
- 删除学生信息, 根据编号删除
- 修改单个学生信息
- 查询单个学生信息
- 遍历查询所有学生信息
- 退出系统
'''

# 1. 定义函数 print_info()，打印提示信息
def print_info():
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')

# 2. 定义容器，用来存储学生信息，格式如下：
info = []
# 3. 定义函数 add_info(), 实现：添加学生，编号必须唯一
def add_info():
    new_id = input('请输入您的id:')

    # 遍历学生列表，查看id是否存在，如果存在则反馈 已存在，如果不存在则进行添加
    for stu in info:
        if stu['id'] == new_id:
            print('您的学号已存在，可以进行别的操作')
            break
        else:
            new_name = input('请输入您的姓名：')
            new_tel = input('请输入您的电话：')
            stu_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
            info.append(stu_dict)
# 4. 定义函数 delete_info(), 实现：删除学生，根据编号删除
def delete_info():
    del_id = input('请输入您要删除的学号：')

    for stu in info:
        if stu['id'] == del_id:
            info.remove(del_id)
            print(f'学号 {del_id} 的学生信息已删除成功！')
            break
    else:
        print(f'您要删除的学号不存在，无需删除')

# 5. 定义函数 update_info(), 实现：修改学生信息，根据编号修改，只能修改：姓名、手机号
def update_info():
    update_id = input('请输入要更新的学生id: ')

    for stu in info:
        if stu['id'] == update_id:
            new_name = input('请更新学生姓名：')
            new_tel = input('请更新学生电话：')
            stu['name'] = new_name
            stu['tel'] = new_tel
            print(f'学号为 {update_id}的学生信息已更新')
            break
    else:
        print('你输入的id不存在，请重新输入')

# 6. 定义函数 search_info(), 实现：查询某个学生信息，根据姓名查询
def search_info():
    # 写法一：按照id进行查找
    search_id = input('请输入要查找的id: ')
    for stu in info:
        if stu['id'] == search_id:
            print(stu)
            break
    else:
        print('id不存在，请重新输入')
    # 写法二：按照姓名进行查找
    # search_name = input('请输入要查找的学生姓名：')
    # for stu in info:
    #     if stu['name'] == search_name:
    #         print(stu)
    #         break
    # else:
    #     print(f'姓名为 {search_name} 的学生不存在，请重新输入！')

# 7. 定义函数 search_all(), 实现：查询所有学生的信息
def search_all():
    if len(info) == 0:
        print('没有学生，请注册')
    else:
        print(info)

# 8. while True 循环，实现：用户录入什么数据，就进行相应的操作
# 注意：处理非法值

while True:
    # 1. 页面提示
    print_info()
    # 2. 提示用户录入ta要进行的操作数字，并接收
    num = input('请录入您要操作的数字：')
    if num == 1:
        add_info()
    elif num == 2:
        delete_info()
    elif num == 3:
        update_info()
    elif num == 4:
        search_info()
    elif num == 5:
        search_all()
    elif num == 6:
        print('谢谢您的使用，下次再会！')
        break
    else:
        print('没有匹配选项，请重新录入！')


