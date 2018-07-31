from django.urls import path
from . import views

app_name = 'Model1'

urlpatterns = [

    path('', views.index, name='index'),
    path('list_<int:list_id>', views.list_page, name='list_page'),
    path('show/', views.show_page, name='list_page'),

]
