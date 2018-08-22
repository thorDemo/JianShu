from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse, Http404
from django.urls import reverse
from django.views import View


class BaseView(View):
    @property
    def ismobile(self):
        # 开发的时候你可以直接返回True或者False来调整不同的模版
        return 'm.maidu.com' in self.request.get_host()

    def render(self, request, temple_name, context):
        if self.ismobile:
            temple_name = 'mobile/%s' % temple_name
        return render(request, temple_name, context)