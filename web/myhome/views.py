from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    
    # return HttpResponse('网站前台首页')
    return render(request,'myadmin/index.html')
