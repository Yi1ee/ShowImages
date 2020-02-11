
from django.urls import path,re_path
from . import views


app_name = 'showimage'

urlpatterns = [
    path('', views.index,name='index'),
    
    re_path(r'^img/(?P<img_file>.*)$', views.img, name='img'),

    re_path(r'^index/(?P<index_file>.*)$', views.get_index, name='get_index'),

    re_path(r'^style/(?P<style_file>.*)$', views.style, name='style'),

    re_path(r'^allimages/$', views.get_Allimgfiles, name='get_Allimgfiles'),
    #re_path(r'^images/$', views.images, name='images'),

    re_path(r'^get_description/(?P<img_file>.*)$', views.get_description, name='get_description'),

    re_path(r'^Jokerdescribe/$', views.Jokerdescribe, name='Jokerdescribe'),
    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^search/$', views.search, name='search'),

]
