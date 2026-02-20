'''
基于文件中歌词，创建生成器，根据传入的每批次的歌词条数 (8行)，生成歌词批次
每批次的歌词条数 8条

'''
import math


def dataloaderMusic(batch_size):
    # 每批次的歌词条数 8条
    with open('jaychou_lyrics.txt', 'r', encoding='utf-8') as src_f:
        data_lines = src_f.readlines()
        # total_lines = [line.strip() for line in total_lines]
        # print(f'数据集：{total_lines}')

        # 计算批次数量 -> 每次8条
        total_batch = math.ceil(len(data_lines) / batch_size)
        # print(f'数据批次数量: {total_batch}')

        # yield -> 暂停代码 -> 将结果返回给调用者
        # for 循环 获得每个批次的数据 -> 创建生成器 -> 返回
        # total_batch range(728) -> 0~727
        for i in range(total_batch):
            #       i   歌词行数    下标    每次暂停返回的歌词行数
            # 第一次 0   [1, 8]    [0,7]   yield data_lines[0:8]
            # 第二次 1   [9, 16]   [8,15]  yield data_lines[8:16]
            # 第三次 2   [17, 24]  [16,23] yield data_lines[16:24]
            yield data_lines[batch_size * i: batch_size * (i + 1)]


res = dataloaderMusic(8)
print(next(res))
print(next(res))
print(next(res))
