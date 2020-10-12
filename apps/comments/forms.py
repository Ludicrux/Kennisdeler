"""Create and update forms for Article model and views"""
from django.forms import ModelForm

from comments.models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'message'
        ]
        exclude = ["author", "article", "seen"]
