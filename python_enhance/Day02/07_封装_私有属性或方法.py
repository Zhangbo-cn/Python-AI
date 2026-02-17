'''
封装：将数据 和 方法 存放到类中

私有属性和方法 -> 针对于隐私的数据或者函数进行不对外暴露的体现
    -属性名
    -方法名
    只能在类的内部访问，外部访问不了的

'''
class BankAccount:
    def __init__(self):
        # _ 单下划线            -> 公共属性
        # __属性__ 前后 双下划线  -> 公共属性

        # 私有： __属性 不能在类外部访问
        self.bank_name = '中国工商银行'
        self.__balance = 10000

    def save_money(self, money):
        self.__balance += money

    def withdraw_money(self, money):
        self.__balance -= money

    def __query_balance(self):
        print(f'{self.bank_name}余额为：{self.__balance}')

# 用户 在银行相关信息 -> 暴漏在外 / 不安全 -> 上锁

bank = BankAccount()
bank.save_money(5000)
bank.withdraw_money(1000)
# bank.query_balance() # 私有方法：无法在类的外部访问

print(bank.bank_name)
# print(bank.__balance) # 私有属性：无法在类的外部访问
