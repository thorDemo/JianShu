from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse


class Row1(MiddlewareMixin):

    def process_request(self, request):
        print("中间件1请求")
        print(request.META)
        print(request.META.get('HTTP_USER_AGENT'))

    def process_response(self, request, response):
        print("中间件1返回")
        return response