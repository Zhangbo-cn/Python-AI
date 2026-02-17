'''
模拟计算器，接收规则和两个整数 -> 3个形参
实现：传入什么规则，也即执行什么操作

实现逻辑：
定义函数
def fn(x1,x2,x3): # x1 函数对象(整数的计算规则 + - * /), x2 和 x3 为整数即可
    xxx

'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

def cal(fn_name, x2, x3):
    return fn_name(x2, x3)

res1 = cal(add, 1, 2)
res2 = cal(sub, 1, 2)
res3 = cal(mul, 1, 2)
print(res1, res2, res3)

ans0 = cal(lambda a, b: a + b, 1, 2)
ans1 = cal(lambda a, b: a - b, 1, 2)
ans2 = cal(lambda a, b: a * b, 1, 2)
print(ans0, ans1, ans2)
