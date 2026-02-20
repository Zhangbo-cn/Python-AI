'''
socket 通信
1. 导包
2. 创建socket对象
    socket.socket(ipv4 or ipv6, 传输协议)
'''
import socket
socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(socket_obj)

# 通信双方 => 传递 -> 二进制

# 字符串 => 二进制 (自己 -> 服务器端)
data = '你好'
print(data.encode())
print(data.encode(encoding='utf-8'))
print(data.encode(encoding='gbk'))

# 纯英文 或 字符 -> 二进制 -> 前面添加 b
data1 = 'hello worldnsbud389y'
print(data1.encode())
print(b'hello worldnsbud389y')
print('hello worldnsbud389y'.encode())

# 二进制 => 字符串
print(data.encode(encoding='utf-8').decode(encoding='utf-8'))

# 编码：utf-8规则 / 解码 gbk规则 -> 编解码不一致 导致乱码
print(data.encode(encoding='utf-8').decode(encoding='gbk')) # 乱码：浣犲ソ