"""
Forms for comments
"""
from django.forms import ModelForm

from comments.models import Comment


class CommentForm(ModelForm):
    """Create a comment for an article"""
    class Meta:
        model = Comment
        fields = [
            'message'
        ]
        exclude = ["author", "article", "seen"]
