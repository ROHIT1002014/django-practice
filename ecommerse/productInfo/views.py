from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from .models import Item
from .form import CreateProduct
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404

def productDetail(request, id):
  queryset = Item.objects.filter(id=id)
  template_name = 'product/product_detail.html'
  if queryset.count() == 0:
    raise Http404
  else:
    product = queryset.first()
    context={'title': 'Welcome to You Blog','product': product}
  return render(request, template_name, context)


@login_required(login_url='/account/login/')  # bcs default it take url like accounts/login
def addProduct(request):
  # if request.user.is_authenticated:
    if request.method == 'POST':
      form = CreateProduct(request.POST, request.FILES) # if we use file the request.FILE must be added
      # print(form.errors)
      # print(form.is_valid())
      if form.is_valid():
        print('form is valid')
        form.save()
        return redirect('product_list')
    else:
      print('invalid request')
      form = CreateProduct()
      return render(request, 'product/addProduct.html', {'form': form })
  # else:
  #   return redirect('login')

@login_required(login_url='/account/login/')
def allProducts(request):
  products = Item.objects.all()
  return TemplateResponse(request, 'product/products.html', {'products': products})
