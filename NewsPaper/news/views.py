from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.models import Group
from django.shortcuts import redirect, get_object_or_404, render, HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.urls import reverse_lazy
from django.core.cache import cache
from django.utils import timezone
import pytz


import logging

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


#for logging
logger = logging.getLogger(__name__)

# Create your views here.
my_timezone = {
        'Moscow': 'Europe/Moscow',
        'Paris': 'Europe/Paris',
        'New York': 'America/New_York',
    }

class News(ListView):
    model = Post
    ordering = '-time_in'
    template_name = 'news.html'
    context_object_name = 'news'
    paginate_by = 10

    def set_timezone(request):
        if request.method == 'POST':
            request.session['django_timezone'] = request.POST['timezone']
            return redirect('/news')
        else:
            return render(request, 'default.html', {'timezone': my_timezone})

    def post(self, request):
        request.session['django_timezone'] = request.POST['timezone']
        return redirect('/news')

    def get_context_data(self, **kwargs):
        current_time = timezone.localtime(timezone.now())
        context = super().get_context_data(**kwargs)
        context['current_time'] = current_time
        context['timezones'] = pytz.common_timezones
        return context

class New(DetailView):
    model = Post
    template_name = 'new.html'
    context_object_name = 'new'
    queryset = Post.objects.all()

    def get_object(self, *args, **kwargs):
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        if not obj:
            obj = super().get_object(queryset=self.queryset)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj


class Search(ListView):
    model = Post
    ordering = 'time_in'
    template_name = 'search.html'
    context_object_name = 'search'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ArticlesPostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.change_news='AR'
        return super().form_valid(form)

class NewsPostCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post')
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_create.html'


    def form_valid(self, form):
        post = form.save(commit=False)
        post.change_news='NE'
        return super().form_valid(form)

class ArticlesPostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.change_news='AR'
        return super().form_valid(form)


class NewsPostUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post')
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.change_news = 'NE'
        return super().form_valid(form)


class ArticlesPostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')


class NewsPostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('news')

@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/news')

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.category = get_object_or_404(Category, id=self.kwargs.get("pk"))
        queryset = Post.objects.filter(category=self.category).order_by('-time_in')
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.category.subscribers.all()
        context['category'] = self.category
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = 'Вы успешно подписались на рассылку новостей категории '
    return render(request, 'subscribe.html', {'category': category, 'message': message})