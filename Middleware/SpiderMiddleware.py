from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Row1(MiddlewareMixin):

    def process_request(self, request):
        print("中间件1请求")
        path = request.META.get('PATH_INFO')
        path_info = request.META.get('PATH_INFO')
        HTTP_X_FORWARDED_HOST = request.META.get('HTTP_X_FORWARDED_HOST')
        HTTP_USER_AGENT = request.META.get('HTTP_USER_AGENT')
        print('path_info :  %s ' % path_info)
        print('HTTP_X_FORWARDED_HOST : %s ' % HTTP_X_FORWARDED_HOST)
        print('HTTP_USER_AGENT : %s ' % HTTP_USER_AGENT)
        path_info = request.META.get('PATH_INFO')
        request.META['PATH_INFO'] = '/show/1_58569468/'
        print('path_info : %s ' % path_info)

    def process_response(self, request, response):
        print("中间件1返回")
        return response