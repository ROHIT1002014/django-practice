from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class BlogPostQuerySet(models.QuerySet):
  def published(self):
    now = timezone.now()
    # get query set means data object like BlogPost.objects.all()
    return self.filter(publish_date__lte=now)

  def search(self, query):
    lookup = (
                Q(title__icontains=query) |
                Q(content__icontains=query) |
                Q(slug__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query) |
                Q(user__username__icontains=query)
              )

    return self.filter(title__icontains=query)  # if we want to search in content then content__icontains  or if we want exact then title__iexact and for complex query used lookups

# Model manager to handle queary set
class BlogPostManager(models.Manager):
  def get_queryset(self):
    # get query set means data object like BlogPost.objects.all()
    return BlogPostQuerySet(self.model, using=self._db)

  def published(self):
    return self.get_queryset().published()

  def search(self, query=None):
    if query is None:
      return self.get_queryset().none()
    return self.get_queryset().published().search(query)

class BlogPost(models.Model): # blogpost_set -> queryset  i.e. it will give object to perform query like fetching data, updating data etc for current user
  user = models.ForeignKey(User, default=1, null= True, on_delete=models.SET_NULL) # i.e. when user is deleted then this class will exist
  image = models.ImageField(upload_to= settings.MEDIA_ROOT, blank=True, null=True)
  title = models.TextField()
  content = models.TextField(blank=True, null=True)
  slug = models.SlugField(unique=True) # hello rohit -> hello-rohit
  publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null = True, blank = True)
  timestamp = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=False)

  objects = BlogPostManager()

  class Meta:
    ordering = ['-publish_date', '-updated', '-timestamp']

  def get_absolute_url(self):
    return f"/blog/{ self.slug }"

  def get_edit_url(self):
    pattern = self.get_absolute_url()
    return f"{ pattern }/edit"

# for more detail https://github.com/comargo/milkshop/blob/master/helpers/models.py

  def get_delete_url(self):
    pattern = self.get_absolute_url()
    return f"{ pattern }/delete"

  def __str__(self):
        return self.title

