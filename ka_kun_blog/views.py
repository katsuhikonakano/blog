from django.shortcuts import render
from .models import Post, Category, Tag
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .forms import PostForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Count, Q

# Create your views here.

class PostListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 4
    
    def get_queryset(self):
        queryset = Post.objects.all().order_by('-created_at')
        search = self.request.GET.get('q')
        if search:
            queryset = Post.objects.filter(
                Q(title__icontains=search) | Q(content__icontains=search))
        return queryset


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy("index")
    template_name = "ka_kun_blog/post_create_form.html"
    login_url = '/login/'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)


class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = "ka_kun_blog/post_update_form.html"
    login_url = '/login/'

    def get_success_url(self):
        post_pk = self.kwargs['pk']
        url = reverse_lazy("detail", kwargs={"pk": post_pk})
        return url

    def form_valid(self, form):
        messages.success(self.request, "更新されました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新できませんでした")
        return super().form_invalid(form)


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("index")
    login_url = '/login/'

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)


class CategoryListView(ListView):
    model = Post
    context_object_name = "posts"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        return context

    def get_queryset(self):
        category = Category.objects.get(name=self.kwargs['category'])
        queryset = Post.objects.order_by('-created_at').filter(category=category)
        return queryset


class TagListView(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 4
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = self.kwargs['tag']
        return context
        
    def get_queryset(self):
        tag = Tag.objects.get(name=self.kwargs['tag'])
        queryset = Post.objects.order_by('-created_at').filter(tag=tag)
        return queryset
