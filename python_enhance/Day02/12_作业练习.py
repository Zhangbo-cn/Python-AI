'''
（1）请写出单继承与多继承的语法格式?

'''


class Animal:

    def __init__(self):
        self.name = '动物'

    def eat(self):
        print('吃吃吃')


# Dog 类继承自 Animal
class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = '狗'

    # 重写方法
    def eat(self):
        super().eat()


# MiniDog 类继承自 Dog
class MiniDog(Dog):
    def __init__(self):
        super().__init__()
        self.name = '小型狗'

    # 重写方法
    def eat(self):
        super().eat()


if __name__ == '__main__':
    dog = Dog()
    print(dog.name)
    dog.eat()
    mini_dog = MiniDog()
    print(mini_dog.name)
    mini_dog.eat()
    print(MiniDog.__mro__)

'''
- 1.创建一个Person 人类基类，其中有一个 sayHi方法，输出`大家好....`；
- 2.创建一个Student 学生类继承于人类，Student类中不仅有 sayHi方法, 还有 study 方法；
- 2.1 sayHi方法 输出 `大家好....`
- 2.2 study方法 输出 `我是学生, 我会学习...` (扩展方法)
'''


class Person:

    def sayHi(self):
        print('大家好....')


class Student(Person):

    def sayHi(self):
        super().sayHi()

    def study(self):
        print('我是学生, 我会学习...')


if __name__ == '__main__':
    student = Student()
    student.sayHi()
    student.study()
    print(Student.__mro__)

'''
- 1. 创建一个Animal类，然后创建Dog类继承Animal类。
- 2. Animal类中, 有name和age属性, 有speak方法
- 3. Dog子类中,有color属性, 有jump方法, 对speak方法进行完全重写

'''


class Animal:

    def __init__(self):
        self.name = '动物'
        self.age = 1

    def speak(self):
        print('动物叫')


class Dog(Animal):

    def __init__(self, color, name, age):
        self.color = color
        self.name = name
        self.age = age

    def jump(self):
        print('狗跳起来')

    def speak(self):
        print('汪汪汪')


if __name__ == '__main__':
    dog = Dog('黑色', '旺财', 2)
    print(dog.name)
    print(dog.age)
    print(dog.color)
    dog.speak()
    dog.jump()

'''
- 1. 创建一个Hero英雄类，然后创建Fighter战士类, 继承Hero类。
- 2. Hero类中, 有health体力值, move位移方法, attack攻击方法
- 3. Fighter子类中,有anger怒气值, 对attack攻击方法进行扩展性重写, 保留原本的攻击, 并添加判断逻辑
-    每次攻击一次, 增加50怒气
-    如果怒气值 >= 100, 则额外释放: 致命一击!
'''


class Hero:

    def __init__(self):
        self.health = 100

    def move(self):
        print('移动')

    def attack(self):
        print('攻击')


class Fighter(Hero):

    def __init__(self):
        super().__init__()
        self.anger = 0

    def attack(self):
        super().attack()
        self.anger += 50
        if self.anger >= 100:
            print('致命一击!')


if __name__ == '__main__':
    fighter = Fighter()
    fighter.attack()
    fighter.attack()

'''
银行账户BankAccount类
私有属性:
	- holder 投保人
	- balance 累计保费
	- min_years 最低持有年限
	
方法:
	- get_holder 获取投保人
	- get_balance 获取累计保费
	- add_balance 添加保费
	- get_minyears 获取最低持有年限
	- set_minyears 修改最低持有年限

'''


class BankAccount:

    def __init__(self, holder, balance, min_years):
        self.__holder = holder
        self.__balance = balance
        self.__min_years = min_years

    def get_holder(self):
        return self.__holder

    def get_balance(self):
        return self.__balance

    def add_balance(self, amount):
        self.__balance += amount

    def get_minyears(self):
        return self.__min_years

    def set_minyears(self, years):
        self.__min_years = years


if __name__ == '__main__':
    ac = BankAccount('小王', 1000, 5)
    print(ac.get_holder())
    print(ac.get_balance())

'''
- 1. 创建一个Prentice学徒类, 有姓名, 有年纪
- 2. 向跑步专家 Runner 类学习, 习得run方法: 百米9.5秒
- 3. 向游泳专家 Swimmer 类学习, 习得swim方法: 百米50秒
- 4. 向做饭专家 Cooker 类学习, 习得cook方法: 烹饪厨艺大成

'''


class Runner:

    def run(self):
        print('百米9.5秒')


class Swimmer:

    def swim(self):
        print('百米50秒')


class Cooker:

    def cook(self):
        print('烹饪厨艺大成')


class Prentice(Runner, Swimmer, Cooker):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        super().run()
        print(Runner.run.__doc__)

    def swim(self):
        super().swim()
        print(Swimmer.swim.__doc__)

    def cook(self):
        super().cook()
        print(Cooker.cook.__doc__)

    def __str__(self):
        return '学徒: %s, 年龄: %d' % (self.name, self.age)


if __name__ == '__main__':
    p = Prentice('小王', 18)
    p.run()
    p.swim()
    p.cook()
    print(Prentice.__mro__)

'''
多态函数: 汽车启动
	定义汽车父类, 油车子类, 电车子类
	分别定义方法 start 启动, 并在子类中重写
	定义多态方法 press 实现无论传入的电车还是油车, 都能启动
	
'''

# 定义汽车父类
class Car:
    def start(self):
        print("子类必须实现 start 方法")


# 定义油车子类
class GasCar(Car):
    def start(self):
        print("汽油车启动：发动机点火，燃油燃烧！")


# 定义电车子类
class ElectricCar(Car):
    def start(self):
        print("电动车启动：电机通电，安静出发！")


# 多态函数：无论传入的是油车还是电车，都能启动
def press(car: Car):
    car.start()


# 测试
if __name__ == '__main__':
    gas_car = GasCar()
    electric_car = ElectricCar()

    press(gas_car)       # 输出: 汽油车启动：发动机点火，燃油燃烧！
    press(electric_car)  # 输出: 电动车启动：电机通电，安静出发！