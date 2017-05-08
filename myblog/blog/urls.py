from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
]
