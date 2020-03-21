from django.shortcuts import render     # 可以用来返回我们渲染的html文件
from django.http import HttpResponse,Http404        # 可以返回渲染的页面
from django.contrib import messages
import os
import json

from .models import All_movies   # 导入所有电影的模型类
from .models import Top_movies   # 导入高分排行榜电影的模型类
from .models import Heat_movies  # 导入本月热度排行榜电影的模型类

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

def AllMovies(request):
    all_movies_list = All_movies.objects.filter()
    context= {'all_movies_list':all_movies_list}
    return render(request,'showimage/AllMovies.html',context)

def RankingList(request):
    top_movies_list = Top_movies.objects.filter()
    heat_movies_list = Heat_movies.objects.filter()
    context= {'top_movies_list':top_movies_list,'heat_movies_list':heat_movies_list}
    return render(request,'showimage/RankingList.html',context)

def get_description(request, img_file):
    '''返回点击某个特定电影后的对该电影更为具体描述的界面'''
    all_movies_list = All_movies.objects.filter()
    for itMovie in all_movies_list:
        if itMovie.filename == img_file:
            '''电影海报唯一，根据文件定位特定内容'''
            context = {'itMovie':itMovie}
    if context == None:
        raise Http404
    return render(request,'showimage/get_description.html',context)

def search(request):
    q=request.GET.get('q')
    #content = get_Jsonfile()
    all_movies_list = All_movies.objects.filter()

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


