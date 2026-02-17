'''
定义 3 个合法变量，分别存储 “Python 国庆作业”（字符串）、2024（整数）、3.8（浮点数），
并使用print()函数依次输出变量值及对应数据类型。

'''

str1 = 'Python 国庆作业'
year = 2024
float1 = 3.8

print(str1, type(str1))
print(year, type(year))
print(float1, type(float1))

'''
判断以下变量名是否合法，若不合法说明原因：123_python、python@2024、_holiday、class。

'''
# 变量命名格式：不能以数字、除_之外的特殊字符开头、也不能使用关键字，怎么结尾倒没所谓
# value1 = 123_python # 不合法，123_python
# python@2024 = str1 # 不合法，@属于特殊字符，！@#￥%……&*）） 都是这个道理
_holiday = '2024' # 合法
# str3 = class # 不合法，class属于关键字


'''
使用input()函数获取用户的国庆出行目的地（字符串）和出行天数（整数）
再用格式化字符串（f-string）输出 “你的国庆目的地是 [目的地]，计划出行 [天数] 天”。

'''
# destination = input('请输入国庆出行目的地：')
# duration = input('请输入国庆出行时长：')
#
# print(f'国庆目的地是{destination}，计划出行{duration}天')

'''
定义变量score = 89.5，使用format()方法格式化输出 “本次作业得分：89.5（保留 1 位小数）” 和 “得分对应的整数形式：89”。

'''
score = 89.5
print(f'本次作业得分：{score:.1f},得分对应的整数形式：{score:.0f}') # 四舍五入
# print(f'本次作业得分：{score:.1f},得分对应的整数形式：{int(score)}') # 向下取整

'''
编写代码，将用户输入的 “3.14”（字符串）转换为浮点数后计算其 2 倍值，再将结果转换为整数并输出；同时将空字符串""转换为布尔值，输出转换结果。
'''
str1 = '3.14'
print(str1)
float1 = float(str1) * 2
print(float1)
int1 = int(float1)
print(int1)

str2 = ''
print(bool(str2))

'''
执行以下代码，分析可能出现的错误并修正：
'''
# num1 = float(input("请输入第一个数字："))
# num2 = float(input("请输入第二个数字："))
#
# result = num1 + num2
# print("两数之和：", result)


'''
根据用户输入的国庆假期每日学习时长（整数，单位：小时），使用多分支判断：

时长≥6：输出 “学习达人，继续保持！”
3≤时长＜6：输出 “学习状态良好，加油！”
1≤时长＜3：输出 “学习时间不足，需调整！”
时长＜1：输出 “请重视国庆复习，增加学习时间！”
'''
# study_time = float(input('请输入您的学习时长：'))
#
# if study_time >= 6:
#     print('学习达人，继续保持！')
# elif study_time >= 3:
#     print('学习状态良好，加油！')
# elif study_time >= 1:
#     print('学习时间不足，需调整！')
# else:
#     print('请重视国庆复习，增加学习时间！')

'''
使用for循环计算 1~100 中所有能被 7 整除的数字的和，并输出结果。
'''
sum = 0

for i in range(1, 101):
    if i % 7 == 0:
        sum += i

print(f'1~100 中所有能被 7 整除的数字的和是：{sum}')

'''
使用for循环,   统计字符串中,  o 字符出现的次数
str = 'ok, hello everybody'
'''
str = 'ok, hello everybody'

cnt = 0

for i, c in enumerate(str):
    if c == 'o':
        # print(i, c)
        cnt += 1
print(cnt)

'''
给定字符串url = "https://www.python.org/downloads"，使用切片提取出 “python.org” 部分并输出。

'''
url = "https://www.python.org/downloads"
str1 = 'python.org'
n = len(str1)
for i, c in enumerate(url):
    if url[i:i+n] == str1:
        print(url[i:i+n])
        break

'''
给定用户邮箱email = "student_2024@school.com"，
通过find()方法找到@的位置，再用切片提取邮箱的用户名（@前面的内容）和域名（@后面的内容）并分别输出。
'''
email = "student_2024@school.com"
index = email.find('@')
# print(index)
print(email[0: index], email[index + 1: ])

'''
# 在列表末尾添加 “整理笔记”
# 在 “练习循环” 和 “写函数作业” 之间插入 “复习字符串切片”
# 删除列表中索引为 1 的元素
# 打印最终列表及列表长度。
'''
holiday_tasks = ["复习变量", "练习循环", "写函数作业", "做面向对象案例"]
# 在列表末尾添加 “整理笔记”
holiday_tasks.append('整理笔记')

# 在 “练习循环” 和 “写函数作业” 之间插入 “复习字符串切片”
for i, c in enumerate(holiday_tasks):
    if c == '练习循环':
        holiday_tasks.insert(i + 1, '复习字符串切片') # 在 “练习循环” 和 “写函数作业” 之间插入 “复习字符串切片”
        break
# print(holiday_tasks) # ['复习变量', '练习循环', '复习字符串切片', '写函数作业', '做面向对象案例', '整理笔记']
holiday_tasks.pop(1)
# print(holiday_tasks) # ['复习变量', '复习字符串切片', '写函数作业', '做面向对象案例', '整理笔记']
print(f'列表内容为：{holiday_tasks}, 列表长度为：{len(holiday_tasks)}')

'''
# 定义列表scores = [78, 92, 85, 66, 95, 78, 88]，完成以下操作：
# 
# 统计 78 出现的次数
# 对列表按降序排序
# 找出列表中的最高分和最低分
# 打印处理后的列表、78 的次数、最高分和最低分。
'''
scores = [78, 92, 85, 66, 95, 78, 88]

scores.sort(reverse=True)
# print(scores)

cnt_78 = 0
for i, x in enumerate(scores):
    if x == 78:
        cnt_78 += 1
print(scores)
print(f'78 出现的次数为:{cnt_78}')
print(f'列表最高分：{scores[0]},最低分为：{scores[len(scores) - 1]}')