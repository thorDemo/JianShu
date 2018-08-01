from django.db import models


# 新闻文章模型
class NewsArticle(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    author = models.CharField(max_length=100, default='佚名')
    author_img = models.CharField(max_length=200, default='0b444f3a9032.jpg')
    title = models.CharField(max_length=200, default='标题')
    keyword = models.CharField(max_length=200, default='关键词')
    description = models.TextField(default='描述')
    create_time = models.DateTimeField('date published')
    quantity = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    comment = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    img = models.CharField(max_length=200)
    context = models.TextField(default='文章内容')
    url = models.CharField(max_length=200, default='url')
    tips_choice = (('list_shehui', '社会热点'), ('list_dushu', '读书'), ('list_renwen', '人文社科'), ('list_ziran', '自然科普')
                   , ('list_gushi', '故事'), ('list_shouhui', '手绘'), ('list_luxing', '旅行。在路上'))
    tips = models.CharField(max_length=100, default='list_gushi', choices=tips_choice)
    source_choice = (('S1', '/47.90.63.143/news/饮食男女/'), ('S2', '/47.90.63.143/news/娱乐/'), ('S3', '/47.90.63.143/news/果籽/'))
    source = models.CharField(max_length=200, choices=source_choice, default='source one')

    def __str__(self):
        return 'id = %s : title = %s' % (self.id ,self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


# 文章列表模型
class ListArticle(models.Model):
    list_url = models.CharField(max_length=100)
    list_name = models.CharField(max_length=100)
    list_img = models.CharField(max_length=200)

    def __str__(self):
        return 'url = %s : name = %s' % (self.list_url, self.list_name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)