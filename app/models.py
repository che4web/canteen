#! -*- coding=utf-8 -*-

"""
Definition of models.
"""
from django.db import models

class BasicData(models.Model):
    canteen_name = models.CharField(max_length=255,verbose_name=u'название столовой')
    city = models.TextField(verbose_name=u'город')
    street_home = models.TextField(verbose_name=u'улица_дом')
    tel = models.TextField(verbose_name=u'телефон')
    main_descr = models.TextField(verbose_name=u'главный текст')
    contact_text = models.TextField(verbose_name=u'текст для напишите нам')
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.canteen_name.encode('utf-8')
    class Meta:
        verbose_name=u"общие данные"
        verbose_name_plural=u"общие данные"

