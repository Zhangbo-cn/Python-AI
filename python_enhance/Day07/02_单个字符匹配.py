import re

# 1. 匹配普通字符, 就是按照自己本身的含义进行查找
text1 = '我是张张，今年27岁，身高175cm，aabccdjjb\nbaabcc'

one_char = re.findall(r'\.com', text1)
print(one_char)

one_char = re.findall(r'，', text1)
print(one_char)

one_char = re.findall(r'27', text1)
print(one_char)
print(len(one_char))
#

# 2. 匹配任意1个字符（除了换行符）.
char1 = re.findall(r'.b', text1)
print(char1)

# 3. 匹配真正的 . 邮箱 test163@qq.com
email = 'test163@qq.com'
char1 = re.findall(r'.com', email)
print(char1)

# 4. 或者 |, 匹配所有的语气词: 啊 哎 哇 哦  嘎 呀 呢

text = '匹配所有的语气词: 啊 哎 哇 哦  嘎 呀 呢'
one_char = re.findall(r'啊|哎|哇|哦|嘎|呀|呢',text)
print(one_char) # ['啊', '哎', '哇', '哦', '嘎', '呀', '呢']

one_char = re.findall(r'啊|哎|哇|哦|嘎|呀|呢',text)
two_char = re.sub(r'啊|哎|哇|哦|嘎|呀|呢', '🐂',text)
print(two_char) # 匹配所有的语气词: 🐂 🐂 🐂 🐂  🐂 🐂 🐂

