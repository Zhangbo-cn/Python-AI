import socket
# 创建客户端对象
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接服务器 -> 端口 和 ip
client_socket.connect(('127.0.0.1', 10012))
# 接收来自于服务器端的消息
data = client_socket.recv(1024)
print(f'来自服务器端的消息：{data.decode()}')

# 客户端 给 服务器端发消息
client_socket.send('hello, this is clent'.encode('utf-8'))
# 释放资源
client_socket.close()