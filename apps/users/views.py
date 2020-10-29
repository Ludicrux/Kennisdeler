"""
Views for users
"""
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from articles.models import Article
from users.models import User


@method_decorator(login_required, name="dispatch")
class UserProfileView(generic.View):
    """User profile for current authenticated user"""
    template_name = "users/user_profile.html"

    def get(self, request, **kwargs):
        """Return list of articles authored by current authenticated user"""
        user = get_object_or_404(User, pk=request.user.pk)
        article_list = Article.objects.filter(author=user)

        context = {
            "user": user,
            "article_list": article_list,
        }
        return render(request, self.template_name, context)


class UserArticleListView(generic.View):
    """User profile list for full_name"""
    template_name = "users/user_article_list.html"

    def get(self, request, **kwargs):
        """Return list of articles for """
        user = get_object_or_404(User, full_name=kwargs.get("full_name"))
        article_list = Article.objects.filter(author=user)

        context = {
            "user": user,
            "article_list": article_list,
        }
        return render(request, self.template_name, context)
