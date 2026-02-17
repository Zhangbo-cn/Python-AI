'''
定义一个既能装饰减法运算，又能装饰加法运算的装饰器

# ⚠️：装饰器只能接收一个参数 fn_name (原函数)
'''
# 有判断条件版本
def my_decorator(fn_1):
    def inner(a, b):
        print('正在计算……')
        # TODO 根据 + / - 判断条件
        # 1. + --> 提示用户 正在进行加法运算
        # 2. - --> 提示用户 正在进行减法运算
        # if judge_type == '+':
        #     print('正在正在进行加法运算')
        # else:
        #     print('正在正在进行减法运算')
        return fn_1(a, b)

    return inner


@my_decorator('+')
def add(a, b):
    return a + b

@my_decorator('-')
def sub(a, b):
    return a - b

print(add(10,20))
print(sub(10,20))


# 无判断条件版本
# def my_decorator(fn_1):
#     def inner(a, b):
#         print('正在计算……')
#         # TODO 根据 + / - 判断条件
#         # 1. + --> 提示用户 正在进行加法运算
#         # 2. - --> 提示用户 正在进行减法运算
#         return fn_1(a, b)
#
#     return inner
#
# @my_decorator
# def add(a, b):
#     return a + b
#
# @my_decorator
# def sub(a, b):
#     return a - b
#
# print(add(10,20))
# print(sub(10,20))