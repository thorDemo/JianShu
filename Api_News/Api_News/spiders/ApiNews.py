# -*- coding: utf-8 -*-
import scrapy
import json
from Api_News.items import ApiNewsItem, NewsImageItem
from snownlp import SnowNLP


class ApinewsSpider(scrapy.Spider):
    name = 'ApiNews'
    allowed_domains = ['47.90.63.143']
    api = 'OrTqAiyVROsmXuQMR6Lmr7eENi5GZX7o6swyVh1KcHHu7nGccWjTgLEBWW7WtqVD'
    start_urls = [
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=0&catid=10028&apikey=%s' % api,
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=20&catid=10028&apikey=%s' % api,
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=40&catid=10028&apikey=%s' % api,
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=60&catid=10028&apikey=%s' % api,
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=80&catid=10028&apikey=%s' % api,
        'https://47.90.63.143/news/appledailyhk?type=2&pageToken=100&catid=10028&apikey=%s' % api,
    ]

    def parse(self, response):
        item = ApiNewsItem()
        image_item = NewsImageItem()
        result = json.loads(response.text)
        hasNext = result['hasNext']
        print(hasNext)
        print(SnowNLP(result['data'][0]['title']))
        item['dataType'] = 'yule'
        item['author'] = result['appCode']
        for news in result['data']:
            if not news['videoUrls']:
                news['videoUrls'] = 'no'
            images = ''
            for img in news['imageUrls']:
                images += str(img).split('/')[-1] + ','
            images = images.strip(',')
            item['re_id'] = news['id']
            item['videoUrls'] = news['videoUrls']
            item['tags'] = SnowNLP(','.join(str(i) for i in news['tags'])).han
            item['title'] = SnowNLP(news['title']).han
            item['image'] = images
            item['publishDateStr'] = str(news['publishDateStr']).replace('T', ' ')
            item['quantity'] = self.comment_quantity(news['content'])
            item['content'] = SnowNLP(news['content']).han
            item['description'] = SnowNLP(item['content']).summary(3)
            item['likeCount'] = news['likeCount']
            item['viewCount'] = news['viewCount']
            yield item
            # for image in news['imageUrls']:
            #     image_item['image_urls'] = [image]
            #     yield image_item

    def comment_quantity(self, value):
        length = len(value)
        utf8_length = len(value.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return length


def test_snow():
    text = """
    其實。。都預咗啦。。逢親D咩手工乜，古早乜，一有大量需求。。
    """
    s = SnowNLP(text)
    print(s.keywords(3))
    print(s.summary(3))
    print(SnowNLP('其實。').sentences)
    x = s.sentences
    y = s.han
    print(x)
    print(y)