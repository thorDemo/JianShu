from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from .models import NewsArticle, ListArticle


def index(request):
    url = request.build_absolute_uri()
    print(url)
    new_article = NewsArticle.objects.order_by('-create_time')[:4]
    template = loader.get_template('JSModel/index.html')
    list_article = ListArticle.objects.order_by('-list_name')[:7]
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
    url = request.path
    print(url.split('/')[1])
    try:
        list_article = NewsArticle.objects.filter(tips__exact=url.split('/')[1])
        print(list_article)
    except NewsArticle.DoesNotExist:
        raise Http404
    template = loader.get_template('JSModel/list.html')
    temp = 0
    for line in list_article:
        img = line.img.split(',')
        list_article[temp].img = img
        temp += 1
    context = {
        'list_article': list_article
    }
    return HttpResponse(template.render(context, request))


def show_page(request, article_id):
    try:
        article = NewsArticle.objects.get(id__exact=article_id)
        new_article = NewsArticle.objects.order_by('-create_time')[:4]
        template = loader.get_template('JSModel/show.html')
        img = article.img.split(',')
        text = article.context.split('\n')
        temp = 0
        img_id = 0
        for line in text:
            if line.startswith('<img/>'):
                text[temp] = '/static/img/%s' % img[img_id]
                img_id += 1
            temp += 1
        article.context = text
        article.img = img
        context = {
            'article': article,
            'new_article': new_article,
        }
    except NewsArticle.url:
        raise Http404
    return HttpResponse(template.render(context, request))
