from django.contrib.auth import logout, login
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, FormView
from taggit.models import Tag

from .forms import *
from django.http import HttpResponseRedirect, HttpResponse
from .models import *

# Create your views here.

posts = Post.objects.all()
tags = Tag.objects.all()


def index(request):
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {'title': 'Добро пожаловать в мой блог', 'posts': posts,
                                          'page_obj': page_obj, 'tags': tags})


class PostDetailView(View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, url=slug)
        post_tag = Post.objects.all()
        common_tags = Post.tag.most_common()
        last_posts = Post.objects.all().order_by('-id')[:5]
        comment_form = CommentForm()
        return render(request, 'post_detail.html', context={
            'post': post, 'title': post.h1, 'post_tag': posts,
            'tags': tags, 'common_tags': common_tags, 'last_posts': last_posts,
            'comment_form': comment_form
        })

    def post(self, request, slug, *args, **kwargs):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            text = request.POST['text']
            username = self.request.user
            post = get_object_or_404(Post, url=slug)
            comment = Comment.objects.create(post=post, username=username, text=text)
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        return render(request, 'post_detail.html', context={
            'comment_form': comment_form
        })


class TagView(View):
    def get(self, request, slug, *args, **kwargs):
        tag = get_object_or_404(Tag, slug=slug)
        posts = Post.objects.filter(tag=tag)
        common_tags = Post.tag.most_common()
        return render(request, 'tag.html', context={
            'title': f'#ТЕГ {tag}',
            'posts': posts,
            'tag': tag,
            'common_tags': common_tags
        })


class SearchPost(ListView):
    model = Post
    template_name = 'search_results.html'

    def get_queryset(self):  # новый
        query = self.request.GET.get('q')
        self.query = query
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
            | Q(title__icontains=query.capitalize()) | Q(content__icontains=query.capitalize()))
        return object_list

    def get_context_data(self, *, object_list=None, **kwargs):
        return {'title': 'Результаты поиска: '+str(self.query), 'posts': self.object_list, 'tags': Tag.objects.all()}


class SignUpView(View):
    def get(self, request, *args, **kwargs):
        form = SigUpForm()
        return render(request, 'register.html', context={
            'form': form, 'posts': posts, 'title': 'Registration'
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
            'form': form, 'title': 'Login'
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


class ContactFormView(FormView):
    template_name = 'contact.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')

    def get_context_data(self, **kwargs):
        return {'title': 'Связаться с нами', 'form': self.form_class, 'tags': Tag.objects.all()}
