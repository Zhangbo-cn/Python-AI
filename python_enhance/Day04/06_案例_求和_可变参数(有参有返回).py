'''
定义一个可以计算多个数据和多个字典 value值之和的函数，并调用

'''

def my_decorator(fn_name):
    def inner(*args, **kwargs):
        print('调用装饰器内部函数')
        return fn_name(*args, **kwargs)
    return inner

@my_decorator
def my_sum(*args, **kwargs):
    sum = 0
    for i in args:
        sum += i

    for v in kwargs.values():
        sum += v
    return sum

total0 = my_sum(1,2,3,4,5, a=10, b=20)
print(total0)
