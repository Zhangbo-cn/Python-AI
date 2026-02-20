'''
多线程特点：
    4. 线程之间的执行是无序的(因为线程的执行，主要由cpu调度决定——高效切换、
                        cpu调度哪个线程，哪个线程就先执行——抢占式调度，谁抢到谁执行)
    5. 主线程会等待所有的子线程结束再结束
    6. 线程之间共享全局变量
    7. 线程之间共享全局变量 数据量较大时出现错误问题 -- 解决：互斥锁

# 问题：大数据量时，预期值错误问题
# 解决方法：
# 1. 创建互斥锁 mutex = threading.Lock()
# 2. 在函数外面 上锁 mutex.acquire()
# 3. 释放锁 mutex.release()
# 注意：1. 确保只有一把锁(真正互斥)； 2. 必须在合适的时机释放锁 (阻塞)
# 两把锁分别锁两个线程，无效！
    原因：锁的本质 - 协调工具
         锁不是“魔法屏障”，它只是一个信号量/标记，用来告诉其他线程：“我正在用这个资源，你别碰！”
         如果线程 A 用锁 L1，线程 B 也用锁 L1 → 它们能互相等待、互斥。
         如果线程 A 用锁 L1，线程 B 用锁 L2 → 它们根本不知道对方的存在 → 无法互斥！
'''
import threading

num = 0

# 问题：大数据量时，预期值错误问题
# 解决方法：
# 1. 创建互斥锁 mutex = threading.Lock()
mutex = threading.Lock()
# mutex2 = threading.Lock()


# 2. 在函数外面 上锁 mutex.acquire()
# 3. 释放锁 mutex.release()

def work1():
    # 上锁
    mutex.acquire()
    global num
    for i in range(1000000):
        num += 1
    print(f'work1线程中num的值为: {num}')
    # 释放锁 -> 其他线程可以进行操作了
    mutex.release()


def work2():
    mutex.acquire()
    # mutex2.acquire()  # 两把不同的锁 没有锁的意义
    global num
    for i in range(1000000):
        num += 1
    print(f'work2线程中num的值为: {num}')
    mutex.release()
    # mutex2.release()


if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)
    t1.start()
    t2.start()

'''
# 数据量较大时，预期值错误
work1线程中num的值为: 1878592
work2线程中num的值为: 2000000
'''
