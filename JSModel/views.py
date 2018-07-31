from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import NewsArticle, ListArticle


def index(request):
    url1 = request.GET.urlencode()
    print(url1)
    new_article = NewsArticle.objects.order_by('-create_time')[:4]
    template = loader.get_template('JSModel/index.html')
    list_article = ListArticle.objects.order_by('-list_name')[:4]
    temp = 0
    for line in new_article:
        img = line.img.split(',')
        new_article[temp].img = img
        temp += 1
    context = {
        'new_article': new_article,
        'list_article': list_article,
    }

    return HttpResponse(template.render(context, request))


def list_page(request):
    return render(request, 'JSModel/list.html')


def show_page(request):
    return render(request, 'JSModel/show.html')
