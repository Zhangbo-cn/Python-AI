'''
服务器端：
    1. 导包
    2. 实例化服务器端套接字
    3. 绑定端口，以元组的形式，ip要加双引号，端口为数字
    4. 监听 (队列 最大等待数)
    5. 创建服务器端接收对象，获取客户端地址，socket.accept()
    6. 接收数据，转二进制
    7. 关闭当前 服务器端接收对象的资源

'''
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 25565))

server_socket.listen(10)

print('服务器已启动，快连接……')

socket_accept, client_adress = server_socket.accept()

read = socket_accept.recv(1024).decode()
print(f'服务器端：{read}')

socket_accept.close()
