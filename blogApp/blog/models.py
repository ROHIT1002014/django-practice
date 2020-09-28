from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.
class BlogPost(models.Model): # blogpost_set -> queryset  i.e. it will give object to perform query like fetching data, updating data etc for current user
  user = models.ForeignKey(User, default=1, null= True, on_delete=models.SET_NULL) # i.e. when user is deleted then this class will exist
  title = models.TextField()
  content = models.TextField(blank=True, null=True)
  slug = models.SlugField(unique=True) # hello rohit -> hello-rohit

  def get_absolute_url(self):
    return f"/blog/{ self.slug }"

  def get_edit_url(self):
    pattern = self.get_absolute_url()
    return f"{ pattern }/edit"

# for more detail https://github.com/comargo/milkshop/blob/master/helpers/models.py

  def get_delete_url(self):
    pattern = self.get_absolute_url()
    return f"{ pattern }/delete"

