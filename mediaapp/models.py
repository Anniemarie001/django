from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
  Author = models.ForeignKey(User, on_delete=models.CASCADE)
  text = models.CharField(max_length=255)
  
  
class Comment(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

  