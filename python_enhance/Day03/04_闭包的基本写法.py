'''
闭包三要素：
1. 有嵌套 - 外层函数嵌套内层函数
2. 有引用 - 内层函数使用外层函数变量
3. 有返回 - 外层函数返回内层函数对象

def fn_outer(num):
    # 外层函数变量
    num = 10
    # 内层函数
    def fn_inner():
        print(num + 10) # 有引用
    return fn_inner # 返回内层函数对象, 也即内层函数的函数名

定义求和的闭包，外部函数有参数num1, 内部函数有参数num2，调用，求解两数之和，观察结果

'''

# def fn_outer():
#     num1 = 10
#
#     def fn_inner():
#         num2 = 20
#         sum = num1 + num2
#         print(f'两数之和{sum}')
#
#     return fn_inner
#
# res = fn_outer() # 拿到的内层函数对象本身，也即fn_inner的地址值
# res()
# fn_outer()() # 结果同上

def fn_outer(num1):

    def fn_inner(num2):
        sum = num1 + num2
        print(f'两数之和{sum}')

    return fn_inner

res = fn_outer(5) # 5 -> num1
res(10) # 10 -> num2

