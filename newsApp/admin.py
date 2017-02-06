#! -*- coding=utf-8 -*-
from django.contrib import admin
from newsApp.models import CategoryNews, New, New_Photos
from app.models import BasicData

class NewsInline(admin.TabularInline):
    model = New

class New_PhotosInline(admin.TabularInline):
    model = New_Photos


@admin.register(CategoryNews)
class CategoryAdmin(admin.ModelAdmin):
    inlines =  [NewsInline,]

@admin.register(New)
class NewsAdmin(admin.ModelAdmin):
    #list_display=('title','category','date'),
    inlines =  [New_PhotosInline,]

@admin.register(New_Photos)
class New_PhotosAdmin(admin.ModelAdmin):
    list_display=('text','photo','new')

@admin.register(BasicData)
class BasicDataAdmin(admin.ModelAdmin):
    list_display=('canteen_name',)
