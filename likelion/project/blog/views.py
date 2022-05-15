from random import randint
from turtle import title
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.db.models import Q
from .form import BlogForm
from django.core.paginator import Paginator


def home(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 3)
    pagnum = request.GET.get('page')
    blogs = paginator.get_page(pagnum)
    return render(request, 'home.html', {'blogs': blogs})


def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'detail.html', {'blog': blog})


def new(request):
    # 1. 데이터가 입려된 후 제출 버튼을 누르고 데이터 저장 -> POST
    # 2. 정보가 입력되지 않은 빈칸으로 되어있는 페이지 보여주기 -> GET
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm()
        return render(request, 'new.html', {'form': form})


def create(request):
    new_blog = Blog()
    new_blog.title = request.POST['title']
    new_blog.content = request.POST['content']
    new_blog.image = request.FILES['image']
    new_blog.save()
    return redirect('detail', new_blog.id)


def edit(request, id):
    edit_blog = get_object_or_404(Blog, pk=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, instance=edit_blog)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BlogForm(instance=edit_blog)
        return render(request, 'edit.html', {'form': form})


def update(request, id):
    update_blog = get_object_or_404(Blog, pk=id)
    update_blog.title = request.POST['title']
    update_blog.content = request.POST['content']
    if request.FILES:
        update_blog.image = request.FILES['image']
    update_blog.save()
    return redirect('detail', update_blog.id)


def delete(request, id):
    delete_blog = get_object_or_404(Blog, pk=id)
    delete_blog.delete()
    return redirect('home')


def search(request):
    blogs = Blog.objects.all()
    search = request.GET.get('search', '')
    if search:
        search_list = blogs.filter(
            Q(title__icontains=search) |  # 제목
            Q(content__icontains=search)  # 내용
        )
    return render(request, 'search.html', {'search_list': search_list})
