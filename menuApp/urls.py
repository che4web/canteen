#! -*- coding=utf-8 -*-

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

from django.conf.urls.static import static
from django.conf import settings

from menuApp import views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include

urlpatterns = [

    url(r'^(?P<pk>\d+)/$', views.DishesDetailView.as_view(), name='menu-detail'),
    url(r'^$', views.DishesListView.as_view(), name='menu-list'),
   
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
