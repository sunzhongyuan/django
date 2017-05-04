from django.shortcuts import render
from . import models
#from django.http import HttpResponse
# Create your views here.

def index(request):
    #return HttpResponse('Hello world')
    #return render(request,'blog/index.html',{'hello':'HELLO BLOG'})
    article = models.Article.objects.get(pk=2)
    return render(request,'blog/index.html',{'article':article})
