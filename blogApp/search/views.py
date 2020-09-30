from django.shortcuts import render
from .models import Search
from blog.models import BlogPost

# Create your views here.
def search_view(request):
  query = request.GET.get('query', None)
  user = None

  if request.user.is_authenticated:
    user = request.user

  context={'query': query}

  if query is not None:
    Search.objects.create(user=user, query=query)
    blog_list = BlogPost.objects.search(query=query)
    context['blog_list'] = blog_list
  template = './searches/search_view.html'
  return render(request, template, context)
