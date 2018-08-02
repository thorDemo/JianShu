from django.contrib import admin
from .models import NewsArticle, ListArticle, ArticleAuthor

admin.site.register(NewsArticle)
admin.site.register(ListArticle)
admin.site.register(ArticleAuthor)
