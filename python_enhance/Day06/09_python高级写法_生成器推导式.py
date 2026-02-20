'''
生成器（generator）：也是迭代器的一种 -> 惰性工厂 -> 不会一次性加工所有的数据，而是用一些，拿一些
        -> 节约内存 + 无需关注内部实现

方式1. 生成器推导式 (i for i in range(10) condition)
方式2. yield 关键字

生成器 vs. 迭代器 ---> 首选生成器 -> 简单一些
'''
import sys

# 1. 列表 / 集合 推导式
l1 = [i for i in range(10)]
print(l1)
s1 = {i for i in range(10)}
print(s1)


# 2. 元组推导式问题 -> 生成器推导式
my_generator = (i for i in range(10))
print(my_generator)
print(type(my_generator))

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

print('- ' * 25)
for i in my_generator:
    print(f'遍历余下的数据{i}')


# 立即生成并存储 1000000 个整数
my_list = [i for i in range(100000)]
# print(my_list)

# 内存使用 -> 占有率低 -> 返回惰性的可迭代的对象，不会一次性加载所有(不预计算任何值)
my_generator = (i for i in range(100000))
# print(my_generator)

# 查看内存的空间占用
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_generator))