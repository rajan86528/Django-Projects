from django.shortcuts import render, redirect, get_object_or_404
from blog. models import BlogPost
from blog. forms import CreateBlogPostForm
from account.models import User
from django.db.models import Q
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def CreateBlogView(request):
    user = request.user
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = User.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    
    return render(request, 'blog/create_blog.html', {'form':form})

@login_required
def BlogDetailView(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail_view.html', {'blog_post':blog_post})

