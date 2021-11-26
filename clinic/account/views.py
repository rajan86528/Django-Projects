from django.contrib import messages
from django.views.generic import CreateView, ListView
from django.shortcuts import render, redirect
from .form import PatientSignUpForm, DoctorSignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout,authenticate
from .models import User
from blog.models import BlogPost
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    if request.user.is_anonymous:
        blog_posts = None
    elif request.user.is_doctor:
        blog_posts = BlogPost.objects.filter()
    else:
        request.user.is_patient
        blog_posts = BlogPost.objects.filter(status=1)
    return render(request, '../templates/home.html', {'blog_posts':blog_posts})

class AllDoctorListView(ListView):
    model = User
    template_name = '../templates/doctor_list.html'
    context_object_name = 'all_doctors'


def register(request):
    return render(request, '../templates/register.html')

class patient_register(CreateView):
    model = User
    form_class = PatientSignUpForm
    template_name = '../templates/patient_sign_up.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')

class doctor_register(CreateView):
    model = User
    form_class = DoctorSignUpForm
    template_name = '../templates/doctor_sign_up.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('/')


def login_request(request):
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None :
                login(request,user)
                return redirect('/')
            else:
                messages.error(request,"Invalid username or password")
        else:
                messages.error(request,"Invalid username or password")
    return render(request, '../templates/sign_in.html',
    context={'form':AuthenticationForm()})

@login_required
def logout_view(request):
    logout(request)
    return redirect('index')
