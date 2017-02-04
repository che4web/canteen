from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from newsApp import views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()
    
urlpatterns = [
    url(r'^$', views.news_list, name='news-list'),
    url(r'^(?P<pk>\d+)/$', views.NewsDetailView.as_view(), name='news-detail'),
    url(r'^news2$', views.NewsListView.as_view(), name='news-list2'),
]
