from django.db import models

# Create your models here.

# 电影地区分类
class Area(models.Model):
    area = models.CharField(max_length=20,unique=True)
    movie = models.ManyToManyField(to='MoviesForm')

    class Meta:
        db_table = 'Area'

    def __str__(self):
        return self.area

# 电影类型分类
class Kind(models.Model):
    kind = models.CharField(max_length=5,unique=True)
    movie = models.ManyToManyField(to='MoviesForm')

    class Meta:
        db_table = 'Kind'

    def __str__(self):
        return self.kind


# 创建所有电影的模型类
class MoviesForm(models.Model):
    movie_id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=10,null=True)
    cname = models.CharField(max_length=30)
    enname = models.CharField(null=True,max_length=50)
    releasetime = models.CharField(max_length=20)
    runtime = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    types = models.CharField(max_length=10)
    actors = models.CharField(max_length=50)
    score = models.CharField(max_length=5)
    introduction = models.CharField(max_length=500)
    location = models.CharField(max_length=30)

    class Meta:
        db_table = 'MoviesForm'

    def __str__(self):
        #重写直接输出类的方法
        return "<MoviesForm:{movie_id=%s,filename=%s,cname=%s,enname=%s,releasetime=%s,\
                runtime=%s,director=%s,types=%s,actors=%s,score=%s,introduction=%s,location=%s}>"\
               %(self.movie_id,self.filename,self.cname,self.enname,self.releasetime,\
                self.runtime,self.director,self.types,self.actors,self.score,self.introduction,self.location)

    



# 创建所有电影的模型类
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
    introduction = models.CharField(max_length=500)
    location = models.CharField(max_length=30)
    def __str__(self):
        #重写直接输出类的方法
        return "<All_movies:{movie_id=%s,filename=%s,cname=%s,enname=%s,releasetime=%s,\
                runtime=%s,director=%s,types=%s,actors=%s,score=%s,introduction=%s,location=%s}>"\
               %(self.movie_id,self.filename,self.cname,self.enname,self.releasetime,\
                self.runtime,self.director,self.types,self.actors,self.score,self.introduction,self.location)

# 创建高分排行榜TOP10电影的模型类
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
 
# 创建热度排行榜TOP10电影的模型类
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


