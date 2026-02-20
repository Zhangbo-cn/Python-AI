'''
实现方法：
1. 导入进程工具包 -- import multiprocessing
2. 通过[进程类] 实例化进程对象：
    子进程对象 = multiprocessing.Process()
        实现细节：multiprocessing.Process(group=None, target=None, name=None, args=None, kwargs=None)
            group: ？还在规划设计
            target: 子进程要执行的函数
            name: 子进程的名字，便于标识和调试
            args: 接收所有的位置参数 -- 以元组的形式传递多个数据
            kwargs: 接收所有的关键字参数 -- 以字典{(k:v),...,(k:v)}的形式传递多个参数
3. 启动进程执行任务 -- 子进程对象.start()

案例需求：使用多进程模拟一边写代码，一边听音乐
案例需求：使用多进程模拟 [小明] 一边写 num 行代码，一边听 count 音乐
'''
import os
import time

def coding(name, num):
    # 获取子进程 PID
    print(f'[PID:{os.getpid()}] {name} 开始写代码')
    # print(f'[PID:{multiprocessing.current_process().pid}] {name} 开始写代码')
    # 获取父进程 PID (ppid p parent p process)
    print(f'小明处的父进程 [PID:{os.getppid()}] ')
    for i in range(1, num + 1):
        print(f'{name} 正在写第{i}代码')
        time.sleep(0.5)

def music(name, count):
    print(f'[PID:{os.getpid()}] {name} 开始听音乐')
    # print(f'[PID:{multiprocessing.current_process().pid}] {name} 开始开始听音乐')

    for i in range(1, count + 1):
        print(f'{name}正在听第{i}音乐')
        time.sleep(0.5)

# 1. 导入进程工具包 -- import multiprocessing
import multiprocessing

# 2. 通过[进程类] 实例化进程对象：
# multiprocessing.Process 创建了两个子进程 帮助我们执行任务
# 默认只有一个主进程 main
process_1 = multiprocessing.Process(name='小明',target=coding, args=('小明', 10))
process_2 = multiprocessing.Process(name='小红',target=music, kwargs={'name': '小王', 'count': 15})
# print(process_1.name)
# print(process_2.name)

# 注："if __name__ == '__main__':" 不能省略：因为需要 main 主进程开启子进程
if __name__ == '__main__': # 启动进程执行任务 -- 子进程对象.start()
    # 打印主进程ID
    print(f'main主进程 [PID:{os.getpid()}]')
    print(f'main主进程的父进程 [PID:{os.getppid()}]')
    # print(f'主进程 [PID:{multiprocessing.current_process().pid}]')

    # 主进程执行下面内容
    # 3. 启动进程执行任务 -- 子进程对象.start()
    # 期待：两个子进程 交替 执行任务
    # 为什么没有交替执行：CPU执行效率太快了
    process_1.start()
    process_2.start()