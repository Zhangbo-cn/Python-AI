'''
使用迭代器实现：
    模拟range(1, 6) 同等逻辑

自定义迭代器：
    更好的理解其内部实现 原理

1. 不需要关注内部的实现(一套机制)，只要会用即可
2. 惰性加载 -> 数据不是一次性返回，一个一个的返回
'''

# for i in range(1, 6):
#     # 数据不是一次性返回，惰性
#     # 第一次 1 第二次 2 第三次 3 ……
#     print(i)

# 自定义迭代器 类 -> 重写 __iter__ __next__

class MyIterator:
    # 通过__init__方法接收两个参数 -> 初始化属性 -> 执行迭代范围
    def __init__(self, start, end):
        # start 当前值 -> 默认是开始值
        self.current_value = start
        # 结束值
        self.end = end

    # 重写__iter__方法 -> 返回当前对象 (迭代器对象)
    # 有__iter__方法，那么当前对象可遍历 / 可迭代
    def __iter__(self):
        return self

    def __next__(self):
        # print('每一次遍历都会进入到这里')
        # 判断当前值的范围是否超过范围(结束值)
        if self.current_value >= self.end:
            # 抛出异常 -> 迭代结束
            raise StopIteration
        # 获取当前的值
        value = self.current_value
        self.current_value += 1
        return value

# 演示了for循环的能力
# for i in MyIterator(1, 6):
#     print(i)

# next函数
my_iter = MyIterator(5, 10)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

print('*' * 20)
for i in my_iter:
    print(i)

# 注意：遍历空[] {} (), 没有任何意义，不会进入到内部的__next__魔法方法里面
for i in my_iter:
    print('你好', i)
