from django.db import models


# 新闻文章模型
class NewsArticle(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    author = models.CharField(max_length=100)
    author_img = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    description = models.TextField(default='无')
    create_time = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    img = models.CharField(max_length=200)
    context = models.TextField(default='无')
    url = models.CharField(max_length=200,default='url')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# 文章列表模型
class ListArticle(models.Model):
    list_url = models.CharField(max_length=100)
    list_name = models.CharField(max_length=100)
    list_img = models.CharField(max_length=200)

    def __str__(self):
        return self.list_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)