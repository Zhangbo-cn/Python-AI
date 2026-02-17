'''
（1）定义一个手机类，能开机、能关机、可以拍照。

'''
# class Iphone:
#
#     def open(self):
#         print(f'开机功能')
#
#     def close(self):
#         print(f'关机功能')
#
#     def take_picture(self):
#         print(f'可以拍照')
#
#     # def __str__(self):
#     #     return f'手机功能'
#
# if __name__ == '__main__':
#     phone = Iphone()
#     phone.open()
#
#     print(phone)


'''
（2）定义一个电脑类，
并给电脑添加品牌、价格等属性，
同时电脑能用于编程、看视频。
'''
# class Computer:
#     def __init__(self, brand='联想', price=0):
#         self.brand = brand
#         self.price = price
#
#     def programming(self):
#         print(f'可以做编程')
#
#     def watch_video(self):
#         print(f'播放视频')
#
#     def __str__(self):
#         return f'电脑品牌是{self.brand}, 电脑价格为{self.price}元'
#
# if __name__ == '__main__':
#     c1 = Computer('mac', 18699)
#     c1.programming()
#     c1.watch_video()
#
#     print(c1)


'''
（3）尝试定义一个算法工程师类，同时使用`__init__()`初始化岗位名称、薪资金额等属性，
   工作内容是每天摸鱼打代码，同时使用`__str__()`展示对象所拥有的所有信息。
'''

# class AlgorithmEngineer:
#     def __init__(self, title, salary):
#         self.job_title = title
#         self.salary = salary
#
#     @property
#     def work_description(self):
#         return '每天摸鱼敲代码'
#
#     def work(self):
#         print(self.work_description)
#
#     def __str__(self):
#         return (f'该对象岗位是{self.job_title}\n'
#                 f'薪资为{self.salary}\n'
#                 f'工作内容是{self.work_description}')
#
# if __name__ == '__main__':
#     a1 = AlgorithmEngineer('算法工程师', 32000)
#     a1.work()
#     print(a1)


'''
类设计, 定义一个书本类 :
创建一个 Book 类，要求：
必需参数：title（书名）、author（作者）
默认参数：price（价格，默认为0）、is_available（是否可借，默认为True）
方法：display_info() 显示图书信息

'''

# class Book:
#     def __init__(self, title, author, price=0, is_available=True):
#         self.title = title
#         self.author = author
#         self.price = price
#         self.is_available = is_available
#
#     def display_info(self):
#         return (f'书名是：{self.title}\n'
#                 f'作者是：{self.author}\n'
#                 f'单价是：{self.price}\n'
#                 f'是否可借用：{"否" if self.is_available == False else "是"}\n')
#
# if __name__ == '__main__':
#     book = Book('活着', '余华', 59, False)
#     print(book.display_info())
#     # print(book)

