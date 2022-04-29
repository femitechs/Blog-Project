from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    category = models.ForeignKey(Category, related_name='post', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='posts/%y/%m/%d', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return f'Title: {self.title}, with ID: {self.id}'
    
    def get_absolute_url(self):
        return reverse('blog:details',
                        args=[
                              self.publish.year,
                              self.publish.month,
                              self.publish.day, self.slug])


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return f'Comment by {self.name} on {self.post}'
