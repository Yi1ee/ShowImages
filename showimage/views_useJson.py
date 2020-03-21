from django.shortcuts import render     # 可以用来返回我们渲染的html文件
from django.http import HttpResponse,Http404        # 可以返回渲染的页面
from django.contrib import messages
import os
import json


# Create your views here.

imagespath = "C:\\project\\ShowImages\\static_files\\poster_images"
stylespath = "C:\\project\\ShowImages\\static_files\\CSS"
description_path="C:\\project\\ShowImages\\static_files\\description_files"
resultfile =description_path + "\\" + 'result.json'
index_path="C:\\project\\ShowImages\\static_files\\index_files"

def get_Jsonfile():
    '''获取json文件中的内容'''
    filename =description_path + "\\" + 'movies_description.json'
    with open(filename, encoding="utf-8") as file_object:
        content = json.load(file_object)
    return content


def index(request):
    '''显示界面主页'''
    return render(request,'showimage/index.html')

def get_index(request,index_file):
    '''某一特定海报的界面'''
    filepath =index_path + "\\"+ index_file
    with open(filepath, 'rb') as f:
        index_data = f.read()
    return HttpResponse(index_data, content_type="image/jpg")

def about(request):
    '''显示about界面'''
    return render(request,'showimage/about.html')

def get_Allimgfiles(request):
    '''从json文件中获取所有的电影内容,并显示所有的电影'''
    content= get_Jsonfile()
    movies = content["movies"]
    context = {'movies':movies}
    return render(request,'showimage/allimages.html',context)

def img(request,img_file):
    '''某一特定海报的界面'''
    imagepath =imagespath + "\\"+ img_file
    with open(imagepath, 'rb') as f:
            image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpg")

def style(request,style_file):
    '''界面CSS返回'''
    stylepath =stylespath + "\\"+ style_file
    with open(stylepath, 'rb') as f:
            style_data = f.read()
    return HttpResponse(style_data, content_type="text/css")


def get_description(request, img_file):
    '''获取每个电影中的对该电影的描述'''
    content = get_Jsonfile()
    for itMovie in content["movies"]:
        if itMovie["file"] == img_file:
            context = {'itMovie':itMovie}
    if context == None:
        raise Http404
    return render(request,'showimage/get_description.html',context)

def Jokerdescribe(request):
    '''Leon相关具体描述'''
    return render(request,'showimage/Jokerdescribe.html')

def search(request):
    q=request.GET.get('q')
    content = get_Jsonfile()
    search_result={'movies':[]}
    #创建一个新的JSON对象result存储搜索结果
    for itMovie in content["movies"]:
        if q in itMovie["name"]:
            search_result['movies'].append(itMovie)
    #此处实际上不需要写入到新的JSON文件中，可直接使用result对象
    # with open(resultfile, mode="w", encoding="utf-8") as file_object:
    #     json.dump(search_result,file_object,ensure_ascii=False)
    movies_result=search_result['movies']
    context = {'movies_result':movies_result}
    return render(request,'showimage/result.html',context)

