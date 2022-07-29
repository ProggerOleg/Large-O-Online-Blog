from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import CreateView
from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from .models import Post
# Create your views here.

posts = Post.objects.all()


def index(request):
    return render(request, 'index.html', {'title': 'Добро пожаловать в мой блог', 'posts': posts})


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'register.html', context={
            'form': form, 'posts': posts,
        })

    def post(self, request, *args, **kwargs):
        form = SigUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'register.html', context={
            'form': form,
        })


class SignInView(View):
    def get(self, request, *args, **kwargs):
        form = SignInForm()
        return render(request, 'login.html', context={
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        form = SignInForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'login.html', context={
            'form': form,
        })