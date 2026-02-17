height = 182
id = 12
name = '蔡徐坤'
age = 25

# 格式二：
print('姓名：%s, 年龄：%d, 身高：%.2f, 学号：%d' % (name, age, height, id))

# 格式三：采用 format 格式化方式输出
print('姓名:{}, 年龄:{}'.format(name, age))

# 格式四：采用format格式化简写
print(f'姓名:{name}, 年龄:{age}, 身高:{height:.2f}, 学号:{id:06d}')

# 定义两个变量title='西红柿'，price=9.8322
title = '西红柿'
price = 9.8322
print('今年收成不错，%s 只要 %.2f 元' % (title, price))
print('今年收成不错，{}只要{}'.format(title, price))
print(f'今年收成不错，{title} 只要{price:.2f}')

# \n 换行、\t 等价于tab键
print('hello\nworld')
print('hello\tworld')

# name = input("请输入你的姓名：")
# id = input("请输入你的卡号：")
# code = input("请输入你的银行卡密码：")

print(type(name))
print(type(age))
#
# good = input("请输入商品名称：")
# price = int(input("请输入价格："))
#
# count = int(input("单价："))
# sum = count * price
# print(f'商品是：{good}, 单价是：{count:.2f}, 总价是：{sum:.2f}')
# print(type(str(price)))
#

name1 = "zhangsan"
age1 = 12
print(f'{name1} 十年之后的年龄是：{age1 + 10}')

# lucky_number = int(input("请输入你的幸运数字："))
# print(f'您的幸运数字是：{lucky_number}')

print(int(10.2))
print(int(10.9))
# print(int("10.2")) # ValueError: invalid literal for int() with base 10: '10.2'
print(int("10"))
print(int(True))
print(int(False))

# 布尔值：0 '' → Fasle / 其他一律是True

print(bool(0))  # False
print(bool(1))  # True
print(bool(False))  # False
print(bool(True))  # True
print(bool("0"))  # True
print(bool("0001"))  # True
print(bool(''))  # False

print('*' * 26)
print(str(10))
print(str(10.1))
print(str(True))

print('*' * 26)

# 演示eval(): 相当于把最外端的那对引号去掉，是啥就转成啥
print(eval('10'))
# print(eval('strn27'))
print(eval('0'))
print(eval('False'))
print(eval('True'))

# someone_age = int(input("请输入您的年龄："))
# print(f"该人十年后的年龄为{someone_age + 10}")


_age = 111

a = 10
b = 3.14
c = "Python"
print(type(a), type(b), type(c))

x = 10
print(type(x))

age = 25
height = 1.75
is_student = False
name = "张三"
print(type(age), type(height), type(is_student), type(name))

name = "李四"
age = 25
print('姓名:%s, 年龄:%d' % (name, age))

score = 95
print(f'分数: {score:05d}')

# 需要输出文本: 商品:苹果, 单价:8.50, 数量:3
product = "苹果"
price = 8.5
quantity = 3

# 方式一
print(f'商品:{product}, 单价:{price:.1f}, 数量:{quantity}')
# 方式二
print('商品: %s, 单价: %.1f, 数量: %d' % (product, price, quantity))

# 6.编写代码实现：要求用户输入姓名和年龄，
# 然后输出"你好，[姓名]！你今年[年龄]岁了。"，并确保年龄是整数类型
# user_name = input("请输入您的姓名：")
# user_age = int(input("请输入您的年龄："))
# print(f'你好，[%s]! 你今年[%d]岁了。' % (user_name, user_age))
# print(f'你好，[{user_name}]! 你今年[{user_age}]岁了。')

# num1 = int(input("请输入第一个数字: "))
# num2 = int(input("请输入第二个数字: "))
# result = num1 + num2
# print(f"两数之和为: {result}")

print(int(3.14))  # →3
print(float("5.5"))  # →5.5
print(bool(""))  # →False
print(eval("3 + 2"))  # →5

int("10")  # 10
float("3.14")  # 3.14
# int("10.5") # 报错
bool(0)  # False

print(int("10"))
print(float("3.14"))
# print(int("10.5")) # 报错
print(bool(0))

# age = eval(input("请输入您的年龄: "))
# print(f"类型: {type(age)}, 值: {age}")

x = y = z = "Python"
y = "Java"
print(x, y, z)

'''
# 综合应用题

编写一个程序，要求用户输入：
- 姓名（字符串）
- 年龄（整数）
- 身高（浮点数）
- 是否在校学生（布尔值）

然后输出格式化信息：
"姓名：[姓名]，年龄：[年龄]岁，身高：[身高]米，10年后年龄：[未来年龄]，学生状态：[是否学生]"
'''
# user_name = input("请输入您的姓名：")
# user_age = int(input("请输入您的年龄："))
# user_height = float(input("请输入您的身高(米，带两位小数，如：1.75)："))
# user_bool = bool(input("请问您是否在校居住，住校输入1，不住校输入0："))
# print(
#     f'姓名：[{user_name}], 年龄：[{user_age}], 身高：[{user_height}]米, 10年后年龄：[{user_age + 10}], 学生状态：[{user_bool}]')

'''
编写一个程序，让用户输入商品名称、单价和购买数量，然后计算总金额并输出以下格式：
您购买了[商品名称]，单价[单价]元，数量[数量]件，总金额为[总金额]元。

要求：
1. 使用input()函数分别获取三个输入
2. 将单价和数量转换为适当的数值类型
3. 计算总金额（单价×数量）
4. 使用f-string格式化输出，总金额保留2位小数
'''
# product1 = input("商品名称：")
# price = int(input("商品单价："))
# count = int(input("请输入购买数量"))
# sum = price * count
#
# print(f'您购买了[{product1}], 单价为[{price}]元,数量[{count}]件, 总金额为[{sum}]元')


'''
## 题目2：简单储蓄计算器
编写一个程序，让用户输入每月储蓄金额和储蓄月数，然后计算总储蓄金额并输出：
```
每月储蓄金额：[金额]元
储蓄月数：[月数]个月
总储蓄金额：[总金额]元
```
要求：
1. 获取用户输入的每月储蓄金额和月数
2. 将输入转换为适当的数值类型
3. 计算总储蓄金额（每月金额×月数）
4. 使用格式化输出显示结果，总金额保留2位小数
'''
# 1. 获取用户输入的每月储蓄金额和月数
# per_month_balance = float(input("请输入每月储蓄金额："))
# month_count = float(input("请输入储蓄月数："))
# sum_amount = per_month_balance * month_count
# print(f"每月储蓄金额：[{per_month_balance}]元")
# print(f"储蓄月数：[{month_count}]个月")
# print(f"总储蓄金额：[{sum_amount:.2f}]元")

'''
## 题目3：旅行时间计算器
编写一个程序，让用户输入出发时间和到达时间（24小时制的小时数，如8表示8:00），然后计算并输出旅行所用小时数：
```
出发时间：[出发时间]:00
到达时间：[到达时间]:00
旅行用时：[用时]小时
```
要求：
1. 获取出发时间和到达时间的输入
2. 将输入转换为整数
3. 计算用时（到达时间-出发时间）
4. 使用格式化输出显示结果
'''
# go_out_time = input("请输入出发时间：")
# arrive_at_time = input("请输入到达时间：")
# spend_time = abs(int(go_out_time) - int(arrive_at_time))
# print(f'出发时间：[{go_out_time}]:00')
# print(f'到达时间：[{arrive_at_time}]:00')
# print(f'旅行花费：[{spend_time}]小时')

'''
## 题目4：水果折扣计算器
编写一个程序，让用户输入水果名称、原价和折扣率（如0.9表示9折），然后计算折后价格并输出：
```
[水果名称]原价[原价]元，打[折扣率×10]折后价格为[折后价]元。
```
要求：
1. 获取水果名称、原价和折扣率的输入
2. 将价格和折扣率转换为浮点数
3. 计算折后价格（原价×折扣率）
4. 使用f-string格式化输出，价格保留1位小数
'''
# fruit_name = input("请输入这是什么水果：")
# original_price = float(input("原价是多少："))
# discount = float(input("折扣是多少："))
# sale_price = original_price * discount
# print(f'[{fruit_name}]原价是[{original_price}]元，打[{discount * 10}]折后价格为[{sale_price:.1f}]元。')

'''
## 题目1：个人信息介绍器
编写一个程序，要求用户依次输入姓名、年龄和爱好，然后使用格式化输出显示以下内容：
```
我的名字是[姓名]，今年[年龄]岁，我的爱好是[爱好]。
不用带 中括号哈
```
要求：
1. 使用input()函数获取用户输入
2. 使用f-string格式化输出（推荐格式）
3. 变量命名要符合规范，见名知意
'''

# user_name = input("请输入您的姓名：")
# user_age = int(input("请输入您的年龄："))
# user_hobby = input("请输入您的爱好：")
#
# print(f'我的名字是:{user_name}, 今年{user_age}, 我的爱好是:{user_hobby}')

'''
## 题目2：简易计算器
编写一个程序，让用户输入两个数字，然后计算并显示：
1. 两个数字的和
2. 两个数字的差
3. 两个数字的乘积
4. 第一个数字除以第二个数字的商（保留2位小数）
要求：
1. 注意将输入的字符串转换为数值类型
2. 使用格式化输出显示结果
3. 为每个操作使用不同的变量存储结果
'''

# num1 = float(input("请输入第1个数字："))
# num2 = float(input("请输入第2个数字："))
# two_sum = num1 + num2
# two_sub = num1 - num2
# two_mul = num1 * num2
# two_div = num1 / num2
# print(f'两数之和为：{two_sum}, 两数之差为：{two_sub}, 两数之积为：{two_mul}, 两数之商：{two_div}')

'''
## 题目3：温度转换器
编写一个程序，让用户输入一个摄氏温度值，然后将其转换为华氏温度并输出。
转换公式：华氏温度 = 摄氏温度 × 1.8 + 32

要求：
1. 使用input()获取用户输入的摄氏温度
2. 将输入转换为浮点数进行计算
3. 使用格式化输出，显示结果保留1位小数，格式如：
[摄氏温度]摄氏度等于[华氏温度]华氏度
'''
# celsius = float(input("请输入要转换的摄氏度："))
# fahrenheit = (celsius * 1.8) + 32
# print(f'{celsius}摄氏度等于{fahrenheit:.1f}华氏度')

'''
## 题目4：学生平均分计算
编写一个程序，让用户输入三门课程的成绩（语文、数学、英语），然后计算并输出平均分。
要求：
1. 使用input()分别获取三门课程的成绩
2. 将输入的成绩转换为浮点数
3. 计算平均分（保留2位小数）
4. 使用格式化输出，显示格式：
'''
# chinese_grade = float(input("请输入语文成绩："))
# english_grade = float(input("请输入英语成绩："))
# math_grade = float(input("请输入数学成绩："))
# avg_grade = (chinese_grade + english_grade + math_grade) / 3
# print(f'语文成绩：{chinese_grade}\n数学成绩：{math_grade}\n英语成绩：{english_grade}\n三门课的平均分为：{avg_grade:.2f}')

'''
## 题目5：长方形面积计算器
编写一个程序，让用户输入长方形的长和宽，然后计算并输出长方形的周长和面积。
要求：
1. 获取用户输入的长和宽
2. 将输入转换为适当的数值类型
3. 计算周长（周长 = 2 × (长 + 宽)）和面积（面积 = 长 × 宽）
4. 使用格式化输出，显示格式：
'''
length = float(input("输入长："))
width = float(input("输入宽："))
perimeter = (length + width) * 2
area = length * width
print(f'长方形的长为：{length}')
print(f'长方形的宽为：{width}')
print(f'长方形的周长为：{perimeter}')
print(f'长方形的面积为：{area}')