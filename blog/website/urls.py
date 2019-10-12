from django.urls import path, include
from .views import hello_blog
from .views import post_detail, save_form

urlpatterns = [
    path('', hello_blog, name='home_blog'),
    path('post/<int:id>/', post_detail, name='post_detail'),
    path('save-form/', save_form, name='save_form'),
]
