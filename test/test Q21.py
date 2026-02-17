'''

定义一个字符串，
如:str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"。

编写一个程序，使用随机数从字符串中抽取4个字符，用于生成验证码

'''

import random

str1 = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

num1 = random.randint(0,len(str1))
num2 = random.randint(0,len(str1))
num3 = random.randint(0,len(str1))
num4 = random.randint(0,len(str1))

list1 = [str1[num1],str1[num2],str1[num3],str1[num4]]
testcode = str(list1)

print(testcode)

