import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 10022))
print('服务器连接成功')

# 读取本地的文件，将读取到的内容 - 发送给服务器
with open('123.png', 'rb') as src_f:
    while True:
        byts = src_f.read(1024)
        if len(byts) == 0:
            break
        client_socket.send(byts)
        data = client_socket.recv(1024)
        print(f'客户端：已经收到服务器端的反馈{data.decode()}')