'''
主程序
- 大任务1:
  - 对视频进行解码处理 - 4s
- 大任务2:
  - 对大数据进行处理, 处理1G的数据集 (利用多线程, 并发读取多个数据分区)
    - 小任务1: 读取处理前一半 0.5G的数据集  - 耗时1.5s
    - 小任务2: 读取处理后一半 0.5G的数据集  - 耗时2s
  - 都读取完成, 进行CPUT密集操作,  数据聚合计算, 耗时 3秒
  - 最后打印  "大数据数据处理完成"

- 大任务3:
  - 机器学习加载多个数据批次 (利用多线程, 并发加载)
    - 小任务1: 加载训练批次1批 - 耗时1s
    - 小任务2: 加载训练批次2批 - 耗时1s
  - 都读取完成, 进行 CPU 密集型操作, 模型训练 - 耗时5s
  - 最后打印  "机器学习训练完成"

请实现此多线程和多进程架构, 并最后计算整体执行时间
'''
import multiprocessing
import threading
import time

mutex = threading.Lock()


def big_task1():
    print('大任务1：对视频进行解码处理……')
    time.sleep(4)


def big_task2():
    print('大任务2：对大数据进行处理, 处理1G的数据集')

    '''
    - 小任务1: 读取处理前一半 0.5G的数据集  - 耗时1.5s
    - 小任务2: 读取处理后一半 0.5G的数据集  - 耗时2s
    '''
    # 创建线程
    t1 = threading.Thread(target=small_task1_read)
    t2 = threading.Thread(target=small_task2_read)
    t_list = [t1, t2]
    for t in t_list:
        t.start()

    for t in t_list:
        t.join()

    print('大任务2 都读取完成, 进行CPUT密集操作, 数据聚合计算')
    time.sleep(3)
    print('大任务2：大数据数据处理完成')


def small_task1_read():
    mutex.acquire()
    print(f'小任务1: 读取文件前一半 0.5G的数据集……')
    time.sleep(1.5)
    print('小任务1: 读取文件前一半完成')
    mutex.release()


def small_task2_read():
    mutex.acquire()
    print(f'小任务2: 读取文件后一半 0.5G的数据集……')
    time.sleep(2)
    print('小任务2: 读取文件后一半完成')
    mutex.release()


def big_task3():
    print('大任务3：机器学习加载多个数据批次 (利用多线程, 并发加载)')
    # 多线程 并发执行
    t1 = threading.Thread(target=small_task1_training)
    t2 = threading.Thread(target=small_task2_training)
    t_list = [t1, t2]
    for t in t_list:
        t.start()
    for t in t_list:
        t.join()
    print('大任务3：都读取完成, 进行 CPU 密集型操作, 模型训练')
    time.sleep(5)
    print('大任务3：机器学习训练完成')


def small_task1_training():
    print(f'小任务1: 加载训练批次1批……')
    time.sleep(1)


def small_task2_training():
    print(f'小任务2: 加载训练批次2批……')
    time.sleep(1)


if __name__ == '__main__':
    print('多任务开始执行')
    start_time = time.time()

    # 定义多进程
    big_task1_process = multiprocessing.Process(target=big_task1)
    big_task2_process = multiprocessing.Process(target=big_task2)
    big_task3_process = multiprocessing.Process(target=big_task3)
    pro_list = [big_task1_process, big_task2_process, big_task3_process]
    for pro in pro_list:
        pro.start()

    for pro in pro_list:
        pro.join()

    end_time = time.time()
    print(f'多任务执行完毕，总耗时：{end_time - start_time}')
