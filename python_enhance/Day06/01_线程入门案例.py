'''
开启多线程可以帮助我们同时执行多个任务
'''
import threading
import time


# 小明敲代码
def coding(name, num):
    for i in range(num):
        print(f'{name} 正在写第{i}代码')
    time.sleep(0.1)


def music(name, count):
    for i in range(count):
        print(f'{name}正在听第{i}音乐')
    time.sleep(0.1)


if __name__ == '__main__':
    # main 内默认有一个主线程
    # 创建多个子线程
    t1 = threading.Thread(target=coding, args=('小明', 10))
    t2 = threading.Thread(target=music, kwargs={'name': '小红', 'count': 15})

    t1.start()
    t2.start()
