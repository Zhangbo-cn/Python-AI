'''
1. 外层函数 Game，内部变量 coin投币数量
2. 内层函数 add, 对投币数量进行添加
3. 内部函数 play，对投币数量进行减少
4. 返回[add, play] 调用测试

'''

def Game():
    coin = 50

    def add():
        nonlocal coin
        coin += 10
        print(f'剩余硬币数量：{coin}')

    def play():
        nonlocal coin
        coin -= 5
        print(f'剩余硬币数量：{coin}')

    # return [add, play]
    return add, play

# res = Game()
# res[0]()
# res[1]()

add, play = Game()
add()
add()
add()
add()
play()
play()


