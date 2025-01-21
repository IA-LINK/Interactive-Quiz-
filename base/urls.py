from django.urls import path
from . import views # . for current directory


urlpatterns = [
    path('', views.home)
]
