class Communication:
    def __init__(self, name):
        self.name = name

    def send_message(self):
        print(f'Comm {self.name}正在发送消息')

    def recieve_message(self):
        print(f'Comm {self.name}正在接收消息')

class Letter(Communication):
    def __init__(self, name):
        self.name = name

    def send_message(self):
        print(f'Le {self.name}正在发送邮件')

    def recieve_message(self):
        print(f'Le {self.name}正在接收邮件')

if __name__ == '__main__':
    # comm = Communication()

    le = Letter('le')
    le.send_message()
    le.recieve_message()


