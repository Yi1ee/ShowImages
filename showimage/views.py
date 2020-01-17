from django.shortcuts import render
from django.http import HttpResponse
import os
import json

# Create your views here.

imagespath = "C:\\project\\ShowImages\\static_files\\poster_images"
description_path="C:\\project\\ShowImages\\static_files\\description_files"

def get_Jsonfile():
    '''获取json文件中的内容'''
    filename =description_path + "\\" + 'movies_description.json'
    with open(filename, encoding="utf-8") as file_object:
        content = json.load(file_object)
    return content


def index(request):
    '''显示界面主页'''
    return render(request,'showimage/index.html')


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


def get_description(request, img_file):
    '''获取每个电影中的对该电影的描述'''
    content = get_Jsonfile()
    for itMovie in content["movies"]:
        if itMovie["file"] == img_file:
            it_file = itMovie["file"]
            it_name = itMovie["name"]
            it_releasetime = itMovie["releasetime"]
            it_director = itMovie["director"]
            it_type = itMovie["type"]
            it_Synopsis = itMovie["Synopsis"]
    
    context = {
        'content':content,
        'movie_file':it_file,
        'movie_name':it_name,
        'movie_releasetime':it_releasetime,
        'movie_type':it_type,
        'movie_director':it_director,
        'movie_Synopsis':it_Synopsis,
        }
    return render(request,'showimage/get_description.html',context)

def Jokerdescribe(request):
    '''Leon相关具体描述'''
    return render(request,'showimage/Jokerdescribe.html')
