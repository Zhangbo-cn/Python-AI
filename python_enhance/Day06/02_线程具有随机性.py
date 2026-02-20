'''
多线程特点：
    4. 线程之间的执行是无序的(因为线程的执行，主要由cpu调度决定——高效切换、
                        cpu调度哪个线程，哪个线程就先执行——抢占式调度，谁抢到谁执行)
    5. 主线程会等待所有的子线程结束再结束
    6. 线程之间共享全局变量
    7. 线程之间共享全局变量数据出现错误问题 -- 解决：互斥锁

需求：
    1. 定义多线程的目标函数，打印当前线程名字
    2. 主线程中遍历创建10个线程，观察其运行效果
'''
import threading
import time


def print_thread_name():
    time.sleep(0.1)
    current_thread = threading.current_thread() # 获取当前线程对象
    print(f'当前线程名字：{current_thread.name}')


if __name__ == '__main__':

    for i in range(10):
        t = threading.Thread(target=print_thread_name)
        t.start()
