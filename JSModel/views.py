from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from .models import NewsArticle, ListArticle, ArticleAuthor
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def index(request):
    url = request.build_absolute_uri()
    print(url)
    new_article = NewsArticle.objects.order_by('?')[:30]
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
        'title': '',
        'keyword': '',
    }

    return HttpResponse(template.render(context, request))


def list_page(request, list_name):
    print(list_name)
    try:
        list_message = ListArticle.objects.get(list_name__exact=list_name)
        list_article = NewsArticle.objects.filter(tips__exact=list_message.list_name)[:30]
    except NewsArticle.DoesNotExist:
        raise Http404
    template = loader.get_template('JSModel/list.html')
    temp = 0
    for line in list_article:
        img = line.img.split(',')
        list_article[temp].img = img
        temp += 1
    context = {
        'list_article': list_article,
        'list_message': list_message
    }
    print("--------------  我运行了一次！ --------------")
    return HttpResponse(template.render(context, request))


def author_page(request, author_id):
    url = request.path
    print(url.split('/')[1])
    try:
        author_message = ArticleAuthor.objects.get(author_id=author_id)
        author_article = NewsArticle.objects.filter(author__exact=author_message.author_name).order_by('-create_time')[:10]
        list_message = dict()
        list_message.list_id = author_message.author_id
        list_message.list_name = author_message.author_name
        list_message.list_img = author_message.author_img
    except NewsArticle.DoesNotExist:
        raise Http404
    template = loader.get_template('JSModel/list.html')
    temp = 0
    for line in author_article:
        img = line.img.split(',')
        author_article[temp].img = img
        temp += 1
    context = {
        'list_article': author_article,
        'list_message': list_message,
    }
    return HttpResponse(template.render(context, request))


@cache_page(60 * 15)
def show_page(request, article_id):
    try:
        article = NewsArticle.objects.get(re_id__exact=article_id)
        author = ArticleAuthor.objects.get(author_name__exact=article.author)
        article.author_img = author.author_img
        new_article = NewsArticle.objects.order_by('-create_time')[:4]
        for line in new_article:
            line.author_img = author.author_img
        template = loader.get_template('JSModel/show.html')
        img = article.img.split(',')
        text = article.context.split('。')
        text_num = len(text)
        img_num = len(img)
        print('%s %s' % (text_num, img_num))
        for x in range(0, img_num):
            text.insert(int(text_num/img_num)*x, '<img/>')
        temp = 0
        img_id = 0
        for line in text:
            line += '。'
            if line.startswith('<img/>'):
                text[temp] = '/static/img/full/%s' % img[img_id]
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
