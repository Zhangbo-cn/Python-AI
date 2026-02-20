'''
定义一个函数, 输出 100000 句  "YYDS" ,  请使用装饰器方式来统计执行时间
'''
# 获取当前时间戳（秒级，从1970年1月1日开始的秒数）
# import time
# timestamp = time.time()

# import time
#
#
# def decorator(print_info):
#     def inner():
#         timestamp_1 = time.time()
#         print_info()
#         timestamp_2 = time.time()
#         sub = timestamp_2 - timestamp_1
#         print(sub)
#     return inner
#
# @decorator
# def print_info():
#     for i in range(100000):
#         print('YYDS')
#
# print_info()

'''
定义一个函数, 返回字符串, 使用装饰器实现对这个字符串添加后缀.txt
'''
def add_txt(func):
    def inner(*wargs, **kwargs):
        result = func(*wargs, **kwargs)
        return result
    return inner

@add_txt
def res_str(s):
    return str(s)

print(res_str('suidb'))