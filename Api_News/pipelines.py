# -*- coding: utf-8 -*-
from Api_News.items import ApiNewsItem, NewsImageItem
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from JSModel.models import NewsArticle


class ApiNewsPipeline(object):

    def process_item(self, item, spider):
        if isinstance(item, ApiNewsItem):
            page = NewsArticle()
            page.re_id = item['re_id']
            page.author = item['author']
            page.title = item['title']
            page.keyword = item['keyword']
            page.description = item['description']
            page.create_time = item['crate_time']
            page.quantity = item['quantity']
            page.read = item['read']
            page.comment = item['comment']
            page.like =item['like']
            page.img = item['img']
            page.videoUrls = item['videoUrls']
            page.context = item['context']
            page.url = item['url']
            page.tips = item['tips']
            page.source = item['source']
            page.save()
            return item


class MyImagesPipeline(ImagesPipeline):
    """自定义图片下载器,以图片url为路径保存图片"""
    def get_media_requests(self, item, info):

        if isinstance(item, NewsImageItem):
            for image_url in item['image_urls']:
                yield scrapy.Request(image_url)

    def file_path(self, request, response=None, info=None):
        """自定义图片保存路径,以图片的url保存,重写前是图片的url经过MD5编码后存储"""
        image_guid = request.url
        name = str(image_guid).split('/')[-1]
        return 'full/%s' % name

