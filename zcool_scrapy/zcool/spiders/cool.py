# -*- coding: utf-8 -*-
import scrapy
import json

from zcool.items import ZcoolItem


class CoolSpider(scrapy.Spider):
    name = 'cool'
    allowed_domains = ['api.hellorf.com']
    start_urls = ['http://www.hellorf.com/']

    def start_requests(self):
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
            'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive',
            'Host': 'api.hellorf.com',
            'Referer': 'https://www.hellorf.com/image/search?q=%E7%BD%91%E7%AB%99',
            'Content-Type': 'application/json;charset=UTF-8'
        }

        for i in range(10):
            data = {'keyword': '圣诞', 'page': '%d' % (i + 1)}

            yield scrapy.FormRequest(url='https://api.hellorf.com/hellorf/image/search?page=%d' % (i + 1),
                                     headers=headers,
                                     formdata=data,
                                     method='POST',
                                     callback=self.parse,
                                     )

    def parse(self, response):
        json_result = json.loads(response.text)
        data_list = json_result['data']['data']
        for data in data_list:
            item = ZcoolItem()

            item['title'] = data.get('title', '')
            item['item_id'] = data.get('_id', '')
            item['preview_url'] = data.get('preview_url', '')
            yield item
