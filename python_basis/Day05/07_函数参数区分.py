# 0. 不加参数
def printme():
    print(0)

printme()

# 1. 必须参数：函数体内有用到形参，则该形参称为必须参数？
def printme(str):
    "打印任何传入的字符串"
    print(str)


# 调用 printme 函数，不加参数会报错
printme('123')
# printme() # TypeError: printme() missing 1 required positional argument: 'str'
