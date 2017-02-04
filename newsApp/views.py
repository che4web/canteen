#! -*- coding=utf-8 -*-
"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from newsApp.models import New

from django.views.generic import ListView, DetailView

def news_list(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'newsApp/new_list.html',
        {
            'title':u'Список новостей',
            'object_list': New.objects.all()
        }
    )
class NewsListView(ListView):
    model = New
    def get_context_data(self, **kwargs):
        context = super(NewsListView, self).get_context_data(**kwargs)
        context['title']= u'Список новостей'
        return context

class NewsDetailView(DetailView):
    model = New