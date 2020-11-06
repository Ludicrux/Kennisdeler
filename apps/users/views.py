"""
Views for users
"""
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from articles.models import Article
from users.models import User, Profile


def count_values(queryset):
    """
    returns the total of article
    likes, views, favorites, downloads and articles posted
    """
    views = 0
    favorites = 0
    downloads = 0
    likes = 0
    article_count = queryset.count()

    for article in queryset:
        likes += article.user_likes.count()
        favorites += article.user_favorites.count()
        views += article.views
        downloads += article.downloads

    count_dict = {
        "article_count": article_count,
        "likes": likes,
        "favorites": favorites,
        "downloads": downloads,
        "views": views,
    }

    return count_dict


@method_decorator(login_required, name="dispatch")
class UserProfileView(generic.View):
    """User profile for current authenticated user"""
    template_name = "users/user_profile.html"

    def get(self, request, **kwargs):
        """Return list of articles authored by current authenticated user"""
        user = get_object_or_404(User, pk=request.user.pk)
        profile = get_object_or_404(Profile, user=user)
        article_list = Article.objects.filter(author=user)

        context = {
            "user": user,
            "profile": profile,
            "article_list": article_list,
            "count": count_values(article_list),
        }
        return render(request, self.template_name, context)


class UserArticleListView(generic.View):
    """User profile list for full_name"""
    template_name = "users/user_article_list.html"

    def get(self, request, **kwargs):
        """Return list of articles for """
        user = get_object_or_404(User, slug=kwargs.get("slug"))
        profile = get_object_or_404(Profile, user=user.id)
        article_list = Article.objects.filter(author=user)

        context = {
            "user": user,
            "profile": profile,
            "article_list": article_list,
            "count": count_values(article_list),
        }
        return render(request, self.template_name, context)
