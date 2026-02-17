# a = int(input("输入梯形的上底： "))
# b = int(input("输入梯形的下底： "))
# c = int(input("输入梯形的高： "))
import random

# s = (a + b) * c / 2
# print(s)

# total_friends = int(input("输入朋友数："))
# total_bill = int(input("输入总账单数：")) * 1.2
# print(total_bill / total_friends)

# chocolates = int(input("输入巧克力总数："))
# children = int(input("输入儿童数量："))
# avg = chocolates / children
# rest = chocolates % children
# print(f'每个儿童可分配{avg:.0f}个巧克力，余下{rest}个')

# # 输入身高、体重，求BMI=体重/身高^2
# height = float(input("请输入身高（米制，保留两位小数）："))
# weight = float(input("请输入体重（Kg，保留两位小鼠）"))
# # 体重的分类标准（国际通用）：
# p1_BMI = weight / (height ** 2)
# if p1_BMI < 18.5:
#     print(f"p1_BMI为{p1_BMI:.1f},BMI小于18.5，体重过轻，注意增肥")
# elif p1_BMI >= 18.5 and p1_BMI < 24.9:
#     print(f"p1_BMI为{p1_BMI:.1f},介于正常范围[18.5,24.9]，很健康")
# elif p1_BMI > 25 and p1_BMI < 29.9:
#     print(f"p1_BMI为{p1_BMI:.1f},介于超重范围[25.0,29.9]，超重")
# elif p1_BMI >= 30.0:
#     print(f"p1_BMI为{p1_BMI:.1f},介于肥胖范围[30.0，？]，注意节食")

# limit_speed = float(input("现行速度为："))
# print(f"现行速度为{limit_speed:.2f}，{limit_speed > 60 and limit_speed < 120}")

# model_height = int(input("输入模特身高："))
# model_weight = int(input("输入模特体重："))
# print(f"模特身高{model_height}cm,体重为{model_weight}斤，{model_height > 170 and model_weight < 110}")

# balance = int(input("请输入余额："))
# age = int(input("请输入年龄："))
# print(f'相亲条件起码要余额10万元，或者年纪小于28岁，{balance < 10 or age < 28}')

# password = input("请输入密码：")
# # if password == "":
# #     print(f'密码为空，请重新输入')
#
# # 0 '' -> / 其他 是True
# if not password:
#     print('密码不能为空')

# pocket_money = float(input("我有零花钱："))
# if pocket_money > 100:
#     print('可以吃个大餐')
# else:
#     print('吃面吧')

# month = int(input('请输入月份：'))
# if month == 12 or month == 1 or month == 2:
#     print('冬季')
# elif 3 <= month <= 5:
#     print('春季')
# elif 6 <= month <= 8:
#     print('夏季')
# elif 9 <= month <= 11:
#     print('秋季')
# else:
#     print('请输入1~12之间的月数')

# pocket_money = float(input('请输入您的零花钱：'))
# if pocket_money >= 10000:
#     print('海南3日游')
# elif pocket_money > 1000:
#     print('迪士尼爽玩1天')
# elif pocket_money > 100:
#     print('吃泡面')
# else:
#     print('家里蹲')


# alcohol_content = float(input('酒精含量为：'))
# if alcohol_content < 20:
#     print('不构成酒驾')
# else:
#     if alcohol_content > 80:
#         print('醉驾')
#     else:
#         print('酒驾')

# profession = input('请输入您的职业：')
# combat_power = int(input('请输入您的战力值：'))
# if profession == 'mage':
#     if combat_power >= 100:
#         print('火球')
#     elif combat_power >= 50:
#         print('冰冻雨水')
#     else:
#         print('闪电剑')
# elif profession == 'warrior':
#     if combat_power >= 100:
#         print('大力神手')
#     elif combat_power >= 50:
#         print('中泰')
#     else:
#         print('暴雨梨花')

# import random
#
# while True:
#     a = random.randint(1, 3)
#     people_count = int(input('1，2,3分别表示石头，剪刀，布：'))
#     if a == 1:
#         if people_count == 1:
#             print('都是石头，重新开始')
#             continue
#         elif people_count == 2:
#             print('机器石头，人出剪刀，电脑获胜')
#             break
#         elif people_count == 3:
#             print('人是布，机器是石头，人获胜')
#             break
#         else:
#             print('匹配错误，请重新输入')
#             continue
#     elif a == 2:
#         if people_count == 2:
#             print('都是剪刀，重新开始')
#             continue
#         elif people_count == 1:
#             print('人是石头，机器是剪刀')
#             break
#         elif people_count == 3:
#             print('人是布，机器是剪刀，机器获胜')
#             break
#         else:
#             print('输入错误，请重新输入')
#             continue
#     else:
#         if people_count == 3:
#             print('都是布，重新开始')
#             continue
#         elif people_count == 2:
#             print('人是剪刀，电脑出布，人获胜')
#             break
#         elif people_count == 1:
#             print('人是石头，电脑是布，电脑获胜')
#             break
#         else:
#             print('匹配错误，请重新输入')
#             continue

# player = int(input('输入手势：（1：石头、 2：剪刀、3：布）:'))
# computer = random.randint(1, 3)
# print(f'player:{player}, computer:{computer}')
# if player == computer:
#     print('平局')
# elif ((player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1)):
#     print('人获胜')
# else:
#     print('电脑获胜')

# name1 = '''I am Tom, Nice to meet you!'''
# print(name1)
# print(type(name1))
#
# print('-' * 20)
#
# name2 = """I am Jennify,
#            Nice to meet you!"""
# print(name2)
# print(type(name2))

# str = "I`m Tom"
# print(str)
# str1 = 'I\'m Tom'
# print(str1)

# a, b = 10, 3
# result = a ** b + a // b - a % b
# print(result)  # 输出结果是什么？

# x = 5
# x **= 2
# x += 1
# print(x)

# x = 5
# x += 3
# x *= 2
# x -= 4
# print(x)  # 输出结果是什么？

# a, b, c = 7, 5, 7
# print(a == c and a > b)  # 输出结果是什么？
# print(a != b or b > c)   # 输出结果是什么？

# x, y, z = True, False, True
# result = not (x and y) or z
# print(result)  # 输出结果是什么？

a = 7
b = 3
c = a > b and a % b == 1
print(c)

username = 'admin'
password = '123456'

i = 0
while i < 3:
    user = input('输入用户名：')
    pwd = input('输入密码：')
    if username == user and pwd == password:
        print('恭喜你，登录成功！')
        break
    else:
        print(f'账户密码错误，请重新输入，还有{3 - i}次机会')
    i += 1

ans = 0
for i in range(50, 101):
    ans += i
print(ans)

res = 0
for i in range(1, 101):
    if i % 5 == 0:
        continue
    else:
        res += i
print(res)

res = 0
cnt = 0
for i in range(1, 100):
    if i % 7 == 0:
        cnt += 1

    if cnt == 3:
        break
    else:
        res += i
print(res)