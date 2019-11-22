from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone

# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'home.html',{'posts': posts})

def detail(request, project_id):
    project_detail = get_object_or_404(Post, pk=project_id)
    return render(request, 'detail.html',{'post': project_detail})

def new(request):
    return render(request,'new.html')

def create(request):
    new_post = Post()
    new_post.name = request.POST['name']
    new_post.date = timezone.datetime.now()
    new_post.writer = request.POST['writer']
    new_post.body = request.POST['body']
    new_post.save()
    return redirect('/app_board/'+str(new_post.id))

def edit(request, project_id):
    edit_post= Post.objects.get(id=project_id)
    return render(request, 'edit.html', {'post':edit_post})

def update(request):
    update_post = Post.objects.get(id= project_id)
    update_post.name = request.POST['name']
    update_post.date = timezone.datetime.now()
    update_post.writer = request.POST ['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return render('/app_board/'+str(update_project.id))