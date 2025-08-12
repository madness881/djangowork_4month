from django.db import models
"""
create table post(id integer primary key autoincrement not null, title varchar(256) not null, content varchar(512))
"""

"""
select *  from posts ==> Post.object.all()
"""

"""
select * from posts where title ILIKE '%p%" ==> Post.objects.filter(title_icontains='probably')
"""
"""
select 1 from posts where id = 123 ==> Post.object.get(id=123) 
"""

class Category(models.Model):
    name = models.CharField(max_length=256)



class Tag(models.Model):
    name = models.CharField(max_length=56)
    
    def __str__(self):
       return self.name 

class Post(models.Model):
    image = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=512, null= True, blank=True)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    tags = models.ManyToManyField(Tag)
    
    def __str__(self):
        return self.title