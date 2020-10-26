"""
Views for Core
"""
from django.views import generic
from django.shortcuts import render
from django.db.models import Count

from articles.models import Article, Subject


class HomePageView(generic.View):
    """List all subjects and most popular items"""
    template_name = "core/homepage.html"

    def get(self, request, *args, **kwargs):
        """Return all subjects and most popular items"""
        subject = Subject.objects.all()
        article = Article.objects.annotate(
            num_likes=Count("user_likes")
        ).order_by("-num_likes")[:3]

        context = {
            "subject_list": subject,
            "article_list": article
        }

        return render(request, self.template_name, context)
