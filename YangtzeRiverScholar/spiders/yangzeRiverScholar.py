# -*- coding: utf-8 -*-
import scrapy
from YangtzeRiverScholar.items import YangtzeRiverScholarItem


class YangzeriverscholarSpider(scrapy.Spider):
    name = 'yangzeRiverScholar'
    allowed_domains = ['http://www.moe.gov.cn']
    start_urls = []

    def __init__(self, url='http://www.moe.gov.cn/srcsite/A04/s7051/201801/t20180105_323866.html'):
        self.start_urls.append(url)

    def start_requests(self):
        return [scrapy.Request(url=self.start_urls[0], callback=self.parse)]

    def parse(self, response):
        tables = response.xpath('//*[@id="xxgk_content_div"]//table/tbody')
        if tables is not None:
            #  此时的table1是特聘教授
            table1 = tables[0]
            cols = len(table1.xpath('tr'))+1
            for col in range(2, cols):
                scholar = YangtzeRiverScholarItem()
                scholar['college'] = "".join(table1.xpath('tr[' + str(col) + ']/td[1]//span/text()').extract())
                scholar['name'] = "".join(table1.xpath('tr[' + str(col) + ']/td[2]//span/text()').extract())
                scholar['researchArea'] = "".join(table1.xpath('tr[' + str(col) + ']/td[3]//span/text()').extract())
                scholar['title'] = '长江学者特聘教授'
                yield scholar

            #  此时的table2是讲座教授
            table2 = tables[1]
            cols = len(table2.xpath('tr')) + 1
            for col in range(2, cols):
                scholar = YangtzeRiverScholarItem()
                scholar['college'] = "".join(table2.xpath('tr[' + str(col) + ']/td[1]//span/text()').extract())
                scholar['name'] = "".join(table2.xpath('tr[' + str(col) + ']/td[2]//span/text()').extract())
                scholar['researchArea'] = "".join(table2.xpath('tr[' + str(col) + ']/td[3]//span/text()').extract())
                scholar['title'] = '长江学者讲座教授'
                yield scholar

            #  此时的table3是青年学者
            table3 = tables[2]
            cols = len(table3.xpath('tr')) + 1
            for col in range(2, cols):
                scholar = YangtzeRiverScholarItem()
                scholar['college'] = "".join(table3.xpath('tr[' + str(col) + ']/td[1]//span/text()').extract())
                scholar['name'] = "".join(table3.xpath('tr[' + str(col) + ']/td[2]//span/text()').extract())
                scholar['researchArea'] = "".join(table3.xpath('tr[' + str(col) + ']/td[3]//span/text()').extract())
                scholar['title'] = '长江学者青年学者'
                yield scholar