'''
案例：服务器端先给客户端发送消息，客户端收到消息，回复消息
服务端开发流程：
1. 创建socket对象
2. 绑定ip地址和端口 (元祖的形式)
3. 设置最大队列监听数
4. 等待客户端连接（阻塞）
5. 给客户端发消息
6. 接收客户端消息
7. 关闭连接，释放资源 (关闭的是与客户端进行连接的服务器端的对象，关闭的是张三的，李四的不受影响)

'''
import socket
# 1. 创建socket对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 设置端口号复用（快速重启服务器，主动释放端口号）
server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
# 2. 绑定ip地址和端口
# 127.0.0.1 -> 自己 -> localhost
# 局域网下的ip
# 0.0.0.0 监听本机上的所有ip地址
# 包括127.0.0.1 还有有线网卡 192.168.74., 无线网卡
# server_socket.bind(('127.0.0.1', 10012))
server_socket.bind(('0.0.0.0', 10012))
while True:
    try:
        # 3. 设置最大队列监听数
        server_socket.listen(10)
        print('服务器已启动，等待客户端连接...')
        # 4. 等待客户端连接（阻塞）
        # accept_socket -> 与客户端通信的socket对象 (自己)
        # client_adress -> 客户端地址，与当前服务器端的客户端ip地址（对方）
        accept_socket, client_adress = server_socket.accept()
        print(f'客户端已连接，来自客户端的ip地址为：{client_adress}, {accept_socket}')
        # 5. 给客户端发消息
        accept_socket.send('hello, this is server'.encode('utf-8'))
        # 6. 接收客户端消息
        data = accept_socket.recv(1024)
        print(f'来自于客户端返回的消息: {data.decode()}')
        # 7. 关闭连接，释放资源
        accept_socket.close()
    except:
        pass
