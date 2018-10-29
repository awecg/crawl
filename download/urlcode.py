#coding=utf-8
import sys
import urlparse, urllib
# help(urlparse.urljoin)

url = "https://baike.baidu.com/item/%E7%99%BE%E5%BA%A6%E7%99%BE%E7%A7%91%EF%BC%9A%E6%9C%AC%E4%BA%BA%E8%AF%8D%E6%9D%A1%E7%BC%96%E8%BE%91%E6%9C%8D%E5%8A%A1/22442459?bk_fr=pcFooter"

strBite = "中文"
strUni = strBite.decode('utf-8')
print strUni, type(strUni), strBite, type(strBite)
print urllib.unquote(url.decode('utf-8').encode('utf-8'))

print type(urllib.quote(strBite.decode(sys.stdin.encoding).encode('gbk')))
print urllib.quote(strBite.decode(sys.stdin.encoding).encode('gbk'))
print urllib.quote(strBite.decode(sys.stdin.encoding).encode('utf-8'))