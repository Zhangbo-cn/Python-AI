stu_dict = {
    'name': '张三',
    'age': '王阳明',
    'city': '北京'
}

# 获取所有的健：
for i in stu_dict.keys():
    print(i)
# 默认遍历健，通上
# for i in stu_dict:
#     print(i)

# 获取值
for i in stu_dict.values():
    print(i)

# 获取对应的k,v
for i in stu_dict:
    print(i, stu_dict[i])

for kv in stu_dict.items():
    print(kv)

for k, v in stu_dict.items():
    print(k, v)

