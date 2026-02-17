import os
print(os.getcwd()) # 当前的工作目录

# 需求：往 Day05（当前工作空间）/1.txt -> 写入 hello python
# 1. 打开文件 -> 指定文件操作模式（写 or 读）
f = open(r'E:\new_work\my_self\icode\python_basis\Day05\1.txt', 'w')

# 2. 进行读 or 写 的操作
f.write('hello1\n')
f.write('hello2\n')
# 3. 关闭文件
f.close()

f1 = open('../Day04/2.txt', 'w')

f1.write('hello')
f1.close()
