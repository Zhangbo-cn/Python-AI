import threading, time

# 定义全局变量
my_list = []

def write_data():
    for i in range(10):
        my_list.append(i)
        # print(f'写入数据：{i}')
        time.sleep(0.2)
    print(f'write子线程 数据列表：{my_list}')

def read_data():
    time.sleep(3)
    print(f'read子线程 数据列表：{my_list}')

if __name__ == '__main__':

    write_thread = threading.Thread(target=write_data)
    read_thread = threading.Thread(target=read_data)
    write_thread.start()
    read_thread.start()
