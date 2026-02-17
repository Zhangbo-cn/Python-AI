import math
from collections import Counter

'''

创建元组national_day = ("10月1日", "国庆节", 75, "放假6天")，完成以下操作：

打印元组的长度
打印元组中索引为 2 的元素
尝试修改元组中索引为 3 的元素，观察结果并说明原因。

'''
national_day = ("10月1日", "国庆节", 75, "放假6天")
print(f'元组的长度: {len(national_day)}')
print(f'元组中索引为 2 的元素: {national_day[2]}')
# national_day[3] = 85 # 元组是不可变序列，一旦创建，不能修改其中的元素
# print(f'元组中索引为 3 的元素: {national_day[3]}') # TypeError: 'tuple' object does not support item assignment


'''
给定元组student_info = ("李四", 20, "计算机专业", 88.5)
使用元组解包将姓名、年龄、专业、成绩分别赋值给name、age、major、score 变量，
再用print()函数依次输出这些变量。
'''
student_info = ("李四", 20, "计算机专业", 88.5)
name = student_info[0]
age = student_info[1]
major = student_info[2]
score = student_info[3]

print(f'name:{name}, age: {age}, major: {major}, score: {score}')

'''
定义字典user = {"name": "张三", "age": 19, "hobby": ["编程", "阅读"]}，完成以下操作：

添加键值对"grade": "大二"
获取打印姓名name
修改age的值为 20
删除hobby键及其对应的值
'''
user = {"name": "张三", "age": 19, "hobby": ["编程", "阅读"]}
print(user)
user['grade'] = '大二'
print(user['name'])
user['age'] = 20
print(user)
del user['hobby']
print(user)

'''
嵌套字典操作:
给定嵌套字典
class_info = {"class_id": "Python2024", "students": [{"name": "王五", "score": 90}, {"name": "赵六", "score": 82}]}，
获取 “赵六” 的成绩并输出；再为 “王五” 添加 “rank”: "班级前 10%" 的键值对，打印修改后的class_info。
'''

class_info = {
    "class_id": "Python2024",
    "students": [
        {"name": "王五", "score": 90},
        {"name": "赵六", "score": 82}
    ]
}

# 1. 获取'赵六'的成绩
print(f'赵六的成绩为：', class_info['students'][1]['score'])
# 2. 为 “王五” 添加 “rank”: "班级前 10%" 的键值对
class_info["students"][0]['rank'] = '成绩前10%'
print(class_info)

# 1. 获取'赵六'的成绩
for stu in class_info["students"]:
    if stu['name'] == '赵六':
        print(f'赵六的成绩是：', stu['score'])
        break
# 2. 为 “王五” 添加 “rank”: "班级前 10%" 的键值对
for stu in class_info['students']:
    if stu['name'] == '王五':
        stu['rank'] = '班级前10%'
        break
print(class_info)

'''
定义列表
shopping_list = ["牛奶", "面包", "鸡蛋", "牛奶", "饼干", "面包", "水果"]，
使用集合去除列表中的重复元素，再将去重后的结果转换为列表并按原顺序排序（提示：可借助列表的index()方法），打印最终列表。

'''
shopping_list = ["牛奶", "面包", "鸡蛋", "牛奶", "饼干", "面包", "水果"]

shopping_list_set = set(shopping_list)
print(shopping_list_set)
shopping_list2 = []
cnt = Counter()
for i, c in enumerate(shopping_list):
    if cnt[c] == 0:
        shopping_list2.append(c)
        cnt[c] += 1
shopping_list = shopping_list2
print(shopping_list)


'''
定义函数calculate_area(radius)，
接收圆的半径radius（默认值为 1），
计算并返回圆的面积（π 取 3.14）。

调用该函数，分别传入半径 3 和使用默认半径，打印两次调用的结果。
'''

def calculate_area(radius=1):
    return math.pi * (radius ** 2)

print(calculate_area())

print(calculate_area(3))

'''
定义函数find_common_elements(list1, list2)，
接收两个列表，返回两个列表中的共同元素组成的新列表（元素不重复）。
调用函数find_common_elements([1, 2, 3, 4], [3, 4, 5, 6])，打印返回结果。

'''
# 方法一：
def find_common_elements(list1, list2):
    list1= list(set(list1))
    list2 = list(set(list2))
    list3 = []
    for i, x in enumerate(list1):
        for j, y in enumerate(list2):
            if x == y:
                list3.append(x)
    return list3


list1 = [1, 2, 3, 3, 4]
list2 = [3, 4, 5, 6]
target = find_common_elements(list1, list2)
print(target)

# 方法二：
def find_common_elements_2(list1, list2):
    return list(set(list1) & set(list2))

target1 = find_common_elements_2(list1, list2)
print(target1)


'''
定义可变参数函数sum_multiple(*args)，
接收任意数量的数字参数，计算并返回这些数字的总和。
调用函数sum_multiple(1, 2, 3, 4, 5)和sum_multiple(10, 20, 30)，打印结果。

'''

# def sum_multiple(*args):
#     """
#    这是一个非常实用且常见的输入校验写法，用于确保函数接收到的所有参数都是数字类型（int 或 float）
#        1. isinstance(x, (int, float))
#        检查变量 x 是否是 int 类型 或 float 类型。
#        (int, float) 是一个元组，isinstance 支持传入多个类型进行“任一匹配”判断。
#        2. (isinstance(x, (int, float)) for x in args)
#        这是一个生成器表达式，遍历 args 中的每个元素 x，并对其做类型检查。
#        它不会立即生成全部结果，而是按需计算，节省内存。
#    :param args:
#    :return:
#    """
#
#     if not all(isinstance(x, (int, float)) for x in args):
#         raise TypeError("所有参数必须是数字")
#     return sum(args)

def sum_multiple(*args):
    if not all(isinstance(x, (int, float)) for x in args):
        raise TypeError('所有参数必须为数字')
    return sum(args)

print(sum_multiple(1, 2, 3, 4, 5))
print(sum_multiple(10, 20, 30))

# print(sum_multiple('huiabid', 5484))

'''
使用lambda函数定义一个计算两个数字乘积的匿名函数，并用变量multiply接收该函数。
调用multiply(4, 5)和multiply(2.5, 3)，打印结果。

'''

multiply = lambda x, y: x * y
print(multiply(4, 5))
print(multiply(2.5, 3))


'''


给定列表employees = [
{"name": "张工", "salary": 8000}, 
{"name": "李工", "salary": 9500}, 
{"name": "王工", "salary": 7800}
]，
使用lambda函数作为sort()方法的key参数，对列表按工资降序排序，打印排序后的列表。
'''
employees = [
{"name": "张工", "salary": 8000},
{"name": "李工", "salary": 9500},
{"name": "王工", "salary": 7800}
]

employees_sorted = sorted(employees, key=lambda x: x['salary'], reverse=True)
print(employees_sorted)

'''
编写代码，将字符串
"国庆Python复习计划：\n1. 复习基础语法\n2. 练习函数与面向对象\n3. 完成综合案例"
写入文件holiday_plan.txt中（若文件不存在则创建）。
'''
f1 = open('./data/holiday_plan.txt', 'w', encoding='utf-8')
f1.write("国庆Python复习计划：\n1. 复习基础语法\n2. 练习函数与面向对象\n3. 完成综合案例")
f1.close()

'''
编写代码，读取上一题创建的holiday_plan.txt文件的所有内容，打印文件内容；再读取文件的前 20 个字符，单独打印。
'''
f2 = open('./data/holiday_plan.txt', 'r', encoding='utf-8')
s1 = f2.read()
print(s1)
# print()
print(s1[:20])

f2.close()

'''
定义 “手机” 类Phone，
包含属性：品牌（brand）、型号（model），
方法：
power_on()：打印 “[品牌][型号] 手机开机中...”
take_photo()：打印 “[品牌][型号] 手机正在拍照...”

创建Phone类的实例my_phone = Phone("华为", "Mate 60")，调用power_on()和take_photo()方法。

'''
class Phone:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def power_on(self):
        print(f'[{self.brand}][{self.model}] 手机开机中……')

    def take_photo(self):
        print(f'[{self.brand}][{self.model}] 手机拍照中……')

my_phone = Phone('华为', 'Mate 60')
my_phone.power_on()
my_phone.take_photo()


'''
定义 “图书” 类Book，要求：
必需参数：书名（title）、作者（author）
默认参数：价格（price，默认 0）、是否可借（is_available，默认 True）
方法display_info()：打印图书的完整信息，如 “书名：Python 编程，作者：张三，价格：59.8 元，是否可借：是”
创建Book实例book1 = Book("Python编程", "张三", 59.8)和book2 = Book("数据结构", "李四", is_available=False)，调用display_info()方法。

'''
class Book:

    def __init__(self, title, author, price = 0, is_available = True):
        self.title = title
        self.author = author
        self.price = price
        self.is_available = is_available

    def display_info(self):
        return (f'书名：{self.title}\n'
                f'作者：{self.author}\n'
                f'价格：{self.price} 元\n'
                f'是否可借：{"否" if self.is_available == False else "是"}\n')

book1 = Book("Python编程", "张三", 59.8)
book2 = Book("数据结构", "李四", is_available=False)
print(book1.display_info())
print(book2.display_info())

'''
定义父类Animal，包含属性name、age，方法 speak()（打印 “[name] 发出叫声...”）

定义子类Dog继承Animal，新增属性color，重写speak()方法（打印 “[name]（[color]）：汪汪汪！”），新增方法 fetch()（打印 “[name] 正在叼飞盘...”）

定义子类Cat继承Animal，重写speak()方法（打印 “[name]：喵喵喵！”）
定义多态函数animal_speak(animal)，接收Animal类或其子类的实例，调用speak()方法
创建Dog实例 my_dog = Dog("旺财", 2, "黄色")和Cat实例my_cat = Cat("咪咪", 1)，调用animal_speak(my_dog)和animal_speak(my_cat)，并调用my_dog.fetch()。

'''
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} 发出了叫声...')

class Dog(Animal):

    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def speak(self):
        print(f"{self.name}({self.color})：汪汪汪！")

    def fetch(self):
        print(f"{self.name} 正在叼飞盘...")

class Cat(Animal):

    def speak(self):
        print(f"{self.name}：喵喵喵！")

def animal_speak(animal):
    animal.speak()

my_dog = Dog("旺财", 2, "黄色")
animal_speak(my_dog)
my_dog.fetch()
my_cat = Cat("咪咪", 1)
animal_speak(my_cat)
