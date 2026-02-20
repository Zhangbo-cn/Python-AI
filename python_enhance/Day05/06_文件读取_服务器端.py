'''
服务器端:
打开文件 - 写入 - 内容来自客户端
'''
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 10022))
server_socket.listen(10)
print('服务器启动成功……')

accept_socket, client_address = server_socket.accept()
count = 0
while True:
    count += 1
    try:
        with open('data/123.png', 'wb') as dest_f:
            while True:
                byts = accept_socket.recv(1024)
                if len(byts) == 0:
                    break
                # 将读取到的内容写入到本地
                dest_f.write(byts)
                # print('服务器端: 已经收到客户端的内容')
                accept_socket.send('服务器已收到内容'.encode('utf-8'))
    except:
        pass