import re

"""
^ 匹配开头  $ 匹配结尾
    当 ^ 和 $ 组合使用时, 此时为严格匹配, 必须连数量都匹配, 不允许有任何额外内容
    r'^hello$' => 只能匹配 hello
"""

text1 = '11hello python hello python'
result1 = re.search('hello', text1)
print(bool(result1))
result1 = re.search('^11hello', text1)
print(bool(result1))

result1 = re.search('^hello$', text1)
print(result1)
print(bool(result1))


text2 = 'ahello python hello python'
result2 = re.search(r'hello$', text2) # False
result2 = re.search(r'python$', text2) #  True
print(bool(result2))

# 用户输入验证: (手机号, 验证码, 银行卡, 密码, 邮箱, ...  => 都是严格匹配 ^..$)
# 验证手机号: 1开头, 第二位3-9, 后面9位数字
my_phone_num = r'^1[3-9][0-9]{9}$'
bool1 = bool(re.search(my_phone_num, '12345678911'))
bool2 = bool(re.search(my_phone_num, '123456'))
bool3 = bool(re.search(my_phone_num, '13345124078'))
print(bool1)
print(bool2)
print(bool3)

# 验证用户名:  4-20个字符, 只能包含字母和数字
username = r'^[a-zA-Z0-9]{4,20}$'
bool1 = bool(re.search(username, 'nuiashd4'))
bool2 = bool(re.search(username, '12345678911'))
bool3 = bool(re.search(username, '1245hisahd'))
print(bool1)
print(bool2)
print(bool3)

print('*' * 26)


# 验证字符串: 是否是以字母开头, 数字结尾
str1 = r'^[a-zA-Z].*[0-9]$'
bool1 = bool(re.search(str1, 'nuiashd4'))
bool2 = bool(re.search(str1, '12345678911'))
print(bool1)
print(bool2)

