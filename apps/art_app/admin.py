from django.contrib import admin

from django.contrib import admin

# from books.models import Tag, Art, Chapter
from xadmin import views

import xadmin
from django.contrib import admin

# Register your models here.

from art_app.models import Home, Details, Zhangjie
from xadmin import views

import xadmin


class BaseSetting(object):
    # 主题修改
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    # 整体配置
    site_title = '小说电商平台管理系统'
    site_footer = '武汉1804班级合作'
    menu_style = 'accordion'  # 菜单折叠


class DetailsAdmin(object):
    '''
     DetailsAdmin是对Tag models类进行的前端自定制
    '''

    # 后台列表显示列

    list_display = ['details_title', 'a_content']
    # 后台列表查询条件
    search_fields = ['home_id']
    # 后台列表通过时间查询
    list_filter = ['image_url']
    list_per_page = 5
    style_fields = {'a_content': 'ueditor'}

class ArtAdmin(object):
    # 后台列表显示列
    list_display = ['read_title']
    # 后台列表查询条件
    search_fields = ['read_url']
    # 后台列表通过时间查询
    list_filter = ['read_zj']
    list_per_page = 20


xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(Details, DetailsAdmin)
xadmin.site.register(Zhangjie, ArtAdmin)
