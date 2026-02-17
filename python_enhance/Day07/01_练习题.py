import re

text='今年18岁，体重62kg，身高175cm'

char1 = re.findall(r'\d',text)
print(char1) # ['1', '8', '6', '2', '1', '7', '5']
char1 = re.findall(r'\d\d',text)
print(char1) # ['18', '62', '17']
char1 = re.findall(r'\d+',text)
print(char1) # ['18', '62', '175']

char1 = re.search(r'\d',text)
print(char1) # <re.Match object; span=(2, 3), match='1'>

char1 = re.match(r'\d',text)
print(char1) # None

char1 = re.findall(r'[^18，kg]', text)
print(char1) # ['今', '年', '岁', '体', '重', '6', '2', '身', '高', '7', '5', 'c', 'm']
