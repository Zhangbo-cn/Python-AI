f = open('3.txt', 'r', encoding='utf-8')
print(f.readline(), end='')
print(f.readline(), end='')

# print(f.readlines())

f.close()

print(f)