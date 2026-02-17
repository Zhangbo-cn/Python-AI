
d = {}
d1 = dict()

print(type(d))
print(type(d1))

d2 = {
    'name':'Iphone',
    'price':7899,
    '原价':8999,
}
print(d2)
print(d2['price'])

print(d2.get('age'))
print(d2.get('name'))

print(d2.keys())
print(d2.values())
print(d2.items()) # k,v 列表嵌套元祖，[(), ()]

print(type(d2.keys())) # 字典视图 对象一种 具备遍历、可迭代能力

