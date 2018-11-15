from django.db import models

from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField

class Home(models.Model):
    home_id = models.IntegerField(primary_key=True)
    home_title = models.CharField(max_length=100, null=True)
    home_url = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'home'
        verbose_name='导航'


class Details(models.Model):
    details_id = models.IntegerField(primary_key=True)
    details_url = models.CharField(max_length=100, null=True)
    details_title = models.CharField(max_length=100, null=True)
    details_zz = models.CharField(max_length=100, null=True)
    details_js = models.CharField(max_length=500, null=True)
    details_hot = models.IntegerField(null=True)
    image_url = models.CharField(max_length=100, null=True)
    image_figer = models.CharField(max_length=100, null=True)
    home_id = models.ForeignKey(Home, models.DO_NOTHING, db_column='home_id', db_index=True)
    a_content = UEditorField(verbose_name="文章内容",
                             width=1000, height=600,
                             imagePath="media/arts_ups/ueditor/",
                             filePath="media/arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')


    class Meta:
        db_table = 'details'
        verbose_name = '详情'

class Zhangjie(models.Model):
    post_id = models.IntegerField(primary_key=True)
    read_title = models.CharField(max_length=100, null=True)
    read_url = models.CharField(max_length=100, null=True)
    read_zj = models.CharField(max_length=100, null=True)
    details_id = models.ForeignKey(Details, models.DO_NOTHING, db_column='details_id', db_index=True)



    class Meta:
        db_table = 'zhangjie'
        verbose_name = '章节'


class UserProfile(models.Model):
    phone = models.CharField(max_length=11, default='110')
    desc = models.CharField(max_length=255, null=True)
    uid = models.IntegerField('用户ID', primary_key=True)
    icon = models.ImageField(verbose_name=u'头像', max_length=100, upload_to='upload/img/%Y%m%d',
                             default=u"apps/static/img/default.png")
    user = models.OneToOneField('auth.User')

    class Meta:
        db_table = 'user_profile'


# class Banner(models.Model):
#     banner_id = models.AutoField('ID', primary_key=True)
#     title = models.CharField('标题', max_length=100)
#     image = models.ImageField('轮播图', upload_to='banner/%Y%m%d', storage=ImageStorage(), max_length=100)
#     detail_url = models.URLField('访问地址', max_length=200)
#     order = models.IntegerField('顺序', default=1)
#     create_time = models.DateTimeField('添加时间', auto_now_add=True)
#
#     class Meta:
#         db_table = 'banner'
#         verbose_name = '轮播图'