from django.shortcuts import render,redirect
from .models import Blog
#from .forms import BlogForm
#from django.views.generic.edit
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, UpdateView

class Getlist(ListView):
    model=Blog
    template_name='news/news.html'

class Getdetail(DetailView):
    model=Blog
    template_name='news/detail.html'

class Getcreate(CreateView):
    model=Blog
    success_url='/news/'
    template_name='news/create.html'
    fields = ['title', 'text', 'date']

class Getdelete(DeleteView):
    model=Blog
    success_url='/news/'
    template_name='news/delete.html'    

class Getupdate(UpdateView):
    model=Blog
    success_url='/news/<int:pk>'
    template_name='news/update.html' 
    fields = ['title', 'text', 'date'] 
    