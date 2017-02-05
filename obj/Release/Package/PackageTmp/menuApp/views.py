#! -*- coding=utf8 -*-
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from menuApp.models import Dish
from menuApp.models import CategoryMenu

from django.views.generic import ListView, DetailView

class DishesListView2(ListView):
    model = Dish
    def get_context_data(self, **kwargs):
        context = super(DishesListView2, self).get_context_data(**kwargs)
        context['title']= u'МЕНЮ'
        return context

class DishesListView(ListView):
    model = CategoryMenu
    #def get_context_data(self, **kwargs):
    #    context = super(DishesListView, self).get_context_data(**kwargs)
    #    context['title']= u'НАШЕ МЕНЮ'
    #    return context

    def get_context_data(self, **kwargs):
        context = super(DishesListView, self).get_context_data(**kwargs)
        object_ls= self.model.objects.all()
        #context['object_list_1']= object_ls[0:len(object_ls)/2]
        #context['object_list_2']= object_ls[len(object_ls)/2:]
        context['object_list_1']=[object_ls[0:int(len(object_ls)/2)], object_ls[int(len(object_ls)/2):]]
        context['title']= u'НАШЕ МЕНЮ'
        return context

class DishesDetailView(DetailView):
    model = Dish
