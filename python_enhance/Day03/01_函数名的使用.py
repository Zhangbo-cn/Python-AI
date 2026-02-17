'''
python中 一切皆对象 包括 元组 / 列表 / 字典 / 整数 …… 还包括函数

def fn():
    函数体

fn -> 函数对象本身(地址)
fn() -> 调用函数方法，会执行函数内部的代码 -> 返回的结果 return 指定结果

'''

def greet():
    # print('hello world')
    return 'hello world'

# print(greet) # <function greet at 0x0000023E7A6FA200>
# print(greet()) # 先执行函数内的逻辑，hello world \n None

fn = greet
fn1 = greet() # hello world
print(fn) # <function greet at 0x0000023E7A6FA200>
print(fn1) # None

print(id(fn))
print(id(greet))
print(fn is greet)

print()

def my_fn(fn_name):
    print(fn_name)
    ans = fn_name() # 调用外部传入进来的函数对象
    print(ans)

# my_fn(greet()) # hello world \n None
# 将greet函数对象传递给了my_fn函数 -> 目的：将来可以在my_fn内部调用greet函数
my_fn(greet) # <function greet at 0x0000023E7A6FA200>


