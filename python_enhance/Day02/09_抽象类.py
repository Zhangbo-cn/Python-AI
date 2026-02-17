'''
抽象类：(接口)
    抽象类是指包含 一个或者多个抽象方法的类

抽象方法：
    没有方法体的方法 方法体是由pass修饰的

'''
# 基类 / 父类：定标准
class AC:
    def cool_wind(self): # 抽象方法
        pass

    def heat_wind(self):
        pass

    def lr_swing(self):
        pass

# 子类：格力
class Gree(AC):
    def cool_wind(self):
        print('Gree 冷风')

    def heat_wind(self):
        print('Gree 热风')

    def lr_swing(self):
        print('Gree 左右摆风')

if __name__ == '__main__':
    gree = Gree()
    gree.cool_wind()
    gree.heat_wind()
    gree.lr_swing()