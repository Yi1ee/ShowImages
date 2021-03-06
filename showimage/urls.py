
from django.urls import path,re_path
from . import views


app_name = 'showimage'

urlpatterns = [
    path('', views.index,name='index'),
    
    re_path(r'^img/(?P<img_file>.*)$', views.img, name='img'),
    re_path(r'^style/(?P<style_file>.*)$', views.style, name='style'),

    re_path(r'^index/(?P<index_file>.*)$', views.get_index, name='get_index'),

    # 通过正则表达式添加kind_id和area_id字段，从前台获取页面选择的当前项
    re_path(r'^Movies_Tags/(?P<kind_id>(\d+))&&(?P<area_id>(\d+))$', views.Movies_Tags, name='Movies_Tags'),
    re_path(r'^recommend/$', views.recommend, name='recommend'),

    re_path(r'^RankingList/$', views.RankingList, name='RankingList'),
    re_path(r'^get_description/(?P<img_file>.*)$', views.get_description, name='get_description'),

    re_path(r'^about/$', views.about, name='about'),
    re_path(r'^search/$', views.search, name='search'),

    #使用Json文件时的测试路径
    # re_path(r'^allimages/$', views.get_Allimgfiles, name='get_Allimgfiles'),
    # re_path(r'^images/$', views.images, name='images'),
    # re_path(r'^Jokerdescribe/$', views.Jokerdescribe, name='Jokerdescribe'),

    #测试路径
    re_path(r'^video_resp/$', views.stream_video, name='stream_video'),
    re_path(r'^video/$', views.video, name='video'),
    re_path(r'^test/$', views.test, name='test'),

    

]
