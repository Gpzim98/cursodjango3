from django.urls import path, include
from .views import hello_blog

urlpatterns = [
    path('', hello_blog),
]
