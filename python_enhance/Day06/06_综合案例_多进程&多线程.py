import multiprocessing
import threading
import time


def big_work1():
    print('[big_work1] 开始视频高清解码……')
    time.sleep(10)
    print('[big_work1] 视频高清解码完成~~')


def big_work2():
    print('[big_work2] 开始文件处理任务……')
    time.sleep(5)
    print('[big_work2] 文件处理任务完成~~')


def big_work3():
    print('[big_work3] 开始音频解析任务……')

    # 开启多个子线程 -> 执行小任务
    t1 = threading.Thread(target=small_task1_for_work3)
    t2 = threading.Thread(target=small_task2_for_work3)
    t3 = threading.Thread(target=small_task3_for_work3)

    t_list = [t1, t2, t3]
    for t in t_list:
        t.start()
    # 开启任务
    # t1.start()
    # t2.start()
    # t3.start()

    # 需求：等待所有的子线程结束之后，再取执行自己(主线程)的任务
    for t in t_list:
        t.join()
    print('[big_work3] 大任务三执行完成~~')

def small_task1_for_work3():
    print(f'小任务 开始读取文件1……')
    time.sleep(1)
    print(f'小任务 读取文件1完成~~')

def small_task2_for_work3():
    print(f'小任务 读取文件2……')
    time.sleep(2)
    print(f'小任务 读取文件2完成~~')

def small_task3_for_work3():
    print(f'小任务 读取文件3……')
    time.sleep(3)
    print(f'小任务 读取文件3完成~~')


if __name__ == '__main__':
    print('[主进程] 开始任务……')
    start_time = time.time()

    # 创建多个子进程 - 同时执行任务
    big_work1_process = multiprocessing.Process(target=big_work1)
    big_work2_process = multiprocessing.Process(target=big_work2)
    big_work3_process = multiprocessing.Process(target=big_work3)
    works_list = [big_work1_process, big_work2_process, big_work3_process]

    # 启动进程
    # big_work1_process.start()
    # big_work2_process.start()
    # big_work3_process.start()
    for work in works_list:
        work.start()

    # 预期目标：主进程等待子进程执行结束之后，再去执行自己(主进程)的任务
    # 进程.join()
    # 线程.join()
    # join() 确保主进程在所有的子进程执行完毕之后，再继续执行自己(主进程)的任务
    # 建议：列表管理 + join等待 =》 多进程的标准
    # big_work1_process.join()
    # big_work2_process.join()
    # big_work3_process.join()

    for work in works_list:
        work.join()

    # 任务执行完毕之后继续执行主进程的任务
    end_time = time.time()
    print(f'[主进程] 所有任务完成，总耗时: {end_time - start_time}')
