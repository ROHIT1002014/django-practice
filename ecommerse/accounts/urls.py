from django.urls import path
from .views import registration_from


urlpatterns = [
    path('registration/', registration_from, name="registration"),
]
