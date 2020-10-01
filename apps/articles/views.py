"""Views for Articles"""
from datetime import date, timedelta

from django.views import generic
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import authenticate
# from django.contrib.auth.models import User

from articles.models import Article
from articles.filters import ArticleFilter

# timespan of how long the likes will count for the hot order (in days)
TIME_DELTA = 2


class ArticleListView(generic.View):
    """Generic list view for the Article model"""
    model = Article
    template_name = "articles/article_list.html"

    def get(self, request, *args, **kwargs):
        if self.kwargs["order_by"] == "nieuw":
            """
            Order by newest first
            """
            article = Article.objects.all().order_by('-created')
            article_filter = ArticleFilter(
                request.GET,
                queryset=article,
                request=request
            )
            article_count = Article.objects.all().count()
            context = {
                "article_list": article_filter,
                "article_count": article_count
            }

            return render(
                request,
                self.template_name,
                context
            )

        elif self.kwargs["order_by"] == "populair":
            """
            Order by most likes all time
            """
            article = Article.objects.annotate(
                num_likes=Count("user_likes")
            ).order_by("-num_likes")
            article_filter = ArticleFilter(
                request.GET,
                queryset=article,
                request=request
            )
            article_count = Article.objects.all().count()
            context = {
                "article_list": article_filter,
                "article_count": article_count
            }

            return render(
                request,
                self.template_name,
                context
            )

        elif self.kwargs["order_by"] == "hot":
            """
            Order by most likes over the last week
            """
            last_week = date.today() - timedelta(days=TIME_DELTA)
            article = Article.objects.annotate(
                num_likes=Count("user_likes", filter=Q(created__gte=last_week))
            ).order_by("-num_likes")
            article_filter = ArticleFilter(
                request.GET,
                queryset=article,
                request=request
            )
            article_count = Article.objects.all().count()
            context = {
                "article_list": article_filter,
                "article_count": article_count
            }

            return render(
                request,
                self.template_name,
                context
            )

        else:
            return redirect("articles:article-list", "nieuw")


class ArticleDetailView(generic.View):
    """Generic detail view for the Article model"""
    model = Article
    template_name = "articles/article_detail.html"

    def get(self, request, *args, **kwargs):
        """
        Render the detail view for an object
        """
        article = get_object_or_404(Article, slug=kwargs.get("slug"))
        context = {
            "article": article,
        }

        return render(
                request,
                self.template_name,
                context
            )


class ArticleCreateView(generic.View):
    """Creation view for Article"""
    model = Article
    template_name = "articles/article_create.html"

    def get(self, request, *args, **kwargs):
        """
        Render the creation view for Article
        """
        if request.user.is_authenticated:
            return redirect("accounts:login")
