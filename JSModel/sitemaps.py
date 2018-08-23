from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import NewsArticle


class NewsArticleSitemap(Sitemap):

    priority = 0.5
    changefreq = 'daily'

    def items(self):
        new_article = NewsArticle.objects.all()
        return new_article

    def lastmod(self, obj):
        return obj.create_time
