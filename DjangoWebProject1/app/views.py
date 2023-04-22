"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

from django.db import models
from .models import Blog
from .forms import BlogForm

def blog(request):
    """Renders the blog page."""

    posts = Blog.objects.all()
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог',
            'posts': posts,
            'year':datetime.now().year,
        }
    )

def blogpost(request, parametr):
    """Renders the blog page."""

    post_1 = Blog.objects.get(id=parametr)
    
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1':post_1,
            'year':datetime.now().year,
            }
    )


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def videopost(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Video', 
            'year':datetime.now().year,
        }
    )

def registration(request): 
    """Renders the registration page."""
    if request.method == "POST": 
        regform = UserCreationForm(request.POST) 
        if regform.is_valid():
            reg_f = regform.save(commit=False) 
            reg_f.is_staff = False
            reg_f.is_active = True 
            reg_f.is_superuser = False 
            reg_f.date_joined = datetime.now()
            reg_f.last_login = datetime.now()
            regform.save() 
            return redirect('home')
    else: 
        regform = UserCreationForm() 
    
    assert isinstance(request, HttpRequest) 
    return render(
        request,
        'app/registration.html',
        {
            'regform': regform,
            'year':datetime.now().year,  
        }
    )
def newpost(request):
    """Renders the newpost page."""
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        blogform = BlogForm(request. POST, request.FILES)
        if blogform.is_valid():
            blog_f = blogform.save(commit=False)
            blog_f.posted = datetime.now()
            blog_f.autor = request.user
            blog_f.save()
            return redirect('blog') 
    else:
        blogform = BlogForm()

    return render(
    request,
    'app/newpost.html',
    {
        'blogform': blogform,
        'title': 'Добавить статью блога',
        # передача формы в шаблон веб-страницы
        'year': datetime.now().year,
    }
)