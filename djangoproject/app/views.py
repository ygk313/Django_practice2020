from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from django.utils import timezone

def home(request):
    blogs = Blog.objects.all()
    return render(request, 'apps/home.html', {'blogs':blogs})

def create(request):
    if request.method == "POST":
        blog = Blog()
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('home')
    return render(request, 'apps/create.html')

def delete(request, id):
    blog = get_object_or_404(Blog, pk=id)
    blog.delete()
    return redirect('home')


def update(request, id):
    if request.method == "POST":
        blog = get_object_or_404(Blog, pk=id)
        blog.title = request.POST['title']
        blog.body = request.POST['body']
        blog.pub_date = timezone.datetime.now()
        blog.save()
        return redirect('home')
    else:
        blog = get_object_or_404(Blog, pk=id)
        return render(request, 'apps/update.html', {'blog':blog})
def detail(request, id):
    blog = get_object_or_404(Blog, pk=id)
    return render(request, 'apps/detail.html', {'blog':blog})