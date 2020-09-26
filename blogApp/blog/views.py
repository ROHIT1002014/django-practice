from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from .models import BlogPost
from django.http import Http404
from .form import BlogPostForm, BlogPostModelForm

from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required

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

# to handle page not found error and to be safe from anonymouse user without using decorator
# if not request.user.is_authenticated:
#   return render(request, 'not_a_user.html',{  })

# @login_required
@staff_member_required
def blog_create_view(request):
  title = 'New Blog'

  # blow code is model form which is due to blog model in models.py
  # form = BlogPostModelForm(request.POST or None)
  # if form.is_valid():
  #   obj =form.save(commit=False) # commit bcs at this point we don't want to save form
  #   obj.title = form.cleaned_data['title'] + "kumar verma"
  #   obj.save()
  #   form = BlogPostModelForm()

  form = BlogPostForm(request.POST or None )

  if form.is_valid():
    # print(form.cleaned_data)
    # title = form.cleaned_data['title']
    # obj = BlogPost.objects.create(title=title) #this is used for adding only selected field into model

    obj = BlogPost.objects.create(**form.cleaned_data) # by this all element's data are being come
    # print(obj.user) it will print admin which is default so we have to assign current user
    obj.user = request.user  # assigning the current user
    form = BlogPostForm()
    obj.save()

  template = './blogs/form.html'
  context = {'form' : form, 'title' : title }

  # template_object = get_template(template)
  # rendered_item = template_object.render(context)
  # return HttpResponse(rendered_item) # this is not returning form with csrf token so we have to use render method
  return render(request, template, context)

def blog_detail_view(request, slug):
  # print(slug)
  queryset = BlogPost.objects.filter(slug = slug) # it will give list of object with matches slug
  # print(queryset.first()) # it will print first object in object list
  # print(queryset.last()) # it will priint last object in object list
  # print(queryset[2]) # it will print selected object in object list

  # if queryset.count() >= 1:
  #   blog_detail = queryset.first()
  # else:
  #   raise Http404

  if queryset.count() == 0:
    raise Http404
  else:
    blog_detail = queryset.first()

  # blog_detail = queryset.first()

  # blog_detail = get_object_or_404(BlogPost, id=1)

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

def blog_list_view(request):
  blog_list = BlogPost.objects.all()
  print(blog_list)
  context = {'blog_list' : blog_list }
  template = './blogs/blogList.html'
  template_object = get_template(template)
  rendered_item = template_object.render(context)
  return HttpResponse(rendered_item)

@staff_member_required
def blog_update_view(request, slug):
  queryset = get_object_or_404(BlogPost, slug = slug)
  form = BlogPostModelForm(request.POST or None, instance=queryset)

  if form.is_valid():
    form.save()
    return redirect('/')

  context = {'form': form, 'title': 'Update blog'}
  # template = './blogs/blogUpdate.html' #  rather than this  we can also use form.html
  template = './blogs/form.html'
  return render(request, template, context)

def blog_retrieve_view(request, slug):
  context = {'form': None }
  template = './blogs/blogretrieved.html'
  return render(request, template, context)

@staff_member_required
def blog_delete_view(request, slug):
  queryset = get_object_or_404(BlogPost, slug = slug)
  if request.method == 'POST':
    queryset.delete()
    redirect ('/')
  context = {'blog_detail': queryset}
  template = './blogs/blogDelete.html'
  return render(request, template, context)
