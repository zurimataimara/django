from django.shortcuts import render
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from projects.models import Post
from django.urls import reverse_lazy
# Create your views here.

class ListProjects(ListView):
    model=Post
    template_name="home.html"

class DetailProjects(DetailView):
    model=Post
    template_name="detail.html"

class CreatePageView(CreateView):
    model=Post
    template_name="create.html"
    fields=["title","description","image"]
    success_url = reverse_lazy("home")

class UpdatePageView(UpdateView):

    model=Post
    fields=["title","description","image"]  
    template_name="update.html"
    success_url = reverse_lazy("home")  

class DeletePageView(DeleteView):

    model=Post
    template_name="delete.html"
    success_url= reverse_lazy("home")

#Vista para la pagina de inicio
def WelcomePage(request):
        return render (request, "Welcome.html")
