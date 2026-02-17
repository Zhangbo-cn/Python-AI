'''
学生管理系统模块
学生：添加 / 删除 / 修改 / 查询单个 / 查询多个 ……

'''

from student import Student


# import student

class StudentCMS:

    def __init__(self):
        self.stu_list = [
            # Student('小王', 18, '男', '12345678901', '无'),
            # Student('小张', 28, '男', '12345678901', '无'),
        ]

    # 管理系统显示界面
    @staticmethod
    def show_view():
        print('*' * 23)
        print('学生管理系统V2.0版')
        print('\t1.添加学生信息')
        print('\t2.删除学生信息')
        print('\t3.修改学生信息')
        print('\t4.查询单个学生信息')
        print('\t5.查询所有学生信息')
        print('\t6.保存学生信息')
        print('\t0.退出系统')
        print('*' * 23)

    # 1. 添加学生信息
    def add_stu(self):
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        sex = input('请输入学生性别：')
        phone = input('请输入学生手机号：')
        desc = input('请输入学生描述：')
        # 封装成学生对象
        stu = Student(name, age, sex, phone, desc)
        # 把学生信息添加到列表中
        self.stu_list.append(stu)
        # 提示 '添加成功'
        print(f'{name} 学生信息添加成功！')

    # 2. 删除学生信息
    def del_stu(self):
        del_name = input('请输入要删除的学生姓名：')
        for stu in self.stu_list:
            if del_name == stu.name:
                self.stu_list.remove(stu)
                print(f'{del_name} 学生信息删除成功！')
                break
        else:
            print(f'没有找到学生{del_name}！')

    # 3. 修改学生信息
    def update_stu(self):
        upd_name = input('请输入要修改的学生姓名：')
        for stu in self.stu_list:
            if upd_name == stu.name:
                stu.gender = input('请输入学生性别：')
                stu.age = input('请输入学生年龄：')
                stu.phone = input('请输入学生手机号：')
                stu.desc = input('请输入学生描述：')
                print(f'学生{upd_name}信息修改成功！')
                break
        else:
            print(f'没有找到学生{upd_name}！')

    # 4. 查询单个学生信息
    def search_one_stu(self):
        search_name = input('请输入要查询的学生姓名：')
        for stu in self.stu_list:
            if search_name == stu.name:
                print(stu)
                break
        else:
            print(f'没有找到学生{search_name}！')

    # 5. 查询所有学生信息
    def search_all_stu(self):
        if self.stu_list == []:
            print('暂无数据！')
            return
        else:
            print('所有学生信息如下：')
            for stu in self.stu_list:
                print(stu)

    # 6. 保存学生信息
    def save_stu(self):
        # # 1. 打开文件 以写的动作打开 指定编码格式 utf-8
        # src_f = open('./stu_list', 'w', encoding='utf-8')
        # # 2. 写入 数据
        # src_f.write(str(self.stu_list))
        # # 3. 关闭文件
        # src_f.close()

        # 优化
        with open('./stu_list', 'w', encoding='utf-8') as src_f:
            # 将对象列表 -> 字典列表
            stu_dict_list = [stu.__dict__ for stu in self.stu_list]
            src_f.write(str(stu_dict_list))

    # 加载学生信息 什么时间加载
    def load_stu(self):
        print('正在加载数据中......')
        # 加载'stu_list'数据文件
        try:
            with open('./stu_list', 'r', encoding='utf-8') as src_f:
                # 读取所有数据
                stu_list = src_f.read()
                # 数据格式转换：str -> list
                # 针对于空字符串''，eval 转换会报错
                stu_list = eval(stu_list)
                # print(f'读取的学生信息：{stu_list}')
                if len(stu_list) == 0:
                    pass
                else:
                    # 读取到数据，要进行转换：[字典，字典] -> [学生对象，学生对象]
                    self.stu_list = [Student(**stu) for stu in stu_list]
        except:
            print('没有找到数据文件！')
            # 文件不存在则主动刚创建
            with open('./stu_list', 'w', encoding='utf-8') as src_f:
                # 为了保证代码的严谨，此处添加异常处理
                src_f.write(str([]))

    # 0. 退出系统
    def exit_stu(self):
        print('谢谢使用，期待下次光临！')

    def start(self):
        # 进入系统，即可加载数据
        self.load_stu()
        while True:
            # 显示操作界面
            # 类的静态方法 -> 类名.静态方法名()
            StudentCMS.show_view()
            input_num = input('请输入您要操作的编号:')
            if input_num == '1':
                print('添加学生信息\n')
                self.add_stu()
            elif input_num == '2':
                print('删除学生信息\n')
                self.del_stu()
            elif input_num == '3':
                print('修改学生信息\n')
                self.update_stu()
            elif input_num == '4':
                print('查询单个学生信息\n')
                self.search_one_stu()
            elif input_num == '5':
                print('查询所有学生信息\n')
                self.search_all_stu()
            elif input_num == '6':
                print('保存学生信息\n')
                self.save_stu()
                print('保存成功！')
            elif input_num == '0':
                exit_res = input('确定要退出系统吗？ y/n ')
                if exit_res.lower() == 'y':
                    self.exit_stu()
                    self.save_stu()
                    break
                else:
                    pass
            else:
                print('输入有误，请重新输入！')


if __name__ == '__main__':
    stu_cms = StudentCMS()
    stu_cms.start()
    print(stu_cms.stu_list)
