
from django.urls import path,re_path
from . import views


app_name = 'showimage'

urlpatterns = [
    path('', views.index,name='index'),
    re_path(r'^img/(?P<img_file>.*)$', views.img, name='img'),

    re_path(r'^allimages/$', views.get_Allimgfiles, name='get_Allimgfiles'),
    #re_path(r'^images/$', views.images, name='images'),

    re_path(r'^get_description/(?P<img_file>.*)$', views.get_description, name='get_description'),

    re_path(r'^Jokerdescribe/$', views.Jokerdescribe, name='Jokerdescribe'),

]
