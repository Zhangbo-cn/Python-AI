'''
需求：定义 地瓜 类，包含以下属性和方法

    属性：
        被烤时间：cook_time
        被烤状态：cook_status
        添加调料：condiments

    方法：
        添加的调料（用户可以按照自己的意愿添加调料）

'''
class Sweetpotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_status = '生的'
        self.condiments = []

    def cook(self, time):
        self.cook_time += time
        if self.cook_time < 0:
            print(f'{self.cook_time} 是不合法的数字，请重新录入')
        else:
            if self.cook_time < 3:
                self.cook_status = '生的'
            elif self.cook_time < 7:
                self.cook_status = '半生不熟'
            elif self.cook_time < 12:
                self.cook_status = '熟了'
            elif self.cook_time > 12:
                self.cook_status = '糊了'
        return self.cook_status

    def add(self, condiment):
        self.condiments.append(condiment)

    def __str__(self):
        return f'地瓜被烤了{self.cook_time}分钟，状态是{self.cook_status}, 可选调料有{self.condiments}'


if __name__ == '__main__':
    digua = Sweetpotato()
    digua.cook(5)

    print(digua)

#
# class Sweetpotato:
#     def __init__(self):
#         self.cook_time = 0
#         self.cook_status = '生的'
#         self.condiments = []
#
#     def cook(self, time):
#         self.cook_time += time
#         if self.cook_time < 0:
#             print(f'数据{self.cook_time}是不合法的数字，请重新输入')
#         else:
#             if self.cook_time < 3:
#                 self.cook_status = '生的'
#             elif self.cook_time < 7:
#                 self.cook_status = '半生不熟'
#             elif self.cook_time < 12:
#                 self.cook_status = '熟了'
#             else:
#                 self.cook_status = '糊了'
#
#         return self.cook_status
#
#     def add_sause(self, condiments):
#         self.condiments.append(condiments)
#
#     def __str__(self):
#         return f'地瓜烤了 {self.cook_time}分钟, 状态是 {self.cook_status}, 可选调料有{self.condiments}'
#
# if __name__ == '__main__':
#     sweet_potato = Sweetpotato()
#
#     sweet_potato.cook(10)
#
#     sweet_potato.add_sause('孜然')
#
#     print(sweet_potato)


