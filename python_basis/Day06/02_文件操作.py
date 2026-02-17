# 1. 打开文件，指定模式 r w a
# 如果是文本格式，需要指定编码格式

# f = open('data/1.txt', 'a', encoding='utf-8')
#
# # 2. 文件操作
# f.write('你好\n')
#
# # 3. 关闭文件
# f.close()

# 文件读取
f = open('data/1.txt', 'r', encoding='utf-8')

s = f.read(3)
print(s)

f.close()


text = '你好呀' # 3个字符
# 转成 utf-8 字节
text_byte = text.encode() # encode：将 字符 转为 字节
print(text_byte)
print(len(text_byte))

# 字节 转为 字符
print(text_byte.decode())
print(len(text_byte.decode()))

