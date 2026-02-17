'''
1. 定义一个外部函数 outer，声明局部变量 count = 0
2. 内部声明一个函数 inner，这inner中让 count += 1
3. 返回inner函数

'''

def outer():
    count = 0
    print(f'outer count:{count}')

    def inner():
        nonlocal count
        count += 10
        print(f'inner count: {count}')

    return inner

res = outer()
res()
res()
res()

res = outer()
