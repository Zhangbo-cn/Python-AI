'''
1. 进程之间不共享全局变量
    子进程相当于父进程的副本(把父进程的内容会拷贝一份， 单独执行)
    图解：……(描述：三个进程分别操作的都是自己进程的全局变量my_list, 不会对其他进程的全局变量产生影响，
            所以进程之间不共享全局变量，只不过进程之间的全局变量名字相同而已，但是操作的不是同一个进程里面的全局变量

            主进程: my_list = []
            子进程1: my_list = []
            子进程2: my_list = []
            )
    案例：定义一个列表，1个进程添加数据，另一个进程查看数据，看是否能看到数据变化

2. 主进程等待所有子进程执行结束再结束
'''
import multiprocessing
import time

# 公共的数据 -> 所有进程都可以拿来使用 -> 相互不影响
my_list = []  # 创建一个列表, 属于主进程


# 写入数据
def write_data():
    for i in range(10):
        my_list.append(i)
        print(f'写入数据：{i}')
    print(f'write子进程 数据列表：{my_list}')


# 读取数据
def read_data():
    time.sleep(3)
    print(f'read子进程 数据列表：{my_list}')


if __name__ == '__main__':
    # my_list = [] # 属于主进程

    # 创建子进程
    write_process = multiprocessing.Process(target=write_data)
    read_process = multiprocessing.Process(target=read_data)

    # 启动进程
    write_process.start()
    read_process.start()

    # 主进程的输出内容
    print(f'main主进程 数据列表：{my_list}')
