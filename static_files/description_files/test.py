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


resultfile = description_path + "\\" + 'result.json'
q=input("关键字：")
content=get_Jsonfile()
movies = content["movies"]
movies_result = {'movies':[]}
for itMovie in movies:
    if q in itMovie["name"]:
       movies_result['movies'].append(itMovie)
with open(resultfile,mode="w",encoding="utf-8") as file_object:
    json.dump(movies_result,file_object,ensure_ascii=False)

