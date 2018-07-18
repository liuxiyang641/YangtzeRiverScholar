# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re


class YangtzeriverscholarPipeline(object):
    def __init__(self):
        self.spacePattern = re.compile(r'\s+')

    def process_item(self, item, spider):
        for key, value in item.items():
            item[key] = value.strip()
            item[key] = self.spacePattern.sub(' ', item[key])
        return item
