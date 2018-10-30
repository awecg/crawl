#coding=utf-8
import re
import urlparse, urllib

from bs4 import BeautifulSoup


class HtmlParser(object):
    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        # print type(html_cont)
        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_data(self, page_url, soup):
        result = {}

        #url
        result['url'] = page_url

        # <dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
        title_node = soup.find('dd', class_="lemmaWgt-lemmaTitle-title").find("h1")
        result['title'] = title_node.get_text()

        #<div class="lemma-summary">
        summary_node = soup.find('div', class_="lemma-summary")
        result['summary'] = summary_node.get_text()

        return result

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # links = soup.find_all(re.compile(r"/item/\d+\.htm"))
        links = soup.find_all('a', href=re.compile(r"/item/"))
        for link in links:
            # new_url = link['href']
            # 将link['href']--unicode格式字符串-encode--
            new_url = urllib.unquote(link['href'].encode('utf-8'))
            new_full_url = urlparse.urljoin(page_url, new_url)
            # print type(new_full_url), new_full_url
            new_urls.add(new_full_url)
        return new_urls