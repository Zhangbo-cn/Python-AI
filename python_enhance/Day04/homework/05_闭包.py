'''
创建一个闭包，实现统计函数执行的次数功能。有如下调用闭包函数的代码：
f = func_count()

f()
f()
f()


hello world
执行了1次
hello world
执行了2次
hello world
执行了3次
'''

# def func_count(count=0):
#
#     def inner():
#         print(f'hello world')
#         nonlocal count
#         count += 1
#         print(f'执行了第{count}次')
#
#     return inner
#
# f = func_count()
# f()
# f()
# f()


'''
创建一个闭包记录银行余额, 可以对余额进行存钱,进行取钱
'''
# def outer(func, x, balance=0):
#     def inner():
#         # nonlocal balance
#         return func(balance, x)
#     return inner
#
# # 存钱
#
# def restore(balance, x):
#
#     print(f'存储了{x}元')
#     return balance + x
#
# # 取钱
#
# def fetch(balance,x):
#     print(f'当前余额为：{balance}元')
#     if balance >= x:
#         balance -= x
#         print(f'取出{x}元，'
#               f'当前余额为：{balance}元')
#     else:
#         print(f'当前余额{balance}元, 不足{x} 元')
#
#     return balance
#
# bal1 = outer(restore, 3, 1)
# print(f'银行余额为：{bal1()}')
#
# bal2 = outer(fetch, 50, bal1())
# print(bal2())

def create_account(initial_balance=0):
    balance = initial_balance # 这是私有变量，外面访问不到

    def deposit(amount):
        nonlocal balance
        balance += amount
        print(f'存入{amount}, 当前余额：{balance}')
        return balance

    def withdraw(amount):
        nonlocal balance
        if balance >= amount:
            balance -= amount
            print(f'取出{amount}, 当前余额：{balance}')
        else:
            print(f'余额不足！当前余额：{balance}')

        return balance
    return {'deposit': deposit, 'withdraw': withdraw}

# 测试
account = create_account(1) # 初始1元

account['deposit'](3)
account['deposit'](3)
