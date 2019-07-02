# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from .sql import Sql
class CrawlJukuPipeline(object):
    def process_item(self, item, spider):
        # print('in pipeline===================================')
        ret = Sql.insert_corpus(item['jp_sen'], item['cn_sen'])
        if ret == 1:
            print('insert success')
        return item
