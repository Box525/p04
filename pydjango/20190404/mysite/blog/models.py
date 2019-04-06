from django.db import models

# Create your models here.


class Country(models.Model):
    # 注意 model类 在创建时默认是创建主键为 id
    # 如果 想自定义主键 model定义了 AutoField 列字段参数
    # 注意 如果使用AutoField 必须添加primary_key 设置为True
    # AutoFile int自增列
    cid = models.AutoField(primary_key=True)
    # CharFiled 字符类型，必须提供max_length 字段参数 最长254
    cname = models.CharField(max_length=254, unique=True)

class Auther(models.Model):
    aid = models.AutoField(primary_key=True)
    aname = models.CharField(max_length=128)
    aaid = models.CharField(max_length=4, unique=True)
    cid = models.ForeignKey(to='Country', null=False, to_field='cid', related_name='authers',on_delete=models.CASCADE)



'''
class ATest(models.Model):
    # 如果 AutoField 不够用
    aid = models.BigAutoField()
    # 整数类型 有范围 -2147483648 ~ 2147483647
    age = models.IntegerField() # 11字节
    models.PositiveSmallIntegerField() #5字节
    models.SmallIntegerField()#6字节
    models.PositiveIntegerField()#10字节
    models.BigIntegerField()#20字节

    # 二进制
    models.BinaryField()

    # 字符串
    models.CharField() #varchar
    models.TextField() #longtext

    # 布尔类型
    models.BooleanField()
    models.NullBooleanField()

    # 时间
    models.DateField()
    models.DateTimeField()
    models.DurationField() #int Python timedate

    # 浮点型
    models.FloatField()
    models.DecimalField() #

    # 其他字段
    models.EmailField()
    models.ImageField()
    models.FileField()
'''''


