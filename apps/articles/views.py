"""Views for Articles"""
from django.views.generic import ListView, DetailView
from articles.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
