# -*- coding: utf-8 -*-
import scrapy


class YangzeriverscholarSpider(scrapy.Spider):
    name = 'yangzeRiverScholar'
    allowed_domains = ['http://www.moe.gov.cn']
    start_urls = []

    def __init__(self, url='http://www.moe.gov.cn/srcsite/A04/s7051/201801/t20180105_323866.html'):
        self.start_urls.append(url)

    def start_requests(self):
        pass

    def parse(self, response):
        pass
