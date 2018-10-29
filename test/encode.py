#coding=utf-8
from bs4 import BeautifulSoup
import re, sys

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
    <a href="http://example.com/中文" class="sister" id="link4">娜娜</a>
</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
print type(soup)
print soup.original_encoding

file = open(sys.path[0] + '\out.txt', 'w')
for link in soup.find_all('a', class_="sister"):
    print type(link.get('href')), link.get_text()
    print type(link.get_text()), link.get('href')
    print >> file, link['href'].encode('gbk'), link.get_text().encode(
        'gbk')
file.close()
