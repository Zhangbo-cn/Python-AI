'''
在无参无返回值的原有函数 求和结果之前
添加一个友好提示(注意：不能改变源代码)：正在努力计算中

注意⚠️：
装饰器内部函数 inner 必须要和被装饰的原函数 保持一致(是否 有参数 和 返回值)
    原函数无参无返回，装饰器的内部也必须是无参无返回……
    ……
'''

# 1.定义装饰器函数
# 外部函数
def my_decorator(fn_name):
    # 内部函数
    def inner(x, y):
        print('正在努力计算中')
        fn_name(x, y) # 调用原函数 - 有引用
    return inner # 有返回

# 2. 定义原函数
# @my_decorator
def sum_fn(a, b):

    sum = a + b
    print(f'两数之和：{sum}')

sum_fn1 = my_decorator(sum_fn)
sum_fn1(100, 300)

# sum_fn(100, 200)