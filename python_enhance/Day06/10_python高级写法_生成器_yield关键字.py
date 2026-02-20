# 生成器

# 方式1. 生成器推导式
# gen = (i for i in range(10))
# # print(gen)
# # print(next(gen))
# # for i in gen:
# #     print(i)

# 方式2. yield关键字
# 一个函数内部只要有yield关键字 -> 生成器
'''
yield 关键字 执行逻辑：
1. 函数内部执行到yield关键字 -> 暂停
2. 把yield关键字后面的结果 -> 返回给调用者
3. 下一次在调用的时候，从上一次暂停的地方继续执行
'''
def fn():
    for i in range(10):
        # yield在此做的三个事情：1. 创建了一个生成器对象 2. 将 i 的值存储到生成器中 3. 返回生成器
        yield i

my_gen = fn()
print(next(my_gen))
print(next(my_gen))

for i in my_gen:
    print(f'遍历的数据：{i}')

