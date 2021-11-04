from django.shortcuts import render, HttpResponse
from .models import Articles
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse

# Create your views here.

class HomeView(ListView):
    model = Articles
    template_name = "hello/home.html"
    context_object_name = 'posts'

class ArticleDetailView(DetailView):
    model = Articles
    template_name = "hello/article.html"

class ArticleCreateView(CreateView):
    model = Articles
    template_name = 'hello/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk':self.object.id})

class ArticleUpdateView(UpdateView):
    model = Articles
    template_name = 'hello/article_form.html'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

    def get_success_url(self):
        return reverse('article-detail', kwargs={'pk':self.object.id})


class ArticleDeleteView(DeleteView):
    model = Articles
    template_name = 'hello/delete_confirm.html'
    success_url = '/'

    def test_func(self):
        article = self.get_object()
        return self.request.user == article.author

#
# def home(request):
#     return render(request, "hello/home.html", {'posts': Articles.objects.all()})

def about(request):
    return render(request, 'hello/about.html')