# -*- coding: utf-8 -*-

# Scrapy settings for Api_Newsx project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Api_Newsx'

SPIDER_MODULES = ['Api_Newsx.spiders']
NEWSPIDER_MODULE = 'Api_Newsx.spiders'

# MYSQL_HOST = '103.56.136.105'
# MYSQL_DBNAME = 'news'
# MYSQL_USER = 'root'
# MYSQL_PASSWD = 'password'
# MYSQL_PORT = 3306

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Api_Newsx (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.25
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-language': 'zh-CN,zh;q=0.8',
    # 'referer': 'https://47.90.63.143/',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36”)',
    # 'Host': '47.90.63.143'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Api_Newsx.middlewares.ApiNewsSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Api_Newsx.middlewares.ApiNewsDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Api_Newsx.pipelines.ApiNewsPipeline': 300,
   'Api_Newsx.pipelines.MyImagesPipeline': 100,
}
# IMAGES_STORE = '/www/wwwroot/Special/JianShu/JSModel/templates/JSModel/static/img/'
IMAGES_STORE = '/Users/hexiaotian/PycharmProjects/JianShu/JSModel/templates/JSModel/static/img/'
# 该字段的值为XxxItem中定义的存储图片链接的image_urls字段
IMAGES_URLS_FIELD = 'image_urls'
# 该字段的值为XxxItem中定义的存储图片信息的images字段
IMAGES_RESULT_FIELD = 'images'
# 生成缩略图(可选)
# IMAGES_THUMBS = {
#     'small': (50, 50),
#     'big': (270, 270),
# }
# 过期时间,单位:天(可选)
IMAGES_EXPIRES = 120
# 过滤小图片(可选)
# IMAGES_MIN_HEIGHT = 110
# IMAGES_MIN_WIDTH = 110
# 是否允许重定向(可选)
# MEDIA_ALLOW_REDIRECTS = True

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
