from django.shortcuts import render
from django.views.generic import ListView,DetailView
from projects.models import Post
# Create your views here.

class ListProjects(ListView):
    model=Post
    template_name="home.html"

class DetailProjects(DetailView):
    model=Post
    template_name="detail.html"
