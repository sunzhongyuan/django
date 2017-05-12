from django.conf.urls import url
from django.contrib import admin

from . import views
urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^index/$', views.index, name='index'),
    url(r'^index/(?P<article_id>[0-9]+)$', views.article_page, name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page, name='edit_page'),
    url(r'^del/(?P<article_id>[0-9]+)$', views.article_del, name='article_del'),
    url(r'^test/$', views.index, name='article_test'),
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
