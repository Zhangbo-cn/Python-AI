'''
创建一个包含 5 个水果名称的列表，然后：
1. 在列表末尾添加 "西瓜"
2. 在第二个位置插入 "香蕉"
3. 删除第三个元素
4. 打印最终列表

'''
from cmath import inf
from collections import Counter

fruits = ['苹果', '橙子', '橘子', '桃子', '火龙果']

fruits.append('西瓜')
# print(fruits)
fruits.insert(1, '香蕉')
# print(fruits)
del fruits[2]
print(fruits)


'''
给定二维列表：matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
1. 提取所有偶数到一个新列表
2. 计算所有元素的和

'''
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target_list = []
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] % 2 == 0:
            target_list.append(matrix[i][j])
print(target_list)

'''
给定列表：numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
1. 对列表进行升序排序
2. 去除重复元素
3. 找出列表中的最大值和最小值

'''
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

sorted_numbers = sorted(numbers)
print(f'升序排序后：{sorted_numbers}')

sorted_numbers = sorted(numbers, reverse=True)
print(f'降序排序后：{sorted_numbers}')

unique_numbers = sorted(set(numbers))
print(f'去重后升序排序：{unique_numbers}')

mx = max(unique_numbers)
mn = min(unique_numbers)
print(f'最大值：{mx}, 最小值：{mn}')

'''
scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
1. 计算平均分
2. 找出高于平均分的学生成绩
3. 将成绩按从高到低排序
4. 统计优秀（90分以上）的学生人数

'''
scores = [85, 92, 78, 90, 88, 76, 95, 89, 84, 91]
# 1. 计算平均分
avg = sum(scores) / len(scores)
print(f'平均分为：{avg}')

# 2. 找出高于平均分的学生成绩
# high_scores = [score for i, score in enumerate(scores) if i > avg]
# print()

high_scores = []
for i in range(len(scores)):
    if scores[i] > avg:
        high_scores.append(scores[i])
print(f'高于均分的成绩如下：', high_scores)


# 3. 将成绩按从高到低排序
sorted_scores = sorted(scores, reverse=True)
print('成绩按从高到低排序: ', sorted_scores)

# 4. 统计优秀（90分以上）的学生人数
cnt = 0
for i in range(len(scores)):
    if scores[i] >= 90:
        cnt += 1
print(f'优秀的学生人数：{cnt}')


'''
创建一个包含 5 个三国人物姓名的元组，然后：
1. 打印元组的长度
2. 打印第三个元素
3. 访问最后一个元素
4. 统计"诸葛亮"出现的次数

'''

t1 = ('诸葛亮', '刘备', '关羽', '张飞', '赵云')
print('t1 长度：', len(t1))
print('第三个人物为：', t1[2])
print('最后一个元素', t1[len(t1) - 1])
cnt = 0
for i in range(len(t1)):
    if t1[i] == '诸葛亮':
        cnt += 1
print('诸葛亮出现的次数为：', cnt)

'''
给定元组：student = ("张三", 18, "男", 90.5)
使用元组解包将姓名、年龄、性别、成绩分别赋值给不同的变量，然后打印这些变量。

'''

student = ("张三", 18, "男", 90.5)
name = student[0]
age = student[1]
sex = student[2]
score = student[3]
print(name, age, sex, score)

'''
创建一个元组：numbers = (1, 2, 3, 4, 5)
尝试执行以下操作，观察结果并解释原因：

numbers[0] = 10
numbers.append(6)
'''
numbers = (1, 2, 3, 4, 5)

# numbers[0] = 10 # TypeError: 'tuple' object does not support item assignment
# numbers.append(6) # AttributeError: 'tuple' object has no attribute 'append'

'''
元组支持的操作非常有限，主要包括：
索引访问：numbers[0]
切片：numbers[1:3]
长度：len(numbers)
成员判断：3 in numbers
拼接/重复：numbers + (6,)、numbers * 2
'''

'''
给定元组：fruits = ("苹果", "香蕉", "橙子", "苹果", "葡萄", "香蕉", "苹果")
1. 统计"苹果"出现的次数
2. 找出"香蕉"第一次出现的位置
3. 获取元组的长度

'''
fruits = ("苹果", "香蕉", "橙子", "苹果", "葡萄", "香蕉", "苹果")
cnt = 0
index = -1
for i in range(len(fruits)):
    if fruits[i] == '苹果':
        cnt += 1
    elif fruits[i] == '香蕉' and index == -1:
        index = i

print('苹果出现的次数：', cnt)
print('香蕉第一次出现的位置：', index)
print('元祖长度：', len(fruits))


'''
给定列表：colors = ["红色", "绿色", "蓝色", "黄色", "紫色"]
1. 将列表转换为元组
2. 对新元组进行切片操作，获取前3个元素
3. 将元组转换回列表
4. 在列表中添加新颜色"橙色"
5. 将列表再次转换为元组

'''
colors = ["红色", "绿色", "蓝色", "黄色", "紫色"]
# 1. 将列表转换为元组
tuple1 = tuple(colors)
print(f'列表转元祖：', tuple1)

# 2. 对新元组进行切片操作，获取前3个元素
t1 = tuple1[0: 3]
print(f'元祖前三个元素：', t1)

# 3. 将元组转换回列表
colors_list = list(tuple1)
print(f'元祖转列表：', colors_list)

# 4. 在列表中添加新颜色"橙色"
colors_list.append('橙色')
print(f'新列表：', colors_list)

# 5. 将列表再次转换为元组
colors_list_tuple = tuple(colors_list)
print(f'将列表再次转换为元组', colors_list_tuple)


'''
创建一个学生信息字典：student = {"name": "张三", "age": 18, "gender": "男", "score": 90}
1. 添加新的键值对："class": "一班"
2. 修改年龄为 19
3. 删除性别信息
4. 打印所有键和所有值

'''
student = {"name": "张三", "age": 18, "gender": "男", "score": 90}

# 1. 添加新的键值对："class": "一班"
student['class'] = '一班'

# 2. 修改年龄为 19
student['age'] = 19
# 3. 删除性别信息
del student['gender']
# 4. 打印所有键和所有值
print(student)


'''
给定字典：fruit_prices = {"苹果": 5.5, "香蕉": 3.0, "橙子": 4.2, "葡萄": 6.8}
1. 遍历并打印所有水果名称
2. 计算所有水果价格的平均值
'''
fruit_prices = {"苹果": 5.5, "香蕉": 3.0, "橙子": 4.2, "葡萄": 6.8}
# 1. 遍历并打印所有水果名称
for fruit in fruit_prices:
    print(fruit)
# 2. 计算所有水果价格的平均值
price = fruit_prices.values()
avg_price = sum(price) / len(price)
print(f'水果均价为：{avg_price:.2f}')



students = {
    "001": {"name": "李华", "scores": {"math": 85, "english": 92, "science": 78}},
    "002": {"name": "王明", "scores": {"math": 90, "english": 88, "science": 95}}
}

# 1. 获取学号"001"的学生的英语成绩
score_001_english = students['001']['scores']['english']
print(f'学号"001"的学生的英语成绩：{score_001_english}')
# 2. 为学号"002"的学生添加新的科目成绩："history": 87
students['002']['scores']['history'] = 87
print(students)


employees = [
    {"id": "E1001", "name": "张三", "department": "技术部", "salary": 8000},
    {"id": "E1002", "name": "李四", "department": "市场部", "salary": 7500},
    {"id": "E1003", "name": "王五", "department": "技术部", "salary": 8500}
]

# 1. 添加新员工：{"id": "E1004", "name": "赵六", "department": "财务部", "salary": 7000}
employees.append({"id": "E1004", "name": "赵六", "department": "财务部", "salary": 7000})
print(employees)
# 2. 求所有人的平均工资
total_salary = sum(emp['salary'] for emp in employees)
avg_salary = total_salary / len(employees)
print(f'平均薪资为:{avg_salary}')



numbers = [1, 2, 2, 3, 4, 4, 4, 5, 5, 6, 7, 7, 8, 9, 9, 9]

# 1. 使用集合去除列表中的重复元素
unique_numbers = set(numbers)
# 2. 统计原列表中有多少种不同的数字
length = len(unique_numbers)
# 3. 找出列表中所有出现次数超过2次的数字（提示：可以先统计次数）
cnt = Counter()
for i, x in enumerate(numbers):
    cnt[x] += 1
    if cnt[x] > 2:
        print(f'列表中出现超过两次的数字为：', x)

# 生成一个 1~10 的立方列表
list_3 = [x * (x ** 2) for x in range(1, 11)]
print(list_3)

# 生成一个 1~20 中 所有3的倍数 的平方列表
list_2 = [i ** 2 for i in range(1, 21) if i % 3 == 0]
print(list_2)

# 需求：使用函数方式定义一个计算器，要求函数可以接收两个整数，并且可以返回这两个整数的加减乘除结果

def cnt(num1, num2):
    return [f'加：{add(num1, num2)}',
            f'减：{sub(num1, num2)}',
            f'乘：{mul(num1, num2)}',
            f'除：{sub(num1, num2)}'
    ]
def add(num1, num2):
    return num1 + num2
def sub(num1, num2):
    return num1 - num2
def mul(num1, num2):
    return num1 * num2
def sub(num1, num2):
    return num1 / num2

fir = cnt(1, 2)
print(fir)