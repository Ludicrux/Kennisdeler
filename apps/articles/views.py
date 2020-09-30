"""Views for Articles"""
from datetime import date, timedelta

from django.views.generic import ListView, DetailView
from articles.models import Article
from django.db.models import Count, Q

from .filters import ArticleFilter

# timespan of how long the likes will count for the hot order (in days)
TIME_DELTA = 2


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"
    context_object_name = "article_list"

    def get_queryset(self):
        if self.kwargs["order_by"] == "nieuw":
            """Order by newest first"""
            article = Article.objects.all().order_by('-created')
            return ArticleFilter(self.request.GET, queryset=article)

        elif self.kwargs["order_by"] == "populair":
            """Order by most likes all time"""
            article = Article.objects.annotate(
                num_likes=Count("user_likes")
            ).order_by("-num_likes")
            return ArticleFilter(self.request.GET, queryset=article)

        elif self.kwargs["order_by"] == "hot":
            """Order by most likes over the last week"""
            last_week = date.today() - timedelta(days=TIME_DELTA)
            article = Article.objects.annotate(
                num_likes=Count("user_likes", filter=Q(created__gte=last_week))
            ).order_by("-num_likes")
            return ArticleFilter(self.request.GET, queryset=article)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["amount"] = Article.objects.all().count()
        return context


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
