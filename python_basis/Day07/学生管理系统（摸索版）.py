'''
- 添加学生信息
- 删除学生信息, 根据编号删除
- 修改单个学生信息
- 查询单个学生信息
- 遍历查询所有学生信息
- 退出系统
'''

def print_info():
    print('1. 添加学生信息')
    print('2. 删除学生信息（根据编号删除）')
    print('3. 修改单个学生信息')
    print('4. 查询学生信息')
    print('5. 查询所有学生信息')
    print('6. 退出系统')

# 存储学生信息，列表嵌套字典
info = []

def add_info():
    add_id = int(input('请输入您要添加的id: '))

    for stu in info:
        if stu['id'] == add_id:
            print('您录入的id 已存在，请重新操作！')
            break
    else:
        new_name = input('请输入学生姓名：')
        new_tel = input('请输入学生电话：')
        stu = {}
        stu['id'] = add_id
        stu['name'] = new_name
        stu['tei'] = new_tel
        info.append(stu)
        print(f'id为 {add_id} 的学生信息已经录入系统, 是否进行后续操作')

def delete_info_by_id():
    delete_id = int(input('请输入要删除的id: '))

    for stu in info:
        if stu['id'] == delete_id:
            info.remove(stu)
            print(f'学生id为{delete_id}的学生已经被删除，请输入更多操作需求')
            break
    else:
        print(f'id为 {delete_id}的学生不存在，请重新输入')

def update_info():
    update_id = int(input('请输入要更新的学生id: '))

    for stu in info:
        if stu['id'] == update_id:
            stu['name'] = input('请输入更新姓名：')
            stu['tel'] = input('请输入更新电话：')
            info.append(stu)
            print(f'id为 {update_id}的学生信息已更新')
            break
    else:
        print(f'id 为{update_id} 的学生id 不存在，请重新输入')

def search_by_id():
    search_id = int(input('请输入要查找的id: '))

    for stu in info:
        if stu['id'] == search_id:
            print(stu)
            break
    else:
        print(f'id 为{search_id} 的学生不存在，请重新输入')

def search_all_info():
    if len(info) == 0:
        print('没有学生信息，请录入')
    else:
        print(info)

while True:
    print_info()
    num = int(input('请输入您要操作的内容：'))
    if num == 1:
        add_info()
    elif num == 2:
        delete_info_by_id()
    elif num == 3:
        update_info()
    elif num == 4:
        search_by_id()
    elif num == 5:
        search_all_info()
    elif num == 6:
        print('回见')
        break
    else:
        print('没有匹配操作，请输入合理内容，谢谢')
