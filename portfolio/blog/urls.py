
from django.urls import path,include
from .models import Blog

from . import views
urlpatterns = [
    path('', views.blogs),
]