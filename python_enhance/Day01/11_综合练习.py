'''
你正在开发一个植物生长跟踪系统，需要实现一个植物类，能够模拟植物生长过程和受到的照料:
根据提供的属性与方法，请实现以下功能：

属性
- growth_days - 生长天数
- growth_state - 生长状态（种子、发芽、幼苗、开花、结果）
- care_methods - 添加的养料列表

方法
- grow() - 植物生长
  用户根据意愿设定生长天数
  判断天数在哪个区间，修改生长状态

- add_care() - 添加养料
  记录添加的养料, 将用户添加的养料存储起来

- 显示对象信息
  显示总生长天数，当前生长状态，已经添加了哪些养料

状态转换规则
- 0-7天：种子
- 7-14天：发芽
- 14-30天：幼苗
- 30-60天：开花
- 60天以上：结果
'''

class Plant:
    def __init__(self, growth_days=0, growth_state='种子'):
        self.growth_days = growth_days
        self.growth_state = growth_state
        self.care_methods = []

    def grow(self, growth_days):
        self.growth_days += growth_days
        if self.growth_days < 0:
            print(f'非法数字，请重新输入')
        else:
            if self.growth_days < 7:
                self.growth_state = '种子'
            elif self.growth_days < 14:
                self.growth_state = '发芽'
            elif self.growth_days < 30:
                self.growth_state = '幼苗'
            elif self.growth_days < 60:
                self.growth_state = '开花'
            elif self.growth_days >= 60:
                self.growth_state = '结果'
        return self.growth_state

    def add_care(self, nutrients):
        for care in self.care_methods:
            if care == nutrients:
                break
        self.care_methods.append(nutrients)

    def __str__(self):
        return (f'总生长天数: {self.growth_days}\n'
               f'生长状态: {self.growth_state}\n'
               f'养料用了:{self.care_methods}\n')

if __name__ == '__main__':
    plant_a = Plant()

    plant_a.grow(15)
    plant_a.add_care('化肥')
    print(plant_a)