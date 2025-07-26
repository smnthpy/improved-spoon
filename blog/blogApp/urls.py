
from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("",views.home,name="home"),
    path("blogs/<str:slug>/",views.blog_details,name="blog_details"),
    path("blog/",views.blog,name="blog"),
]