'''
定义 4 个变量，分别存储 “国庆假期”（字符串）、7（整数，代表假期天数）、36.5（浮点数，代表体温）、True（布尔值，代表是否完成作业），
使用print()函数输出所有变量的 “变量名 - 值 - 数据类型”，格式如 “holiday_name: 国庆假期，类型: <class'str'>”。

'''
from random import random

holiday_name = '国庆假期'
day = 7
temperature = 36.5
is_complete = True

print(f'holiday_name: {holiday_name}, 类型: {type(holiday_name)}')
print(f'day: {day}, 类型: {type(day)}')
print(f'temperature: {temperature}, 类型：{type(temperature)}')
print(f'is_complete: {is_complete}, 类型： {type(is_complete)}')

'''
分析以下变量名的合法性，若合法说明原因，若不合法指出问题：python_2024、2024_python、python@holiday、break、_score。
'''
# 变量名不能包括特殊字符（特殊字符：除字母、_（下划线）、数字外的其他任意字符）
# 变量名通常以小写字母开头，或者__开头，或者_结尾，单词之间使用 _ 连接

python_2024 = '' # 合法
# 2024_python = '' # 错误，不能以数字开头
# python@holiday = '' # 错误，不能含有特殊字符
# break、_score = '' # 错误，不能含有特殊字符

'''
使用input()函数获取用户的姓名和国庆期间完成的 Python 练习题数量（整数），
通过格式化字符串输出 “[姓名] 国庆期间完成了 [数量] 道 Python 练习题，继续加油！”。
'''
# usr = input('请输入用户姓名：')
# p_num = int(input('请输入练习题数量：'))
#
# print(f'[{usr}] 国庆期间完成了 [{p_num}] 道 Python 练习题，继续加油！')

'''
定义变量weight = 62.3，height = 1.75，
使用format()方法格式化输出:
    “体重：62.30kg（保留 2 位小数），身高：1.75m，
    BMI 值：20.3（BMI = 体重 / 身高 ²，保留 1 位小数）”。
'''
weight = 62.3
height = 1.75
print(f'体重：{weight:.2f}kg，身高：{height:.2f}m，BMI 值：{weight / height ** 2:.1f}')

'''
编写代码，将用户输入的 “123”（字符串）转换为整数后加 50，再将结果转换为字符串并拼接 “分” 字，输出如 “173 分”；
同时将数字 0 转换为布尔值，将字符串 “False” 转换为布尔值，分别输出两个转换结果。

'''
# s1 = str(int(input('请输入分数：'))) + ' 分'
# print(s1)
# 数字的布尔值只看数字是否为0，0为假，非0为真
print(bool(0)) # False
# 判断字符串真假值的逻辑是：非空字符串为真，空字符串为假
print(bool('False')) # True
print(bool('')) # False
print(bool(False)) # False

# num1 = int(input("请输入第一个整数：")) # 传入的是字符串，需要将字符串转换为数字，int(str) 强制转换即可
# num2 = int(input("请输入第二个小数："))
# result = num1 * num2
# print("两数乘积：", result)

'''
根据用户输入的 Python 考试分数（0~100 的整数），使用多分支判断成绩等级：
90~100：输出 “等级：A（优秀）”
80~89：输出 “等级：B（良好）”
60~79：输出 “等级：C（及格）”
0~59：输出 “等级：D（不及格）”
若输入分数超出 0~100 范围，输出 “请输入有效的分数（0~100）”。
'''
# score = int(input("请输入 Python 考试分数："))
# if score >= 90 and score <= 100:
#     print("等级：A（优秀）")
# elif score >= 80 and score <= 89:
#     print("等级：B（良好）")
# elif score >= 60 and score <= 79:
#     print("等级：C（及格）")
# elif score >= 0 and score <= 59:
#     print("等级：D（不及格）")
# else:
#     print("请输入有效的分数（0~100）")

'''
编写代码判断一个年份是否为闰年（闰年规则：能被 4 整除但不能被 100 整除，或能被 400 整除），
若用户输入的不是整数，提示 “请输入有效的年份（整数）”。
'''
# year = int(input("请输入年份："))
# if (year % 4 == 0 and year % 100 == 0) or year % 400 == 0:
#     print(f'{year}是闰年')
# else:
#     print(f'{year}非闰年')

'''
使用for循环计算 20~50 中所有偶数的和，并输出结果；同时统计该范围内偶数的个数，一并输出。
'''
cnt = 0
num = 0
for i in range(20, 51):
    if i % 2 == 0:
        cnt += 1
        num += i

print(f'[20, 50]之间偶数个数为：{cnt}个，偶数和为：{num}')

'''
定义字符串 python_code = "for i in range(10): print(i) if i%2==0 else pass"，
使用for循环统计字符串中字母 “i” 出现的次数，以及数字 “0” 出现的次数，分别输出。

'''
python_code = "for i in range(10): print(i) if i%2==0 else pass"
cnt_i = cnt_0 = 0
for i, c in enumerate(python_code):
    if c == 'i':
        cnt_i += 1
    elif c == '0':
        cnt_0 += 1

print(f'i出现的次数为：{cnt_i}\n'
      f'0出现的次数为：{cnt_0}')

'''
给定字符串 file_path = "D:/PythonProjects/holiday/homework.py"，
使用切片提取出文件名 “homework.py”，再进一步提取文件后缀名 “py”，分别输出。

'''
file_path = "D:/PythonProjects/holiday/homework.py"
index = file_path.rfind('/')
print(file_path[index + 1:])

'''
给定字符串 time_str = "2024-10-01 08:30:00"，
通过切片提取出 “2024”（年份）、“10”（月份）、“01”（日期），
并按 “日期：2024 年 10 月 01 日” 的格式输出。
'''
time_str = "2024-10-01 08:30:00"
print(f'日期：{time_str[0:4]} 年 {time_str[5:7]} 月 {time_str[9:11]} 日')


# 使用 split() 方法，split是字符串切割的一个方法
# 底层默认的切分割逻辑：当遇到空格时，将该空格处作为切割点对字符串进行切割，返回一个列表；（空格包含' ' \n \t \f \r）
# 另外，分割符号也可以自主指定，例如：.split('-')

data_part = time_str.split()
print(data_part[0])
year, month, day = data_part[0].split('-')
# print(year, month, day)
print(f'日期：{year} 年 {month} 月 {day} 日')

'''
定义列表shopping_cart = ["薯片", "可乐", "巧克力", "坚果"]，完成以下操作：
在 “可乐” 前面插入 “饼干”
删除列表中最后一个元素
将 “巧克力” 修改为 “黑巧克力”
打印最终列表及列表中元素的个数。
'''
shopping_cart = ["薯片", "可乐", "巧克力", "坚果"]
shopping_cart.insert(1, '饼干')
# remove 删除指定元素, pop 删除列表中最后一个元素, 列表和集合 都有remove 和 pop方法，字典有pop方法 没有remove方法，字符串和元组都没有(因为不可变性质)
shopping_cart.pop()
shopping_cart[2] = '黑巧克力'
print(shopping_cart)

'''
┌─────────────────────────────────────────────────────────────────┐
│              Python 常见类型的删除方法对比                       │
├──────────────┬──────────┬──────────┬──────────┬────────────────┤
│    类型       │ remove() │  pop()   │  del     │     说明       │
├──────────────┼──────────┼──────────┼──────────┼────────────────┤
│   list 列表  │   ✅     │   ✅     │   ✅     │ remove按值，pop按索引 │
│   set 集合   │   ✅     │   ✅     │   ✅     │ remove/pop都按值     │
│   dict 字典  │   ❌     │   ✅     │   ✅     │ pop按键，del按键    │
│   str 字符串 │   ❌     │   ❌     │   ❌     │ 字符串不可变       │
│   tuple 元组 │   ❌     │   ❌     │   ❌     │ 元组不可变         │
└──────────────┴──────────┴──────────┴──────────┴────────────────┘
'''

'''
定义列表 temperatures = [26.5, 28.3, 27.1, 29.5, 26.5, 27.8]，完成以下操作：
找出 28.3 在列表中的索引位置
对列表按升序排序
计算列表中所有温度的平均值（保留 1 位小数）
打印处理后的列表、28.3 的索引、温度平均值。

'''
temperatures = [26.5, 28.3, 27.1, 29.5, 26.5, 27.8]
index = temperatures.index(28.3)
# print(index)

temperatures_sorted = sorted(temperatures)
# print(temperatures_sorted)
avg = sum(temperatures_sorted) / len(temperatures_sorted)
print( f'列表为：{temperatures_sorted}\n'
       f'28.3的索引为：{index}'
       f'列表中国数据均值为：{avg:.1f}')

'''
创建元组season_fruits = ("春天", ["草莓", "樱桃"], "夏天", ["西瓜", "桃子"])，完成以下操作：
打印元组中索引为 1 的元素
尝试修改元组中 “春天” 为 “春季”，观察结果；再尝试修改索引 1 列表中的 “草莓” 为 “大草莓”，观察结果并说明原因。

'''
season_fruits = ("春天", ["草莓", "樱桃"], "夏天", ["西瓜", "桃子"])
print(season_fruits[1])
season_fruits[1][0] = '西瓜' # 元组中的列表可以被修改
print(season_fruits[1])
# season_fruits[0] = '橙子' # 元组内容不可被修改
# print(season_fruits[0])

'''
给定元组coordinates = ((10, 20), (30, 40), (50, 60))，
使用嵌套解包将每个子元组的两个元素分别赋值给x1,y1、x2,y2、x3,y3，
计算并输出x1+y1+x2+y2+x3+y3的结果。
'''
coordinates = ((10, 20), (30, 40), (50, 60))
((x1, y1), (x2, y2), (x3, y3)) = coordinates
print(x1 + y1 + x2 + y2 + x3 + y3)
print(sum(sum(i) for i in coordinates))

'''
定义字典 movie = {"name": "国庆档电影", "type": ["动作", "喜剧"], "duration": 120}，完成以下操作：
添加键值对"release_date": "2024-10-01"
修改duration的值为 135
向type列表中添加 “悬疑”
打印字典的所有键值对。
'''
movie = {"name": "国庆档电影", "type": ["动作", "喜剧"], "duration": 120}
movie["release_date"] = "2024-10-01"
movie["duration"] = 135
movie["type"].append("悬疑")
print(movie)

'''
给定字典
student_scores = {
    "张三": {"math": 85, "english": 92}, 
    "李四": {"math": 90, "english": 88}}
获取 “张三” 的英语成绩并输出；
再为 “李四” 添加 “science”: 95 的键值对，计算 “李四” 三门学科的平均分并输出。
'''
student_scores = {
    "张三": {"math": 85, "english": 92},
    "李四": {"math": 90, "english": 88}}

print(f'张三英语成绩为：{student_scores["张三"]["english"]}')
student_scores["李四"]["science"] = 95
score_sum = sum(student_scores["李四"].values())
print(f'李四三门学科的平均分为：{score_sum / len(student_scores["李四"])}')

'''
定义列表
words = ["apple", "banana", "apple", "orange", "banana", "grape"]，
使用集合去除重复元素，再将去重后的结果转换为列表并按字母顺序排序，打印排序后的列表。
'''
words = ["apple", "banana", "apple", "orange", "banana", "grape"]
words_set = set(words)
# print(words_set)
words_set_list_sorted = sorted((list(words_set)))
print(words_set_list_sorted)

'''
使用列表推导式生成 1~15 中所有能被 2 整除的数字的立方组成的列表，如[8, 64, ...]。
'''
list0 = [i ** 3 for i in range(1, 16) if i % 2 == 0]
print(list0)

'''
定义函数calculate_rectangle_area(length, width)，
接收长方形的长和宽（默认值均为 1），计算并返回长方形的面积和周长（返回两个值）。
调用该函数，传入长 5、宽 3，分别接收面积和周长并打印。

'''
def calculate_rectangle_area(length = 1, width = 1):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter
s, l = calculate_rectangle_area(5, 3)
print(f'面积为：{s}\n'
      f'周长为：{l}')

'''
定义函数 filter_even_numbers(numbers)，
接收一个数字列表，返回列表中所有偶数组成的新列表（若列表中无偶数，返回空列表）。
调用函数filter_even_numbers([1, 2, 3, 4, 5, 6])和filter_even_numbers([7, 9, 11])，打印返回结果。
'''
def filter_even_numbers(numbers):
    return [i for i in range(len(numbers)) if numbers[i] % 2 == 0]
list1 = filter_even_numbers([1, 2, 3, 4, 5, 6])
list2 = filter_even_numbers([7, 9, 11])
print(f'列表一：{list1}, 列表二：{list2}')

'''
定义函数 print_info(name, age, gender="未知")，
接收姓名、年龄、性别（默认 “未知”），
打印 “姓名：[name]，年龄：[age]，性别：[gender]”。
分别调用print_info("张三", 19, "男")和print_info("李四", 20)，观察输出结果。
'''
def print_info(name, age, gender="未知"):
    print(f'姓名：{name}，年龄：{age}，性别：{gender}')

print_info("张三", 19, "男")
print_info("李四", 20)

'''
定义可变关键字参数函数 create_product(**kwargs)，
接收商品的名称、价格、数量等关键字参数，
返回一个包含这些信息的字典，且字典中必须包含 “product_id” 键，值为 “PROD-”+ 随机 3 位数字（提示：使用random.randint(100,999)生成随机数）。
调用函数 create_product(name="Python书籍", price=59.8, quantity=100)，打印返回的字典。
'''
import random
def create_product(**kwargs):
    kwargs["product_id"] = "PROD-" + str(random.randint(100, 999))
    return kwargs

print(create_product(name='Python书籍', price=59.8, quantity=100))

'''
使用lambda函数定义一个计算 “a 的平方加 b 的平方” 的匿名函数，
用变量sum_of_squares接收。
调用 sum_of_squares(3,4)和sum_of_squares(5,6)，打印结果（预期 1：25，预期 2：61）。
'''
# def sum_of_squares(a, b):
#     return a ** 2 + b ** 2
# res1 = sum_of_squares(3, 4)
# print(res1)

res2 = lambda a, b: a ** 2 + b ** 2
print(res2(3, 4))
print(res2(5, 6))

'''
给定列表
scores = [(90, "张三"), (85, "李四"), (95, "王五"), (88, "赵六")]，
使用lambda函数作为sort()方法的key参数，对列表按分数降序排序（分数相同时按姓名首字母升序），打印排序后的列表。
'''
scores = [(90, "张三"), (85, "李四"), (95, "王五"), (88, "赵六")]
scores_sorted_1 = sorted(scores, key=lambda x : (-x[0], x[1]))
print(scores_sorted_1)
summary = """
┌─────────────────────────────────────────────────────────────────┐
│                      sort() 多条件排序要点                       │
├─────────────────────────────────────────────────────────────────┤
│  1. key 参数接收函数，为每个元素生成排序键                       │
│  2. lambda x: (-x[0], x[1]) 返回元组实现多条件排序              │
│  3. 元组比较：从左到右依次比较元素                               │
│  4. 降序技巧：对数值取负数 (-x[0])                               │
│  5. reverse=True 会反转所有条件的排序方向                        │
│  6. sort() 原地修改，sorted() 返回新列表                         │
│  7. Python 排序是稳定的，相同键值保持原有相对顺序                │
└─────────────────────────────────────────────────────────────────┘
"""
'''
┌─────────────────────────────────────────────────────────────────┐
│                    lambda 排序键生成过程                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  原始元素          lambda 处理          排序键                  │
│  ────────          ───────────          ───────                 │
│  (90, "张三")  →  lambda x: (-x[0], x[1])  →  (-90, "张三")    │
│  (90, "李白")  →  lambda x: (-x[0], x[1])  →  (-90, "李白")    │
│       │                                      │                 │
│       │                                      └─→ 先比 -90 = -90│
│       │                                         再比 "李" < "张"│
│       └────────────────────────────────────────→ "李白" 排前面  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
'''

'''
编写代码，
将列表["张三:90", "李四:85", "王五:95", "赵六:88"]中的每个元素作为一行，
写入文件 student_scores.txt中（覆盖原有内容）。
'''
f1 = open('./data/student_scores.txt', 'w', encoding='utf-8')
list3 = ["张三:90", "李四:85", "王五:95", "赵六:88"]

for i in range(len(list3)):
    f1.write(list3[i] + '\n')
print('写入完成')
f1.close()

'''
编写代码，读取 student_scores.txt文件的内容，统计所有学生的分数总和及平均分，
打印 “总分：[总和]，平均分：[平均分]”（平均分保留 1 位小数）；
同时将分数大于 90 的学生信息写入excellent_students.txt中。
'''
f2 = open('./data/student_scores.txt', 'r', encoding='utf-8')
read = f2.read()
print(read)
list4 = read.split()
print(list4)
sum = 0
for i in range(len(list4)):
    num = int(list4[i].split(':')[1])
    sum += num

print(f'总分为：{sum}, 均分为：{sum / len(list4)}')

f2.close()

'''
定义 “电脑” 类Computer，包含属性：品牌（brand）、价格（price），方法：
programming()：打印 “[品牌] 电脑正在运行 Python 编程”
watch_video()：打印 “[品牌] 电脑正在播放视频，价格：[price] 元”
创建Computer实例my_computer = Computer("联想", 5999)，调用两个方法并观察输出。
'''
class Computer:

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def programming(self):
        print(f'{self.brand} 电脑正在运行 Python 编程')

    def watch_video(self):
        print(f'{self.brand} 电脑正在播放视频，价格：{self.price} 元')

my_computer = Computer("联想", 5999)
my_computer.programming()
my_computer.watch_video()

'''
定义 “学生” 类 Student，要求：
必需参数：学号（student_id）、姓名（name）
默认参数：年级（grade，默认 “大一”）、成绩（score，默认 0）
方法 update_score(new_score)：更新学生成绩（若新成绩超出 0~100，提示 “无效成绩”，不更新）
方法 show_info()：打印学生完整信息，如 “学号：2024001，姓名：张三，年级：大一，成绩：85”
创建Student实例stu1 = Student("2024001", "张三", "大二")，调用 update_score(92)和show_info()；再调用update_score(105)，观察是否更新。

'''
class Student:

    def __init__(self, student_id, name, grade='大一', score=0):
        self.student_id = student_id
        self.name = name
        self.grade = grade
        self.score = score
        # print(f'学号：{self.student_id}，姓名：{self.name}，年级：{self.grade}，成绩：{self.score}')

    def update_score(self, new_score):
        if new_score < 0 or new_score > 100:
            print('无效成绩')
        else:
            self.score = new_score
            print(f'成绩更新成功')

    def show_info(self):
        print(f'学号：{self.student_id}，姓名：{self.name}，年级：{self.grade}，成绩：{self.score}')

if __name__ == '__main__':
    stu1 = Student("2024001", "张三", "大二")
    stu1.update_score(92)
    stu1.show_info()
    stu1.update_score(105)  # 无效成绩
    stu1.show_info()

'''
基于面向对象三大特性完成以下需求：
定义父类 Vehicle，包含属性 brand、color，方法run()（打印 “[brand][color] 车辆正在行驶”）
定义子类 Car继承Vehicle，新增属性seat_count（座位数），重写run()方法（打印 “[brand][color] 汽车（[seat_count] 座）正在公路行驶”），新增方法honk()（打印 “汽车鸣笛：嘀嘀嘀！”）
定义子类 Bicycle继承Vehicle，重写run()方法（打印 “[brand][color] 自行车正在非机动车道行驶”）
定义多态函数 vehicle_run(vehicle)，接收Vehicle或其子类实例，调用run()方法
创建Car实例 my_car = Car("特斯拉", "红色", 5)和Bicycle实例my_bike = Bicycle("捷安特", "黑色")，调用vehicle_run(my_car)、vehicle_run(my_bike)，并调用my_car.honk()。
'''
class Vehicle:

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def run(self):
        print(f'{self.brand}{self.color}车辆正在行驶')


class Car(Vehicle):

    def __init__(self, seat_count, brand, color):
        super().__init__(brand, color) # 这行代码的意义？
        self.seat_count = seat_count

    def run(self):
        print(f'{self.brand}{self.color} 汽车 （[{self.seat_count}] 座）正在公路行驶')

    def honk(self):
        print('汽车鸣笛：嘀嘀嘀！')

class Bicycle(Vehicle):
    def run(self):
        print(f'{self.brand}{self.color} 自行车正在非机动车道行驶')

def vehicle_run(vehicle):
    vehicle.run()

if __name__ == '__main__':
    my_car = Car(5, "特斯拉", "红色")
    my_bike = Bicycle("捷安特", "黑色")
    vehicle_run(my_car)
    vehicle_run(my_bike)
    my_car.honk()

