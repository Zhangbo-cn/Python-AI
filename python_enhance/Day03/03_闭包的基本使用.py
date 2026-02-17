'''
定义一个函数用于保存变量10，然后调用函数返回值变量并重复累加数值

'''

def fn():
    # a 局部变量 -> 只能在函数内部被访问
    # 在函数外面访问 -> 出错 -> 当前函数执行完毕之后，当前空间会被释放(包含num)
    a = 10
    return a

res = fn()
print(res)
# print(num) # 默认访问全局变量，但num是局部变量，所以会报错
print(res + 1)
print(res + 1)
print(res + 1)