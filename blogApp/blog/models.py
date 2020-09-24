from django.db import models

# Create your models here.
class BlogPost(models.Model):
  title = models.TextField()
  content = models.TextField(blank=True, null=True)
  slug = models.SlugField() # hello rohit -> hello-rohit