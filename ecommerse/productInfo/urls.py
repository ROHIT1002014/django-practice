from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import homePage, addProduct, allProducts

urlpatterns = [
    path('', homePage, name='home'),
    path('add-product/', addProduct, name='addProduct'),
    path('product-list/', allProducts, name='productList'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

