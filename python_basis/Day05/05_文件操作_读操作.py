# f = open('2.txt', 'w', encoding='utf-8')
# f.write('这是2.txt')
#
# f.close()

# f = open('2.txt', 'r', encoding='utf-8')
# # 如果不指定长度，读取所有的
# # c1 = f.read()
# # print(c1)
#
# c3 = f.readline()
# print(c3)
#
# # 指定要读取的字符长度 n，接续上面的读取
# n = 5
# c2 = f.read(n)
# print(c2)
#
# f.close()


# 每次读3个字符，直到读取完毕

f = open('2.txt', 'r', encoding= 'utf-8')
while True:

    char = f.read(3)
    if not char:
        break
    print(char)

f.close()



