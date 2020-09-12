from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Item
from .form import CreateProduct
from django.shortcuts import redirect


def homePage(request):
  # return TemplateResponse(request, 'entry_list.html', {'entries': Entry.objects.all()})
  return TemplateResponse(request, 'index.html')

def addProduct(request):
  if request.method == 'POST':
    form = CreateProduct(request.POST, request.FILES) # if we use file the request.FILE must be added
    # print(form.errors)
    # print(form.is_valid())
    if form.is_valid():
      print('form is valid')
      form.save()
      return redirect('productList')
  else:
    print('invalid request')
    form = CreateProduct()
    return TemplateResponse(request, 'product/addProduct.html', {'form': form })

def allProducts(request):
  products = Item.objects.all()
  return TemplateResponse(request, 'product/products.html', {'products': products})
