from django.shortcuts import render
import random
import string

# Create your views here.

def HomePageView(request):
    return render(request, 'generator\home.html')

def PasswordPageView(request):
    letters = list(string.ascii_lowercase)

    length = int(request.GET.get('length'))

    if request.GET.get('uppercase'):
        letters.extend(list(string.ascii_uppercase))
    if request.GET.get('special'):
        letters.extend(list('!@#$%^&*()'))
    if request.GET.get('numbers'):
        letters.extend(list('123456790'))
        
    password = ''.join(random.choice(letters) for i in range(length))
    
    return render(request, 'generator\password.html', {'password': password})