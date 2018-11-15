from django.conf.urls import url

from apps.art_app import views

urlpatterns = [
    url('login/',views.login_view,name='login'),
    url('register/',views.register,name='register'),
    url('datails/$',views.details, name='deta'),
    url('data_li/',views.data_li,name='data_li'),
]
