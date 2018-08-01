from django.urls import path, re_path
from . import views

app_name = 'Model1'

urlpatterns = [
    path('', views.index, name='index_page'),
    re_path(r'list_\w+/', views.list_page),
    path('show/<int:article_id>/', views.show_page),
]
