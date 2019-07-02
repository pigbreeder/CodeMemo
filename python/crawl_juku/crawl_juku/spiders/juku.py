# encoding=utf8
import re
import os
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from crawl_juku.items import CrawlJukuItem


class MySpider(scrapy.Spider):
    name = 'juku'
    allowed_domain = ['jukuu.com']
    base_path = 'http://www.jukuu.com/'
    path_prefix = '.html'

    def start_requests(self):
        print(os.getcwd())
        self.keywords = []
        with open('chnWordSegVocab',encoding='utf8') as f:
            cnt = 0
            for line in f:
                self.keywords.append(line.strip())
                # cnt += 1
                # if cnt > 1:
                #     self.keywords = ['选修课']
                #     break
        for kw in self.keywords:
            # url = self.base_path + 'display-' + kw + '-0' + self.path_prefix
            url = self.base_path + 'jcsearch.php?q=' + kw
            yield Request(url, self.parse)

    # def parse(self, response):
    #     print(response.text)
        # yield Request(url, callback=self.get_name)

    def parse(self, response):
        tds = BeautifulSoup(response.text, 'lxml').find_all('p')
        print('in parse')
        if len(tds) < 4:
            for item in self.get_sent(response):
                yield item
            # yield Request(response.url, callback=self.get_sent)
        else:
            tag_a = tds[-2].find_all('a')
            hrefs = list(map(lambda x: x['href'], tag_a))[:-1]
            for href in hrefs:
                url = self.base_path + href
                yield Request(url, callback=self.get_sent)

    def get_sent(self, response):
        print('in get_sent')
        tds = BeautifulSoup(response.text, 'lxml')
        # ret = []
        sens = list(tds.find_all('table')[5].find_all('tr', {'class': ['c', 'e']}))
        for idx in range(0, len(sens), 2):
            item = CrawlJukuItem()
            item['jp_sen'] = sens[idx].find_all('td')[1].get_text(strip=True)
            item['cn_sen'] = sens[idx + 1].find_all('td')[1].get_text(strip=True)
            yield item
            # ret.append(item)
        # return ret
