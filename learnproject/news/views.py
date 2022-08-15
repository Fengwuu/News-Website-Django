from .models import News, Category
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login


class HomeNews(ListView):  # Different way to make page
    model = News  # Nodel, that we need to use
    template_name = 'news/home_news_list.html'
    context_object_name = 'news'  # Name for templates to use instead 'object'
    paginate_by = 3

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)   # hard to understand, but it for content in template
        context['title'] = 'Главная страница'
        return context

    def get_queryset(self):  # MAke is_published function working
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(ListView):
    model = News
    template_name = 'news/category.html'
    context_object_name = 'news'
    allow_empty = False
    paginate_by = 3

    def get_queryset(self):
        return News.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(pk=self.kwargs['category_id'])
        return context


class ViewNews(DetailView):
    model = News
    template_name = 'news/view_news.html'
    context_object_name = 'news_item'


class CreateNews(LoginRequiredMixin, CreateView):
    form_class = NewsForm
    template_name = 'news/add_news.html'
    login_url = '/admin/'


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно прошли регистрацию! ')
            return redirect('home')
        else:
            messages.error(request, 'Произошла ошибка регистрации!')
    else:
        form = UserRegisterForm()
    return render(request, 'news/register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'news/login.html', {"form": form})


def for_journalists(request):
    return render(request, 'news/for_journalists.html')

