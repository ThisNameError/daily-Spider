# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from pymongo import MongoClient
from mongoengine import *

from mongo import Movie


class Day08ScrapyPipeline(object):

    def __init__(self, host, port, database, username, password):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            port=crawler.settings.get('MYSQL_PORT'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            username=crawler.settings.get('MYSQL_USERNAME'),
            password=crawler.settings.get('MYSQL_PASSWORD')
        )

    def open_spider(self, spider):
        self.db = pymysql.connect(self.host, self.username, self.password, self.database, self.port, charset='utf8')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.db.close()

    def process_item(self, item, spider):
        sql = 'insert into movie(title, actor, release_time) values ("%s", "%s", "%s")' % (item['title'], item['actor'], item['time'])
        print(sql)
        self.cursor.execute(sql)
        self.db.commit()
        return item


class MaoyanPymongoPipeline(object):
    def __init__(self, database):
        self.client = MongoClient()
        self.db = self.client[database]

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            database=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        # self.client = pymongo.MongoClient()
        # self.db = self.client[self.mongo_db]
        pass

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        movie = {}
        movie['title'] = item['title']
        movie['actor'] = item['actor']
        movie['time'] = item['time']
        self.db.movie.insert(movie)
        return item


class MaoyanMongoPipeline(object):
    def __init__(self, database):
        self.db = database

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            database=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        connect(self.db)

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        movie = Movie()
        movie.title = item['title']
        movie.actor = item['actor']
        movie.time = item['time']
        movie.save()

        return item

