# f = open('data/test.txt', 'w')
# content = "Hello, Python File IO!"
#
# f.write(content)
#
# f.close()
#
# f = open('data/test.txt', 'r')
#
# print(f.read())
#
# f.close()

# f = open('data/config.txt','r')
#
# print(f.readline().strip())
# print(f.readline().strip())
#
# f.close()

# a.png 图片(自己准备),  生成一个新的 b.png
# f1 = open('data/a.png', 'rb')
# f2 = open('data/b.png', 'wb')
#
# while True:
#     f = f1.read(1024)
#     if len(f) == 0:
#         break
#     f2.write(f)
#
# f1.close()
# f2.close()

try:
    f = open('data/aa/bb/cc', 'r')

    f.read()

    f.close()
except Exception as e:
    print(e)