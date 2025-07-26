from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from .models import *
# Create your views here.
def home(request):
    return render(request,"blogApp/index.html")

def blog_details(request,slug):
    post = get_object_or_404(Post,slug=slug)
    comments = Comments.objects.filter(post=post)
    if request.method == "POST":
        comment = request.POST.get('comment')

        if comment.strip():  # prevent empty comments
            Comments.objects.create(comment=comment, post=post)
        return redirect('core:blog_details',slug=slug) 
      
    return render(request, "blogApp/blog-detail.html",{
        'post':post,
        'comments':comments,
    })
def blog(request):
    posts = Post.objects.all()
    return render(request,"blogApp/blog.html",{
        'posts':posts,
    })
