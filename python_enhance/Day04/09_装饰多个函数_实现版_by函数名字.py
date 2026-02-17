'''
定义一个既能装饰减法运算，又能装饰加法运算的装饰器

# ⚠️：装饰器只能接收一个参数 fn_name (原函数)
'''
# 有判断条件版本
# 思路：基于函数的名称进行判断

def my_decorator(fn_1):
    def inner(a, b):
        # print(fn_1.__name__) # 获取传递过来的函数名称
        if fn_1.__name__ == 'add':
            print('正在正在进行加法运算')
        else:
            print('正在正在进行减法运算')
        return fn_1(a, b)

    return inner


@my_decorator
def add(a, b):
    return a + b

@my_decorator
def sub(a, b):
    return a - b

print(add(10,20))
print(sub(10,20))

