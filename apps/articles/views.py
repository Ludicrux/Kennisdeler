"""
Views for Articles
"""
from datetime import date, timedelta

from django.views import generic
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from articles.models import Article
from articles.filters import ArticleFilter
from articles.forms import ArticleForm


# timespan of how long the likes will count for the hot order (in days)
TIME_DELTA = 2


class ArticleListView(generic.View):
    """Generic list view for the Article model"""
    model = Article
    template_name = "articles/article_list.html"

    def get(self, request, *args, **kwargs):
        article_count = Article.objects.all().count()
        context = {
            "article_count": article_count
        }

        if self.kwargs["order_by"] == "nieuw":
            """
            Order by newest first
            """
            article = Article.objects.all().order_by('-created')

        elif self.kwargs["order_by"] == "populair":
            """
            Order by most likes all time
            """
            article = Article.objects.annotate(
                num_likes=Count("user_likes")
            ).order_by("-num_likes")

        elif self.kwargs["order_by"] == "hot":
            """
            Order by most likes over the last week
            """
            last_week = date.today() - timedelta(days=TIME_DELTA)
            article = Article.objects.annotate(
                num_likes=Count("user_likes", filter=Q(created__gte=last_week))
            ).order_by("-num_likes")

        else:
            return redirect("articles:article-list", "nieuw")

        if "favorite" in request.GET:
            context["favorite_selected"] = True
            article = article.filter(user_favorites=request.user)

        article_filter = ArticleFilter(
            request.GET,
            queryset=article,
            request=request
        )
        context["article_list"] = article_filter

        return render(
            request,
            self.template_name,
            context
        )


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

        if request.user.is_authenticated & (request.user == article.author):
            context["article_author"] = request.user

        if request.user in article.user_favorites.all():
            context["article_favorite"] = request.user

        return render(
                request,
                self.template_name,
                context
            )


def FavoriteArticle(request, *args, **kwargs):
    """favorite or unfavorite an article"""
    article = get_object_or_404(Article, slug=kwargs.get("slug"))
    if request.user in article.user_favorites.all():
        article.user_favorites.remove(request.user)
    else:
        article.user_favorites.add(request.user)
    return redirect(article.get_absolute_url())


class ArticleCreateView(generic.View):
    """Creation view for Article"""
    model = Article
    template_name = "articles/article_create.html"

    def get(self, request, *args, **kwargs):
        """
        Render the creation view for Article
        """
        if not request.user.is_authenticated:
            return redirect("login")

        form = ArticleForm()
        context = {
            "form": form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """save the form to the Article model database"""
        if not request.user.is_authenticated:
            return redirect("login")

        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = get_object_or_404(User, pk=request.user.id)
            article.save()
            return redirect(article.get_absolute_url())

        context = {
            "form": form
        }

        return render(request, self.template_name, context)


class ArticleEditView(generic.View):
    """Authenticated user can edit Article"""
    model = Article
    template_name = "articles/article_edit.html"

    def get(self, request, *args, **kwargs):
        """
        Render the edit view for an object, form filled in with
        existing data
        """
        article = get_object_or_404(Article, slug=kwargs.get("slug"))

        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user == article.author:
            return redirect("articles:article-list", "nieuw")

        form = ArticleForm(instance=article)
        context = {
            "form": form,
        }

        return render(
            request,
            self.template_name,
            context
            )

    def post(self, request, *args, **kwargs):
        """
        Update the Article object with the new form details
        """
        article = get_object_or_404(Article, slug=kwargs.get("slug"))
        if not request.user.is_authenticated:
            return redirect("login")

        if not request.user == article.author:
            return redirect("articles:article-list", "nieuw")

        form = ArticleForm(
            request.POST or None,
            request.FILES,
            instance=article
        )
        if form.is_valid():
            form.save()
            return redirect(article.get_absolute_url())

        context = {
            "form": form,
        }

        return render(
            request,
            self.template_name,
            context
        )
