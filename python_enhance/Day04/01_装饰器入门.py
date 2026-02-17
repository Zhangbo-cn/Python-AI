'''
1. 装饰器的能力体现：
    在不改变原有函数的基础上，添加一些额外的功能

2. 构建装饰器的条件：
    有嵌套 - 外层函数嵌套内层函数
    有引用 - 内层函数引用外层函数的变量
    有返回 - 外层函数返回内层函数对象本身（地址值）
    有额外功能 - 要拓展的功能

'''


# 需求：
# 2. 在不改变原有函数的基础上，需要提示用户要先登录
# 外层函数
def check_login(fn_name):
    # 内层函数
    def inner():
        print('校验用户是否登录……登录成功')  # 验证是否登录的逻辑代码 简写
        fn_name()  # 有引用

    return inner  # 有返回


# 1. 定义有发表评论的功能函数
@check_login
def publish_comment():
    print('发表评论')


@check_login
def shopping():
    print('可以购物啦')


# 3. 测试调用
# 传统方式
# check_comment = check_login(publish_comment)
# print(check_comment)  # 返回的是 inner对象本身：0x0000024B4FF9A3E0，内部没有调用inner()函数
# check_comment()  # 调用inner()函数

# check_shopping = check_login(shopping)
# print(check_shopping)
# check_shopping()

# 4. 装饰器
publish_comment()
shopping()