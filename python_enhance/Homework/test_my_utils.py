'''
新建自定义模块 my_utils.py，在模块中定义以下两个函数：
- greet(name)：接收姓名参数，打印 “你好，[name]！国庆快乐！”
- calculate_average(numbers)：接收数字列表，计算并返回列表的平均值。
再新建另一个文件 test_my_utils.py，导入my_utils模块，
调用greet("张三")和calculate_average([85, 92, 78, 90])，打印结果。
'''

import my_utils

name = my_utils.greet('张三')
print(name)

res = my_utils.calculate_average([85, 92, 78, 90])
print(res)

