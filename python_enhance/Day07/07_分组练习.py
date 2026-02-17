"""
分组:
    (ab) 将括号中字符作为一个分组
        从左往右数, 第几个左小括号(,  就表示几组
    result.group()  result.group(0)  获取所有匹配到的数据
    result.group(1) 获取匹配到第1组数据,  以左小括号为依据, 数数字
    ....

需求:
    匹配出 163, 126, qq 邮箱
    规则: 4~20位数字, 字母, 下划线  +  @标记    +   邮箱域名  +   .com 或 .cn
    例子: 99abc@163.com   aaabbbCCC@qq.cn
"""

import re

email = r'^([a-zA-Z0-9_]{4,20})@(163|126|qq)\.(com|cn)$'

email1 = re.match(email, 'huisdiuabf@163.com')
if email1:
    print('邮箱符合规则：', email1.group())
    print('邮箱符合规则：', email1.group(0))
    print('邮箱符合规则：', email1.group(1))
    print('邮箱符合规则：', email1.group(2))
    print('邮箱符合规则：', email1.group(3))
else:
    print('邮箱格式错误')
