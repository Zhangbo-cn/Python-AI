import re
import requests

# 1. 获取数据
url = 'https://httpbin.org/'
response = requests.get(url)
# print(response.text)
html_content = response.text

# 2. 提取信息：使用正则表达式匹配所有链接
# 解释模式：匹配'href="……"' 中引号内的内容
# (.*?)是一个非常贪婪匹配组，匹配任何字符，直到遇到下一个'"'
link_pattern = r'href="(.*?)"'

links = re.findall(link_pattern, html_content)

# 3. 打印结果
# print('找到的链接：')
# for link in links:
#     print(link)
