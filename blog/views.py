from django.shortcuts import render
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
from .models import Post
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy




# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'blog/home.html'

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(CreateView):
    model = Post
    fields = ['title','content']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('post_list') 

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')




