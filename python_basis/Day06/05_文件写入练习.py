'''
1. 把数据源文件内容反转后, 写入目的地文件中
数据源文件 a.txt:[

                好好学习,
                天天向上.
                abc123!@#
                ]
'''

# src_f1 = open('data/a.txt', 'r', encoding='utf-8')
# src_f2 = open('data/b.txt', 'w', encoding='utf-8')
#
# while True:
#     # strip() 去除字符串首尾空格，空白字符 包括 \n 等
#     line = src_f1.readline().strip()
#     if not line:
#         break
#     line = line[::-1]
#     # print(line)
#     src_f2.write(line + '\n')
#     # src_f2.flush()  # 强制将缓冲区内容写入文件
#
# src_f1.close()
# src_f2.close()

# with (open('./data/a.txt', 'r', encoding='utf-8') as src_f,
#      open('./data/b.txt', 'w', encoding='utf-8') as dst_f):
#     for line in src_f:  # 更简洁的写法
#         line = line.strip()
#         if not line:
#             continue
#         reversed_line = line[::-1]
#         print(reversed_line)
#         dst_f.write(reversed_line + '\n')


with (open('data/1.txt', 'r', encoding='utf-8') as src_f1,
      open('data/2.txt', 'w', encoding='utf-8') as src_f2):
    while True:
        line = src_f1.readline().strip()
        if len(line) == 0:
            break
        src_f2.write(line[::-1])

