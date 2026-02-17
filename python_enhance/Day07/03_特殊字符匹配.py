import re
text = 'Aa\nab0啊啊啊 388699_!@\t123'

# 1. \d 匹配所有数字 [0-9]
char1 = re.findall(r'\d', text)
char2 = re.findall(r'[0-9]', text)
char3 = re.findall(r'[0,9]', text)
print(char1)
print(char2)
print(char3)

# 2. \D 匹配所有非数字 除了0-9, 其他都要
char1 = re.findall(r'\D', text)
print(char1)

# 3. \w 匹配字符, 数字, 下划线, 汉字
char1 = re.findall(r'\w', text)
print(char1)

# 4. \W 特殊字符
char1 = re.findall(r'\W', text)
print(char1)

# 5. \s 匹配空白字符  \n \t 空格
char1 = re.findall(r'\s', text)
print(char1)

# 6. \S 匹配非空白字符
char1 = re.findall(r'\S', text)
print(char1)
