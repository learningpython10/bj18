from django.db import models

# Create your models here.


class BookInfo(models.Model):
    '''图书模板'''
    # 图书名
    book_name = models.CharField( max_length=20)
    # 出版日期
    book_date = models.DateField()
    # 阅读量
    bread = models.IntegerField(default=0)
    # 评论量
    bcomment = models.IntegerField(default=0)
    # 删除标记
    isDelete = models.BooleanField(default=False)


class HeroInfo(models.Model):
    '''与图书关联的英雄'模板'''
    # 英雄名
    hname = models.CharField(max_length=20)
    # 性别
    hgender = models.BooleanField(default=False)
    # 备注
    hcomment = models.CharField(max_length=200)
    # 关系属性
    hbook = models.ForeignKey('BookInfo')
    # 删除标记
    isDelete = models.BooleanField(default=False)
