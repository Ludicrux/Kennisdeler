"""Create and update forms for Article model and views"""
from django.forms import ModelForm
# from django.forms import ClearableFileInput

from articles.models import Article


class ArticleForm(ModelForm):
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


class ArticleFormEdit(ModelForm):
    class Meta:
        model = Article
        fields = [
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
