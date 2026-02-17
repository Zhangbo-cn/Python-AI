'''
定义一个既能装饰减法运算，又能装饰加法运算的装饰器

# ⚠️：装饰器只能接收一个参数 fn_name (原函数)
'''
# 有判断条件版本
# 思路：现有的函数基础上，外面再套一层函数，最终将内层函数返回即可

def logging(judge_type):
    def my_decorator(fn_1):
        def inner(a, b):
            # TODO 根据 + / - 判断条件
            # 1. + --> 提示用户 正在进行加法运算
            # 2. - --> 提示用户 正在进行减法运算
            if judge_type == '+':
                print('正在正在进行加法运算')
            else:
                print('正在正在进行减法运算')
            return fn_1(a, b)

        return inner
    return my_decorator


@logging('+')
def add(a, b):
    return a + b

@logging('-')
def sub(a, b):
    return a - b

print(add(10,20))
print(sub(10,20))

