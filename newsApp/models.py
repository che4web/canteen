"""
Definition of models.
"""

from django.db import models

DEFAULT_PHOTO = "/static/img_sources/holyday/no_photo.jpg"
class CategoryNews(models.Model):
    title = models.CharField(max_length=255,verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Описание категории')
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name=u"категория новостей"
        verbose_name_plural=u"категории новостей"

class New(models.Model):
    title = models.CharField(max_length=255,verbose_name=u'Название')
    text = models.TextField(verbose_name=u'Текст новости')
    #img = models.ImageField()
    date =  models.DateTimeField(auto_now_add=True,verbose_name=u'Дата')
    category = models.ForeignKey(CategoryNews,verbose_name=u'Категория новости')
    
    @models.permalink
    def get_absolute_url(self):
        return ('news-detail', [self.id])

    class Meta:
        verbose_name=u"Новость"
        verbose_name_plural=u"Новости"

class New_Photos(models.Model):
    text = models.TextField(verbose_name=u'текст к фото если нужен')
    photo = models.ImageField(blank=True,verbose_name=u'фото')
    isDefault = models.BooleanField(verbose_name=u'обложка альбома')
    new = models.ForeignKey(New,verbose_name=u'фото относится к этой нвоости \ событию')   
    
    
    def get_photo(self):
        if self.photo:
            return self.photo.url
        else:
            return DEFAULT_PHOTO

    class Meta:
        verbose_name=u"Фото"
        verbose_name_plural=u"Фотографии"

