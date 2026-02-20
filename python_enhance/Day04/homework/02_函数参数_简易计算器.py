'''
def calculator(a, b, operation):
    # 请补充代码
    pass

# 测试用例
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# 应该输出 8 和 15
print(calculator(3, 5, add))
print(calculator(3, 5, multiply))
'''

# 方法一：不用装饰器，直接调用，简单清晰
def calculator(a, b, operation):
    # 请补充代码
    return operation(a, b)

# 测试用例
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

# 应该输出 8 和 15
print(calculator(3, 5, add))
print(calculator(3, 5, multiply))

