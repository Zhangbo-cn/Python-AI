# str1 = 'Hello, Python, World!'
# print(str1[6:13])
#
# # 字符串的翻转
# print(str1[::-1])
#
# str2 = 'http://www.baidu.com'
# print(str2[7::])
#
# str3 = 'report_2024.pdf'
# print(str3[12::])
# print(str3[:11:])
#
# str4 = '18839118755'
# print(str4[0:3] + '*' * 4 + str4[len(str4) - 4::])

# str1 = 'Hello, Python, World!'
# print(str1.find('Hello', 5)) # 不存在返回-1
#
# # todo 抛出异常问题 -> 不影响后续代码的执行
# try:
#     print(str1.index('Hello', 5)) # 不存在返回-1
# except:
#     print('要查找的结果不存在')

# 我认为人工智能必然是未来的方向，人工智能将改变世界，人工智能很重要
str1 = '我认为人工智能必然是未来的方向，人工智能将改变世界，人工智能很重要'
# print(str1.find('人工智能', 0))
# print(str1.index('人工智能',8))

# str2 = 'username@example.com'
# print(str2[:str2.find('@',0)])
# print(str2[str2.find('@',0) + 1:])

# start = 0
# while True:
#     index = str1.find('人工智能', start)
#     if index == -1:
#         break
#     print(index)
#     start += 4

str1 = '我认为人工智能必然是未来的方向，人工智能将改变世界，人工智能很重要'
str2 = str1.replace('人工智能', 'AI', 2)
print(str2)
str2 = str1.replace('人工智能', 'AI')
print(str2)

# 列表转字符串
a = ['a', 'b', 'c']
# print(''.join(a))
list1 = ''.join(a)
print(list1)

# 字符串转列表
list1 = 'a-b-c'
list2 = list1.split('-')
print(list2)

# 敏感词脱敏，将一段话中的所有'你大爷'，换成'**'
list1 = '我去你大爷，你大爷董哥，你大爷找小鸡'
list2 = list1.replace('你大爷', '**')
print(list2)

list1 = '2025-09-19'
list2 = list1.split('-')
print(list2)

# 列表转字符串
a = ['orange', 'juice']
list1 = '_'.join(a)
print(list1)










