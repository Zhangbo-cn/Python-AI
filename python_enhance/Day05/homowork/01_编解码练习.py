'''
将字符串“AI人工智能进阶班”转换为二进制bytes类型的结果；
将二进制bytes数据 b"AI python"转换为字符串str类型的结果。
'''
str1 = 'AI人工智能进阶班'
print(str1.encode())

print(b"AI python".decode())