'''
需求：定义有发表评论的功能函数，需要先检查用户登录和输入验证码

'''

def check_login(fn_name):
    def inner():
        print('校验用户是否登录……')
        fn_name()
        # return comment()
    return inner

def check_code(fn_name):
    def inner():
        print('校验验证码……')
        print('登录成功')
        fn_name()
        # return comment()
    return inner

# 装饰器执行 -> 子上而下顺序执行

@check_login
@check_code
def comment():
    print('发表评论')
    # return 1

# print(comment())

# 多个函数调用，入栈和出栈 -> FILO
# comment = check_code(comment) # 为什么这个位置的comment 对象地址不会被下面的给覆盖住？
# comment = check_login(comment)
# comment()
'''
check_code 接收原始comment函数
       ↓
返回一个新的 inner 函数（这个inner内部引用了原始comment）
       ↓
comment ──→ check_code的inner函数
                │
                └──→ 原始comment函数（被闭包保存，不会丢失）
'''