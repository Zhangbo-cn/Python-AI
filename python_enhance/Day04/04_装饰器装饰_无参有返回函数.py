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
    def inner():
        print('正在努力计算中')
        return fn_name() # 调用原函数 - 有引用

    return inner # 有返回

# 2. 定义原函数
@my_decorator
def sum_fn():
    a = 10
    b = 20
    sum = a + b
    return sum

# sum_fn1 = my_decorator(sum_fn)
# sum_fn1()

print(sum_fn())

