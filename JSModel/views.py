from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.template import loader
from .models import NewsArticle, ListArticle, ArticleAuthor
from django.views.decorators.cache import cache_page
from django.shortcuts import redirect
import os
import random
import linecache
import json
from subprocess import PIPE, Popen
from JSModel.spider import Spider
# 配置信息
############
path = os.path.split(os.path.realpath(__file__))[0]     # 根目录
keywords_path = '%s/templates/JSModel/static/keywords.txt' % path      # 关键词目录
re_url = 'www.aidshe.com'   # 改为站群的域名
############


@cache_page(60 * 60 * 2)
def index(request):
    """
    缓存时间2小时
    关键词路径变量 keyword_file  文件keywords.txt

    :param request:
    :return:
    """
    url = request.META
    print('take in')
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
        'title': '香港生活_赌场游戏名字_大世界娱乐平台',
        'keywords': '最好平台，真人在线，香港生活，香港娱乐，香港赛马，香港美食',
        'description': '香港生活线上娱乐平台为您提供体育赛事，视讯直播，电子游艺，彩票游戏，香港娱乐，香港赛马，香港美食。香港生活是“亚洲最受玩家喜爱品牌”，如今也成为亚洲最具有领导地位的顶级娱乐平台，拥有15年资深行业经验，8项设计系统保障，在线玩家超过10000+，96%客户满意度，我们将竭诚为您服务，为您提供顶级娱乐享受。',
    }
    return HttpResponse(template.render(context, request))


@cache_page(60 * 60 * 2)
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
    return HttpResponse(template.render(context, request))


@cache_page(60 * 60 * 2)
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


@cache_page(60 * 60 * 2)
def show_page(request, article_id):
    """
    内容页管理程序
    缓存时间2小时
    如果没有找到指定id的内容页 随机重定向到一个内容页
    :param request:
    :param article_id:
    :return:
    """
    path_info = request.META.get('PATH_INFO')
    host = request.get_host()
    print('views path_info : %s' % path_info)
    print('views host : %s' % host)
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
            'bc_keyword': get_one_keyword(),
        }
    except NewsArticle.DoesNotExist:
        # 如果没有匹配到默认url  随机重定向到一个内容页
        article = NewsArticle.objects.order_by('?')[0]
        return redirect('/show/%s/' % article.re_id)
    return HttpResponse(template.render(context, request))


def spider_page(request):
    template = loader.get_template('JSModel/logs.html')
    context = {}
    return HttpResponse(template.render(context, request))


def spider_data(request, method, url):
    number = []
    res = {}
    spider_name = ['Baiduspider', 'Yisouspider', '360Spider', 'sogou']
    spider = Spider()
    if method == 'day':
        for typ in spider_name:
            for date in spider.seven_day():
                order = 'cat /www/wwwlogs/%s-access_log |grep %s|grep %s|wc -l' % (re_url, typ, date)
                print(order)
                pi = Popen(order, shell=True, stdout=PIPE)
                result = int(pi.stdout.read())
                print(result)
                number.append(result)
        res['category'] = spider.seven_day()
        res['Baidu'] = number[0:7]
        res['Yisou'] = number[7:14]
        res['Sp360'] = number[14:21]
        res['sogou'] = number[21:28]
    elif method == 'hou':
        for typ in spider_name:
            print("loading spider number ...")
            for date in spider.twenty_four_hours():
                order = 'cat /www/wwwlogs/%s-access_log |grep %s|grep %s|wc -l' % (url, typ, date)
                pi = Popen(order, shell=True, stdout=PIPE)
                result = int(pi.stdout.read())
                number.append(result)
        res['category'] = spider.twenty_four_hours()
        res['Baidu'] = number[0:24]
        res['Yisou'] = number[24:48]
        res['Sp360'] = number[48:72]
        res['sogou'] = number[72:96]
    else:
        return Http404
    return HttpResponse(json.dumps(res))


@cache_page(60 * 60 * 2)
def random_page(request):
    """
    如果没有匹配到默认url  随机重定向到一个内容页
    内容页缓存时间2小时
    :param request:
    :return:
    """
    article = NewsArticle.objects.order_by('?')[0]
    return redirect('/show/%s/' % article.re_id)


def get_one_keyword():
    """
    随机取一个关键词
    :return:
    """
    count = 0
    keywords_file = open(keywords_path, 'r+', encoding='utf-8')
    for line in keywords_file:
        count += 1
    line = random.randint(1, count-1)
    keyword = linecache.getlines(keywords_path)[line].strip('\n')
    return keyword

