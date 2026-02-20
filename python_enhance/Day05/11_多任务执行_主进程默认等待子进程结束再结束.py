'''
案例：创建一个子进程，执行完成需要2s,而主进程执行完成需要1s,观察结果
默认情况：
    主进程会等待子进程执行结束之后再结束
    预期：
        一旦主进程结束执行，子进程立刻结束
    实现方式：
        方式1：守护进程 -> 推荐
        方式2：强制关闭子进程
'''
import multiprocessing
import time


def work():
    for i in range(10):
        print(f'正在执行子进程：{i}')
        time.sleep(0.2)
    print('子进程执行完成')


if __name__ == '__main__':
    # 创建子进程
    process = multiprocessing.Process(target=work)

    # 设置process进程 为 守护进程
    process.daemon = True # 主进程结束，当前子进程立即结束 (推荐)

    # 启动子进程
    process.start()

    # 模拟主进程耗时 1s
    time.sleep(1)

    # 主动终止当前的子进程 -> 不推荐 僵尸进程 -> 交给python解释器管理自动回收(容易造成内存泄露，管理混乱)
    # process.terminate()

    print('主进程执行完成')
