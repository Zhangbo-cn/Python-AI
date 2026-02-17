'''
捕获异常

try:
    尝试执行的代码（可能出错）

except:
    程序出错 -> 执行

esle:
    程序正常运行

finally:
    程序无论失败 or 成功，都会输出结果

'''

try:
    age = int(input('请输入您的年龄：'))
    print(age)
except Exception as e:
    print('程序运行失败', e)
else:
    print('try 内部代码执行成功')

finally:
    pass # pass不会执行，占位
    # print('无论成功还是失败，都会执行！')


import random

random_num = random.randint(1, 100)

while True:
    try:
        num = int(input('请输入是哪个数字：'))
        if num > random_num:
            print('猜大了')
        elif num < random_num:
            print('猜小了')
        else:
            print('恭喜你猜对了')
            break
    except Exception as e:
        pass
        # print('请输入正确数字格式', e)
