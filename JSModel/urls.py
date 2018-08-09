from django.urls import path, re_path
from . import views

app_name = 'Model1'

urlpatterns = [
    path('', views.index, name='index_page'),
    path('list_<list_name>/', views.list_page),
    path('show/<article_id>/', views.show_page),
    path('author/<int:author_id>', views.author_page),
    path('spider/', views.spider_page),
    path('spider_data/<method>', views.spider_data),
    re_path(r'.+', views.random_page)
]
