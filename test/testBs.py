import urllib2
from bs4 import BeautifulSoup

url = 'http://baike.baidu.com/item/Python'
soup = BeautifulSoup(urllib2.urlopen(url).read(), 'html.parser')

vote_tip = soup.find('span',"vote-tip")
vote_node = soup.find('span',"vote-count")
print type(vote_node)
print vote_node.get_text().encode('utf-8')
print vote_tip.get_text().encode('utf-8')