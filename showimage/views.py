from django.shortcuts import render     # 可以用来返回我们渲染的html文件
from django.http import HttpResponse,Http404        # 可以返回渲染的页面
from django.contrib import messages
import os
import json
import logging

logger = logging.getLogger("django")

from .models import Top_movies   # 导入高分排行榜电影的模型类
from .models import Heat_movies  # 导入本月热度排行榜电影的模型类
from .models import Animation_movies  # 导入动画电影排行榜电影的模型类

from .models import MoviesForm   
from .models import Kind         # 导入电影类型的模型类
from .models import Area         # 导入电影地区的模型类


# Create your views here.

imagespath = "C:\\project\\ShowImages\\static_files\\poster_images"
stylespath = "C:\\project\\ShowImages\\static_files\\CSS"
description_path="C:\\project\\ShowImages\\static_files\\description_files"
resultfile =description_path + "\\" + 'result.json'
index_path="C:\\project\\ShowImages\\static_files\\index_files"


def index(request):
    '''显示界面主页'''
    return render(request,'showimage/index.html')

def about(request):
    '''显示about界面'''
    return render(request,'showimage/about.html')

def RankingList(request):
    top_movies_list = Top_movies.objects.filter()
    heat_movies_list = Heat_movies.objects.filter()
    animation_movies_list = Animation_movies.objects.filter()
    context= {'top_movies_list':top_movies_list,'heat_movies_list':heat_movies_list,'animation_movies_list':animation_movies_list}
    return render(request,'showimage/RankingList.html',context)

def get_description(request, img_file):
    '''返回点击某个特定电影后的对该电影更为具体描述的界面'''
    movies_list = MoviesForm.objects.filter()
    for itMovie in movies_list:
        if itMovie.filename == img_file:
            '''电影海报唯一，根据文件定位特定内容'''
            context = {'itMovie':itMovie}
    if context == None:
        raise Http404
    return render(request,'showimage/get_description.html',context)

def search(request):
    q=request.GET.get('q')
    #content = get_Jsonfile()
    all_movies_list = MoviesForm.objects.filter()

    search_result={'movies':[]}
    #创建一个新的JSON对象result存储搜索结果
    for itMovie in all_movies_list:
        if q in itMovie.cname:
            search_result['movies'].append(itMovie)
    movies_result=search_result['movies']
    context = {'movies_result':movies_result}
    return render(request,'showimage/result.html',context)



def get_index(request,index_file):
    '''获取首页轮播海报图片'''
    filepath =index_path + "\\"+ index_file
    with open(filepath, 'rb') as f:
        index_data = f.read()
    return HttpResponse(index_data, content_type="image/jpg")

def img(request,img_file):
    '''获取某一特定电影的海报图片'''
    imagepath =imagespath + "\\"+ img_file
    with open(imagepath, 'rb') as f:
            image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpg")

def style(request,style_file):
    '''返回界面的CSS'''
    stylepath =stylespath + "\\"+ style_file
    with open(stylepath, 'rb') as f:
            style_data = f.read()
    return HttpResponse(style_data, content_type="text/css")



def Movies_Tags(request, *args, **kwargs):
    '''全部电影界面以及分类功能'''
    # 初始化传递参数，若无传参则代表要显示全部的电影
    if not kwargs:
        kwargs = {
            'kind_id':0,
            'area_id':0,
        }

    for k, v in kwargs.items():
        temp = int(v)
        kwargs[k] = temp

    # 从kwargs中取出相应的id
    kind_id = kwargs.get('kind_id')
    area_id = kwargs.get('area_id')

    # 从数据库中取出所有的Kind和area列表，因为所有分类都要在页面上显示
    kind_list = Kind.objects.all()
    area_list = Area.objects.all()

    if kind_id == 0:
        if area_id == 0:
            movies_list = MoviesForm.objects.filter()
        else:
            area_obj = Area.objects.get(id=area_id)
            movies_list = area_obj.movie.all()
    else:
        if area_id == 0:
            kind_obj = Kind.objects.get(id=kind_id)
            movies_list = kind_obj.movie.all()
        else:
            kind_obj = Kind.objects.get(id=kind_id)
            movies_list_kind = kind_obj.movie.all()
            area_obj = Area.objects.get(id=area_id)
            movies_list_area = area_obj.movie.all()
            #返回的是两个Queryset的交集并去掉重复值，如是需要返回交集把&替换为|即可
            movies_list = (movies_list_kind & movies_list_area).distinct()
            #logger.error("*********************yilee*****************", movies_list)

    return render(
        request,
        'showimage/Movies_Tags.html',
        {
            'kind_list': kind_list,
            'area_list': area_list,
            'kwargs': kwargs,
            'movies_list': movies_list,
        }
    )

