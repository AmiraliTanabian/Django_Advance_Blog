from django.contrib.auth.models import User
from django.db import models



class Post(models.Model):
    banner = models.ImageField(null=True, blank=True, upload_to='blog-banner')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    text = models.TextField()
    category = models.ForeignKey('PostCategory', on_delete=models.SET_NULL, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

class PostCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name