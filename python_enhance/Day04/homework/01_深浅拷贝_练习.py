'''
自定义电视机设置: 改成对比度 80, 亮度85, 音量90,  然后能重置回默认配置
'''
import copy

default_config = {
    'contrast': 75, # 对比度
    'brightness': 75, # 亮度
    'volume': 30, # 音量
}
# 浅拷贝，仅复制第一层内容，内容可更改
current_config = copy.copy(default_config)
print(default_config)
print(f'浅拷贝: {current_config}')

default_config['contrast'] = 80
current_config['brightness'] = 85
current_config['volume'] = 90
print(f'浅拷贝内容更新: {current_config}')
print(default_config)

deep_copy_config = copy.deepcopy(default_config)
print(f'深拷贝：{deep_copy_config}')
deep_copy_config['contrast'] = 90
print(f'深拷贝内容更新：{deep_copy_config}')

print(id(default_config))
print(id(current_config))
print(id(deep_copy_config))


'''
游戏存档备份: 将游戏中的信息复制一份, 要保证互相没有关联
新增访问的城市 "天津" 看备份是否有影响
修改车车的价格, 看备份是否有影响
'''

current_game_state = {
    'name': '游遍天下大王君',
    'money': 20000000, # 存款
    'car': {
        'brand': '宝马',
        'price': 200000
    }, # 座驾
    'cities': ['上海', '北京', '南京'], # 已通关的城市
    'friends': ['刘阳', '马飞', '吴军'] # 好友
}

# 深拷贝：多层嵌套拷贝
player_info = copy.deepcopy(current_game_state)
print(f'当前游戏状态: {id(current_game_state)}')
print(f'玩家信息：{id(player_info)}')
print(f'玩家信息：{player_info}')

player_info['cities'].append('天津')
print(f'玩家 城市信息更新：{id(player_info)}')
print(f'玩家 城市信息更新：{player_info}')

player_info['car']['price'] = 300000
print(f'玩家 车子价格更新：{id(player_info)}')
print(f'玩家 车子价格更新：{player_info}')
print(f'当前游戏状态：{current_game_state}') # 不影响