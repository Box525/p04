from django.db import models

# Create your models here.
class Auther(models.Model):
    aname = models.CharField('姓名', max_length=128)
    asex = models.CharField('性别', max_length=1)

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = u'作者列表'

    def __str__(self):
        return self.aname

    # 新增加一列数据 非数据表中的列
    def new_column(self):
        if self.asex == '1':
            return u'男'
        else:
            return u'女'

    new_column.short_description = u'转化之后的性别'
    info = property(new_column)