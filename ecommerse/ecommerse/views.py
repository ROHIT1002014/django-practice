from django.shortcuts import render
from django.template.response import TemplateResponse
from productInfo.models import Item

def homePage(request):
  products = Item.objects.all()[:4]
  context = {'product_list': products, 'title': 'Product list'}
  # return TemplateResponse(request, 'entry_list.html', {'entries': Entry.objects.all()})
  return TemplateResponse(request, 'home.html', context)
