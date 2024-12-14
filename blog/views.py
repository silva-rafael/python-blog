from django.shortcuts import render
from .models import Post

def home_view(request):
    posts = Post.objects.all()
    return render(request, 'blog/home.html', {'posts' : posts})
