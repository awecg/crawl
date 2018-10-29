#coding=utf-8
from bs4 import BeautifulSoup
import re, sys

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.
</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser', from_encoding='utf-8')
# print soup.prettify()
file = open(sys.path[0]+'\out.txt','w')
for link in soup.find_all('a', class_="sister"):
    print link.get('href'), link.get_text()
    print >> file, link.get('href'), link.get_text()
file.close()

print "Only get lacie: ", soup.find('a', href="http://example.com/lacie")['href']
print "use regexp: ", soup.find('a', href=re.compile(r"ac"))['href']
