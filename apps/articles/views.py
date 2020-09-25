"""Views for Articles"""
from datetime import date, timedelta

from django.views.generic import ListView, DetailView
from articles.models import Article
from django.db.models import Count, Q


class ArticleListView(ListView):
    model = Article
    template_name = "articles/article_list.html"

    def get_queryset(self):
        if self.kwargs["order_by"] == "nieuw":
            """Order by newest first"""
            return Article.objects.all().order_by('-created')

        elif self.kwargs["order_by"] == "populair":
            """Order by most likes all time"""
            return Article.objects.annotate(
                num_likes=Count("user_likes")
            ).order_by("-num_likes")

        elif self.kwargs["order_by"] == "hot":
            """Order by most likes over the last week"""
            last_week = date.today() - timedelta(days=1)
            return Article.objects.annotate(
                num_likes=Count("user_likes", filter=Q(created__gte=last_week))
            ).order_by("-num_likes")


class ArticleDetailView(DetailView):
    model = Article
    context_object_name = "article"
    template_name = "articles/article_detail.html"
