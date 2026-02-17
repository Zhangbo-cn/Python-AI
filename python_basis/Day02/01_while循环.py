# # while循环入门案例：使用while循环，循环输出5遍“Hello World”
# i = 0
# while i < 5:
#     print(f'Hello World {i}')
#     i += 1
#
# print('结束')


# print('*' * 26)
#
# # 案例1：使用while循环求1..100的和
# cnt = 1
# ans = 0
# while cnt <= 100:
#     ans += cnt
#     cnt += 1
# print(ans)

# 案例2：求1~100之间，所有偶数的和
# i = 1
# ans = 0
# while i <= 100:
#     if i % 2 == 0:
#         ans += i
#     i += 1
# print(ans)

# coins = 10
# while coins > 0:
#     print(f'投币啦，剩余{coins} 个币')
#     coins -= 1
# print('穷光蛋')
#
# i = 1
# mul = 1
# while i < 11:
#     mul *= i
#     i +=1
#
# print(mul)

# i = 1
# while i < 5:
#     if i == 3:
#         print(f'吃了第{i}个包子')
#         continue
#     i += 1

# import random
# num = random.randint(1, 100)
#
# while True:
#     guess = int(input('Guess a number between 1 and 100: '))
#     if guess == num:
#         print(f'恭喜你猜对了，是{num}')
#         break
#     elif guess > num:
#         print('Guess lower')
#     else:
#         print('Guess upper')

# s = 'apple'
# cnt = 0
# for i in s:
#     if i == 'a':
#         cnt += 1
#     print(i)
# print(cnt)

# sum1 = 0
# for i in range(100):
#     if i % 2 == 0:
#         sum1 += i
# print(sum1)

# sum = 0
# for i in range(0, 101, 2):
#     sum += i
# print(sum)

# sum = 0
# for i in range(10, 30):
#     if i % 7 != 0:
#         sum += i
# print(sum)

# password = '123'
# i = 1
# while i <= 3:
#     print(f'第{i}次输入密码')
#     s = input('请输入三位数密码：')
#     if s == password:
#         print(f'恭喜你登录成功，在第{i}次输入密码正确')
#         break
#     else:
#         print(f'密码错误，请重新输入，你还有{3 - i}次机会')
#     i += 1

# 1. 设定账号和密码
# username = 'admin'
# password = '123456'
# for i in range(3):
#     # 2. 获取用户输入的用户名和密码
#     uname = input('请输入用户名：')
#     pwd = input('请输入密码：')
#     # 3. 判断输入是否正确
#     if uname == username and pwd == password:
#         print(f'欢迎光临，{uname}')
#         break
#     else:
#         # 嵌套
#         if i == 2:
#             print('输入错误，账号密码已锁定，请联系管理员')
#         else:
#             print(f'录入有误，剩下{2 - i}次机会')

# s = 'HelloPython'
# for char in s:
#     if char == ' ':
#         print('发现空格，循环已退出')
#         break
# else:
#     print('执行到这里说明循环正常执行，这段字符串没有空格')

digits = '45678910'
for char in digits:
    if int(char) > 9:
        print('发现大于9的字符，返回')
        break
else:
    print('没有大于9的字符')

