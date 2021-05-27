from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from .forms import UserCreationForm, UserLoginForm, AddTovar
from django.contrib.auth import logout
from .models import Question

def index(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Регистрация в АИС прошла успешо')
            return redirect('login')
        else:
            messages.error(request, 'Одна ошибка и ты ошибся')

    else:
        form = UserCreationForm()
    return render(request, 'user/index.html', {'form':form})

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'user/login.html', {'form':form})

def home(request):
    addT = 0
    if request.method == 'POST':
        addT = AddTovar(request.POST)
        if addT.is_valid():
            addT.save()

    data = Question.objects.order_by('-id_tovara')
    return render(request, 'user/home.html', {'data':data, 'addT':addT})

def logout_user(request):
    logout(request)
    return redirect('login')