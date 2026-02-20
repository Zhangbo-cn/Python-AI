import threading
import time


def work():
    for i in range(10):
        print(f'正在执行子线程：{i}')
        time.sleep(0.2)


if __name__ == '__main__':
    # 1. 开启守护线程 - 传参：daemon=True
    # t1 = threading.Thread(target=work, daemon=True)

    # 2. 语法 (属性 or 方法) 标记删除线 -> 过时了,可以用，但未来某一天可能会删除掉
    # t1 = threading.Thread(target=work)
    # t1.setDaemon(True)

    # 3. t1.damon = True
    t1 = threading.Thread(target=work)
    t1.daemon = True

    # 默认：主线程等待子线程执行完毕之后结束
    t1.start()
    time.sleep(1)
    print(f'主线程执行结束')