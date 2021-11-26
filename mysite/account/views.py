from django.shortcuts import render, redirect
from . models import Account
from django.contrib.auth import login, logout, authenticate
from . forms import RegistrationForm, LoginForm, AccountUpdateForm
from blog.models import BlogPost
# Create your views here.

def Register_view(request):
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'account/register.html', {'form':form})


def Login_view(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home')
        
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})


def Logout_view(request):
    logout(request)
    return redirect('home')

def account_view(request):
    # account = Account.objects.all()
    # context = {'accounts': account}
    blog_posts = BlogPost.objects.filter(author=request.user)
    return render(request, 'account/account.html', {'blog_posts':blog_posts})

def ChangeProfile(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {'email':request.POST['email'], 'username':request.POST['username']}
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username
            }
        )
    return render(request, 'account/change_profile.html',{'form':form})


def must_auth(request):
    return render(request, 'account/must_auth.html', {})