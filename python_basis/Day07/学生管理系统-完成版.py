# 1. 定义函数 print_info()  , 打印提示信息.
def print_info():
    print('1. 添加学生信息')
    print('2. 删除学生信息')
    print('3. 修改学生信息')
    print('4. 查询单个学生信息')
    print('5. 查询所有的学生信息')
    print('6. 退出系统')


# 3.1 定义容器, 用来存储学生信息, 格式如下:
# [{'id':'heima001', 'name':'刘亦菲', 'tel': '111'}, {'id':'heima002', 'name':'高圆圆', 'tel': '222'}]
info = []

# 3. 自定义函数 add_info(), 实现: 添加学生, 编号必须唯一
def add_info():
    # 3.2 提示用户录入 学生的学号并接收.
    new_id = input('请录入您要添加的学生的学号: ')  # heima001, heima002, abc...

    # 3.3 判断, 用户录入的学号是否存在, 如果存在, 就提示 学号存在, 然后添加结束.  如果不存在, 就提示录入 其它信息, 接收并存储.
    for stu in info:  # stu的格式, {'id':'heima001', 'name':'刘亦菲', 'tel': '111'}
        if stu['id'] == new_id:
            # 走这里, 说明学号存在
            print('您录入的学号已存在, 请重新操作')
            break
    else:
        # 走这里, 说明没有走break, 说明 录入的学号不存在, 就提示录入其它信息, 并添加.
        new_name = input('请录入您要添加的学生的姓名: ')
        new_tel = input('请录入您要添加的学生的手机号: ')
        # 3.4 将用户录入的数据封装成字典.
        stu_dict = {'id': new_id, 'name': new_name, 'tel': new_tel}
        # 3.5 将上述的字典(一个学生的信息), 添加到 学生列表中(info)
        # global info  说明我们在操作全局变量, 但是因为 info是一个列表, 它是可变类型, 所以形参的改变直接影响实参.
        info.append(stu_dict)


# 4. 自定义函数 delete_info(), 实现: 删除学生, 根据编号删除
def delete_info():
    # 4.1 提示用户录入要删除的学生学号, 并接收.
    del_id = input('请录入您要删除的学生的id:')
    # 4.2 判断该学号是否存在.
    for stu in info:
        # stu 就是已经存在的每一个学生的信息, 格式为:  {'id':'heima001', 'name':'刘亦菲', 'tel': '111'}
        if stu['id'] == del_id:
            # 4.3 如果学号存在就删除该学生.
            info.remove(stu)  # 删除学生信息
            print(f'学号为 {del_id} 的学生信息已删除成功!')
            break
    else:
        # 4.4 如果学号不存在, 就提示: 该学号不存在, 请重新操作.
        print('您录入的学号不存在, 请重新操作')


# 5. 自定义函数 update_info(), 实现: 修改学生信息, 根据编号修改, 只能修改: 姓名, 手机号.
def update_info():
    # 5.1 提示用户录入要修改的学生学号, 并接收.
    update_id = input('请录入您要修改的学生的id:')
    # 5.2 判断该学号是否存在.
    for stu in info:
        # stu 就是已经存在的每一个学生的信息, 格式为:  {'id':'heima001', 'name':'刘亦菲', 'tel': '111'}
        if stu['id'] == update_id:
            # 5.3 如果学号存在就修改 该学生信息.
            new_name = input('请录入您要修改的学生的姓名: ')
            new_tel = input('请录入您要修改的学生的手机号: ')
            # 5.4 根据录入的信息, 修改元素值.
            stu['name'] = new_name
            stu['tel'] = new_tel

            print(f'学号为 {update_id} 的学生信息已修改成功!')
            break
    else:
        # 4.4 如果学号不存在, 就提示: 该学号不存在, 请重新操作.
        print('您录入的学号不存在, 请重新操作')


# 6. 自定义函数 search_info(), 实现: 查询某个学生信息, 根据姓名查询
def search_info():
    # 6.1 提示用户录入要查询的学生的姓名, 并接收.
    search_name = input('请录入您要查询的学生的姓名:')

    # 6.5 我们用bool类型的变量标记是否查找到学生, True: 有这个人, False: 没有这人
    # 6.5.1 初值为 False, 假设没有这个学生.
    flag = False

    # 6.2 判断该姓名是否存在.
    for stu in info:
        # stu 就是已经存在的每一个学生的信息, 格式为:  {'id':'heima001', 'name':'刘亦菲', 'tel': '111'}
        if stu['name'] == search_name:
            # 6.3 如果姓名存在就打印该学生.
            print(stu)
            # 6.5.2 查找到学生了, 就将flag的值改为 True
            flag = True

    # 6.5.3 判断是否查询到学生.
    # if flag == False:
    if not flag:  # 逻辑运算符, and, or, not
        # 6.4 如果姓名不存在, 就提示: 查无此人, 请重新操作.
        print('查无此人, 请重新操作')


# 7. 自定义函数 search_all(), 实现: 查询所有学生的信息.
# 数据格式为: [{'id':'heima001', 'name':'刘亦菲', 'tel': '111'}, {'id':'heima002', 'name':'高圆圆', 'tel': '222'}]

def search_all():
    # 7.1 判断是否有学生信息, 如果没有则提示用户先添加再查询.
    if len(info) == 0:
        print('没有学生信息, 请先添加, 后查询!')
    else:
        # 7.2 如果有, 则打印所有学生信息.
        # 直接遍历所有.
        for stu in info:
            print(f'学生id:{stu["id"]}, 学生姓名:{stu["name"]}, 学生手机号:{stu["tel"]}')


# 2. 自定义while True循环逻辑, 实现: 用户录入什么数据, 就进行相应的操作
# 注意: 处理一下非法值.
# if __name__ == '__main__':
while True:
    # 2.1 打印操作界面信息.
    print_info()

    # 2.2 提示用户录入他/她要进行操作的数字, 并接收.
    num = input('请录入您要操作的数字: ')
    if num == '1':
        add_info()
    elif num == '2':
        delete_info()
    elif num == '3':
        update_info()
    elif num == '4':
        search_info()
    elif num == '5':
        search_all()
    elif num == '6':
        print('谢谢您的使用, 让我们下次再会!')
        break  # 记得结束循环
    else:
        print('没有这样的数字, 录入有误, 请重新录入')
    print()  # 目的, 更好的展示结果.
