# # 列表转字符串
# a = ['a', 'b', 'c']
# # print(''.join(a))
# list1 = ''.join(a)
# print(list1)
#
# # 字符串转列表
# list1 = 'a-b-c'
# list2 = list1.split('-')
# print(list2)
#
# # 敏感词脱敏，将一段话中的所有'你大爷'，换成'**'
# list1 = '我去你大爷，你大爷董哥，你大爷找小鸡'
# list2 = list1.replace('你大爷', '**')
# print(list2)
#
# list1 = '2025-09-19'
# list2 = list1.split('-')
# print(list2)
#
# # 列表转字符串
# a = ['orange', 'juice']
# list1 = '_'.join(a)
# print(list1)


l = ['关羽', '张飞', '赵云', '张飞']
print(l.index('关羽'))
print(l.index('张飞'))
# print(l.index('张飞1')) # ValueError: '张飞1' is not in list

print(l.count('张飞'))

print('*' * 26)

a = [1, 2, 3]
a.append(4)
print(a)

# a.insert(a, '2')
# print(a)

# a = ['a', 'b', 'c']
# print(a)
# a.insert(2, 'd')
# print(a)
#
# b = ['1', '2', '3']
# a.extend(b)
# print(a)

arrange = ['张明', 'xiali', '小刘']
arrange.append('小美')
print(arrange)
arrange1 = ['董事长','皮民1', '皮民2']
arrange1.insert(arrange1.index('董事长') + 1, '董事长儿子')
print(arrange1)

class1 = ['张三班级']
class2 = ['李四班级']
class1.extend(class2)
print(class1)

arrange1.reverse()
print(arrange1)

# sort()排序 -> utf unicode 编码排序
# 1 -> 2 -> ... -> 5
# 中文 -> 排在20000之后
# 中文：1. 部首 你 们 他 2. 笔画数等
# 希望按照中文拼音... 导包 pinyin
arrange1.sort()
print(arrange1)

a = [4, 5, 3, 9, 2]
print(a)

# 升序
a.sort()
print(a)

# 降序
a.sort(reverse=True)
print(a)

del a[0]
print(a)

# 传参，删除指定索引项
a.pop(0)
print(a)

# 不传参默认删除最后一项，并可以返回该值
del_content = a.pop()
print(del_content )
print(a)

employee = ['张三', '李四', '王五', '李四']
# 删除下标是1 的李四
del employee[1]
print(employee)

print(f'出差调离的是:{employee[2]}')

employee.remove('李四')
print(employee)

list1 = ['安琪拉', '妲己', '小乔', '西施']
# i 此时代表对应的内容
for i in list1:
    print(i)

# i 此时代表索引下标
for i in range(len(list1)):
    print(list1[i])

sum = 0
grade_list = [80, 50, 30]
for i in grade_list:
    sum += i
print(f'平均分为{sum/len(grade_list):.2f}')

price_list = [500, 100, 5000, 2000]
price_list2 = []
for i in price_list:
    if i > 100:
        price_list2.append(i)

print(price_list2)

for i in range(len(price_list2)):
    print(i, price_list2[i])

i = 0
while True:
    if i >= len(price_list2):
        break
    print(i, price_list2[i])
    i += 1

heros = [
    ['关羽0', '亚瑟0', '吕布0'],
    ['关羽1', '亚瑟1', '吕布1'],
    ['关羽2', '亚瑟2', '吕布2']
]
for i in range(len(heros)):
    for j in range(len(heros[i])):
        print(heros[i][j], end='\t')
    print()

orange_list = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
orange_list.sort()
new_list = []
for i in range(len(orange_list)):
    if i > 0 and orange_list[i] == orange_list[i - 1]:
        continue
    new_list.append(orange_list[i])
print(new_list)

max_num = [7, 8, 9, 5, 6, 7, 2, 3]
record_max = max_num[0]
for i in range(len(max_num)):
    record_max = max(record_max, max_num[i])
    max_num[i] = record_max
print(max_num)