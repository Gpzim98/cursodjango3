from django.shortcuts import render
from .models import Post, Contact


def hello_blog(request):
    lista = [
        'Django', 'Python', 'Git', 'Html', 
        'Banco de dados', 'Linux', 'Nginx', 'Uwsgi',
        'Systemctl'
    ]
    list_posts = Post.objects.filter(deleted=False)

    data = {
        'name': 'Curso de Django 3', 
        'lista_tecnologias': lista, 
        'posts': list_posts }

    return render(request, 'index.html', data)

def post_detail(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post_detail.html', {'post': post})

def save_form(request):
    name = request.POST['name']
    Contact.objects.create(
        name=name, 
        email=request.POST['email'],
        message=request.POST['message']    
    )
    return render(request, 'contact_success.html', {'name_contact': name})
