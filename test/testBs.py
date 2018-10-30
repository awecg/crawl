#coding=utf-8
# dynamic pages


import urllib2
from bs4 import BeautifulSoup

span = '<span class="vote-count">9159</span>'
url = 'http://baike.baidu.com/item/Python'
# soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')
soup = BeautifulSoup(span, 'html.parser')
print type(span)

vote_tip = soup.find('span',"vote-tip")
vote_node = soup.find('span',"vote-count")
print type(vote_node)
print vote_node.get_text().encode('utf-8')
# print vote_tip.get_text().encode('utf-8')