import re

text = 'a ab abb abbb ababbbb'

# ab? => a ab   b可以出现 0次 或 1次
char1 = re.findall(r'ab?', text)
print(char1)

# ab+ => ab abb abbb abbbb  b可以出现1次或多次
char1 = re.findall(r'ab+', text)
print(char1)

# ab* => a ab abb abbb abbbb b可以出现0次或多次
char1 = re.findall(r'ab*', text)
print(char1)

# (ab)+ => ab abab ababab ...  匹配 ab 出现1次或多次
char1 = re.findall(r'(ab)+', text)
print(char1)

text2 = '大家好, 我叫渣渣辉, 我今年18岁, 我考了100分, 我体重150斤, 我余额40000, 工资3000, 我老婆余额800000000'

print(re.findall(r'\d+', text2))

print(re.findall(r'\d{5}', text2))

print(re.findall(r'\d{3,5}', text2))

print(re.findall(r'\d{3,}', text2))
