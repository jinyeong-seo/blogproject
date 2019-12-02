from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.

def home(request):
    post = Post.objects
    post_list = Post.objects.all()
    paginator = Paginator(post_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'post': post, 'posts':posts})

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

def update(request, project_id):
    update_post = Post.objects.get(id= project_id)
    update_post.name = request.POST['name']
    update_post.date = timezone.datetime.now()
    update_post.writer = request.POST ['writer']
    update_post.body = request.POST['body']
    update_post.save()
    return redirect('/app_board/'+str(update_post.id))

def delete(requst,project_id):
    delete_post = Post.objects.get( id = project_id)
    delete_post.delete()
    return redirect('home')
    