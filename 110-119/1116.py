from bs4 import BeautifulSoup
import sys

# 初始化一个空字符串来存储 HTML 内容
html_s = ""

try:
    # 从标准输入逐行读取内容
    for line in iter(sys.stdin.readline, ''):
        html_s += line
except KeyboardInterrupt:
    pass

# 使用 BeautifulSoup 解析 HTML 内容
#soup = BeautifulSoup(html_s, 'html.parser')
soup = BeautifulSoup(html_s, 'html.parser', from_encoding='utf-8', features='lxml', exclude_encodings=['utf-8'], replace_entities=False, parse_only=None, builder=None, formatter=None)
# 打印格式化后的 HTML 内容
print(soup.prettify())



"""
# 理论可运行,但不能正确读取
html_s = ""
stopword = ''
try:
    for line in iter(input, stopword):
        html_s += line + ''
        for line in iter(input, stopword):
            html_s += line + ''
            for line in iter(input, stopword):
                html_s += line + ''
                for line in iter(input, stopword):
                    html_s += line + ''
except KeyboardInterrupt:
    pass
soup = BeautifulSoup(html_s, 'html.parser')
print(soup.prettify())
"""
"""
# 运行-样例输入
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""