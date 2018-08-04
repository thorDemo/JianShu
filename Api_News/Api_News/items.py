# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from peewee import *

# db = MySQLDatabase("station", host='23.110.211.170', port=3306, user='station', passwd='password', charset='utf8')
db = MySQLDatabase("station", host='127.0.0.1', port=3306, user='root', passwd='123456', charset='utf8')


class ApiNewsItem(scrapy.Item):
    re_id = scrapy.Field()
    dataType = scrapy.Field()
    pageToken = scrapy.Field()
    hasNext = scrapy.Field()
    videoUrls = scrapy.Field()
    tags = scrapy.Field()
    description = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    image = scrapy.Field()
    publishDateStr = scrapy.Field()
    quantity = scrapy.Field()
    content = scrapy.Field()
    likeCount = scrapy.Field()
    viewCount = scrapy.Field()


class JSModel_newsarticle(Model):
    re_id = CharField(max_length=100, unique=True)
    author = CharField(max_length=100)
    title = CharField(max_length=200)
    keyword = CharField(max_length=200)
    description = TextField()
    create_time = DateTimeField(formats='%Y-%m-%d %H:%M:%S')
    quantity = IntegerField()
    read = IntegerField()
    comment = IntegerField()
    like = IntegerField()
    img = TextField()
    videoUrls = TextField(default='1.mp4')
    context = TextField()
    url = CharField(max_length=200)
    tips = CharField(max_length=100)
    source = CharField(max_length=200)

    class Meta:
        database = db


# 图片下载对象
class NewsImageItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()


class Person(Model):
    name = CharField()
    birthday = DateField()

    class Meta:
        database = db # This model uses the "people.db" database.


def test_db():
    db.connect()
    db.create_tables([Person])