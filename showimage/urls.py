
from django.urls import path,re_path
from . import views

app_name = 'showimage'

urlpatterns = [
    path('', views.index,name='index'),
    re_path(r'^img/(?P<img_file>.*)$', views.img, name='img'),
    re_path(r'^images/$', views.images, name='images'),
    re_path(r'^Leondescribe/$', views.Leondescribe, name='Leondescribe'),
    re_path(r'^Jokerdescribe/$', views.Jokerdescribe, name='Jokerdescribe'),

]
