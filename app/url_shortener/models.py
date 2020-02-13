from django.db import models
from mysite.settings import HOSTNAME

class UrlRecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u'url id')
    origin_url = models.URLField(max_length=200, verbose_name=u'縮網址')
    class Meta:
        verbose_name = u'縮網址紀錄'
        verbose_name_plural = verbose_name
    def __str__(self):
        return u'縮網址id(%s)對應原始網址(%s)' % (self.id, self.origin_url)
    
    @staticmethod
    def shortener_url(key):
        # 生成縮網址
        return HOSTNAME + '\\' + str(key)