# **1. 基础列表推导式**
# **题目**：使用列表推导式创建一个包含1到10的平方的列表
# **期望输出**：`[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]`
from collections import Counter

list1 = [i ** 2 for i in range(1, 11)]
print(list1)

# **2. 带条件的列表推导式**
# **题目**：使用列表推导式创建一个包含1到20中所有偶数的列表
# **期望输出**：`[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]`
list2 = [i for i in range(1, 21) if i % 2 == 0]
print(list2)

# **3. 字典推导式**
# **题目**：使用字典推导式创建一个字典，其中键为1到5的数字，值为对应数字的立方
# **期望输出**：`{1: 1, 2: 8, 3: 27, 4: 64, 5: 125}`
dict1 = {i: i * (i ** 2) for i in range(1, 6)}
print(dict1)

# **4. 复杂的字典推导式**
# **题目**：有一个字符串列表 `words = ['apple', 'banana', 'cherry', 'date']`，
# 使用字典推导式创建一个字典，其中键为单词，值为单词的长度，但只包含长度大于4的单词
# **期望输出**：`{'apple': 5, 'banana': 6, 'cherry': 6}`
words = ['apple', 'banana', 'cherry', 'date']

words_dict = {word: len(word) for word in words if len(word) > 4}
print(words_dict)


# **题目**：定义一个函数 `greet()`，当调用时打印 "Hello, World!"
# **调用示例**：`greet()`
# **期望输出**：`Hello, World!`

def greet():
    print('Hello, world!')


greet()


# **题目**：定义一个函数 `greet_name(name)`，接收一个名字参数并打印问候语
# **调用示例**：`greet_name("Alice")`
# **期望输出**：`Hello, Alice!`

def greet_name(name):
    print(f'Hello, {name}!')


greet_name('Alice')


# **题目**：定义一个函数 `add(a, b)`，接收两个数字参数并返回它们的和
# **调用示例**：`result = add(3, 5)`
# **期望输出**：`8`
def add(a, b):
    return a + b


result = add(3, 5)
print(result)


# **题目**：定义一个函数 `power(base, exponent=2)`，计算base的exponent次方，默认指数为2
# **调用示例**：`power(3)` 和 `power(2, 3)`
# **期望输出**：`9` 和 `8`

def power(base, exponent=2):
    return base ** exponent


print(power(3))
print(power(2, 3))


# **题目**：定义一个函数 `min_max(numbers)`，接收一个数字列表，返回最小值和最大值
# **调用示例**：`min_val, max_val = min_max([3, 1, 4, 1, 5, 9, 2])`
# **期望输出**：`(1, 9)`
def min_max(numbers):
    return (min(numbers), max(numbers))


min_val, max_val = min_max([3, 1, 4, 1, 5, 9, 2])
print(f"'{min_val, max_val}'")


# **题目**：定义一个函数 `sum_all`，接收任意数量的数字参数并返回它们的和
# **调用示例**：`sum_all(1, 2, 3, 4, 5)`
# **期望输出**：`15`
def sum_all(*args):
    return sum(args)


print(sum_all(1, 2, 3, 4, 5))


# **题目**：定义一个函数 `create_person`，接收关键字参数并返回一个包含这些信息的字典
# **调用示例**：`create_person(name="Bob", age=25, city="New York")`
# **期望输出**：`{'name': 'Bob', 'age': 25, 'city': 'New York'}`
def create_person(**kwargs):
    return kwargs


print(create_person(name="Bob", age=25, city="New York"))

num = 10
print(num)


def sum():
    global num
    num = 1
    print(num)


sum()


# **题目**：定义两个函数：`square(x)` 返回x的平方，`double(x)` 返回x的两倍。
# 然后定义一个函数 `square_then_double(x)` 组合这两个函数

# **调用示例**：`square_then_double(3)`
# **期望输出**：`18` (因为3²=9，然后9×2=18)

def square(x):
    return x ** 2

def double(x):
    return 2 * x

def square_then_double(x):
    return double(square(x))

print(square_then_double(3))

x = 10

def func():
    x = 20
    print(x)

func()
print(x)

x = 10

def func():
    global x
    x = 20
    print(x)

func()
print(x)

my_list = [1, 2, 3]

def modify_list():
    my_list.append(4)
    print(my_list)

modify_list()
print(my_list)

x = 10
print(id(x))
x += 1
print(id(x))

y = [1, 2, 3]
print(id(y))
y.append(4)
print(id(y))


# **1. 列表去重并保持顺序**
# **题目**：编写一个函数 `remove_duplicates(lst)`，去除列表中的重复元素，同时保持原有顺序
# **要求**：不能使用set
# **调用示例**：`remove_duplicates([3, 1, 2, 3, 4, 2, 1])`
# **期望输出**：`[3, 1, 2, 4]`

def remove_duplicates(lst):
    cnt = Counter()
    for i, x in enumerate(lst):
        cnt[x] += 1
        if cnt[x] > 1:
            del lst[i]
    print(lst)

remove_duplicates([3, 1, 2, 3, 4, 2, 1])

# **题目**：编写一个函数 `count_chars(s)`，统计字符串中每个字符的出现次数
# **调用示例**：`count_chars("hello world")`
# **期望输出**：`{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}`
# def count_chars(s):
#     cnt = Counter()
#     for i, c in enumerate(s):
#         cnt[c] += 1
#     print(cnt)
#
# count_chars("hello world")

def count_chars(s):
    char_count = {}
    for i, c in enumerate(s):
        char_count[c] = char_count.get(c, 0) + 1
    print(char_count)
count_chars("hello world") # {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}

# **题目**：编写一个函数 `group_by_length(words)`，将单词列表按长度分组
# **调用示例**：`group_by_length(['apple', 'bat', 'cat', 'elephant', 'dog'])`
# **期望输出**：`{3: ['bat', 'cat', 'dog'], 5: ['apple'], 8: ['elephant']}`

def group_by_length(words):
    dict1 = {}
    for word in words:
        length = len(word)
        if length not in dict1:
            dict1[length] = []
        dict1[length].append(word)
    return dict1

print(group_by_length(['apple', 'bat', 'cat', 'elephant', 'dog']))

def group_by_length2(words):
    dict1 = {}
    for word in words:
        dict1.setdefault(len(word), []).append(word)
    return dict1

print(group_by_length(['apple', 'bat', 'cat', 'elephant', 'dog']))

tuple1 = (1, 2)
num1, num2 = tuple1
print(num1, num2)

# 容器拆包
c1 = '咖啡'
c2 = '汽水'

c1, c2 = (c2, c1)
print(c1, c2)