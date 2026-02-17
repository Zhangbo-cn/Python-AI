# lambda 函数
# 作用：简化代码 -> 要求有1个返回值，只有一行代码 / 可以接受参数


# 不带参数 -> 没返回值
def fn_1():
    print('Hello fn_1')


fn_1()

# 变量名 -> 函数名
# 变量名 = lambda 参数：一行代码 # 一行代码：不需要添加 return，默认返回结果
# 调用：变量名（）
fn_11 = lambda: print('hello fn_11')
fn_11()


def fn_2():
    return 100


fn_22 = lambda: 100

print(fn_22())


# 带参数 -> 有返回值
def fn_3(x, y):
    return x + y


print(fn_3(3, 4))

fn_33 = lambda x, y: x + y
print(fn_33(3, 5))

# 带参数 -> 有默认值
fn_44 = lambda x, y, z=100: x + y + z

print(fn_44(100, 200))  # 400
print(fn_44(100, 200, 300))  # 600

x = 1
y = 2
ans = x if x > y else y
print(ans)

lambda_three = lambda x, y : x if x > y else y
max_num = lambda_three(100, 2)
print(max_num)

students = [
    {'name': 'Tom', 'age': 20},
    {'name': 'Rose', 'age': 19},
    {'name': 'Jack', 'age': 22}
]
# sort() 排序 -> 基于排序列表中 两两比较
# 字典和字典之间无法进行比较 -> 报错
# studen.sort()
# 但可以按照key / value 进行排序
# name 升序
students.sort(key=lambda x: x['name'])
print(students)