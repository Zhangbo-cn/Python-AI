'''
下载文件回调: 请改造以下基础代码, 完成回调自定义处理
- 自定义过程进度提示:  拼命加载中.... 当前进度 20%  40% ......
- 自定义下载完成提示:  恭喜下载完成,  正在为您自动安装...
'''
import time


def download_file(url, loading=None, loaded=None):
    # 模拟文件下载

    # 模拟下载进度
    print(f'开始下载{url}')
    for i in range(0, 101, 20):
        # print(f'下载进度...{i}%')
        # if loading:
        #     loading(i)
        loading and loading(i)
        time.sleep(0.5)
    # 下载完成
    if loaded:
        loaded()


def loading(percentage):
    print(f'下载的进度……{percentage}%')


def loaded():
    print('下载完成')


# 难点-> 如何捕获下载完成 / 下载中的提示信息 -> 外部定义的函数中输出
download_file('http://www.baidu.com/ok.pdf', loading, loaded)
# download_file('http://www.baidu.com/ok.pdf')
