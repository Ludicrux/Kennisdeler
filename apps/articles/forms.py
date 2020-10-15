
"""
Forms for articles
"""
from django.forms import ModelForm
# from django.forms import ClearableFileInput

from articles.models import Article


class ArticleForm(ModelForm):
    """
    Create or update an article
    """
    class Meta:
        model = Article
        fields = [
            'title',
            'short_desc',
            'long_desc',
            'image',
            "uploaded_file",
            'subject',
            'level',
            'is_public',
        ]
        exclude = ["author"]

        # Future Feature: Multiple files
        # widgets = {
        #    'uploaded_file': ClearableFileInput(attrs={'multiple': True}),
        # }
