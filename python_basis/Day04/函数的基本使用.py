
def greet():
    '''
    描述：打招呼
    :return: None
    '''
    print('hello world')

greet()


def greet1(name):
    '''
    描述：打招呼
    :return:None
    '''
    print(f'hello, {name}')

greet1('张三')

def twoSum(a, b):
    c = a + b
    return c

res = twoSum(150, 220)
print(res)
