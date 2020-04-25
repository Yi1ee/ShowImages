from django.shortcuts import render     # 可以用来返回我们渲染的html文件
from django.http import HttpResponse,Http404        # 可以返回渲染的页面
from django.contrib import messages
from django.utils import timezone   #引入timezone模块
from datetime import datetime

import os
import json
import logging
import random
from django.db.models import Q   # Queryset结果   

logger = logging.getLogger("django")

from .models import Top_movies   # 导入高分排行榜电影的模型类
from .models import Heat_movies  # 导入本月热度排行榜电影的模型类
from .models import Animation_movies  # 导入动画电影排行榜电影的模型类

from .models import MoviesForm   # 导入包含分类标签的全部电影的模型类
from .models import Kind         # 导入电影类型的模型类
from .models import Area         # 导入电影地区的模型类
from .models import Ranking_movies

# Create your views here.

imagespath = "C:\\project\\ShowImages\\static_files\\poster_images"
stylespath = "C:\\project\\ShowImages\\static_files\\CSS"
index_path="C:\\project\\ShowImages\\static_files\\index_files"



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


def index(request):
    '''显示界面主页'''
    return render(request,'showimage/index.html')

def get_index(request,index_file):
    '''获取首页轮播海报图片'''
    filepath =index_path + "\\"+ index_file
    with open(filepath, 'rb') as f:
        index_data = f.read()
    return HttpResponse(index_data, content_type="image/jpg")


def about(request):
    '''显示about界面'''
    return render(request,'showimage/about.html')


def RankingList(request):
    # 获取高分电影TOP榜
    top_movies_list = Top_movies.objects.filter()
    movies_list = Ranking_movies.objects.filter()
    # 获取热度电影TOP10
    heat_movies_list = movies_list[:10]
    # 获取动画电影TOP10
    animation_movies_list = movies_list[10:20]
    context= {'top_movies_list':top_movies_list,'heat_movies_list':heat_movies_list,'animation_movies_list':animation_movies_list}
    return render(request,'showimage/RankingList.html',context)


def get_description(request, img_file):
    '''返回点击某个特定电影后的对该电影更为具体描述的界面'''
    # all_movies_list = MoviesForm.objects.filter()
    # for itMovie in all_movies_list:
    #     if itMovie.filename == img_file:
    #         '''电影海报唯一，根据文件定位特定内容'''
    #         context = {'itMovie':itMovie}
    # 有关电影描述的内容除了全部电影外还需要加入榜单里面的电影，所以需要更改查找方式
    all_movies_list = MoviesForm.objects.filter(filename__exact = img_file)
    '''电影海报唯一，根据文件定位特定内容'''
    if all_movies_list.exists():
        itMovie = all_movies_list[0]
    else :
        ranking_movies_list = Ranking_movies.objects.filter(filename__exact = img_file)
        itMovie = ranking_movies_list[0]
    context = {'itMovie':itMovie}
    if context == None:
        raise Http404
    return render(request,'showimage/get_description.html',context)

def search(request):
    q=request.GET.get('q')
    '''获取只要满足其中一个条件的所有电影'''
    movies_list = MoviesForm.objects.filter(Q(cname__contains = q)|Q(actors__contains = q)|Q(director__contains = q))
    actors_list = MoviesForm.objects.filter(actors__contains = q)
    director_list = MoviesForm.objects.filter(director__contains = q)
    # search_result={'movies':[]}
    # 创建一个新的JSON对象result存储搜索结果
    # for itMovie in all_movies_list:
    #     if q in itMovie.cname:
    #         search_result['movies'].append(itMovie)
    # movies_result=search_result['movies']
    # context = {'movies_result':movies_result}
    # logger.error("*********************yilee*****************", actors_list  )
    context = {
        'movies_list':movies_list,
        "actors_list":actors_list,
        "director_list":director_list,
        "q":q
    }
    return render(request,'showimage/result.html',context)



def Movies_Tags(request, *args, **kwargs):
    '''显示全部电影界面以及所带的分类功能'''
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
            # 返回的是两个Queryset的交集并去掉重复值，如是需要返回并集把&替换为|即可
            movies_list = (movies_list_kind & movies_list_area).distinct()
            # logger.error("*********************yilee*****************", movies_list)
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


def recommend(request):
    '''显示今日推荐页面'''
    # num1:获取的是今天是今年的第num1天
    # num1 = dt.strftime( '%j' ) 
    # month1 ：获取的是月份英文全拼%B
    # month1 = dt.strftime( '%B' ) 
    # dt获取系统当前时间
    dt = datetime.now()
    year = datetime.now().year
    month = datetime.now().month
    day = datetime.now().day
    
    movie_list = MoviesForm.objects.filter(movie_id__exact = day)
    itMovie = movie_list[0]
    # logger.error("*********************yilee*****************", num1)

    return render(
        request,
        'showimage/recommend.html',
        {
            'year':year,
            'month':month,
            'day':day,
            'itMovie':itMovie,
        }
    )
