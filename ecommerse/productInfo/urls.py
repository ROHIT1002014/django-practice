from django.urls import path
from .views import homePage, addProduct
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', homePage, name='home'),
    path('add-product/', addProduct, name='addProduct'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

