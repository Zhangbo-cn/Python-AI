import os
# 重命名
# os.rename('data/2.txt', 'data/3.txt')

# os.remove('data/3.txt')

# os.mkdir('data/aa')

# 获取当前工作目录 -> 相对路径参考的项目目录
# print(os.getcwd())

# 更改当前工作目录
# os.chdir('../day05')

# 查看当前子目录
# print(os.listdir())

# 删除目录：仅能删除空目录
# os.rmdir('data/aa')

# 删除多个层级的目录
# import shutil
# 递归思想 -> 全部干掉 -> 慎用
# shutil.rmtree('data/aa')

