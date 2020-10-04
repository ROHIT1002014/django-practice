from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import addProduct, allProducts, productDetail

urlpatterns = [
    path('/list', allProducts, name='product_list'),
    path('/<int:id>', productDetail, name='product_detail'),
    path('/new', addProduct, name='add_product'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

