from django.shortcuts import render
from django.views.generic import ListView
from projects.models import Post
# Create your views here.

class ListProjects(ListView):
    model=Post
    template_name="home.html"


