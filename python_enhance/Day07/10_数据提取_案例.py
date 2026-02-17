import re
import requests

# 假设的章节页面 URL
chapter_url = 'https://example-novel-site.com/chapter/1'

response = requests.get(chapter_url)
html_content = response.text

# 2. 提取信息
# 提取章节标题：匹配<h1> 标签内的内容
tittle_pattern = r'<h1>(.*?)</h1>'
# 提取章节内容：匹配<div class='content'> 标签内的所有内容（包括换行）
content_pattern = r'<div class="content">(.*?)</div>'

title_match = re.search(tittle_pattern, html_content, re.IGNORECASE)
content_match = re.search(content_pattern, html_content, re.DOTALL) # re.DOTALL 让 . 也能匹配换行符

if title_match and content_match:
    title = title_match.group(1)
    content = content_match.group(1).strip() # 去除收尾空白
    print(f'标题： {title}')
    print('内容：')
    print(content)
else:
    print('未找到标题或内容')
