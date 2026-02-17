'''
global -> 告诉python解释器 -> 函数内修改全局变量

nonlocal -> 告诉 xxx -> 内部函数修改外部函数的变量

'''

age = 15

def change_age():
    # 局部变量 -> 默认不能修改掉全局变量
    # age = 20
    # 修改全局变量
    global age
    age = 25
    print(age)

change_age()
print(age)

print()

def fn_outer():
    num = 50
    print(f'外部函数值：{num}')

    def fn_inner():
        # 1. 内部函数可以访问外部函数
        # print(f'内部函数值：{num}')

        # 创建局部变量 num / 和外部函数的num 没有关系
        # num = 200

        # 报错 -> 默认内部函数不具备修改外部函数变量的能力
        # num += 50
        # 解决机制：关键字 nonlocal
        nonlocal num
        num += 50

        print(f'内部函数值：{num}')
        # nonlocal age
    return fn_inner

res_out = fn_outer()
res_out()
