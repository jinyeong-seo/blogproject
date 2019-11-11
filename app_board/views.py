from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html',{'posts': posts})

def detail(request, project_id):
    project_detail = get_object_or_404(Post, pk=project_id)
    return render(request,'detail.html', {'project_detail':project_detail})