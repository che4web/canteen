from django.db import models

DEFAULT_PHOTO = "/static/img_sources/default_dish.png"
class CategoryMenu(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    order = models.IntegerField()
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name=u"категория"
        verbose_name_plural=u"категории"
        ordering=["order"]

class Dish(models.Model):
    name = models.CharField(max_length=255,verbose_name=u'название')
    descr = models.TextField(verbose_name=u'описание')
    price = models.FloatField(verbose_name=u'цена')
    isToday = models.BooleanField(verbose_name=u'сегодня в меню')
    img = models.ImageField(blank=True,verbose_name=u'фото блюда')
    category = models.ForeignKey(CategoryMenu,verbose_name=u'категория блюда')   
    
    @models.permalink
    def get_absolute_url(self):
        return ('menu-detail', [self.id])

    def get_img(self):
        if self.img:
            return self.img.url
        else:
            return DEFAULT_PHOTO

    class Meta:
        verbose_name=u"блюдо"
        verbose_name_plural=u"блюда"
