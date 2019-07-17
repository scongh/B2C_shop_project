from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 首页视图
def myhome_index(request):

    return render(request, 'myhome/index/index.html')

def myhome_list(request):

    return render(request, 'myhome/index/list.html')

def myhome_info(request):

    return render(request, 'myhome/index/info.html')


