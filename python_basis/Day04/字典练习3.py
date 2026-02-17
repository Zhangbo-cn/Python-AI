# 学生成绩
grade = {
    '数学': 135,
    '语文': 70,
    '英语': 110,
    '物理': 85,
    '化学': 80,
    '生物': 78,
}

# 1. 获取所有考试的科目，并打印出来
for key in grade.keys():
    print(key)

# 2. 求取学生的平均分
avg = 0
sum = 0
for value in grade.values():
    sum += value

print(f'总分是{sum}, 均分为{sum / len(grade)}')

# 3. 打印成绩表，将科目和成绩对应起来
for k, v in grade.items():
    print(k, v)

# 假设输入五个字符串
# num = 0
# d2 = {}
# while num < 3:
#     my_str = input('请输入字符串：')
#     if my_str in d2:
#         d2[my_str] += 1
#         print(f'输入次数：{d2[my_str]}')
#     else:
#         d2[my_str] = 1
#         print(d2[my_str])
#         print(f'my_str不存在d2中，初次加入')
#     num += 1
# print(d2)

str = 'aaabbbCCC1112255'
d = {}
for key in str:
    if key not in d:
        d[key] = 1
    else:
        d[key] += 1

print(d)

str1 = 'name=坤坤&age=18&desc=唱跳rap'
str2 = str1.split('&')
print(str2)
d1 = {}
l1 = []
for i in str2:
    l1 = i.split('=')
    # print(l1)
    d1[l1[0]] = l1[1]
print(d1)
