
'''
### 学习目标
- 理解break和continue关键词的作用。
- 能够在循环中正确使用break和continue。
break：代表终止整个循环结构
continue：代表中止当前本次循环，继续下一次循环
'''
'''
场景一：如果吃的过程中，吃完第三个吃饱了，则不需要再吃第4个和第5个苹果，
即是吃苹果的动作停止，这里就是break控制循环流程，即终止此循环。
'''
# 演示break
i = 1
while i <= 5:
    if i > 3:
        print("我已经吃过三个苹果了，吃饱了，不吃了")
        break
    else:
        print(f"炫第{i}个苹果")
        i += 1
        # print(f"这是第{i}个苹果")

'''
场景二：如果吃的过程中，吃到第三个吃出一个大虫子...,
是不是这个苹果就不吃了，开始吃第四个苹果，这里就是continue控制循环流程，
即退出当前一次循环继而执行下一次循环代码。
'''
# 演示continue
i = 1
while i <= 5:
    print(f"开始炫第{i}个苹果")
    if i == 3:
        print(f"第{i}个苹果里面有虫子，换下一个炫")
        i += 1
        # continue
    i += 1

'''
#### 案例需求
编写一个Python程序，随机生成一个1到100之间的整数，用户通过输入猜测的数字，程序会根据用户的输入提示“猜大了”、“猜小了”或“猜对了”。用户可以无限次猜测，直到猜对为止。猜对后，程序会提示用户并结束游戏。
#### 实现思路
① 编写一个循环，满足条件后停止。
② 要从1 ~ 100之间选择一个随机数 
③ if分支判断
'''
# import random
#
# random_num = random.randint(1, 50)
# print(random_num)
#
# while True:
#     guess_num = int(input('请输出您要猜测的数字：'))
#     if guess_num == random_num:
#         print('恭喜你，猜对了')
#         break
#     elif guess_num > random_num:
#         print('猜测大了')
#     else:
#         print('猜测小了')

# 需求: 在指定位置处填写代码, 使得完成指定需求

# i = 1
# while i <= 10:
#     if i % 3 == 0: # 3 6 9
#         # 在这里填写代码, 使得循环分别输出2次, 7次, 13次Hello World
#         # pass
#         j = i
#         while j > 0:
#             print(f'hello world{j}')
#             j -= 1
#     # print(f'hello world {i}')
#     i += 1

'''
### 综合案例：使用for循环实现用户名+密码认证-作业
案例：用for循环实现用户登录
① 输入用户名和密码
② 判断用户名和密码是否正确（username='admin'，password='admin888'） 
③ 登录仅有三次机会，超过3次会报错 

分析：用户登陆情况有3种:
① 用户名错误(此时便无需判断密码是否正确)  -- 登陆失败 
② 用户名正确 密码错误 --登陆失败 
③ 用户名正确 密码正确 --登陆成功
'''
# 定义变量，记录尝试次数
trycount = 3

# 输入用户名和密码
username = input('请输入用户名：')
password = input('请输入密码：')

# 循环执行，判断是否有误
for i in range(3):
    if username == 'admin':
        if password == 'admin888':
            print('恭喜你，登录成功！')
            break
        else:
            print(f'您输入的密码有误，还有{3 - trycount}次数，请重新输入：')
            trycount += 1
    else:
        print(f'您输入的账号有误，还有{3 - trycount}次数，请重新输入：')


