from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from .models import BlogPost
from django.http import Http404

# Create your views here.
def homePageView(request):
  title = 'Hello there ...'

  context = {'title' : title, 'my_list': [1,2,3,4,5]}
  template = 'home.html'
  return render(request, template, context)

def aboutPageView(request):
  title = 'Hello there this is about page ...'

  context = {'title' : title}
  template = 'home.html'
  template_object = get_template(template)
  rendered_item = template_object.render(context)
  return HttpResponse(rendered_item)

def blogDetail(request, slug):

  blog_detail = get_object_or_404(BlogPost, slug=slug)

  # try:
  #   blog_detail = BlogPost.objects.get(id=str(blog_id)) # take str datatype to remove value error
  # except BlogPost.DoesNotExist:
  #   raise Http404
  # except ValueError:
  #   raise Http404

  context = {'blog_detail' : blog_detail }
  template = './blogs/blogDetail.html'
  template_object = get_template(template)
  rendered_item = template_object.render(context)
  return HttpResponse(rendered_item)