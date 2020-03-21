from django.db import models

# Create your models here.

#创建所有电影的模型类
class All_movies(models.Model):
    movie_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=10,null=True)
    cname = models.CharField(max_length=30)
    enname = models.CharField(null=True,max_length=50)
    releasetime = models.CharField(max_length=20)
    runtime = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    types = models.CharField(max_length=10)
    actors = models.CharField(max_length=30)
    score = models.CharField(max_length=5)
    introduction = models.CharField(max_length=500,default='')
    # movie_year = models.CharField(max_length=4)
    # score_integer = models.CharField(max_length=3)
    # score_fraction = models.CharField(max_length=3)

    def __str__(self):
        #重写直接输出类的方法
        return "<All_movies:{movie_id=%s,filename=%s,cname=%s,enname=%s,releasetime=%s,\
                runtime=%s,director=%s,types=%s,actors=%s,score=%s}>"\
               %(self.movie_id,self.filename,self.cname,self.enname,self.releasetime,\
                self.runtime,self.director,self.types,self.actors,self.score,self.introduction)
 

class Top_movies(models.Model):
    top_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=10,null=True)
    cname = models.CharField(max_length=30)
    enname = models.CharField(null=True,max_length=50)
    score_integer = models.CharField(max_length=3)
    score_fraction = models.CharField(max_length=3)

    def __str__(self):
        #重写直接输出类的方法
        return "<Top_movies:{top_id=%s,filename=%s,cname=%s,enname=%s,score_integer=%s,score_fraction=%s}>"\
               %(self.top_id,self.filename,self.cname,self.enname,self.score_integer,self.score_fraction)
 

class Heat_movies(models.Model):
    top_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=10,null=True)
    cname = models.CharField(max_length=30)
    enname = models.CharField(null=True,max_length=50)
    releasetime = models.CharField(max_length=20)
    types = models.CharField(max_length=10)
    director = models.CharField(max_length=20)
    actors = models.CharField(max_length=30)

    def __str__(self):
        #重写直接输出类的方法
        return "<Heat_movies:{top_id=%s,filename=%s,cname=%s,enname=%s,releasetime=%s,\
               types=%s,director=%s,actors=%s}>"\
               %(self.top_id,self.filename,self.cname,self.enname,self.releasetime,\
                self.types,self.director,self.actors)
 
