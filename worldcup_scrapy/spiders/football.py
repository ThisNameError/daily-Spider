# -*- coding: utf-8 -*-
import scrapy

from worldcup.items import WorldcupItem


class FootballSpider(scrapy.Spider):
    name = 'football'
    allowed_domains = ['sports.sina.com.cn']
    start_urls = ['http://sports.sina.com.cn/g/2018worldcupeq/']

    def parse(self, response):
        headline = response.selector.css('.hdlineBox a::text').extract()
        print('-' * 20)
        print(headline)
        for title in headline:
            item = WorldcupItem()
            item['title'] = title
            yield item
