'''
python 中继承：将别的类中的属性和方法 拿来用

一切类 直接或间接继承自object 一切皆对象 object就是最顶层对象
'''

class Father(object):
    def __init__(self):
        self.gender = '男'

    def walk(self):
        print('散步 锻炼身体')

# 第1个儿子 敲代码
class Son1(Father):
    def coding(self):
        print('敲代码')

# 第2个儿子 玩手机
class Son2(Father):
    def play_mobile(self):
        print('玩手机')


s1 = Son1()
print(s1.gender)
s1.coding()


s2 = Son2()
s2.play_mobile()
