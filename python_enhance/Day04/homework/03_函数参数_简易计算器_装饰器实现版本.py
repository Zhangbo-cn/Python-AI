# 装饰器：有参数 有返回，且有多个参数，函数嵌套？

# 创建一个字典，用于存储所有通过装饰器注册的运算函数
# 键：运算名称(字符串)，值：对应的函数对象
operations = {}

# 装饰器函数：

def decorator(fn_name):
    def inner(func):

        operations[fn_name] = func
        return func
    return inner

@decorator('add')
def add(a, b):
    return a + b

def calcultor(a, b, operation):

    if isinstance(operation, str):
        operation = operations[operation]
    return operation(a, b)

print(calcultor(100, 300, add))
