
from django.urls import path
from projects.views import ListProjects,DetailProjects

urlpatterns=[
    
    path("",ListProjects.as_view()),
    path("detail/<int:pk>",DetailProjects.as_view(),name="detail")

]