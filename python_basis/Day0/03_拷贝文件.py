# 拷贝 cat1.jpg -> cat2.jpg 文件
# 1. 打开 cat1.jpg -> 读 -> 需指定字节进行读取 rb

src_f1 = open('data/cat1.png', 'rb')

# 2. 打开 cat2.jpg -> 写 -> 指定字节进行写入 wb -> 自动创建
src_f2 = open('data/cat2.png', 'wb')

# 3. while True 按照一定的长度循环读取
while True:

    read_byte = src_f1.read(1024)
    if len(read_byte) == 0:
        break
    # 4. 将读取的二进制数据 -> 写入 cat2 文件中
    src_f2.write(read_byte)

src_f1.close()
src_f2.close()

# 字节的形式
# 1. 打开并读取 1.txt
text_f1 = open('data/1.txt', 'rb')
# 2. 创建并写入 2.txt
text_f2 = open('data/2.txt', 'wb')

while True:
    text_byte = text_f1.read(1024)
    if len(text_byte) == 0:
        break
    text_f2.write(text_byte)

text_f1.close()
text_f2.close()