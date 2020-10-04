from django.shortcuts import render
from django.template.response import TemplateResponse

def homePage(request):
  # return TemplateResponse(request, 'entry_list.html', {'entries': Entry.objects.all()})
  return TemplateResponse(request, 'index.html')
