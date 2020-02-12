from django.db import models

class UrlRecord(models.Model):
    id = models.AutoField(primary_key=True, verbose_name=u'url id')
    origin_url = models.CharField(max_length=30, verbose_name=u'縮網址')
    class Meta:
        verbose_name = u'縮網址紀錄'
        verbose_name_plural = verbose_name
    def __str__(self):
        return u'縮網址id(%s)對應網址館別(%s)' % (self.id, self.origin_url)
