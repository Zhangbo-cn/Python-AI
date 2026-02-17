'''

定义一个参数为不定长（可变）类型的函数fun，同时传入一个列表和字典，
求列表里的数字元素和字典里的value值它们的累积结果例如：列表[1,2,3]，字典{‘a’: 4,‘b’: 5, ‘c’: 6},
定义一个函数fun，输出它们的累积结果（1+2+3+4+5+6）

'''

def fun():
    list1 = [1,2,3]
    dict1 = {'a':4,'b':5,'c':6}
    ans = 0

    for i in list1:
        ans += i

    for i in dict1:
        ans += dict1[i]
    return ans

res = fun()
print(res)
