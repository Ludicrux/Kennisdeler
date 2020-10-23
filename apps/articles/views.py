"""
Views for Articles
"""
from pathlib import Path
from datetime import date, timedelta

from django.views import generic
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404, render, redirect
# from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.core.paginator import Paginator

from articles.models import Article
from articles.filters import ArticleFilter
from articles.forms import ArticleForm
from comments.forms import CommentForm

from formtools.wizard.views import SessionWizardView


TIME_DELTA = 2      # days
ORDER_TYPES = ["nieuw", "populair", "hot"]


@login_required
def favorite_article(request, **kwargs):
    """favorite or unfavorite an article"""
    article = get_object_or_404(Article, slug=kwargs.get("slug"))
    if request.user in article.user_favorites.all():
        article.user_favorites.remove(request.user)
    else:
        article.user_favorites.add(request.user)
    return redirect(article.get_absolute_url())


@login_required
def like_article(request, **kwargs):
    """favorite or unfavorite an article"""
    article = get_object_or_404(Article, slug=kwargs.get("slug"))
    if request.user in article.user_likes.all():
        article.user_likes.remove(request.user)
    else:
        article.user_likes.add(request.user)
    return redirect(article.get_absolute_url())


@login_required
def create_comment(request, **kwargs):
    """
    User created comment
    """
    form = CommentForm(request.POST)
    author = get_object_or_404(User, pk=request.user.id)
    article = get_object_or_404(Article, slug=kwargs.get("slug"))
    if request.user == article.author:
        return redirect(article.get_absolute_url())

    if form.is_valid():
        comment = form.save(commit=False)
        comment.author = author
        comment.article = article
        comment.save()

    return redirect(article.get_absolute_url())


class ArticleListView(generic.View):
    """Generic list view for the Article model"""
    model = Article
    template_name = "articles/article_list.html"

    def get(self, request, order_by=ORDER_TYPES[0], page=1, **kwargs):
        """Filtered list views"""
        context = {}


        if order_by == ORDER_TYPES[0]:
            """
            Order by newest first
            """
            article = Article.objects.all().order_by('-created')

        elif order_by == ORDER_TYPES[1]:
            """
            Order by most likes all time
            """
            article = Article.objects.annotate(
                num_likes=Count("user_likes")
            ).order_by("-num_likes")

        elif order_by == ORDER_TYPES[2]:
            """
            Order by most likes over the TIME_DELTA in days
            """
            last_week = date.today() - timedelta(days=TIME_DELTA)
            article = Article.objects.annotate(
                num_likes=Count("user_likes", filter=Q(created__gte=last_week))
            ).order_by("-num_likes")

        if request.user.is_authenticated:
            context["logged_in"] = True
        else:
            article = article.filter(is_public=False)

        if "favorite" in request.GET:
            context["favorite_selected"] = True
            article = article.filter(user_favorites=request.user)

        # filter on search
        if "search" in request.GET:
            context["search_str"] = request.GET["search"]
            article = article.filter(
                Q(title__icontains=context["search_str"]) |
                Q(author__username__icontains=context["search_str"]) |
                Q(short_desc__icontains=context["search_str"]) |
                Q(long_desc__icontains=context["search_str"])
            )

        # Apply filter over qs with the corresponding form
        article_filter = ArticleFilter(
            request.GET,
            queryset=article,
            request=request
        )
        context["article_filter"] = article_filter

        # Paginate filter qs
        paginator = Paginator(article_filter.qs, 6)
        article_list = paginator.get_page(page)
        context["article_list"] = article_list

        # add a readable GET url string for linking to the context
        url_path = request.get_full_path()
        get_ext = ""
        if "?" in url_path:
            get_ext = url_path.split("?")[-1]
            get_ext = f"?{get_ext}"
        context["get_string"] = get_ext
        context["current_order"] = str(order_by)

        # add all order_types to the context and highlight the currently selected
        order_types = []
        for otype in ORDER_TYPES:
            if otype == context["current_order"]:
                order_types.append({"name": otype, "current": "red"})
            else:
                order_types.append({"name": otype, "current": ""})
        context["order_by"] = order_types

        return render(request, self.template_name, context)


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

        if not article.is_public:
            context["not_public"] = True

        # Check to see if the current user is the author of the article
        if request.user.is_authenticated:
            if request.user == article.author:
                context["article_author"] = request.user
            else:
                commentform = CommentForm()
                context["comment_form"] = commentform

        # Check if the user favorited the post
        if request.user in article.user_favorites.all():
            context["article_favorite"] = "Favorite"
        else:
            context["article_favorite"] = "Unfavorite"

        if request.user in article.user_likes.all():
            context["article_like"] = "Like"
        else:
            context["article_like"] = "Dislike"

        return render(request, self.template_name, context)


@method_decorator(login_required, name="dispatch")
class ArticleCreateView(SessionWizardView):
    """Creation view for Article"""
    template_name = "articles/article_create.html"
    file_storage = FileSystemStorage(
        location=Path(settings.MEDIA_ROOT).joinpath('temp')
    )

    def done(self, form_list, **kwargs):
        temp = []
        for form in form_list:
            temp.append(form.cleaned_data)
        form_dict = temp[0]
        form_dict.update(temp[1])
        form_dict["author"] = get_object_or_404(User, pk=self.request.user.id)
        article = Article(**form_dict)
        article.save()

        return redirect(article.get_absolute_url())


@method_decorator(login_required, name="dispatch")
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

        if not request.user == article.author:
            return redirect(article.get_absolute_url())

        form = ArticleForm(instance=article)
        context = {
            "form": form,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """
        Update the Article object with the new form details
        """
        article = get_object_or_404(Article, slug=kwargs.get("slug"))

        if not request.user == article.author:
            return redirect(article.get_absolute_url())

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

        return render(request, self.template_name, context)
