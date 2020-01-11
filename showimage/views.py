from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    '''显示界面主页'''
    return render(request,'showimage/index.html')

def img(request,img_file):
    '''获取某一特定界面'''
    imagepath = "C:\\project\\ShowImages\\images"
    imagepath += "\\"+ img_file
    with open(imagepath, 'rb') as f:
            image_data = f.read()
    return HttpResponse(image_data, content_type="image/jpg")

def images(request):
    '''显示界面主页'''
    return render(request,'showimage/images.html')

def Leondescribe(request):
    '''Leon相关具体描述'''
    return render(request,'showimage/Leondescribe.html')

def Jokerdescribe(request):
    '''Leon相关具体描述'''
    return render(request,'showimage/Jokerdescribe.html')