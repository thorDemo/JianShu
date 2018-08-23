from django.urls import path, re_path
from django.contrib.sitemaps.views import sitemap
from . import views
from .sitemaps import NewsArticleSitemap

app_name = 'Model1'

sitemaps = {
    'NewsArticle': NewsArticleSitemap,
}

urlpatterns = [
    path('', views.index, name='index_page'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),

    path('list_<list_name>/', views.list_page, name='list_page'),
    path('show/<article_id>/', views.show_page, name='show_page'),
    path('author/<int:author_id>', views.author_page),
    path('spider/', views.spider_page),
    path('spider_data/<method>/', views.spider_data),
    re_path(r'.+', views.random_page),
]
