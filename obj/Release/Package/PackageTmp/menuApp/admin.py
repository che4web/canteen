#! -*- coding=utf-8 -*-

from django.contrib import admin
from menuApp.models import CategoryMenu, Dish

class DishesInline(admin.TabularInline):
    model = Dish

@admin.register(CategoryMenu)
class CategoryMenuAdmin(admin.ModelAdmin):
    inlines =  [DishesInline,]

@admin.register(Dish)
class DishesInline(admin.ModelAdmin):
    list_display=('name','descr','price','category','isToday')