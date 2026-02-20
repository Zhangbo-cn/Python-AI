'''
请使用多任务形式完成：一边吃水果、一边听音乐、一边跟同事聊天。要求如下：
    1. 使用多进程完成；
    2. 使用多线程完成；
'''
import multiprocessing
import threading

mutex = threading.Lock()
def eating_fruit():
    mutex.acquire()
    print(f'吃水果')
    for i in range(10000000):
        pass
    print(f'吃水果结束')
    # mutex.release()

def listening_music():
    mutex.acquire()
    print(f'听音乐')
    mutex.release()

def talking_with_colleague():
    mutex.acquire()
    print(f'跟同事聊天')
    # mutex.release()

# 多线程练习
if __name__ == '__main__':

    # 创建线程
    '''
    控制台输出结果：资源输出错乱，共享数据导致 -> 加锁
    吃水果
    听音乐跟同事聊天
    '''
    t1 = threading.Thread(target=eating_fruit)
    t2 = threading.Thread(target=listening_music)
    t3 = threading.Thread(target=talking_with_colleague)
    t_list = [t1, t2, t3]
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()


# 多进程练习
# if __name__ == '__main__':
#     print('多任务执行开始')
#     p1 = multiprocessing.Process(target=eating_fruit)
#     p2 = multiprocessing.Process(target=listening_music)
#     p3 = multiprocessing.Process(target=talking_with_colleague)
#     p_list = [p1, p2, p3]
#
#     for p in p_list:
#         p.start()
#
#     for p in p_list:
#         p.join()
#
#     print('多任务执行结束')