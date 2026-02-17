'''

接收用户输入的账号和密码，
如果账号为'admin'，密码为'admin888'，则提示用户登录成功，
其他情况则提示用户名或密码输入错误，只有3次输入机会

'''

# 定义账号、密码
username = 'admin'
password = 'admin888'

# 计数器，给三次机会
cnt = 0

while True:
    # 输入账号、密码 用于验证
    user1 = input('请输入账号：')
    pwd1 = input('请输入密码：')

    if user1 == username and pwd1 == password:
        print(f'欢迎进入XXX，{user1}')
    else:
        if cnt < 2:
            cnt += 1
            print(f'对不起，你的账户或密码错误，你还有{3 - cnt}次机会')
        else:
            print(f'你的输入次数过多，请下个工作日尝试')
            break