from django.conf.urls import url,include
from django.contrib import admin
from art_app import views
from art_app import apps
import xadmin
urlpatterns = [
    url('^$',views.index,name='index'),
    url(r'^xadmin/', xadmin.site.urls),
    url('login/',include('apps.art_app.urls')),
    url('register/',include('apps.art_app.urls')),
    url('page/', include('art_app.urls')),
    url('daohan/', include('art_app.urls')),
    url('data_li/',include('art_app.urls')),
    url('search/',include('home.urls')),
    url(r'^ueditor/',include('DjangoUeditor.urls')),
]
