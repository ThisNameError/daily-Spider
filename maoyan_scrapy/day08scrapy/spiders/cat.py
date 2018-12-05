# -*- coding: utf-8 -*-
import scrapy

from day08scrapy.items import Day08ScrapyItem


class CatSpider(scrapy.Spider):
    name = 'cat'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/board/4']

    # 构造请求头
    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
            'Connection': 'keep-alive',
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        }
        for i in range(10):
            yield scrapy.Request(url='http://maoyan.com/board/4?offset=%d' % (i * 10),
                                 headers=headers,
                                 method='GET',
                                 callback=self.parse,
                                 )

    # 解析响应
    def parse(self, response):
        title = response.selector.xpath('//div[@class="board-item-content"]//p[@class="name"]/a/text()').extract()
        actor = response.selector.xpath('//div[@class="board-item-content"]//p[@class="star"]/text()').extract()
        time = response.selector.xpath('//div[@class="board-item-content"]//p[@class="releasetime"]/text()').extract()
        for i in range(len(title)):
            movie = Day08ScrapyItem()
            movie['title'] = title[i]
            movie['actor'] = actor[i].strip()
            movie['time'] = time[i]
            yield movie
