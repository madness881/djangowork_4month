from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    image = models.ImageField(null = True, blank=True)
    title = models.CharField(max_length=100)
    content = models.CharField(max_length=300, null=True, blank=True)
    rate = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True, null=True)
    updated = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, null=True)
    tags = models.ManyToManyField(Tag, blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()   
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author}"