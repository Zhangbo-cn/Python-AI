'''
四步走：
    1. 导包
    2. 实例化客户端对象
    3. 建立连接
    4. 发送数据，发之前编码转成二进制字节(接收数据，接之后将二进制内容进行解码)
    5. 关闭资源

'''
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 25565))

client_socket.send('欢迎来到我的世界!'.encode())

data = client_socket.recv(1024)
print(f'服务器端：{data.decode()}')
client_socket.close()
