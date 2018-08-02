# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import csv
from YangtzeRiverScholar.items import YangtzeRiverScholarItem


class YangtzeriverscholarPipeline(object):
    def __init__(self):
        self.spacePattern = re.compile(r'\s+')

    def open_spider(self, spider):
        self.file = open('../docs/YangtzeRiverScholar.csv', 'w', encoding='utf')
        header = []
        for key in YangtzeRiverScholarItem.fields:
            header.append(key)
        self.writer = csv.DictWriter(self.file, fieldnames=header)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        for key, value in item.items():
            item[key] = value.strip()
            item[key] = (self.spacePattern.sub(' ', item[key]))
        self.writer.writerow(item)
        self.file.flush()
        return item
