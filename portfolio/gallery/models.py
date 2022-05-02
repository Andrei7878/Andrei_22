from django.db import models
class Category(models.Model):
    name = models.CharField(max_length = 20)

class Gallery(models.Model):
    title = models.CharField(max_length = 255)
    body = models.TextField()
    image = models.ImageField(upload_to='img/')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modifield = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='gallery')
