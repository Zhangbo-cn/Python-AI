'''
多态: 同样的一个函数,在不同的场景下,表现出不同的状态 或 结果
    三个结果:
        1. 有继承(定义父类、定义子类，子类继承父类)
        2. 函数重写(子类重写父类的函数)
        3. 父类引用指向子类对象(子类对象传给父类对象调用者)

'''
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('汪汪汪')

class Cat(Animal):
    def speak(self):
        print('喵喵喵')


# 1. 没有继承也没关系 -> python 中伪多态，不严格
# 2. 函数重写 -> 如果不重写也没关系，不报错，只不过代码没意义
class Car:
    def speak(self):
        print('车在响')

# 3. 父类引用指向子类对象
# 实参：Cat() 形参 an
# an: Animal = Cat() -> 父类引用 指向 子类的对象 Cat() -> c
def make_noise(an: Animal):
    an.speak()


if __name__ == '__main__':
    dog = Dog()
    make_noise(dog)

    cat = Cat()
    make_noise(cat)

    car1 = Car()
    make_noise(car1)

