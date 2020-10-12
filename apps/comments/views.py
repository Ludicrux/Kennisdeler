from django.views import generic
from django.shortcuts import render

from comments.models import Comment


class CommentListView(generic.View):
    """Generic list view for user comments"""
    model = Comment
    template_name = "comments/comment_list.html"

    # Login required decorator
    def get(self, request, *args, **kwargs):
        """retrieve a list of comments for the user"""

        comment = Comment.objects.filter(article__author=request.user)

        context = {
            "comment_list": comment
        }

        return render(
            request,
            self.template_name,
            context
        )
