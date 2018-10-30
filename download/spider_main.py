#coding=utf-8
import url_manager, html_downloader, html_parser, html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                # 保证url格式
                new_url = new_url.replace(' ', '%20')
                print 'crawl %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)

                new_urls, new_data = self.parser.parse(new_url, html_cont)

                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                # if count == 1000:
                if count == 20:
                    print "finished!!!!"
                    break
                count = count + 1
            except:
                print 'crawl failed'

        self.urls.output_url()
        # self.outputer.output_html()
        

if __name__ == "__main__":
    root_url = "http://baike.baidu.com/item/Python"
    obj_spider = SpiderMain()
    obj_spider.crawl(root_url)

    # for url in obj_spider.urls.old_urls:
        # print type(url.encode('utf-8')), url.encode('utf-8')
