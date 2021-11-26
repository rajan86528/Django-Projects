from django.shortcuts import render, redirect, get_object_or_404
from blog. models import BlogPost
from blog. forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from django.db.models import Q
from django.http import HttpResponse
# Create your views here.

def CreateBlogView(request):
    user = request.user
    if not user.is_authenticated:
        return redirect('must_auth')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
    
    return render(request, 'blog/create_blog.html', {'form':form})


def BlogDetailView(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug)
    return render(request, 'blog/detail_view.html', {'blog_post':blog_post})

def EditBlogView(request, slug):
    context={}
    user = request.user
    if not user.is_authenticated:
        return redirect('must_auth')

    blog_post = get_object_or_404(BlogPost, slug=slug)

    if blog_post.author != user:
        return HttpResponse("You are Not Author of this post.")

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success'] = "updated"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            'title':blog_post.title,
            'body':blog_post.body,
            'image':blog_post.image,
        }
    )
    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


def get_blog_queryset(query=None):
    queryset = []
    queries = query.split(" ") # python install 2019 = [python, install, 2019]
    for q in queries:
        posts = BlogPost.objects.filter(
                Q(title__icontains=q) | 
                Q(body__icontains=q)
            ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))