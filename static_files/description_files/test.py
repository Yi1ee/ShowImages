import json

description_path="C:\\project\\ShowImages\\static_files\\description_files"
imagespath = "C:\\project\\ShowImages\\static_files\\poster_images"


def traversal_imgfiles(request):
    '''遍历图片文件夹下的所有图片'''
    img_list=[]
    list_imgfiles = os.listdir(imagespath) #列出文件夹下所有的目录与文件
    list_imgfiles.sort(key = lambda x:int(x[:-4]))#返回的文件列表不是有序的，需要将字典中的文件进行排序
    context = {'list_imgfiles':list_imgfiles}
    return context


def get_Jsonfile():
    filename =description_path + "\\" + 'movies_description.json'
    with open(filename, encoding="utf-8") as file_object:
        content = json.load(file_object)
    return content



img_list = []
content=get_Jsonfile()
for itmovie in content["movies"]:
    itmovie
    img_list.append(itmovie["name"])

print(img_list[1])