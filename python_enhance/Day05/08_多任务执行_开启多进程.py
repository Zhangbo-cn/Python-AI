'''
实现方法：
1. 导入进程工具包 -- import multiprocessing
2. 通过[进程类] 实例化进程对象：
    子进程对象 = multiprocessing.Process()
        实现细节：multiprocessing.Process(group=None, target=None, name=None, args=None, kwargs=None)
            group: ？
            target: 子进程要执行的函数
            name: 子进程的名字，便于标识和调试
            args: 以元组的形式传递多个数据
            kwargs: 以字典{(k:v),...,(k:v)}的形式传递多个参数
3. 启动进程执行任务 -- 子进程对象.start()

案例需求：使用多进程模拟一边写代码，一边听音乐
'''
import time

def coding():
    for i in range(10):
        print(f'正在写第{i}代码')
        time.sleep(0.5)

def music():
    for i in range(10):
        print(f'正在听第{i}音乐')
        time.sleep(0.5)

# 1. 导入进程工具包 -- import multiprocessing
import multiprocessing

# 2. 通过[进程类] 实例化进程对象：
# multiprocessing.Process 创建了两个子进程 帮助我们执行任务
# 默认只有一个主进程 main
process_1 = multiprocessing.Process(target=coding)
process_2 = multiprocessing.Process(target=music)

# 注："if __name__ == '__main__':" 不能省略：因为需要 main 主进程开启子进程
if __name__ == '__main__': # 启动进程执行任务 -- 子进程对象.start()
    # 主进程执行下面内容
    # 3. 启动进程执行任务 -- 子进程对象.start()
    # 期待：两个子进程 交替 执行任务
    # 为什么没有交替执行：CPU执行效率太快了
    process_1.start()
    process_2.start()